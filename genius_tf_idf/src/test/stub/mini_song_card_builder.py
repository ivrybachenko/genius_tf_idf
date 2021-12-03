class MiniSongCardBuilder:
    _template="""
    <mini-song-card object="song" artist="$ctrl.artist">
        <a ng-href="{URL}" class="mini_card" ng-class="{'mini_card--small': $ctrl.variants.small}" href="{URL}" style="outline-width: 0px !important; user-select: auto !important;">
          <div class="mini_card-thumbnail clipped_background_image--background_fill clipped_background_image" clipped-background-image=":: $ctrl.song.song_art_image_thumbnail_url" style="background-image: url(&quot;https://images.genius.com/e0120c08bc5dadac09401cfd4ceee588.224x224x1.jpg&quot;);">
            <!---->
          </div>
          <div class="mini_card-info">
            <div class="mini_card-title_and_subtitle">
              <div class="mini_card-title">{SONG_NAME}</div>
              <div class="mini_card-subtitle">
                {ARTIST_NAME}<!---->
              </div>
            </div>
            <!---->
            <!----><div ng-if="!$ctrl.excerpt_with_markup">
              <!----><div ng-if="$ctrl.song.lyrics_state === 'complete'" class="mini_card-metadata">
                <!---->
                <!---->
                <!---->
                <!---->
              </div><!---->
              <!---->
              <!---->
            </div><!---->
          </div>
        </a>
    </mini-song-card>
    """

    def __init__(self, template=_template):
        self._template = template

    def with_artist_name(self, artist_name):
        return MiniSongCardBuilder(self._template.replace('{ARTIST_NAME}', artist_name))

    def is_artist_name_filled(self):
        return '{ARTIST_NAME}' not in self._template

    def with_song_name(self, song_name):
        return MiniSongCardBuilder(self._template.replace('{SONG_NAME}', song_name))

    def is_song_name_filled(self):
        return '{SONG_NAME}' not in self._template

    def with_song_url(self, song_url):
        return MiniSongCardBuilder(self._template.replace('{URL}', song_url))

    def is_song_url_filled(self):
        return '{URL}' not in self._template

    def are_all_required_fields_filled(self):
        return self.is_artist_name_filled() and self.is_song_name_filled() and self.is_song_url_filled()

    def build_html(self):
        if not self.are_all_required_fields_filled():
            raise ValueError
        return self._template