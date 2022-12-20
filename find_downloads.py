from common.BaseClass import BaseClass
from controllers.DownloadShows import DownloadShows
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
    downloads=DownloadShows(bc)
    downloads.find_episodes()

    