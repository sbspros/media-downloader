from common.BaseClass import BaseClass
from exceptions.MediaTypeMissing import MediaTypeMissing
from models.PlexTvSearch import PlexTvSearch
import argparse
import traceback


__author__ = "Richard Chamberlain"
__copyright__ = "Copyright 2022"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Richard Chamberlain"
__email__ = "richard@sbspros.ca"
__status__ = "Dev"
""" A ulitity to find tv information in Plex"""

if __name__ == '__main__':
    bc=BaseClass()
    
    parser = argparse.ArgumentParser(description = 'A ulitity to find tv information in Plex')

    parser.add_argument('-n', 
        '--tv_name',
        type=str, 
        help='The name of the tv show')    
    

    arg = parser.parse_args()
    try:
        if arg.tv_name == None:
            raise MissingParam

        plex_search=PlexTvSearch(bc)   
        plex_search.section_shows(arg.tv_name)
    except:
        bc.log.error("\t"+":"+traceback.format_exc()) 
        print('Application fail to start. Review the log file')
        exit()
