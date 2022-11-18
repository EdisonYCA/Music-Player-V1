from artist import Artist
from album import Album
from song import Song


def main():
    artist1 = Artist("Lil Uzi Vert")
    song1 = Song("Money Longer", 3.18)
    song2 = Song("Canadian Goose", 3.38)
    song3 = Song("Hi Roller", 4.36)
    song4 = Song("Grab the Wheel", 4.55)
    song5 = Song("You Was Right", 2.43)
    song6 = Song("Baby Are You Home", 2.43)
    song7 = Song("Ps & Qs", 3.41)
    song8 = Song("Team Rocket", 3.26)
    song9 = Song("Scott and Ramona", 3.41)
    songs = [song1, song2, song3, song4, song5, song6, song7, song8, song9]
    artist1.add_album(songs)


if __name__ == "__main__":
    main()
