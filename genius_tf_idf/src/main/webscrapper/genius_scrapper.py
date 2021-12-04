from parser.page import SearchResultPage, ArtistPage, SongPage
from webscrapper import WebScrapper


class GeniusScrapper:
    def __init__(self):
        self.scrapper = WebScrapper()

    def get_songs(self, artist_name, count):
        search_page_url = self.create_search_url(artist_name)
        search_page_html = self.scrapper.load_page_source(search_page_url)
        artist = SearchResultPage(search_page_html).get_artists()[0]
        artist_page_html = self.scrapper.load_page_source(artist['artist_url'])
        songs_info = ArtistPage(artist_page_html).get_songs()
        songs = []
        for song_info in songs_info:
            songs.append({
                'artist_name': artist['artist_name'],
                'artist_url': artist['artist_url'],
                'song_name': song_info['song_name'],
                'song_text': SongPage(self.scrapper.load_page_source(song_info['song_url'])).get_text(),
                'song_url': song_info['song_url']
            })
            if len(songs) == count:
                break
        return songs

    def dispose(self):
        self.scrapper.dispose()

    def create_search_url(self, search_query):
        return f"https://genius.com/search?q={search_query.replace(' ', '%20')}"
