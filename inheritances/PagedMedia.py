from interfaces.Media import TMDB_Media as MediaInterface
from inheritances.Media import Media as MediaBaseClass
from common.BaseClass import BaseClass
from exceptions.ApiExceptions import ApiRequestException,ApiOtherException
import requests
import traceback


class PagedMedia(MediaInterface,MediaBaseClass):

    def __init__(self,bc:BaseClass)->None:
        super().__init__(bc)
        self._api_key=self._bc._config._api_key
        self._lang=self._bc._config._lang
        self._max_pages=self._bc._config._max_pages


    def get_media(self):
        '''  Returns a dictionary from multiple calls of the API
        takes a url and make a API to TMDB.
        TMDB could return 1 or more pages of results
        the code below loads in the multiple API pages
        '''
        retreive_array = []
        page = 1
        i = 0
        try:
            retreive_list = requests.get(self._link.\
                format(page=str(page),api_key=self._api_key,lang=self._lang))
            if retreive_list.status_code!=200:
                raise requests.exceptions.HTTPError

            total_page = retreive_list.json()['total_pages']
            while page <= total_page:
                for item in retreive_list.json()['results']:
                    retreive_array.append(item)
                    i = i +1
                if page>int(self._max_pages):
                    break
                page = page +1
                retreive_list = requests.get(self._link+"&page={page}".\
                    format(page=str(page),key=self._api_key,lang=self._lang))
                #retreivePage = retreive_list.json()['page']
            return retreive_array

        except requests.exceptions.HTTPError:
            self._bc.log.error("\t"+":"+traceback.format_exc())
            raise (ApiRequestException)

        except:
            self._bc.log.error("\t"+":"+traceback.format_exc())
            raise (ApiOtherException)