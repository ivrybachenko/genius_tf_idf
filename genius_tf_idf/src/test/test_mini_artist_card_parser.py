import unittest

from parser import MiniArtistCardParser


class MiniArtistCardParserTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.html_artist1 = """
        <mini-artist-card object="$ctrl.hit.result" ng-switch-when="artist">
            <a ng-href="https://genius.com/artists/Trent-tomlinson" class="mini_card" set-class-before-navigate="mini_card--active" href="https://genius.com/artists/Trent-tomlinson">
              <div class="mini_card-thumbnail">
                <div class="user_avatar user_avatar--large clipped_background_image--background_fill clipped_background_image" clipped-background-image=":: $ctrl.artist.image_url" style="background-image: url(&quot;https://t2.genius.com/unsafe/48x48/https%3A%2F%2Fimages.genius.com%2F683a9c04dd52aa224f7a54bce77ac5a3.250x250x1.jpg&quot;);"></div>
              </div>
              <div class="mini_card-info mini_card-info--centered">
                <div class="mini_card-title">Trent Tomlinson</div>
              </div>
            </a>
        </mini-artist-card>
        """
    def test_get_source(self):
        parser = MiniArtistCardParser(self.html_artist1)
        self.assertEqual(self.html_artist1, parser.get_source())

if __name__ == '__main__':
    unittest.main()
