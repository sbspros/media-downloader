from common.BaseClass import BaseClass
from exceptions.MediaTypeMissing import MediaTypeMissing
from controllers.CreateTables import CreateTables
from controllers.EpisodeParse import EpisodeParse
from models.TvSeasonsGet import TvSeasonsGet
import argparse
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
    
    parser = argparse.ArgumentParser(description = 'Setup a new download show')

    parser.add_argument('-t', 
        '--tv_show',
        type=str, 
        help='Enter the id of the show to setup')    

    parser.add_argument('-s', 
        '--season',
        type=str, 
        help='Enter the id of the show to setup')    

    arg = parser.parse_args()
    try:
        if arg.season == None or arg.tv_show==None:
            raise MissingParam

        CreateTables(bc)
        seasons=TvSeasonsGet(bc)
        seasons_list=seasons.get_season_info(arg.tv_show,arg.season)
        episodes=EpisodeParse(bc)
        episodes.parse_episodes(seasons_list['episodes'],arg.tv_show,arg.season)
    except:
        bc.log.error("\t"+":"+traceback.format_exc()) 
        print('Application fail to start. Review the log file')
        exit()
