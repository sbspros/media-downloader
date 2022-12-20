from common.BaseClass import BaseClass
from inheritances.PagedMedia import PagedMedia
from models.Genre import Genre
import datetime
import time

class TvSearch(PagedMedia):

    def __init__(self,bc:BaseClass):
        super().__init__(bc)
        self._bc.log.debug(self._link)
        self._genre=Genre(self._bc)
        self._genre.genre()
        self._format_str="""
{original_name}  
\t{id}
\tVote Average {vote_average}
\tgenre {genre_ids}
\tfirst_air_date {first_air_date}
\t{overview}\n      """

    def __str__(self):
        pass

    def media(self,show_name:str):
        self._link=self._bc._config._api_tv_search.format(tv_name=show_name,\
            adult=self._bc._config._adult,\
            api_key=self._bc._config._api_key,\
            lang=self._bc._config._lang)
        data=self.get_media()
  
        for rec in data:
            if rec['original_language']=='en' \
                and  'US' in rec['origin_country']:
                genres=self._genre.lookup_list(rec['genre_ids'])
                self._bc.log.info(self._format_str.format(id=rec['id'],original_name=rec['original_name'],vote_average=rec['vote_average'],overview=rec['overview'],genre_ids=genres,first_air_date=rec['first_air_date']))
        return self.get_media()

