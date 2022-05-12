from epigenomic_dataset import active_enhancers_vs_inactive_enhancers
from epigenomic_dataset import active_promoters_vs_inactive_promoters
import matplotlib.pyplot as plt


# retrieve data 

enhancers, enhancers_labels = active_enhancers_vs_inactive_enhancers(cell_line='A549')
promoters, promoters_labels = active_promoters_vs_inactive_promoters(cell_line='A549')

labels = {
    "promoters": promoters_labels,
    "enhancers": enhancers_labels
}


# plot labels distribution

bins = 100
fig, axes = plt.subplots(ncols=len(labels), figsize=(10, 5))

for axis, (region, lbl) in zip(axes, labels.items()):
    lbl.hist(ax = axis, bins = bins, log = True)
    axis.set_title('Labels in ' + region)
    plt.savefig('.\img\labels_distribution.jpg')

# print(promoters_labels.describe())

# THRESHOLD for labels

def threshold_imbalance(dict_labels:dict, pro_thre:int, enh_thre:int) -> tuple:
    
    rate1 = (dict_labels['promoters']['A549']> pro_thre).mean()
    rate2 = (dict_labels['enhancers']['A549']> enh_thre).mean()
    
    return print('promoters_rate: ' + str(rate1),'enhancers_rate: '+ str(rate2))

threshold_imbalance(labels, 5, 0) # first solution: Wasserman 

threshold_imbalance(labels, 1, 1) # second solution: FANTOM5

# Third solution is threshold at 1TPMs for both promoters and enhancers, dropping values between 0 and 1

def drop_01_binarization_1() -> dict:
    labels_drop = {}
    
    for region, data in labels.items():
    
        df = labels[region]
        df_drop = df[(df['A549'] == 0) | (df['A549'] >= 1)] 
        df_drop = df_drop['A549'] > 1
        labels_drop[region] = df_drop
    
    return labels_drop

labels_drop = drop_01_binarization_1()

fig, axes = plt.subplots(ncols=2, figsize=(10, 5))

for axis, (region, lbl) in zip(axes.ravel(), labels_drop.items()):
    lbl.astype(int).hist(ax=axis, bins=2, alpha=0.5, rwidth=0.6)
    axis.set_title(f"Classes count in {region} - dropping & thres = 1", pad=20)
    axis.set_xticks([])
    axis.set_ylim(0, 83000)
    plt.subplots_adjust(wspace = 0.9)
    plt.savefig('.\img\class_count_drop_1threa.jpg')


print('promoters_rate: ' + str(labels_drop['promoters'].mean()), 'enhancers_rate: ' + str(labels_drop['enhancers'].mean()))

# Second solution FANTOM 5, threshold at 1 without dropping values

enhancers, enhancers_labels_bin = active_enhancers_vs_inactive_enhancers(cell_line='A549', binarize = True)
promoters, promoters_labels_bin = active_promoters_vs_inactive_promoters(cell_line='A549', binarize = True)

labels_bin = {
    "promoters": promoters_labels_bin,
    "enhancers": enhancers_labels_bin
}

fig, axes = plt.subplots(ncols=2, figsize=(10, 5))

for axis, (region, lbl) in zip(axes.ravel(), labels_bin.items()):
    lbl['A549'].astype(int).hist(ax=axis, bins=2, alpha=0.5, rwidth=0.6)
    axis.set_title(f"Classes count in {region} - thres = 1", pad=20)
    plt.subplots_adjust(wspace = 0.9)
    axis.set_xticks([])
    axis.set_ylim(0, 83000)
    plt.savefig('.\img\class_count_1threa.jpg')
    

# Promoters threshold at 1 without dropping, enhancers threshold at 0 (no biological meaning, only for learning)

labels['enhancers'] = labels['enhancers'] > 0
print(labels['enhancers'].mean())
labels['promoters'] = labels['promoters'] > 1
print(labels['promoters'].mean())

labels['promoters'].to_csv('./pre_processed_dataset/labels_promoters.csv')  
labels['enhancers'].to_csv('./pre_processed_dataset/labels_enhancers.csv')

