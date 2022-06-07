from epigenomic_dataset import active_enhancers_vs_inactive_enhancers
from epigenomic_dataset import active_promoters_vs_inactive_promoters
import pandas as pd
import numpy as np

enhancers, enhancers_labels = active_enhancers_vs_inactive_enhancers(cell_line='A549')
promoters, promoters_labels = active_promoters_vs_inactive_promoters(cell_line='A549')

epigenomes = {
    "promoters": promoters,
    "enhancers": enhancers
}


labels = {
    "promoters": promoters_labels,
    "enhancers": enhancers_labels
}

labels['promoters'].to_csv('./pre_processed_dataset/labels_promoters.csv')  
labels['enhancers'].to_csv('./pre_processed_dataset/labels_enhancers.csv')
epigenomes['enhancers'].to_csv('./pre_processed_dataset/epigenomes_enhancers.csv')  
epigenomes['promoters'].to_csv('./pre_processed_dataset/epigenomes_promoters.csv') 

