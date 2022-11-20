from artist import Artist
from album import Album
from song import Song


def main():
    run_program = True
    while run_program:
        # ask the user to enter an artist name
        print("Welcome to Music Player V1\n"
              "Let's begin by adding an artist!")
        artist_name = input("Enter the artist name -> ")

        # ask the user to enter a song or album for the artist
        print(f"\nWould you like to enter a song, or a album for {artist_name}?\n"
              "1. None\n"
              "2. Album\n"
              "3. Song")
        artist_request = input("->")

        run_program = False



    # if user wants to enter album, while user enters song name and length,
    # create new unique song object and append to album
    # if user wants to enter a single song, append song into artist song list
    # else exit program




if __name__ == "__main__":
    main()
