from dataclasses import dataclass,field
from tables.AppConfig import AppConfig
import yaml
import os


class YamlFailure(Exception):
    def __init__(self):
        self.msg = 'Yaml file failed to load'
        super().__init__(self.msg) 

@dataclass
class MediaBuilderConfig(AppConfig):
    _symbols:list=field(init=False,default_factory=list)    

    def parse_config_file(self):
        try:
            with open('yaml/config.yaml','r') as file:
                app_info=yaml.safe_load(file)
        except:
            raise YamlFailure()
        
        ## Letup Logging
        self._file_name=app_info['Logging']['fileName']
        self._log_level=app_info['Logging']['logLevel']

        ##Database Setup
        self._schema_name=app_info['DataBase']['Schema']

        ## Api Keys
        self._api_key=os.environ.get('TMDB_API')

        ## Link Params
        self._lang=app_info['Api']['Lang']
        self._max_pages=app_info['Api']['MaxPages']
        self._adult=app_info['Api']['Adult']       

        ##Api links
        self._api_tv_search=app_info['TvApi']['TvSearch']
        self._api_tv_get=app_info['TvApi']['TvGet']
        self._api_genre=app_info['Genre']['Genre']
        self._api_tv_season=app_info['TvApi']['TvSeasons']
        
        ## Plex API
        self._plex_server=app_info['Plex']['Server']
        self._plex_key=os.environ.get('PLEX_KEY')

        ##Plex TV Sectons
        self._tv_sections=app_info['Plex']['TvSection']

        ##Transmission
        self._transmission_ip=os.environ.get('TRANSMISSION_IP')
        self._transmission_port=os.environ.get('TRANSMISSION_PORT')
        self._transmission_user=os.environ.get('TRANSMISSION_USER')
        self._transmission_passwd=os.environ.get('TRANSMISSION_PASSWORD')
