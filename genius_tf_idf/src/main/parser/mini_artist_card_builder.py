class MiniArtistCardBuilder:
    _template = """
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
        """

    def __init__(self, template=_template):
        self._template = template

    def with_artist_name(self, artist_name):
        return MiniArtistCardBuilder(self._template.replace('{ARTIST_NAME}', artist_name))

    def build_html(self):
        return self._template

    def with_artist_url(self, artist_url):
        return MiniArtistCardBuilder(self._template.replace('{URL}', artist_url))