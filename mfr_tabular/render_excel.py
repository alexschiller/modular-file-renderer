import pandas as pd
from utilities import render_tabular
import xlrd

def render_excel(fp, *args, **kwargs):
    workbook = xlrd.open_workbook(fp.name)
    sheets = workbook.sheet_names()
    # sheet = workbook.sheet_by_name(sheets[0])

    returned = {"dataframe":pd.read_excel(fp, sheets[0])}
    return render_tabular(fp, returned, *args, **kwargs)



