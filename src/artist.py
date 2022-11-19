class Artist:
    def __init__(self, name):
        self.name = name
        self.albums = None
        self.songs = None

    def get_albums(self):
        """Returns a list of artists albums"""
        return self.albums

    def print_albums(self):
        """Returns a string of artists albums with song count"""
        album_names = ""
        for album in range(len(self.albums)):
            album_names += str(self.albums[album])
        return album_names

    def get_name(self):
        """Returns artists name"""
        return self.name.title()

    def get_songs(self):
        """Returns an artists songs"""
        return self.songs

    def add_album(self, album):
        """add album to artists current album list"""
        for songs in range(len(album)):  # all songs in album should also be added into the artists song list
            self.add_song(album[songs])

        if self.get_albums() is None:
            self.albums = []
            self.albums.append(album)
        else:
            self.albums.append(album)

    def add_song(self, song):
        """add song to artists current song list"""
        if self.get_songs() is None:
            self.songs = []
            self.songs.append(song)
        else:
            self.songs.append(song)

    def __repr__(self):
        """Represent artist object as a string"""
        return f"Artist: {self.name.title()}\n" \
               f"Albums: {str(self.print_albums())}\n" \
               f"Songs: {str(self.get_songs())}"

