import pandas as pd
import numpy as np
from scipy.cluster.vq import kmeans2
from sklearn.metrics import pairwise_distances_argmin_min

def wrangle(filename):
    # Read Data and drop columns with more than thershold missing values
    df = pd.read_csv(filename)
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    dtypes = df.select_dtypes(exclude=numerics).columns
    for column in dtypes:
        if df[column].nunique() >  len(df)/2:
            df = df.drop(column,1)

    #Convert the empty stings  to np.nan objects using replace(), and then call dropna()
    df.replace('', np.nan, inplace=True)

    # drop columns with Nan values greater than half
    df = df.dropna(thresh=len(df) - len(df) / 2, axis=1)


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
    closest = PFA(df)
    x = list(df)
    variable = []
    for i in closest:
        variable.append(x[i])
    return variable

def PFA(df):
    corrMat = df.corr()
    eigen_values, eigen_vectors = np.linalg.eig(corrMat)

    # Using Kmeans2 for getting the centroids of clusters and an array which
    centroids, labels = kmeans2(eigen_vectors[:,:7],7)

    # Getting vectors closest to each cluster centroid
    closest, _ = pairwise_distances_argmin_min(centroids, eigen_vectors[:,:7])
    return closest

