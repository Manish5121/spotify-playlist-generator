import spotipy
import sys, os
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
from rich import print


# load env variables
load_dotenv()
CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")

# create spotify object with respective scope
SCOPE = "user-library-read user-top-read playlist-modify-public user-read-recently-played"

def authenticate_with_spotify():
    auth_manager = SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=SCOPE)
    return spotipy.Spotify(auth_manager=auth_manager)

sp = authenticate_with_spotify()

# get input of songs
def parse_multiple_songs(song_str: str):
    """ Parse comma separated songs """
    songs = song_str.strip().split(",")
    parsed_song = [song for song in songs]
    return parsed_song

def get_last_played_tracks(n = 5):
    if not isinstance(n, int):
        raise ValueError("Input argument must be integer.")
    try:
        recent_tracks = sp.current_user_recently_played(limit=n)
        if recent_tracks['items']:
            last_played_tracks = [rt['track'] for rt in recent_tracks['items']]
            return last_played_tracks
        else:
            raise Exception('No recently played tracks were found!')
    except Exception as e:
        print(e)
        return []

# get recommend track
def get_recommended_tracks(query: str):
    if not isinstance(query, str):
        raise ValueError("Input argument must be string.")
    """get recommended tracks."""
    try:
        results = sp.search(q=query, type='track')
        if len(results['tracks']['items']) > 0:
            seed_track = results['tracks']['items'][0]['id']
            recommendations = sp.recommendations(seed_artists=[], seed_genres=[], seed_tracks=[seed_track], limit=5)
            return recommendations['tracks']
        else:
            raise Exception('No matching track found!')
    except Exception as e:
        print(e)
        return []

def process_recommended_tracks(all_related_tracks):
    """Process further actions after getting recommended tracks."""
    if all_related_tracks:
        print("\nRecommended Tracks:\n")
        for i, track in enumerate(all_related_tracks):
            print(f"{i+1}. {track['name']} - {track['album']['artists'][0]['name']}")

        if input('\nDo you want to create a new playlist? (yes/no)\n').lower() == 'yes':
            user_id = sp.current_user()["id"]
            playlist_name = input("Enter a name for the new playlist: ")
            playlist_desc = input("Enter description for the new playlist (optional): ")
            new_playlist = sp.user_playlist_create(user_id, playlist_name, public=True, description=playlist_desc)
            uri = [track['uri'] for track in all_related_tracks]
            try:
                sp.user_playlist_add_tracks(user_id, new_playlist["id"], uri )
                print(f"\n🎉Successfully created a new playlist '{playlist_name}' with {len(uri)} tracks!\n")
            except Exception as e:
                print(f"Error adding tracks to the playlist: {str(e)}\n")
        else:
            print('Aborted...\n')



# main function
def main():
    print(f'''[cyan]
    :'######::'########:::'#######::'########:'####:'########:'##:::'##:
    '##... ##: ##.... ##:'##.... ##:... ##..::. ##:: ##.....::. ##:'##::
     ##:::..:: ##:::: ##: ##:::: ##:::: ##::::: ##:: ##::::::::. ####:::
    . ######:: ########:: ##:::: ##:::: ##::::: ##:: ######:::::. ##::::
    :..... ##: ##.....::: ##:::: ##:::: ##::::: ##:: ##...::::::: ##::::
    '##::: ##: ##:::::::: ##:::: ##:::: ##::::: ##:: ##:::::::::: ##::::
    . ######:: ##::::::::. #######::::: ##::::'####: ##:::::::::: ##::::
    :......:::..::::::::::.......::::::..:::::....::..:::::::::::..:::::
    [/cyan]
    [hot_pink2]Automated Playlist Generator[/hot_pink2]
    ''')

    while True:
        # print Menu Options
        print('''
    Select an option:
        1. Enter Song Names Manually
        2. Get Songs From Last Played Track
        3. Quit
            ''')

        choice = int(input("Entered Value: "))
        if choice == 1:
            user_input = input("Enter one or more song names ('quit' to exit), separate each song with a comma: ")
            songs = parse_multiple_songs(user_input)
            print(songs)

            all_related_tracks = []

            for song in songs:
                related_tracks = get_recommended_tracks(song)
                if related_tracks:
                    all_related_tracks += related_tracks
                else:
                    print(f"No matching track found for '{song}', skipping...")

            if all_related_tracks:
                process_recommended_tracks(all_related_tracks)
                break
            else:
                print("No valid tracks were found.\n")
        elif choice == 2:
            num_last_played = input("Enter number of last played tracks to consider (default: 5): ")
            if num_last_played != "":
                last_played_tracks = get_last_played_tracks(int(num_last_played))
            else:
                last_played_tracks = get_last_played_tracks()
            name_of_tracks = []
            print()
            for i, track in enumerate(last_played_tracks):
                name_of_tracks.append(track['name'])
                print(f"{i+1}. {track['name']} - {track['album']['artists'][0]['name']}")

            song_index = input("\nEnter number of songs you like to seed (space sep numbers or 'all'): ").strip()
            if song_index.lower() == "all":
                songs = name_of_tracks
            else:
                song_index = song_index.split(" ")
                songs = []
                for i in song_index:
                    songs.append(name_of_tracks[int(i)-1])


            all_related_tracks = []

            for song in songs:
                related_tracks = get_recommended_tracks(song)
                if related_tracks:
                    all_related_tracks += related_tracks
                else:
                    print(f"No matching track found for '{song}', skipping...")

            if all_related_tracks:
                process_recommended_tracks(all_related_tracks)
                break
            else:
                print("No valid tracks were found.\n")


        elif choice == 3:
            break
        else:
            print("Invalid Option Selected! Please Try Again.")


if __name__ == "__main__":
    main()
