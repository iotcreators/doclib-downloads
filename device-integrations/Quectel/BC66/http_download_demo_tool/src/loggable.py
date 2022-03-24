from datetime import datetime
from os.path import dirname, abspath
import os


class Loggable:
    """This superclass can be inherited by every module willing to have logging (in stdout and/or file) capabilities"""
    def __init__(self, log_prefix):
        self.log_prefix = log_prefix
        self.log_root_path = dirname(dirname(abspath(__file__))) + os.sep + 'logs' + os.sep
        if not os.path.exists(self.log_root_path):
            os.makedirs(self.log_root_path)

    def build_debug_str(self, msg):
        """This function build a debug string appending the current timestamp to the input msg"""
        now = datetime.now()
        date_time = now.strftime("%H:%M:%S")
        return date_time + ' ' + self.log_prefix + ' ' + msg

    def save_log_to_file(self, log_msg):
        """This function saves a string to a file named by date"""
        now = datetime.now()
        log_file_name = now.strftime("%d-%m-%Y") + '.log'
        log_file_path = self.log_root_path + log_file_name
        f = open(log_file_path, "a")
        f.write(log_msg + '\n')
        f.close()

    def print_stdout_and_file(self, log_msg):
        """this function both prints on stdout and file a log string"""
        self.print_log_stdout(log_msg)
        self.save_log_to_file(self.build_debug_str(log_msg))

    def print_log_stdout(self, log_msg):
        """This function print a log message on the stdout"""
        print(self.build_debug_str(log_msg))
