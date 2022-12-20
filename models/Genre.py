from common.BaseClass import BaseClass
from inheritances.UnpagedMedia import UnpagedMedia

class Genre(UnpagedMedia):

    def __init__(self,bc:BaseClass):
        super().__init__(bc)
        self._link=self._bc._config._api_genre
        self._bc.log.debug(self._link)
        self._genre_list=None


    def __str__(self):
        pass

    def genre(self):
        rec=self.get_media()
        self._bc.log.debug("Genre "+str(rec))
        self._genre_list= rec['genres']


    def lookup(self,key):
        for genre in self._genre_list:
            if genre['id']==key:
                return genre['name']
        return key
    
    def lookup_list(self,genre_list):
        genres=[]
        for key in genre_list:
            genres.append(self.lookup(key))
        return genres