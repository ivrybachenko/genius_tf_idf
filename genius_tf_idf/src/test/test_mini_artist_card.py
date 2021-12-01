import unittest

from parser import MiniArtistCard


class MiniArtistCardFactory:
    def create(self, artist_name, artist_url):
        return """
        <mini-artist-card object="$ctrl.hit.result" ng-switch-when="artist">
            <a ng-href="{URL}" class="mini_card" set-class-before-navigate="mini_card--active" href="{URL}">
              <div class="mini_card-thumbnail">
                <div class="user_avatar user_avatar--large clipped_background_image--background_fill clipped_background_image" clipped-background-image=":: $ctrl.artist.image_url" style="background-image: url(&quot;https://t2.genius.com/unsafe/48x48/https%3A%2F%2Fimages.genius.com%2F683a9c04dd52aa224f7a54bce77ac5a3.250x250x1.jpg&quot;);"></div>
              </div>
              <div class="mini_card-info mini_card-info--centered">
                <div class="mini_card-title">{ARTIST_NAME}</div>
              </div>
            </a>
        </mini-artist-card>
        """.replace('{ARTIST_NAME}', artist_name) \
           .replace('{URL}', artist_url)


class MiniArtistCardFactoryTestCase(unittest.TestCase):

    def test_fills_gaps(self):
        actual_mini_artist_card = MiniArtistCardFactory().create(artist_name='Bob Marley',
                                                                 artist_url='https://genius.com/artists/Trent-tomlinson')
        expected_mini_artist_card = """
        <mini-artist-card object="$ctrl.hit.result" ng-switch-when="artist">
            <a ng-href="https://genius.com/artists/Trent-tomlinson" class="mini_card" set-class-before-navigate="mini_card--active" href="https://genius.com/artists/Trent-tomlinson">
              <div class="mini_card-thumbnail">
                <div class="user_avatar user_avatar--large clipped_background_image--background_fill clipped_background_image" clipped-background-image=":: $ctrl.artist.image_url" style="background-image: url(&quot;https://t2.genius.com/unsafe/48x48/https%3A%2F%2Fimages.genius.com%2F683a9c04dd52aa224f7a54bce77ac5a3.250x250x1.jpg&quot;);"></div>
              </div>
              <div class="mini_card-info mini_card-info--centered">
                <div class="mini_card-title">Bob Marley</div>
              </div>
            </a>
        </mini-artist-card>
        """
        self.assertEqual(expected_mini_artist_card, actual_mini_artist_card)


class MiniArtistCardTestCase(unittest.TestCase):

    def test_get_source(self):
        mini_artist_card_html = MiniArtistCardFactory().create(artist_name='Trent Tomlinson',
                                                               artist_url='https://genius.com/artists/Trent-tomlinson')
        parser = MiniArtistCard(mini_artist_card_html)
        self.assertEqual(mini_artist_card_html, parser.get_source())

    def test_get_artist_name(self):
        mini_artist_card_html = MiniArtistCardFactory().create(artist_name='Trent Tomlinson',
                                                               artist_url='https://genius.com/artists/Trent-tomlinson')
        parser = MiniArtistCard(mini_artist_card_html)
        self.assertEqual('Trent Tomlinson', parser.get_artist_name())

    def test_get_artist_url(self):
        mini_artist_card_html = MiniArtistCardFactory().create(artist_name='Trent Tomlinson',
                                                               artist_url='https://genius.com/artists/Trent-tomlinson')
        parser = MiniArtistCard(mini_artist_card_html)
        self.assertEqual('https://genius.com/artists/Trent-tomlinson', parser.get_artist_url())

if __name__ == '__main__':
    unittest.main()
