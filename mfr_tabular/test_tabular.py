import pytest
import mfr_tabular
from mfr_tabular.render_csv import render_csv

### Test Csv
def test_detect_csv(fakefile):
    fakefile.name = 'tabular.csv'
    handler = mfr_tabular.CsvHandler()
    assert handler.detect(fakefile) is True

@pytest.mark.parametrize('filename',[
    'other.v',
    'othercsv',
    'other.cssv',
    'other.',
    'other.xlsx',
])
def test_csv_does_not_detect_other_extensions(fakefile, filename):
    fakefile.name = filename
    handler = mfr_tabular.CsvHandler()
    assert handler.detect(fakefile) is False


def test_csv_render_csv(fakefile):
    fakefile.name = "this.csv"
    content = "a,b,c,d\n1,2,3,4\n1,2,3,4"
    fakefile.read.return_value = content
    print render_csv(open(fakefile).read())

### Test Excel
@pytest.mark.parametrize('filename', [
    'tabular.xls',
    'tabular.xlsx'
])
def test_detect_excel(fakefile, filename):
    fakefile.name = filename
    handler = mfr_tabular.ExcelHandler()
    assert handler.detect(fakefile) is True

@pytest.mark.parametrize('filename',[
    'other.x',
    'otherxlsx',
    'other.xxlsx',
    'other.',
    'other.csv',
])
def test_excel_does_not_detect_other_extensions(fakefile, filename):
    fakefile.name = filename
    handler = mfr_tabular.ExcelHandler()
    assert handler.detect(fakefile) is False
