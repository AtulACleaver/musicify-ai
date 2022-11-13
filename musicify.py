import os
from client import Client


def create_playlist():
    spotify_client = Client(os.getenv("SPOTIFY_AUTH_TOKEN"), os.getenv("SPOTIFY_USER_ID"))

    num_tracks_to_see = int(input("How many tracks would you like to see? "))
    last_played_tracks = spotify_client.get_last_played_tracks(num_tracks_to_see)

    print(f"\nHere are the last {num_tracks_to_see} tracks you listened to on Spotify:")
    for index, track in enumerate(last_played_tracks):
        print(f"{index + 1}- {track}")

    indexes = input("\nEnter a list of up to 5 tracks you'd like to use as seeds. Use indexes separated by a space: ")
    indexes = indexes.split()
    seed_tracks = [last_played_tracks[int(index) - 1] for index in indexes]

    recommended_tracks = spotify_client.get_track_recommendations(seed_tracks)
    print("\nHere are the recommended tracks which will be included in your new playlist:")
    for index, track in enumerate(recommended_tracks):
        print(f"{index + 1}- {track}")

    playlist_name = input("\nWhat's the playlist name? ")
    playlist = spotify_client.create_playlist(playlist_name)
    print(f"\nPlaylist '{playlist.name}' was created successfully.")

    spotify_client.populate_playlist(playlist, recommended_tracks)
    print(f"\nRecommended tracks successfully uploaded to playlist '{playlist.name}'.")


create_playlist()
