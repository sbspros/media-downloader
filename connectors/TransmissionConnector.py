from transmission_rpc import Client
from common.BaseClass import BaseClass,AppException
import traceback

__author__ = "Richard Chamberlain"
__copyright__ = "Copyright 2022"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Richard Chamberlain"
__email__ = "richard@sbspros.ca"
__status__ = "Dev"


class TransmissionConnectionFailed(Exception):
    def __init__(self):
        self.msg = 'Media Finder failed to initialize'
        super().__init__(self.msg)

class TransmissionConnector():

    def __init__(self,bc:BaseClass):
        self._bc=bc
        try:
            self._transmission_connect==Client(host="192.168.1.138",port= 9091,protocol="http")
        except:
            self._bc.log.error("\t"+":"+traceback.format_exc())
            raise TransmissionConnectionFailed
