from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from boruta import BorutaPy
from multiprocessing import cpu_count
import numpy as np
import pandas as pd
from retrieve_preprocessed_dataset import *

epigenomes, labels = retrieve_epigenomes_labels()

def execute_boruta_feature_selection(
    X_train: pd.DataFrame,
    y_train: np.ndarray,
    regression: bool,
    max_iter: int = 100 ):
    
    boruta_selector = BorutaPy(
        RandomForestClassifier(
            n_jobs=cpu_count(), class_weight='balanced', max_depth=5),
        n_estimators='auto',
        verbose=False,
        alpha=0.05,
        max_iter=max_iter, 
        random_state=42,
    )

    boruta_selector.fit(X_train.values, y_train.values.ravel())
    
    kept_features = list(X_train.columns[boruta_selector.support_])
    discarded_features = list(X_train.columns[~boruta_selector.support_])
        
    if(len(discarded_features) == 0):
        print('there arent features to discard')

    return(kept_features, discarded_features) 

for region in ['promoters', 'enhancers']:
     execute_boruta_feature_selection(
     X_train = epigenomes[region],
     y_train = labels[region], 
     regression = False)