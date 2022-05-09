# Pearson

from scipy.stats import pearsonr, spearmanr
import numpy as np
from tqdm.auto import tqdm 

def output_correlation(corr:str, epigenomes:dict, p_value_threshold:float, uncorrelated:dict, labels:dict):

    for region, x in epigenomes.items():
        print(f'\nCalcolo coefficiente di Pearson per {region}:\n')
        for col in x.columns:
            method = pearsonr if corr=='pearson' else spearmanr
            correlation, p_value = method(x[col].values, labels[region].values.ravel())
            
            if(p_value > p_value_threshold):
                print(f'La feature {col} non è correlata in modo significativo con l\'output, corr: {correlation}')
                uncorrelated[region].add(col)


def features_correlation(corr:str, epigenomes:dict, p_value_thre:float, correlation_thre:float, extr_corr:dict, scores:dict,):
   
    method = pearsonr if corr =='pearson' else spearmanr

    for region, x in epigenomes.items():
        for i, column in tqdm(
            enumerate(x.columns),
            total=len(x.columns), desc=f"Running Pearson test for {region}", dynamic_ncols=True, leave=False):
            
            for feature in x.columns[i+1:]:
                correlation, p_value = method(x[column].values.ravel(), x[feature].values.ravel())
                correlation = np.abs(correlation)
                scores[region].append((correlation, column, feature))
                if p_value < p_value_thre and correlation > correlation_thre:
                    print(region, column, feature, correlation)
                    if entropy(x[column]) > entropy(x[feature]):
                        extr_corr[region].add(feature)
                    else:
                        extr_corr[region].add(column) 