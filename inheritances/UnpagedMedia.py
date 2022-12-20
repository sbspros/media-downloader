from interfaces.Media import TMDB_Media as MediaInterface
from inheritances.Media import Media as MediaBaseClass
from common.BaseClass import BaseClass
from exceptions.ApiExceptions import ApiRequestException,ApiOtherException
import requests

class UnpagedMedia(MediaInterface,MediaBaseClass):

    def __init__(self,bc:BaseClass)->None:
        self._bc=bc
        super().__init__(self._bc)

        self._api_key=self._bc._config._api_key
        self._lang=self._bc._config._lang
        self._adult=self._bc._config._adult

    def get_media(self):
        ''' Returns a dictionary from a single API call
            Make a API call that returns all of its data
            at once
        '''
        try:
            return requests.get(self._link.\
               format(key=self._api_key,lang=self._lang)).json()
        except requests.exceptions.HTTPError:
            return []
        except:
            pass
