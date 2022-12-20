from common.BaseClass import BaseClass
from inheritances.UnpagedMedia import UnpagedMedia
from connectors.SqlConnector import SqlConnector
from tables.TvSeasons import TvSeasons

class TvSeasonsGet(UnpagedMedia):

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

    def get_season_info(self,tv_id:int, season:int):
        self._link=self._bc._config._api_tv_season.format(tv_id=tv_id,\
            season_number=season,\
            api_key=self._bc._config._api_key,\
            lang=self._bc._config._lang)
        data=self.get_media()
        tv_seasons=TvSeasons(self._bc)
        tv_seasons.parse_data(data,tv_id)
        if tv_seasons.in_database(self._bc,self._sql_conn._conn,tv_id,season)==False:
            tv_seasons.insert(self._bc, self._sql_conn._conn)
        return data




