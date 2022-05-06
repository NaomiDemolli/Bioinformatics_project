# Pearson

from scipy.stats import pearsonr, spearmanr

def output_correlation(corr:str, epigenomes:dict, p_value_threshold:float, uncorrelated:dict, labels:dict):

    for region, x in epigenomes.items():
        print(f'\nCalcolo coefficiente di Pearson per {region}:\n')
        for col in x.columns:
            method = pearsonr if corr=='pearson' else spearmanr
            correlation, p_value = method(x[col].values, labels[region].values.ravel())
            
            if(p_value > p_value_threshold):
                print(f'La feature {col} non è correlata in modo significativo con l\'output, corr: {correlation}')
                uncorrelated[region].add(col)