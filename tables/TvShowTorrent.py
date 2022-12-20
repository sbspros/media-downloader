from dataclasses import dataclass,field

## TvShowTorrent is based on the record returned form 1337x
## It will parse the the record returned from 1337x API and
## Have utilities to standardize the actions on that return data

class TvTorrentParsingError(Exception):
    def __init__(self):
        self.msg = 'There was an error parsing the torrent API data'
        super().__init__(self.msg)  
        

@dataclass
class TvShowTorrent():
    _name:str=field(init=False)
    _torrent_id:str=field(init=False)
    _link:str=field(init=False)
    _seeders:int=field(init=False)
    _leechers:str=field(init=False)
    _size:str=field(init=False)
    _upload_date:str=field(init=False)
    _uploader:str=field(init=False)
    _uploader_link:str=field(init=False)
    _adjusted_size:float=field(init=False)
    def __lt__(self, other):
        return self._adjusted_size < other.score

    def parse_data(self, torrent_record)->None:
        try:
            self._name=torrent_record['name']
            self._torrent_id=torrent_record['torrentId']
            self._link=torrent_record['link']                              
            self._seeders=int(torrent_record['seeders'] )                             
            self._leechers=torrent_record['leechers']                              
            self._size=torrent_record['size']
            self._upload_date=torrent_record['time']
            self._uploader=torrent_record['uploader']
            self._uploader_link=torrent_record['uploaderLink']
            self._adjusted_size=self.startard_sizes()
        except:
           raise TvTorrentParsingError()

    ## The size of the torrent files are on Mb and Gb but as strings and 
    ## This will standardize them as Gb as a float 
    def startard_sizes(self):
        size=float(self._size[0:len(self._size)-3])
        if self._size.upper().find('MB')!=-1:
            size=size/1000
        return size

                                           
    ## Takes a string of a show name, season and episode and returns
    ## True or False if it matches
    def matches(self,name:str,season:int,episode:int):
        ## Make it upper to match easier
        upper_show=self._name.upper().replace(' ','.')

        ## Make it upper to match easier
        search_show='{show}.S{season:02d}E{episode:02d}'.format(\
            show=name.upper(),season=season,episode=episode)

        if upper_show.find(search_show.upper().replace(' ','.'))==0:
            return True
        else:
            return False