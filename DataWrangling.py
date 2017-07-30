import pandas as pd
import numpy as np


def wrangle(filename):
    # Read Data and drop columns with more than thershold missing values
    df = pd.read_csv(filename)
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    dtypes = df.select_dtypes(exclude=numerics).columns
    for column in dtypes:
        if df[column].nunique() >  len(df)/2:
            df = df.drop(column,1)

    # drop columns with Nan values greater than half
    df = df.dropna(thresh=len(df) - len(df) / 2, axis=1)

    # Dropping columns with missing values greater than half
    for column in df:
        if any(df[column] == "" or pd.isnull(df[column])):
            missing_values_count = df[column].value_counts()[""]
            count_nan = len(df[column]) - df[column].count()

            # drop columns with missing or nan values more than half
            if missing_values_count > len(df) / 2 or count_nan > len(df) / 2:
                del df[column]

    # Filling missing values
    df.fillna(df.mean())
	# df.fillna(df.ffill())     # Forward Fill
    # df.fillna(bfill())	   # BackwardFill

    # Converting categorical to numeric values (Label Encoding)
    dtypes = df.select_dtypes(exclude=numerics).columns
    for column in dtypes:
        df[column] = df[column].astype('category')
        df[column] = df[column].cat.codes
        df.head()

    # Pricipal Feature Analysis
    # PFA(df)
    return df

def PFA(df):
    corrMat = df.corr()