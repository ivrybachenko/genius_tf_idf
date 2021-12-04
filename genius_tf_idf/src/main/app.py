from tqdm import tqdm
import json

from webscrapper import GeniusScrapper

artists = ['Trent Tomlinson', 'Sting', 'The Parakit',
           'Evanescence', 'Robbie Williams', 'Three Days Grace',
           'R.E.M.', 'Simon & Garfunkel', 'Mr. President',
           'The Subways', 'D-12', 'Fleetwood Mac',
           'Nathaniel Dawkins', 'Hurts', 'The Rasmus',
           'Grace', 'Palastic', 'Eminem', 'Xzibit',
           'No Doubt', 'Bad Meets Evil', 'Snoop Dogg']


def load_songs_from_web():
    scrapper = GeniusScrapper()
    songs = []
    for artist in tqdm(artists):
        songs.extend(scrapper.get_songs(artist, 100))
    scrapper.dispose()
    with open('songs.json', 'w') as f:
        json.dump(songs, f, sort_keys=True)
    return songs

def load_songs_from_file():
    with open('songs.json', 'r') as f:
        return json.load(f)


DOWNLOAD = True
if __name__ == '__main__':
    songs = []
    if DOWNLOAD:
        songs = load_songs_from_web()
    else:
        songs = load_songs_from_file()
    print(f'There are {len(songs)} in total')
