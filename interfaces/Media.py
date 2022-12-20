from abc import ABCMeta
class TMDB_Media(metaclass=ABCMeta):

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'get_media') and 
                callable(subclass.get_media) and  
                NotImplemented)    