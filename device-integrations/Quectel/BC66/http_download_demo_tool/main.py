import serial
from serial import SerialException
from src.config_manager import *
from src.file_down_man import *
from src.network_context import NetworkContext
from src.serial_man import SerialMan
serial_man = None


def main():
    try:
        global serial_man
        config = ConfigManager('[CONFIG]').config
        ser = serial.Serial(port=config['serial_port'], baudrate=115200)
        serial_man = SerialMan(ser, '[SERIAL]')
        nwk = NetworkContext('[NWK]', config['remote_host'],
                             str(config['remote_port']), str(config['local_port']))
        file_down_man = FileDownMan('[DOWNLOAD]', serial_man, nwk, config['access_mode'], config['output_path'])
        file_down_man.download_file(config['remote_path'])
    except SerialException as ser_exc:
        print(str(ser_exc))
    except MissingConfigAttributeException as arg_err:
        print(str(arg_err))
    except MandatoryFileNotFoundException as file_miss:
        print(str(file_miss))
    except ModemConnectionException as conn_err:
        print(str(conn_err))
    except Exception as e:
        print('Program terminated unexpectedly for ' + str(e))
    finally:
        try:
            if serial_man is not None:
                serial_man.send_command('AT+QICLOSE=0')
        except NameError:
            pass


if __name__ == "__main__":
    main()
