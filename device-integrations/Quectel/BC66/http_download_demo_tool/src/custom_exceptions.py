from src.custom_error_codes import AppErrorCodes


class AppException(Exception):
    def __init__(self, msg, code):
        super().__init__(msg)
        self.msg = msg
        self.code = code

    def __str__(self):
        return self.msg

    def get_code(self):
        return self.code


class WrongConfigAttributeException(AppException):
    """This exception is used to represent misconfigured parameters"""
    def __init__(self, msg, code=AppErrorCodes.WRONG_CONFIG_ATTRIBUTE_ERR):
        super().__init__(msg, code)


class MandatoryFileNotFoundException(AppException):
    """This exception is used to represent a mandatory file missing"""
    def __init__(self, msg, code=AppErrorCodes.MANDATORY_FILE_NOT_FOUND_ERR):
        super().__init__(msg, code)


class MissingConfigAttributeException(AppException):
    """This exception is used to represent a missing parameter in config"""
    def __init__(self, msg, code=AppErrorCodes.MISSING_CONFIG_ATTRIBUTE_ERR):
        super().__init__(msg, code)


class ModemConnectionException(AppException):
    """This exception is used to represent a connection error raised by the modem"""
    def __init__(self, msg, code=AppErrorCodes.CONNECTION_ERR):
        super().__init__(msg, code)
