from enum import IntEnum


class AppErrorCodes(IntEnum):
    """A class containing error codes useful for the entire application"""
    MISSING_CONFIG_ATTRIBUTE_ERR = 1
    WRONG_CONFIG_ATTRIBUTE_ERR = 2
    CONNECTION_ERR = 3
    MANDATORY_FILE_NOT_FOUND_ERR = 4
