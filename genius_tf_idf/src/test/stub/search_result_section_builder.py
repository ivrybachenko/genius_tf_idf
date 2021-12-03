import copy


class SearchResultSectionBuilder:
    _template = """
    <search-result-section 
        ng-if="!['top_hit', 'song', 'lyric'].includes(section.type)" 
        section="section" 
        on-show-more="$ctrl.filter = section_type" 
        limit-to="3" variants="{no_horizontal_label_padding: true}">
        <!----><div ng-if="$ctrl.section.hits.length > 0">
            <div class="search_results_label text_label text_label--x_small_text_size text_label--gray search_results_label--no_horizontal_padding" 
                ng-class="{'search_results_label--no_horizontal_padding': $ctrl.variants.no_horizontal_label_padding}" 
                ng-bind=":: 'search.sections.' + $ctrl.section.type + '.title' | i18n">{LABEL}</div>
              <div ng-switch="$ctrl.section.type === 'album' || ($ctrl.section.type === 'top_hit' &amp;&amp; $ctrl.section.hits[0].index === 'album')">
                <!---->
            
                <!----><search-result-items ng-switch-default="" results="$ctrl.section.hits" limit-to="$ctrl.limit_to"><!----><div ng-repeat="hit in $ctrl.results | limitTo: $ctrl.limit_to">
      
    </div><!---->
    </search-result-items><!---->
      </div>
    
      <!----><a href="" prevent-default-click="" ng-if="$ctrl.section.type !== 'top_hit'" ng-click="$ctrl.on_show_more({section_type: $ctrl.section.type})" class="full_width_button u-bottom_margin" tracking="click" tracking-event="Search More Results Page View">
        Show more artists
        <svg class="inline_icon inline_icon--reading_size inline_icon--up_1" src="right_arrow.svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10.87 21.32"><path d="M1.5 21.32L0 20l8.21-9.34L0 1.32 1.5 0l9.37 10.66L1.5 21.32"></path></svg>
      </a><!---->
      {ITEMS}
    </div><!---->
    </search-result-section>
    """

    TEMPLATE_LABEL = '{LABEL}'
    TEMPLATE_ITEMS = '{ITEMS}'

    DATA_LABEL = 'label'
    DATA_ITEMS = 'items'

    _data = {
        DATA_LABEL: '',
        DATA_ITEMS: []
    }


    def __init__(self, data=_data):
        self._data = data

    def with_label(self, label):
        new_data = copy.deepcopy(self._data)
        new_data[self.DATA_LABEL] = label
        return SearchResultSectionBuilder(new_data)

    def with_item(self, item):
        new_data = copy.deepcopy(self._data)
        new_data[self.DATA_ITEMS].append(item)
        return SearchResultSectionBuilder(new_data)

    def are_all_required_fields_filled(self):
        return True

    def build_html(self):
        if not self.are_all_required_fields_filled():
            raise ValueError
        return self.template_with_data_filled()

    def template_with_data_filled(self):
        return self._template\
            .replace(self.TEMPLATE_LABEL, self._data[self.DATA_LABEL])\
            .replace(self.TEMPLATE_ITEMS, ''.join(self._data[self.DATA_ITEMS]))
