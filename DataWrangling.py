import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from scipy.cluster.vq import kmeans2
from sklearn.metrics import pairwise_distances_argmin_min


def wrangle(filename):
    # Read Data and drop columns with more than thershold missing values
    df = pd.read_csv(filename, low_memory=False)
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    dtypes = df.select_dtypes(exclude=numerics).columns
    for column in dtypes:
        if df[column].nunique() != df[column].count and df[column].nunique() > len(df) / 2:
            df = df.drop(column, 1)

    # Convert the empty stings  to np.nan objects using replace(), and then call dropna()
    df.replace('', np.nan, inplace=True)

    # drop columns with Nan values greater than half
    df = df.dropna(thresh=len(df) - len(df) / 2, axis=1)
    max_iter = 5

    # Converting categorical to numeric values (Label Encoding)
    dtypes = df.select_dtypes(exclude=numerics).columns
    for column in dtypes:
        df[column] = df[column].astype('category')
        df[column] = df[column].cat.codes
        df.head()

    # Filling missing values
    #df.fillna(df.mean())
    # df.fillna(df.ffill())     # Forward Fill
    # df.fillna(bfill())	   # BackwardFill

    # Initialize missing values to their column means
    missing = df.isnull()
    mu = np.nanmean(df, 0, keepdims=1)
    n_clusters = 5
    X_hat = np.where(missing, mu, df)
    df_cols = list(df)

    for i in range(max_iter):
        if i > 0:
            # initialize KMeans with the previous set of centroids. this is much
            # faster and makes it easier to check convergence (since labels
            # won't be permuted on every iteration), but might be more prone to
            # getting stuck in local minima.
            cls = KMeans(n_clusters, init=prev_centroids)
        else:
            # do multiple random initializations in parallel
            cls = KMeans(n_clusters, n_jobs=-1)

        # perform clustering on the filled-in data
        labels = cls.fit_predict(X_hat)
        centroids = cls.cluster_centers_

        # fill in the missing values based on their cluster centroids
        X_hat[missing] = centroids[labels][missing]

        # when the labels have stopped changing then we have converged
        if i > 0 and np.all(labels == prev_labels):
            break

        prev_labels = labels
        prev_centroids = cls.cluster_centers_
        #df = X_hat

        df = pd.DataFrame(data=X_hat[1:,0:], columns=np.asarray(df_cols))

    # Pricipal Feature Analysis
    closest, clusterVectors = PFA(df)
    x = list(df)
    topFeatures = []
    for i in closest:
        topFeatures.append(x[i])
    groupedFeatures = [[] for i in range(7)]
    count = 0
    for row in clusterVectors:
        for i in row:
            groupedFeatures[count].append(x[i])
        count = count + 1
    return topFeatures, groupedFeatures


def PFA(df):
    corrMat = df.corr()
    eigen_values, eigen_vectors = np.linalg.eig(corrMat)

    # Using Kmeans2 for getting the centroids of clusters and an array which
    centroids, labels = kmeans2(eigen_vectors[:, :7], 7)
    clusterVectors = [[] for i in range(7)]
    count = 0
    for i in labels:
        clusterVectors[i].append(count)
        count = count + 1

    # Getting vectors closest to each cluster centroid
    closest, _ = pairwise_distances_argmin_min(centroids, eigen_vectors[:, :7])
    return closest, clusterVectors

