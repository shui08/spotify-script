import spotipy
from spotipy.oauth2 import SpotifyOAuth
import keyboard
from dotenv import load_dotenv
import os

load_dotenv()

SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")
DEVICE_ID = os.getenv("DEVICE_ID")


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    scope="user-read-playback-state,user-modify-playback-state"
))


def next_song():
    sp.next_track(DEVICE_ID)

def previous_song():
    sp.previous_track(DEVICE_ID)

def play_pause():
    current_playback = sp.current_playback()
    if current_playback and current_playback['is_playing']:
        sp.pause_playback(DEVICE_ID)
    else:
        sp.start_playback(DEVICE_ID)
        

keyboard.add_hotkey('ctrl+right', next_song)
keyboard.add_hotkey('ctrl+left', previous_song)
keyboard.add_hotkey('ctrl+up', play_pause)


print("Press f12 to stop.")
keyboard.wait('f12')