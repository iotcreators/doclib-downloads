import argparse
import ipaddress
from os.path import dirname, abspath
import os
import json
from src.custom_exceptions import MissingConfigAttributeException, WrongConfigAttributeException, \
    MandatoryFileNotFoundException
from src.constants import *
from src.loggable import Loggable


def check_config_completeness(config):
    """Checks that the config object contains all the needed parameters"""
    try:
        # noinspection PyUnusedLocal
        var = config['remote_host']
        # noinspection PyUnusedLocal
        var = config['remote_port']
        # noinspection PyUnusedLocal
        var = config['local_port']
        # noinspection PyUnusedLocal
        var = config['remote_path']
        # noinspection PyUnusedLocal
        var = config['serial_port']
    except KeyError as key_err:
        raise MissingConfigAttributeException("Settings not complete, missing " + str(key_err) + " field.")


def validate_config_settings(config):
    """Checks that the config parameters are within the right boundaries"""
    check_config_completeness(config)
    try:
        ipaddress.ip_address(config['remote_host'])
    except:
        raise WrongConfigAttributeException("Wrong remote host ip address!")
    if config['remote_path'] == '' or " " in config['remote_path'] or config['remote_path'][0] != '/':
        raise WrongConfigAttributeException("Remote path is empty or with invalid format!")
    if config['access_mode'] != 'direct' and config['access_mode'] != 'buffer':
        raise WrongConfigAttributeException("Access mode can only be direct or buffer")
    if config['remote_port'] < MIN_PORT_VALUE or config['remote_port'] > MAX_PORT_VALUE:
        raise WrongConfigAttributeException(f"Ports can only be between {MIN_PORT_VALUE} and {MAX_PORT_VALUE}")
    if config['local_port'] < MIN_PORT_VALUE or config['local_port'] > MAX_PORT_VALUE:
        raise WrongConfigAttributeException(f"Ports can only be between {MIN_PORT_VALUE} and {MAX_PORT_VALUE}")


class ConfigManager(Loggable):
    """A class used to manage the config parameters received from config file and CLI"""
    def __init__(self, log_prefix):
        super().__init__(log_prefix)
        self.config_name = 'config.json'
        self.output_path = dirname(dirname(abspath(__file__))) + os.sep + 'download' + os.sep + 'output.bin'
        self.serial_port = ''
        self.access_mode = 'direct'
        self.config_path = dirname(dirname(abspath(__file__))) + os.sep + self.config_name
        self.parse_cli_args()
        self.config = self.load_config()

    """Parses the CLI arguments inserted by the user"""
    def parse_cli_args(self):
        parser = argparse.ArgumentParser(description='Download a file through HTTP with Quectel BC66 Nb-IoT modem.',
                                         exit_on_error=False)
        parser.add_argument('-o', '--output_file', help='Set absolute file output path (with extension)', nargs='?',
                            const=self.output_path)
        parser.add_argument('-m', '--mode', help='Set access mode for modem [direct/buffered]', nargs='?',
                            const=self.access_mode)
        required_named = parser.add_argument_group('Required parameters')
        required_named.add_argument("-p", "--Port", help="Set serial port", required=True)
        try:
            args = parser.parse_args()
            if args.Port:
                self.serial_port = args.Port
            if args.output_file:
                self.output_path = args.output_file
            if args.mode:
                self.access_mode = args.mode
            self.print_stdout_and_file(f'Output file save pos: {self.output_path}')
        except Exception:
            raise MissingConfigAttributeException('Program has been terminated due to missing arguments from CLI.')

    """Creates the config parameters by merging the cli 
    parameters received from the users with the parameters in the config file"""
    def load_config(self):
        try:
            with open(self.config_path, 'r') as f:
                config = json.load(f)
        except Exception:
            raise MandatoryFileNotFoundException(f'Unable to read config file {self.config_path}')
        config['serial_port'] = self.serial_port
        config['output_path'] = self.output_path
        config['access_mode'] = self.access_mode
        validate_config_settings(config)

        return config
