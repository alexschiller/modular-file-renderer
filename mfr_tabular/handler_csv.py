from mfr.core import FileHandler, get_file_extension
from mfr_tabular.render_csv import render_csv

EXTENSIONS = [
    '.csv',
]

try:  # requires pygments
    from mfr_tabular.render_csv import render_csv
    renderers = {
        'html': render_csv,
    }
except ImportError:
    renderers = {}


class CsvHandler(FileHandler):
    renderers = renderers
    namespace = "mfr_tabular"
    def detect(self, fp):
        return get_file_extension(fp.name) in EXTENSIONS
