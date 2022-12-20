from common.BaseClass import BaseClass
from connectors.PlexConnector import PlexConnector,PlexConnectionFailed
import inspect

class PlexTvSearch():

    def __init__(self,bc:BaseClass):
        self._bc=bc
        self._plex=PlexConnector(bc)

    def section_shows(self,show:str)->{}:
        """ Queries a Plex Server to find out shows in a section """
        for section in self._bc._config._tv_sections:
            print(section)
            try:
                show_data=self._plex.conn.library.section(section).get(show)
                print(self._plex.conn.library.section(section).all())
                for show in self._plex.conn.library.section(section).all():
                    print(show.title)

                #print(inspect.getmembers(self._plex.conn.library.section(section).get(show), lambda a:not(inspect.isroutine(a))))
                #for season in show_data.seasons():
                #    print(season.index)
                #    for episode in season.episodes():
                #        print(episode.index)
                #print(show_data.key) 
                #print(show_data.episodes()[-1])
                last_episode=self._plex_connect.library.section(section).get(show).episodes()[-1]
                print({'name':show.replace(' ','-'),'season':int(last_episode.seasonNumber),'episode':(last_episode.episodeNumber)})

            except:
                print("not found")
                pass
        #return {'name':show.replace(' ','-'),'season':int(last_episode.seasonNumber),'episode':(last_episode.episodeNumber)}
        return{}


