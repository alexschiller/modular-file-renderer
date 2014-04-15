import numpy as np
import logging
import os
import json
from mfr import config as core_config
# from mfr_tabular.configuration import config as module_config

logger = logging.getLogger(__name__)


def _ensure_unicode(value):

    if not isinstance(value, basestring):
        if isinstance(value, int) or isinstance(value, float):
            if np.isnan(value):
                return ""
        return value

    try:
        return value.encode('utf-8')
    except ValueError:
        try:
            return value.decode('utf-8')
        except:
            return u''


def column_population(dataframe):
    """make column headers from the keys in dataframe
    :param dataframe:
    :return: a list of dictionaries
    """
    fields = dataframe.keys()

    columns = []
    for field in fields:
        uni = _ensure_unicode(field)
        columns.append({
            'id': uni,
            'name': uni,
            'field': uni,
        })
    return columns


def row_population(dataframe):
    """Convert the dictionary of lists Pandas has generated from the CSV into
    a list of dicts.
    :param dataframe:
    :return: JSON representation of rows
    """
    #todo (ajs) this needs to be reformatted NOT to use the row names as a variable
    # to iterate over, this will break spss files that need rownames
    #todo (ajs) right now it is renaming the rows in [r] when it reads it in
    fields = dataframe.keys()
    rows = []
    for n in range(len(dataframe[fields[0]])):
        rows.append({})
        for col_field in fields:
            rows[n][_ensure_unicode(col_field)] = str(_ensure_unicode(dataframe[col_field][n]))
    return rows

MAX_COLS = 400
MAX_ROWS = 1000


def check_shape(dataframe):
    """ Takes a data_frame and checks if the number of rows or columns is too
    big to quickly reformat into slickgrid's json data
    """
    return dataframe.shape[0] > MAX_ROWS or dataframe.shape[1] > MAX_COLS

def get_stylesheets():
    return """
        <link rel="stylesheet" href="{static_url}/mfr_tabular/css/slick.grid.css" type="text/css"/>
        <link rel="stylesheet" href="{static_url}/mfr_tabular/css/jquery-ui-1.8.16.custom.css" type="text/css"/>
        <link rel="stylesheet" href="{static_url}/mfr_tabular/css/examples.css" type="text/css"/>
        <link rel="stylesheet" href="{static_url}/mfr_tabular/css/slick-default-theme.css" type="text/css"/>
        """.format(static_url=core_config['STATIC_URL'])


def get_js():
    return """
        <script src="{static_url}/mfr_tabular/js/jquery-1.7.min.js"></script>
        <script src="{static_url}/mfr_tabular/js/jquery.event.drag-2.2.js"></script>
        <script src="{static_url}/mfr_tabular/js/slick.core.js"></script>
        <script src="{static_url}/mfr_tabular/js/slick.grid.js"></script>
        <script src="{static_url}/mfr_tabular/js/base_tabular.js"></script>
        """.format(static_url=core_config['STATIC_URL'])

def render_tabular(fp, returned, *args, **kwargs):
    _, file_name = os.path.split(fp.name)
    _, ext = os.path.splitext(file_name)
    dataframe = returned['dataframe']
    columns = json.dumps(column_population(dataframe))
    rows = json.dumps(row_population(dataframe))
    content = """
        <div id="mfrGrid" style="width: 600px; height: 600px;"></div>
        <script>
        var mfr_tabular = {columns: %s,
        rows: %s};
        </script>
    """ % (columns, rows)

    if core_config['INCLUDE_STATIC']:
        link = get_stylesheets()
        js = get_js()
        return '\n'.join([link, content, js, ])
    else:
        return content
