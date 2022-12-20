from common.BaseClass import BaseClass
from exceptions.MediaTypeMissing import MediaTypeMissing
from models.TvSearch import TvSearch 
import argparse
import traceback


__author__ = "Richard Chamberlain"
__copyright__ = "Copyright 2022"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Richard Chamberlain"
__email__ = "richard@sbspros.ca"
__status__ = "Dev"
""" A ulitity to find tv information from TMDB"""

class MissingParam(Exception):
    def __init__(self):
        self.msg = 'Missing one of the calling params'
        super().__init__(self.msg)  
        

if __name__ == '__main__':
    bc=BaseClass()
    
    parser = argparse.ArgumentParser(description = 'A ulitity to find tv information from TMDB')

    parser.add_argument('-n', 
        '--tv_show',
        type=str, 
        help='The name of the tv show')    

    arg = parser.parse_args()
    try:
        if arg.tv_show == None:
            raise MissingParam

        media_search=TvSearch(bc)   
        media_search.media(arg.tv_show)
    except:
        bc.log.error("\t"+":"+traceback.format_exc()) 
        print('Application fail to start. Review the log file')
        exit()
