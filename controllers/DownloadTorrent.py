from common.BaseClass import BaseClass
from transmission_rpc import Client
import requests

__author__ = "Richard Chamberlain"
__copyright__ = "Copyright 2022"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Richard Chamberlain"
__email__ = "richard@sbspros.ca"
__status__ = "Dev"

class DownloadTorrent():
    """   """

    def __init__(self,bc:BaseClass)->None:
        self._bc=bc

    def get_download_link(self,torrent):
        torrent_html=requests.get(torrent._link)
        if int(torrent_html.status_code) >= 200 and int(torrent_html.status_code) <= 299:
            starting_point=torrent_html.text.find("magnet")
            mag_link_start=torrent_html.text[starting_point:starting_point+200]
            end_point=mag_link_start.find('"')
            self._mag_link=mag_link_start[:end_point]

    def start_download(self):
        transmission=Client(host="192.168.1.138",port= 9091,protocol="http")

        transmission.add_torrent(self._mag_link)