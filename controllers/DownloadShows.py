from common.BaseClass import BaseClass
from connectors.SqlConnector import SqlConnector
from connectors.TransmissionConnector import TransmissionConnector
from models.MediaFinder import MediaFinder
from tables.TvEpisodes import TvEpisodes
from controllers.DownloadTorrent import DownloadTorrent
from lists.Shows import Shows
import traceback

class MediaFinderFailed(Exception):
    def __init__(self):
        self.msg = 'Media Finder failed to initialize'
        super().__init__(self.msg)


class DownloadShows():

    def __init__(self,bc:BaseClass):
        self._bc=bc
        self._sql_conn=SqlConnector(self._bc, self._bc._config._schema_name)
        self._transm_conn=TransmissionConnector
        self._episode_table=TvEpisodes()
        self._query=MediaFinder(bc)
        self._show_list=Shows(bc)

    def find_episodes(self):
        episodes=self._episode_table.search_downloadable(self._bc, self._sql_conn._conn)
        for episode in episodes:
            search_show='{show} S{season:02d}E{episode:02d}'.format(\
                show=episode[9].upper(),\
                season=int(episode[2]),episode=int(episode[3]))
            results = self._query.query('tv',search_show)
            if results !=[]:
                show_list=Shows(self._bc)
                show_list.parse_shows(results,episode[9],\
                    int(episode[2]),\
                    int(episode[3]))
                link=DownloadTorrent(self._bc)
                max_seeds=show_list.return_max_seeds()
                if max_seeds!=None:
                    link.get_download_link(show_list.return_max_seeds())
                    self._bc.log.info(search_show+' '+episode[4])
                    link.start_download()
