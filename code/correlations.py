from scipy.stats import pearsonr, spearmanr
import numpy as np
from tqdm.auto import tqdm 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# FUNCTION

def output_corr(corr:str, epigenomes:dict, p_value_threshold:float, uncorrelated:dict, labels:dict):

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

# DATASET

promoters = pd.read_csv('./pre_processed_dataset/epigenomes_promoters.csv', index_col = [0,1,2,3])
enhancers = pd.read_csv('./pre_processed_dataset/epigenomes_enhancers.csv', index_col = [0,1,2,3])
promoters_labels = pd.read_csv('./pre_processed_dataset/labels_promoters.csv', index_col = [0,1,2,3])
enhancers_labels = pd.read_csv('./pre_processed_dataset/labels_enhancers.csv', index_col = [0,1,2,3])

epigenomes = {
    "promoters": promoters,
    "enhancers": enhancers
}

labels = {
    "promoters": promoters_labels,
    "enhancers": enhancers_labels
}

# Output correlation

def outpt_correlation_drop():

    p_value_threshold = 0.01 

    uncorrelated = {
        region: set()
        for region in epigenomes
    }

    print('---> Doing output correlation with Pearson')
    output_corr('pearson', epigenomes, p_value_threshold, uncorrelated, labels)
    print("-"*80)

    print('---> Doing output correlation with Spearson')
    output_corr('spearman', epigenomes, p_value_threshold, uncorrelated, labels)
    print("-"*80)


    # drop uncorrelated features

    for region, x in epigenomes.items():
        epigenomes[region] =x.drop(columns=[
            col
            for col in uncorrelated[region]
            if col in x.columns
        ])

outpt_correlation_drop()

# features correlation 

def features_correlation_drop():

    p_value_threshold = 0.01 
    correlation_threshold = 0.95

    extremely_correlated = {
        region: set()
        for region in epigenomes
    }

    scores = {
        region: []
        for region in epigenomes
    }

    features_correlation(
    'pearson', epigenomes, p_value_threshold, correlation_threshold, extremely_correlated, scores)

    features_correlation(
    'spearman', epigenomes, p_value_threshold, correlation_threshold, extremely_correlated, scores)

    print('There arent extremely correlated features')

    # descending order
    scores = {
        region:sorted(score, key=lambda x: np.abs(x[0]), reverse=True)
        for region, score in scores.items()
    }

    return scores

scores = features_correlation_drop()        

# visualization of 3 most correlated features

for region, x in epigenomes.items():
    _, firsts, seconds = list(zip(*scores[region][:3]))
    columns = list(set(firsts+seconds))
    print(f"Most correlated features from {region} epigenomes")
    pairplot = sns.pairplot(pd.concat([
        x[columns],
        labels[region],
    ], axis=1), hue=labels[region].columns[0], palette = 'CMRmap_r')
    plt.show()
    
    fig = pairplot.fig
    fig.savefig(f"./img/most_correlated_features_{region}.png")


