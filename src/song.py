class Song:
    def __init__(self, name, length):
        self.name = name
        self.length = length

    def get_song_name(self):
        """Returns name of a song"""
        return self.name.title()

    def get_song_length(self):
        """Returns length of a song"""
        return self.length

    def __str__(self):
        """Returns string representation of song object"""
        return self.name.title() + ", " + str(self.length)
