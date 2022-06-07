import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.preprocessing import RobustScaler
from retrieve_preprocessed_dataset import retrieve_epigenomes_labels

# retrieve data
epigenomes, labels = retrieve_epigenomes_labels()

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
    #  Usiamo robust_scaler (sottraendo la mediana, non sensibile agli outlier, e dividendo per la sd tra il primo e il terzo quartile,
    #  è una versione migliore di z-scoring 
    return pd.DataFrame(
        RobustScaler().fit_transform(df.values),
        columns=df.columns,
        index=df.index
    )

def pre_processing(epigenomes):
    rate_samples_features(epigenomes)

    # NaN values

    for region, x in epigenomes.items():
        print("\n".join((
            f"Nan values report for {region} data:\n",
            f"- In the document there are {x.isna().values.sum()} NaN values out of {x.values.size} values.",
            f"  % nan/totale = {x.isna().values.sum()/x.values.size*100}.",
            f"- The sample (row) with most values has {x.isna().sum(axis=1).max()} NaN values out of {x.shape[1]} values.",
            f"- The feature (column) with most values has {x.isna().sum().max()} NaN values out of {x.shape[0]} values.",
            f"- % nan_col_values/tot_samples = {x.isna().sum().max()/x.shape[0]*100}"
        )))
        print("-"*80)

    # NaN values are replaces with KNN imputation

    for region, x in epigenomes.items():
        epigenomes[region] = knn_imputer(x)

    print('Nan values replaced with KNN imputation') 
    print("-"*80)   

    # Drop constant features
     
    for region, x in epigenomes.items():
        result = drop_constant_features(x)
        if x.shape[1] != result.shape[1]:
            print(f"Features in {region} were constant and had to be dropped!")
            epigenomes[region] = result
        else:
            print(f"No constant features were found in {region}!")    

    # Normalization robust_zscoring
    
    epigenomes = {
        region: robust_zscoring(x)
        for region, x in epigenomes.items()
    }

    print("-"*80)
    print('Normalization with robust_scalar done')
    print("-"*80)

    print('Pre-processing done! Saving results ...')
    epigenomes['enhancers'].to_csv('./pre_processed_dataset/epigenomes_enhancers.csv')  
    epigenomes['promoters'].to_csv('./pre_processed_dataset/epigenomes_promoters.csv') 

pre_processing(epigenomes)