import pandas as pd
from utilities import render_tabular


def render_csv(fp, *args, **kwargs):
    returned = {"dataframe":pd.read_csv(fp)}
    return render_tabular(fp, returned, *args, **kwargs)



