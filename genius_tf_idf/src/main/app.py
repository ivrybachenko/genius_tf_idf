import json

from lyricsgenius import Genius


artists = ['Trent Tomlinson', 'Sting', 'The Parakit',
           'Evanescence', 'Robbie Williams', 'Three Days Grace',
           'R.E.M.', 'Simon & Garfunkel', 'Mr. President',
           'The Subways', 'D-12', 'Fleetwood Mac',
           'Nathaniel Dawkins', 'Hurts', 'The Rasmus',
           'Grace', 'Palastic', 'Eminem', 'Xzibit',
           'No Doubt', 'Bad Meets Evil', 'Snoop Dogg']

if __name__ == '__main__':
    token = 'LKKhOfsEcIj6vDyXyQFCIWgoQ1O_SwNq16umN9wAXaSzDOPwOqmk1X1FNNPWH97Z'
    genius = Genius(token)
    songs = []
    for artist in artists:
        artist = genius.search_artist(artist, max_songs=10, sort="title")
        for song in artist.songs:
            songs.append({
                'name': song.full_title,
                'lyrics': song.lyrics,
                'artist': song.artist
            })
        with open('songs.json', 'w') as f:
            json.dump(songs, f, sort_keys=True)
    print(f'There are {len(songs)} in total')
