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

Genes also include parts of DNA that are not copied into RNA, each genes contains a sequence called  <b> promoters </b> which specifies under which conditions the RNA copies a part of the gene. Further, the concentration of any type of proteins in a cell, can be influenced by changing the efficiencies of the above steps. This is called <i> regulation </i> of expression. In addition to the general transcription factors, there are additional TFs which modify the probabilità or speed of transcription. They bind to short DNA motifs, caleed <b> enhancers </b> and <b> silencers </b>.

Therefore, gene expression involves non-coding regions of DNA called cis-regulatory:
- promoters: sequence of nucleotides, located near a gene, which represent the starting point of the transcription
- enhancers: DNA sequences that help induce transcription of a gene, but they're far from the gene itself (this makes more difficult the identification of these regions) 
<< The CRRs, through interactions with proteins and TFs, help specify the formation of different cell types and to respondo to changing physiological conditions. Deciphering the active CRRs in each cell type is a fundamental step to uncover the misregulations underlying numerous human genetic diseas >> 

### Goal of the project
This project aims to design a good experimental setup for a classification problem on bioinformatics data. The project focuses on learning how to desing model and experimental approaches to obtain statistically reliable results. 

### Dataset
<i> (retrieve_dataset.py, retrieve_sequences) </i>

- ENCODE (Encyclopedia of DNA Elements): thanks to epigenomic_datase, preprocessed epigenomic data for 7 cell line (A549, GM12878, H1, HEK293, HepG2, K562, MCF-7) are available
- FANTOM5 (Functional Annotation of the Mammalian Genome): provides labels relative to CRRs for 250 different lines

In this work, I focues my attention on predicting enhancers and promoters regions in a single cell line A549. 

Cell line A549 is derived from a 58 year old Caucasian male and was established in 1972 by D.J. Giard, et al., through an explant culture of adenocarcinomic lung tissue

#### Labels and threshold

First of all, it may be useful to plot the distribution of the values of the labels

<p align="center">
  <img width="450" height="200" src="https://github.com/NaomiDemolli/Bioinformatics_project/blob/main/code/img/labels_distribution.jpg">
</p>

For both promoters and enhancers the distribution is unbalanced (almost exponential), moreover the ranges of values are very different from each other.

At this point, I need to binarize labels in order to convert the real values of the labels to a binary task, several approaches are possibile:
- the FANTOM suggested threshold at 1TPMs for both promoters and enhancers, this is good for promoters with ad unbalance of 0.204, but on this cell line it would cause a high unbalance of 0.0037 for enhancers. 

<p align="center">
  <img width="350" height="200" src="https://github.com/NaomiDemolli/Bioinformatics_project/blob/main/code/img/class_count_1threa.jpg">
</p>

- another approach suggested by FANTOM authors is setting threshold at 1TPMs, dropping values between 0 and 1 for both promoters and enhancers. This reduces the unbalance both for promoters and enhancers, respectively at 0.255 and 0.0038. Focusing on the highest unbalance, namely that of enhancers, this decrease is not enough to remove part of the samples from the dataset and the improvement for promoters' labels is small. 

<p align="center">
  <img width="350" height="200" src="https://github.com/NaomiDemolli/Bioinformatics_project/blob/main/code/img/class_count_drop_1threa.jpg">
</p>

- in the end, I decided to choose two different values for the thresholds - remembering that the ranges are very different - and don't drop values between 0 and 1: for promoters I left the suggested threshold of 1TPMs and an unbalance of 0.204, for enhancers I chose threshold at 0TPMs - almost all values of enhancers labels are 0 (third quartile is 0) - with an unbalance of  0.057.

I'm not focusing on the biological meaning of my choices, the threshold are chosen to obtain a dataset useful for learning. 

#### Pre-processing 
TO WRITE
#### Correlations
TO WRITE
#### Features selection
TO WRITE
### Model and learning
TO DO
