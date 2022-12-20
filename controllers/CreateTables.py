from common.BaseClass import BaseClass
from connectors.SqlConnector import SqlConnector
from tables.Tv import Tv
from tables.TvSeasons import TvSeasons
from tables.TvEpisodes import TvEpisodes



class CreateTables():
    def __init__(self,bc:BaseClass):
        self._bc=bc
        self._sql_conn=SqlConnector(self._bc, self._bc._config._schema_name)
        self.check_tv()
        self.check_tv_seasons()
        self.check_tv_episodes()

    def check_tv(self):
        tv_show=Tv()
        if tv_show.is_created(self._sql_conn._conn)==False:
            tv_show.create_table(self._bc,self._sql_conn._conn)

    def check_tv_episodes(self):
        tv_episodes=TvEpisodes()
        if tv_episodes.is_created(self._sql_conn._conn)==False:
            tv_episodes.create_table(self._bc,self._sql_conn._conn)

    def check_tv_seasons(self):
        tv_seasons=TvSeasons()
        if tv_seasons.is_created(self._sql_conn._conn)==False:
            tv_seasons.create_table(self._bc,self._sql_conn._conn)
