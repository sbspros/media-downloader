from common.BaseClass import BaseClass
from controllers.PlexTvSectionSync import PlexTvSectionSync
import traceback


__author__ = "Richard Chamberlain"
__copyright__ = "Copyright 2022"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Richard Chamberlain"
__email__ = "richard@sbspros.ca"
__status__ = "Dev"
""" Setup a new download show"""

class MissingParam(Exception):
    def __init__(self):
        self.msg = 'Missing one of the calling params'
        super().__init__(self.msg)  
        

if __name__ == '__main__':
    bc=BaseClass()
    sync=PlexTvSectionSync(bc)
    for section in bc._config._tv_sections:
        sync.sync_section(section)
    