class Song:
    def __init__(self,title,duration,artist="Unknown Artist"):
        self.__title=title
        self.__artist=artist
        self.__duration=duration
    def getName(self):
        return self.__artist
    def gettitle(self):
        return self.__title
    def getduration(self):
      return self.__duration
    def info(self):

        print(f"{self.__title} by {self.__artist} {self.__duration}")
class Playlist:
    def __init__(self,name,song_list,now_id):
        self.__name=name
        self.__song_list=song_list
        self.__now_id=now_id
        