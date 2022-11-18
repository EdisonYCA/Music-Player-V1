class Artist:
    def __init__(self, name):
        self.name = name
        self.albums = None
        self.songs = None

    def get_albums(self):
        """Returns artists albums"""
        return self.albums

    def get_name(self):
        """Returns artists name"""
        return self.name.title()

    def get_songs(self):
        """Returns an artists songs"""
        return self.songs

    def add_album(self, album):
        """add album to artists current album list"""
        if self.get_albums() is None:
            self.albums = album

    def add_song(self, song):
        """add song to artists current song list"""
        if self.get_songs() is None:
            self.songs = song

    def __str__(self):
        """Represent artist object as a string"""
        return self.name.title() + ", " + str(self.get_albums()) + ", " + str(self.get_songs())
