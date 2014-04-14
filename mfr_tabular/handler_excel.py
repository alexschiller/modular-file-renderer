from mfr.core import FileHandler, get_file_extension
from mfr_tabular.render_excel import render_excel

EXTENSIONS = [
    '.xls',
    '.xlsx',
]

try:  # requires pygments
    from mfr_tabular.render_csv import render_csv
    renderers = {
        'html': render_excel,
    }
except ImportError:
    renderers = {}


class ExcelHandler(FileHandler):
    renderers = renderers
    namespace = "mfr_tabular"
    def detect(self, fp):
        return get_file_extension(fp.name) in EXTENSIONS
