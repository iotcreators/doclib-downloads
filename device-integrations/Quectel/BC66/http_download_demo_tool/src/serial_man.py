from src.loggable import Loggable


class SerialMan(Loggable):
    """this class manages the in and out communication through serial port"""
    def __init__(self, serial_com, log_prefix):
        super().__init__(log_prefix)
        self.serial_com = serial_com
        self.print_stdout_and_file(f'Opened serial connection at port {self.serial_com.name}')

    def send_command(self, cmd):
        """This function sends an AT command through the serial line"""
        term_str = cmd + '\r'
        self.serial_com.write(term_str.encode('utf-8'))
        self.print_stdout_and_file(f'Sent command {cmd} to modem.')

    def read_bytes(self, bytes_num):
        """This function reads the specified number of bytes from the serial line and returns the correspondent
        byte array object"""
        return self.serial_com.read(bytes_num)

    def read_answer_placeholder(self, placeholder):
        """This function reads the serial line and returns the first line that starts with the specified placeholder"""
        serial_read_lines = []
        log_str = ''
        while True:
            line = self.serial_com.read_until().decode("utf-8")
            log_str += self.build_debug_str(line.rstrip() + '\n')
            serial_read_lines.append(line)
            if len(serial_read_lines) != 1:
                if line.startswith(placeholder):
                    break
        self.save_log_to_file(log_str)
        return serial_read_lines[len(serial_read_lines)-1]
