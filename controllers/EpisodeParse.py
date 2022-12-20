from common.BaseClass import BaseClass
from connectors.SqlConnector import SqlConnector
from tables.TvEpisodes import TvEpisodes

class EpisodeParse():

    def __init__(self,bc:BaseClass):
        self._bc=bc
        self._sql_conn=SqlConnector(self._bc, self._bc._config._schema_name)

    def parse_episodes(self,episodes,tv_id,season):
        for episode in episodes:
            season_episode=TvEpisodes()
            season_episode.parse_data(episode,tv_id,season)
            if season_episode.in_database(self._bc,self._sql_conn._conn) == False:
                season_episode.insert(self._bc,self._sql_conn._conn)