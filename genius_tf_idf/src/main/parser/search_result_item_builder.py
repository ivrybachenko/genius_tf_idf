class SearchResultItemBuilder:
    _template = """
    <search-result-item hit="hit">
        <div class="u-quarter_vertical_margins u-clickable">
            {DATA}
        </div>
    </search-result-item>
    """

    def __init__(self, template=_template):
        self._template = template

    def with_data(self, data):
        return SearchResultItemBuilder(self._template.replace('{DATA}', data))

    def build_html(self):
        return self._template
