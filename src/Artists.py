class Artist:
    def __init__(self, name):
        self.name = name
        self.albums = None
        self.songs = None

    def add_album(self, songs):
        """Add a list of songs to artist's album"""
        pass

    def add_song(self, song):
        """Add a song to artists list of songs"""
        pass

    def __str__(self):
        """Represent artist object as a string"""
        pass
