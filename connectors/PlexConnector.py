from plexapi.server import PlexServer
from common.BaseClass import BaseClass,AppException
import traceback

__author__ = "Richard Chamberlain"
__copyright__ = "Copyright 2022"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Richard Chamberlain"
__email__ = "richard@sbspros.ca"
__status__ = "Dev"


class PlexConnectionFailed(Exception):
    def __init__(self):
        self.msg = 'Media Finder failed to initialize'
        super().__init__(self.msg)

class PlexConnector():

    def __init__(self,bc:BaseClass):
        self._bc=bc
        self._bc.log.info("\tStarting class "+self.__class__.__name__) 

        try:
            self._plex_connect=PlexServer(self._bc._config._plex_server,self._bc._config._plex_key)
        except:
            self._bc.log.error("\t"+":"+traceback.format_exc())
            raise PlexConnectionFailed

    @property
    def conn(self):return self._plex_connect