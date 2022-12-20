from dataclasses import dataclass,field
from sql_tables.SqlTvSeasons import SqlTvSeasons

@dataclass
class TvSeasons(SqlTvSeasons):
    _tv_id:str=field(init=False)
    _season_id:str=field(init=False)
    _season_number:int=field(init=False)
    _complete:str='False'
    _air_date:str=field(init=False)
    _creatation_date:int=0
    _modification_date:int=0
    _table_name:str='tv_seasons'

    def parse_data(self,data,tv_id):
        self._tv_id=tv_id
        self._season_id=data['id']
        self._season_number=data['season_number']
        self._air_date=data['air_date']
