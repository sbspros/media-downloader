from common.BaseClass import BaseClass
from inheritances.UnpagedMedia import UnpagedMedia
from connectors.SqlConnector import SqlConnector
from tables.Tv import Tv

class TvGet(UnpagedMedia):

    def __init__(self,bc:BaseClass):
        super().__init__(bc)
        self._bc.log.debug(self._link)
        self._sql_conn=SqlConnector(self._bc, self._bc._config._schema_name)
        self._format_str="""
{original_name}  
\t{id}
\tVote Average {vote_average}
\tfirst_air_date {first_air_date}
\t{overview}\n      """

    def __str__(self):
        pass

    def get_show_info(self,tv_id:int):
        self._link=self._bc._config._api_tv_get.format(tv_id=tv_id,\
            api_key=self._bc._config._api_key,\
            lang=self._bc._config._lang)
        data=self.get_media()
        self._bc.log.error(self._link)
        self._bc.log.error(data)
        tv=Tv()
        tv.parse_data(data)
        if tv.in_database(self._bc,self._sql_conn._conn)==False:
            tv.insert(self._bc, self._sql_conn._conn)
        return tv




