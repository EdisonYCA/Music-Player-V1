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

    song10 = Song("Mone Longer", 3.18)
    song11 = Song("Canadan Goose", 3.38)
    song12 = Song("Hi Rller", 4.36)
    song13 = Song("Gra the Wheel", 4.55)
    song14 = Song("Yo Was Right", 2.43)
    song15 = Song("Bby Are You Home", 2.43)
    song16 = Song("s & Qs", 3.41)
    song17 = Song("eam Rocket", 3.26)
    song18 = Song("cott and Ramona", 3.41)

    lilUziVsTheWorld = Album("Lil uzi vs the world", [song1, song2, song3, song4, song5, song6, song7, song8, song9])
    lilUziVsTheWorldRe = Album("Lil Uzi vs the world remaster", [song10, song11, song12, song13, song14, song15, song16, song17, song18])

    artist1.add_album(lilUziVsTheWorld)
    artist1.add_album(lilUziVsTheWorldRe)

    print(artist1.albums)




if __name__ == "__main__":
    main()
