import copy


class ArtistPageBuilder:
    _template = """
    <div class="column_layout">
        <div class="column_layout-column_span column_layout-column_span--secondary">
            <div class="profile_identity_and_description">
              <profile-identity artist="$ctrl.artist" user="$ctrl.user"><div class="profile_identity">
                  <div class="profile_identity-text">
                    <h1 class="profile_identity-name_iq_and_role_icon u-hair_bottom_margin">
                      {ARTIST_NAME}
                    </h1>
                  </div>
                </div>
            </profile-identity>
        </div>
      </div>
      <div class="column_layout-column_span column_layout-column_span--primary" ng-switch-when="description">
            <!----><artist-songs-and-albums ng-if="$ctrl.artist" artist="$ctrl.artist" artist-songs="$ctrl.artist_songs" artist-albums="$ctrl.artist_albums" artist-has-more-songs="$ctrl.artist_has_more_songs" open-all-songs-pane="$ctrl.open_all_songs_pane()"><!----><div ng-if="$ctrl.artist_songs.length > 0" class="text_label text_label--gray u-xx_large_top_margin u-half_bottom_margin">Popular {ARTIST_NAME} songs</div><!---->
        
        <div class="mini_card_grid">
          <div class="mini_card_grid-song" ng-if="$ctrl.artist_songs.length > 0" ng-repeat="song in $ctrl.artist_songs">
            {SONGS}
          </div><!---->
        </div>
        <div ng-if="$ctrl.artist_has_more_songs &amp;&amp; $ctrl.artist_songs.length > 0" class="full_width_button u-clickable u-bottom_margin" ng-class="{'u-bottom_margin' :$ctrl.artist_songs.length >= 10}" ng-click="$ctrl.open_all_songs_pane()">
          Show all songs by {ARTIST_NAME} <svg class="inline_icon inline_icon--reading_size inline_icon--up_1" src="right_arrow.svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10.87 21.32"><path d="M1.5 21.32L0 20l8.21-9.34L0 1.32 1.5 0l9.37 10.66L1.5 21.32"></path></svg>
        </div>
        <div ng-if="$ctrl.artist_albums.length" class="text_label text_label--gray u-xx_large_top_margin u-half_bottom_margin">Popular {ARTIST_NAME} albums</div><!---->

        </artist-songs-and-albums>
          </div>
    </div>
    """
    TEMPLATE_ARTIST_NAME = '{ARTIST_NAME}'
    TEMPLATE_SONGS = '{SONGS}'

    DATA_ARTIST_NAME = 'artist_name'
    DATA_SONGS = 'songs'

    _data = {
        DATA_ARTIST_NAME: '',
        DATA_SONGS: []
    }

    def __init__(self, data=_data):
        self._data = data

    def with_artist_name(self, artist_name):
        new_data = copy.deepcopy(self._data)
        new_data[self.DATA_ARTIST_NAME] = artist_name
        return ArtistPageBuilder(new_data)

    def is_artist_name_filled(self):
        return self._data[self.DATA_ARTIST_NAME] != ''

    def with_song(self, song):
        new_data = copy.deepcopy(self._data)
        new_data[self.DATA_SONGS].append(song)
        return ArtistPageBuilder(new_data)

    def are_all_required_fields_filled(self):
        return self.is_artist_name_filled()

    def build_html(self):
        if not self.are_all_required_fields_filled():
            raise ValueError
        return self.template_with_data_filled()

    def template_with_data_filled(self):
        return self._template \
            .replace(self.TEMPLATE_ARTIST_NAME, self._data[self.DATA_ARTIST_NAME]) \
            .replace(self.TEMPLATE_SONGS, ''.join(self._data[self.DATA_SONGS]))
