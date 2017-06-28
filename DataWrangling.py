import pandas as pd
import numpy as np


def wrangle(filename):
    df = pd.read_csv(filename)
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    dtypes = df.select_dtypes(exclude=numerics).columns
    for column in dtypes:
        if df[column].nunique() >  len(df)/2:
            df = df.drop(column,1)
    return dtypes
