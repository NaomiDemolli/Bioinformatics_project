# Bioinformatics_project
 project for bioinformatics course of Professor G.Valentini - UNIMI, 2021-2022

### Biology introduction

<p align="center">
  <img width="400" height="300" src="https://github.com/LucaCappelletti94/bioinformatics_practice/blob/master/Notebooks/arr.png?raw=true">
</p>

(warning: I'm not an expert in biology)

The basic unit of all biological life is cell, the major part of the heritable information of a cell is stored in the form of DNA molecules (called the cell's genome), a gene is a substring of the genome. Gene expression is the process by which the instructions in our DNA are converted into a functional product (such as protein) and it's summarized in the central dogma of molecular biology. 

There are two fundamental parts in central dogma:
1) Transcription: double helix of the DNA is opened, the nucleotides of the RNA are created complementary to those present on a DNA strand. The ribosomes inside the cell bind to RNA.
2) Translation: inside the ribosomes there is transfer RNA, which has three "pins" whose job is to 
read 3 letters of the m-RNA, in this manner the ribosomes create amminoacids. 

Genes also include parts of DNA that are not copied into RNA, each genes contains a sequence called  <b> promoters </b> which specifies under which conditions the RNA copies a part of the gene. Further, the concentration of any type of proteins in a cell, can be influenced by changing the efficiencies of the above steps. This is called <i> regulation </i> of expression. In addition to the general transcription factors, there are additional TFs which modify the probability or speed of transcription. They bind to short DNA motifs, caleed <b> enhancers </b> and <b> silencers </b>.

Therefore, gene expression involves non-coding regions of DNA called cis-regulatory:
- promoters: sequences of nucleotides, located near a gene, which represent the starting point of the transcription
- enhancers: DNA sequences that help induce transcription of a gene, but they're far from the gene itself (this makes more difficult the identification of these regions) 
<< The CRRs, through interactions with proteins and TFs, help specify the formation of different cell types and to respondo to changing physiological conditions. Deciphering the active CRRs in each cell type is a fundamental step to uncover the misregulations underlying numerous human genetic diseas >> 

### Goal of the project
This project aims to design a good experimental setup for a classification problem on bioinformatics data. The project focuses on learning how to desing model and experimental approaches to obtain statistically reliable results. 

### Dataset
<i> (retrieve_dataset.py, retrieve_sequences.ipynb) </i>

- ENCODE (Encyclopedia of DNA Elements): thanks to epigenomic_dataset, preprocessed epigenomic data for 7 cell line (A549, GM12878, H1, HEK293, HepG2, K562, MCF-7) are available
- FANTOM5 (Functional Annotation of the Mammalian Genome): provides labels relative to CRRs for 250 different lines

In this work, I focus my attention on predicting enhancers and promoters regions in a single cell line A549. 

Cell line A549 is derived from a 58 year old Caucasian male and was established in 1972 by D.J. Giard, et al., through an explant culture of adenocarcinomic lung tissue

#### Labels and threshold
<i> (labels_threshold.py) </i>

First of all, it may be useful to plot the distribution of the values of the labels

<p align="center">
  <img width="450" height="200" src="https://github.com/NaomiDemolli/Bioinformatics_project/blob/main/code/img/labels_distribution.jpg">
</p>

For both promoters and enhancers the distribution is unbalanced (almost exponential), moreover the ranges of values are very different from each other.

At this point, I need to binarize labels in order to convert the real values of the labels to a binary task, several approaches are possibile:
- the FANTOM suggested threshold at 1TPMs for both promoters and enhancers, this is good for promoters with an unbalance of 0.204, but on this cell line it would cause a high unbalance of 0.0037 for enhancers. 

<p align="center">
  <img width="400" height="200" src="https://github.com/NaomiDemolli/Bioinformatics_project/blob/main/code/img/class_count_1threa.jpg">
</p>

- another approach suggested by FANTOM authors is setting threshold at 1TPMs, dropping values between 0 and 1 for both promoters and enhancers. This reduces the unbalance both for promoters and enhancers, respectively at 0.255 and 0.0038. Focusing on the highest unbalance, namely that of enhancers, this decrease is not enough to remove part of the samples from the dataset, in addition the improvement for promoters' labels is small. 

<p align="center">
  <img width="400" height="200" src="https://github.com/NaomiDemolli/Bioinformatics_project/blob/main/code/img/class_count_drop_1threa.jpg">
</p>

- in the end, I decided to choose two different values for the thresholds - remembering that the ranges are very different - and not to drop values between 0 and 1: for promoters I left the suggested threshold of 1TPMs and thus an unbalance of 0.204, for enhancers I chose threshold at 0TPMs - almost all values of enhancers labels are 0 (third quartile is 0) - with an unbalance of 0.057.

(Warning: I'm not focusing on the biological meaning of my choices, the threshold are chosen to obtain a dataset useful for learning)

#### Pre-processing 
<i> (pre_processing.py) </i>

First thing to do is check the rate between number of samples and features in the dataset: in the case of promoters is 2080.9, while 1318.3 for enhancers. 

The second step is imputation of missing values: 
- for promoters only the 0.007% is NaN values, the sample with most values has 2 NaN values out of 48 and the feature with the most missing values has 189 NaN values out of 99881 
- for enhancers only the 0.001% is NaN values, the sample with most values has 1 NaN values out of 48 and the feature with the most missing values has 32 NaN values out of 63285
There are several approaches to replace NaN values, I decided to use nearest neighbors imputation: each missing feature is imputed using values from k nearest neighbors that have a value for the feature. The features of the neighbors are averaged uniformly, K is an hyperparams and is set to 5 in this project.

In addition, it must be check the presence of features whose values are constant: these features don’t provide any information to the target feature and are redundant data available in the dataset. In the epigenomic data of cell line A549 there are no costant features for either promoters or enhancers.

In the end, it is necessary to normalize the data: I used a better version of Z-score named Robust Scaler that scales features using statistics that are robust to outliers (this Scaler removes the median and scales the data according to the quantile range)

#### Correlations
<i> (correlations.py) </i>
Once the pro-processed dataset is obtained, it is needed to verify the correlation between features and output and the correlation between features. 

Correlation is a statistical measure that tells us about the association between the two variables, it describes how one variable behaves if there is some change in the other variable. I used two different correlation coefficient, Pearson and Spearman. 
- Pearson coefficient measures the linear correlation between to variables (it has a value between +1 and -1, with +1 total positive linear correlation, 0 no linear correlation and -1 negative linear correlation)
- Spearman coefficient assesses how well the relationship between two variables can be described using a monotonic function (perfect Spearman correlation of +1 or −1 occurs when each of the variables is a perfect monotone function of the other)

For promoters the features EHMT2, FOSB and RNF are considered unrelated to the output for Pearson, the feature ZFP36 is evaluated uncorrelated with output for Spearman. For enhancers, both Pearson's test and Spearman's test identify 2 unrelated features with the output: ZC3H11A and CBX2 are not linearly correlated with output and features CBX2 and KDM5A are not correlated with output for Spearman's test. 

I used same correlation tests in order to identify interrelated features, no single feature turns out to be extremely correlated with another. 

I then proceeded to eliminate the features not correlated to the output.

#### Features selection
TO WRITE
### Model and learning
TO DO
