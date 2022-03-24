from enum import Enum
from src.loggable import Loggable


class ProtocolType(Enum):
    TCP = 1
    HTTP = 2


class NetworkContext(Loggable):
    """This class acts as a storage class to store information about the network"""
    def __init__(self, log_prefix, remote_host, remote_port, local_port, protocol=ProtocolType.HTTP):
        super().__init__(log_prefix)
        self.remote_host = remote_host
        self.remote_port = remote_port
        self.local_port = local_port
        self.protocol = protocol

