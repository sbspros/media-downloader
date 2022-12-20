from dataclasses import dataclass,field
from sql_tables.SqlTvEpisodes import SqlTvEpisodes

@dataclass
class TvEpisodes(SqlTvEpisodes):
    _tv_id:str=field(init=False)
    _season_number:str=field(init=False)
    _episode_number:int=field(init=False)
    _air_date:str=field(init=False)
    _download:str='False'
    _creatation_date:int=0
    _modification_date:int=0
    _table_name:str='tv_episodes'

    def parse_data(self,data,tv_id,season_number):
        self._tv_id=tv_id
        self._season_number=season_number
        self._episode_number=data['episode_number']
        self._air_date=data['air_date']
