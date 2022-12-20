from common.BaseClass import BaseClass
from connectors.PlexConnector import PlexConnector,PlexConnectionFailed
from connectors.SqlConnector import SqlConnector
from tables.Tv import Tv
from tables.TvSeasons import TvSeasons
from tables.TvEpisodes import TvEpisodes
import traceback
import inspect

class SyncFailed(Exception):
    def __init__(self):
        self.msg = 'Media Sync failed'
        super().__init__(self.msg)

class PlexTvSectionSync():

    def __init__(self,bc:BaseClass):
        self._bc=bc
        self._plex=PlexConnector(bc)
        self._tv_table=Tv()
        self._season_table=TvSeasons()
        self._episode_table=TvEpisodes()
        self._sql_conn=SqlConnector(self._bc, self._bc._config._schema_name)
        self._episode_table.episode_reset(self._bc, self._sql_conn._conn)

    def sync_section(self,section:str):
        """ Queries a Plex Server to find out shows in a section """
        try:
            for show in self._plex.conn.library.section(section).all():
                db_show=self._tv_table.search_name(self._bc, self._sql_conn._conn,show.title)
                if db_show!=[]:
                    tv_id=db_show[0][2]
                    for season in show.seasons():
                        db_season=self._season_table.search_season(self._bc, self._sql_conn._conn,tv_id,season.index)
                        if db_season!=[]:            
                            for episode in season.episodes():
                                db_episode=self._episode_table.search_episode(self._bc, self._sql_conn._conn,tv_id,season.index,episode.index)
                                if db_season!=[]:
                                    self._episode_table.episode_download(self._bc, self._sql_conn._conn,tv_id,season.index,episode.index)





                #print(inspect.getmembers(self._plex.conn.library.section(section).get(show), lambda a:not(inspect.isroutine(a))))
                #for season in show_data.seasons():
                #    print(season.index)
                #    for episode in season.episodes():
                #        print(episode.index)
                #print(show_data.key) 
                #print(show_data.episodes()[-1])
                #last_episode=self._plex_connect.library.section(section).get(show).episodes()[-1]
                #print({'name':show.replace(' ','-'),'season':int(last_episode.seasonNumber),'episode':(last_episode.episodeNumber)})

        except:
            self._bc.log.error("\t"+":"+traceback.format_exc())
            raise SyncFailed()
        #return {'name':show.replace(' ','-'),'season':int(last_episode.seasonNumber),'episode':(last_episode.episodeNumber)}
        return{}


