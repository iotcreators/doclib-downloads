import os
import time
from binascii import hexlify
from os.path import dirname, abspath

from src.custom_exceptions import ModemConnectionException, WrongConfigAttributeException
from src.loggable import Loggable
from src.modem_answer_parser_utils import *


class FileDownMan(Loggable):
    """This class is used to manage the file download"""
    def __init__(self, log_prefix, serial_man, nwk_ctx, access_mode, output_file_path):
        super().__init__(log_prefix)
        self.serial_man = serial_man
        self.nwk_ctx = nwk_ctx
        self.access_mode = access_mode
        self.download_root_path = dirname(dirname(abspath(__file__))) + os.sep + 'download' + os.sep
        self.download_file_path = output_file_path
        self.is_first_chunk_http = True
        self.total_down_size = 0
        self.remaining_bytes = 0
        if not os.path.exists(self.download_root_path):
            os.makedirs(self.download_root_path)

    def download_file(self, path):
        """This function manages the entire download flow for both buffer and direct access mode"""
        self.clean_down_folder()
        if self.access_mode == 'direct':
            access_mode_val = '1'
        elif self.access_mode == 'buffer':
            access_mode_val = '0'
            # Configure the modem to also show the current buffer length after read
            self.serial_man.send_command('AT+QICFG="showlength",1')
            self.serial_man.read_answer_placeholder('OK')
        else:
            raise WrongConfigAttributeException("Access mode can only be direct or buffer")

        # Connection opening phase
        at_sock_open_cmd = 'AT+QIOPEN=1,0,"TCP","'+self.nwk_ctx.remote_host + \
                       f'",{self.nwk_ctx.remote_port},{self.nwk_ctx.local_port},{access_mode_val}'
        self.serial_man.send_command(at_sock_open_cmd)
        resp = extract_qiopen_info(self.serial_man.read_answer_placeholder('+QIOPEN'))
        qiopen_err_code = resp['err_code']
        if qiopen_err_code != 0:
            raise ModemConnectionException(f'Unable to open connection with '
                                           f'{self.nwk_ctx.remote_host}, received error {qiopen_err_code},'
                                           f'see BC66 manual for further details.')
        self.print_stdout_and_file(f'Correctly opened connection with '
                                   f'{self.nwk_ctx.remote_host} at port {self.nwk_ctx.remote_port}.')

        # HTTP request phase
        http_get_str = f'GET {path} HTTP/1.1\r\nHost: {self.nwk_ctx.remote_host}\r\n\r\n'
        http_get_str_len = len(http_get_str)
        at_sock_send_cmd = f'AT+QISENDEX=0,{str(http_get_str_len)},{hexlify(http_get_str.encode()).decode()}'
        self.serial_man.send_command(at_sock_send_cmd)
        self.print_stdout_and_file(f'Starting file download in {self.access_mode} mode.')
        if self.access_mode == 'direct':
            self.down_direct_mode()
        elif self.access_mode == 'buffer':
            self.down_buffer_mode()

    def down_buffer_mode(self):
        """This function manages the download in buffer access mode"""
        extract_quirc_info(self.serial_man.read_answer_placeholder('+QIURC').rstrip())
        self.serial_man.send_command('AT+QIRD=0,512')
        qird_info = extract_qird_info(self.serial_man.read_answer_placeholder('+QIRD').rstrip())
        current_chunk_size = qird_info['bytes_read']
        self.parse_write_data_file(current_chunk_size)

        while True:
            self.print_stdout_and_file(f'Remaining bytes: {self.remaining_bytes}')
            self.serial_man.send_command('AT+QIRD=0,512')
            qird_info = extract_qird_info(self.serial_man.read_answer_placeholder('+QIRD').rstrip())
            bytes_in_buffer = qird_info['bytes_in_buf']
            current_chunk_size = qird_info['bytes_read']

            if current_chunk_size > 0:
                self.remaining_bytes -= self.parse_write_data_file(current_chunk_size)
            if self.remaining_bytes == 0:
                self.print_stdout_and_file(f'All {self.total_down_size} bytes downloaded, download completed.')
                break
            if bytes_in_buffer == 0:
                time.sleep(0.1)

    def parse_write_data_file(self, size):
        """this function is called upon reception of a number of bytes and performs the read from the serial buffer and the store
        of such bytes into the output download file"""
        read_bytes = self.serial_man.read_bytes(size)
        self.print_stdout_and_file(f'Received {str(size)} bytes.')
        if self.is_first_chunk_http:
            self.is_first_chunk_http = False
            headers_digest = parse_http_headers(read_bytes)
            first_byte_data_index = headers_digest['first_data_byte']
            self.total_down_size = headers_digest['total_size']
            self.remaining_bytes = self.total_down_size
            self.print_stdout_and_file(f'Starting download of {self.total_down_size} bytes.')
            read_bytes = read_bytes[first_byte_data_index:]
        self.print_stdout_and_file('Data: ' + hexlify(read_bytes).decode('utf-8'))
        self.write_data_to_file(read_bytes)
        self.remaining_bytes -= len(read_bytes)
        self.print_stdout_and_file(f'Written {str(size)} bytes to file.')
        return len(read_bytes)

    def down_direct_mode(self):
        """this function manages the download in direct access mode"""
        current_chunk_size = self.parse_chunk_info_direct()
        if current_chunk_size > 0:
            self.parse_write_data_file(current_chunk_size)
        while True:
            self.print_stdout_and_file(f'Remaining bytes: {self.remaining_bytes}')
            current_chunk_size = self.parse_chunk_info_direct()
            if current_chunk_size > 0:
                self.parse_write_data_file(current_chunk_size)
            if self.remaining_bytes == 0:
                self.print_stdout_and_file(f'All {self.total_down_size} bytes downloaded, download completed.')
                break

    def parse_chunk_info_direct(self):
        """This function parses the response of the modem in direct access mode"""
        quirc_ans = self.serial_man.read_answer_placeholder('+QIURC')
        quirc_info = extract_quirc_info(quirc_ans.rstrip())
        current_chunk_size = quirc_info['curr_size']
        return current_chunk_size

    def clean_down_folder(self):
        """This function deletes the output file in case it is already existent"""
        if os.path.exists(self.download_file_path):
            os.remove(self.download_file_path)
            self.print_stdout_and_file('Removed previously downloaded file.')

    def write_data_to_file(self, data):
        """This function write data to the specified output file"""
        with open(self.download_file_path, "ab") as binary_file:
            binary_file.write(data)
