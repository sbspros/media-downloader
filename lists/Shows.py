from common.BaseClass import BaseClass
from tables.TvShowTorrent import TvShowTorrent, TvTorrentParsingError
import operator

class Shows():
    def __init__(self,bc:BaseClass):
        self._bc=bc
        self._show_list=[]

    def parse_shows(self,torrent_list,show_name,season,episode):
        for show in torrent_list:
            search_show=TvShowTorrent()
            search_show.parse_data(show)

            if search_show.matches(show_name,season,episode) and \
                search_show._adjusted_size >0.5 \
                and search_show._adjusted_size <2.5:
                self._show_list.append(search_show)            

    def return_max_seeds(self):
        try:
            sorted_max = sorted(self._show_list, key=operator.attrgetter('_seeders'),reverse=True)
            return sorted_max[0]
        except:
            return None