import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.preprocessing import RobustScaler


def rate_samples_features(epigenomes:dict):
    for region, x in epigenomes.items():
        print(
            f"The rate between samples and features for {region} data is: {x.shape[0]/x.shape[1]}"
        )
        print("-"*80)


def knn_imputer(df:pd.DataFrame, neighbours:int=5)->pd.DataFrame:
    return pd.DataFrame(
        KNNImputer(n_neighbors=neighbours).fit_transform(df.values),
        columns=df.columns,
        index=df.index
    )        


def drop_constant_features(df:pd.DataFrame)->pd.DataFrame:
    """Return DataFrame without constant features."""
    return df.loc[:, (df != df.iloc[0]).any()]
    

def robust_zscoring(df:pd.DataFrame)->pd.DataFrame:
    return pd.DataFrame(
        RobustScaler().fit_transform(df.values),
        columns=df.columns,
        index=df.index
    )