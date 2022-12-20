from dataclasses import dataclass,field
from sql_tables.SqlTv import SqlTv

@dataclass
class Tv(SqlTv):
    _name:str=field(init=False)
    _tv_id:int=field(init=False)
    _status:str=field(init=False)
    _in_production:str=field(init=False)
    _creatation_date:int=0
    _modification_date:int=0
    _table_name:str='tv_shows'

    def parse_data(self,data):
        name=data['name'].replace("'", "")
        self._name=name
        self._tv_id=data['id']
        self._in_production=data['in_production']
