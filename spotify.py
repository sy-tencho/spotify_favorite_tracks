import requests
import json
import os.path
import pandas as pd

class Spotify:
  def __init__(self):
    self.uri = 'https://api.spotify.com/v1'
    self.headers = { 'Authorization': '' }

  def popular_track_ids(self, time_range, limit):
    uri = os.path.join(self.uri, 'me', 'top', 'tracks')
    payload = {'time_range': time_range, 'limit': limit }
    result  = requests.get(uri, headers = self.headers, params = payload).json()
    items = result['items']

    track_ids = []
    for item in items:
      track_ids.append(item['id'])

    return track_ids
  
  def track_features(self, comma_spaced_track_ids):
    uri = os.path.join(self.uri, 'audio-features')
    payload = {'ids': comma_spaced_track_ids }
    result = requests.get(uri, headers = self.headers, params = payload).json()

    return result

# Create instance
spotify = Spotify()

popular_track_ids = spotify.popular_track_ids(time_range = 'medium_term', limit = '50')
comma_spaced_popular_track_ids = ','.join(map(str, popular_track_ids)) 

track_features = spotify.track_features(comma_spaced_track_ids = comma_spaced_popular_track_ids)['audio_features']
df = pd.DataFrame(track_features)

df
