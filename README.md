# Bioinformatics_project
 project for bioinformatics course of Professor G.Valentini - UNIMI, 2021-2022

### Biology introduction

<p align="center">
  <img width="400" height="300" src="https://github.com/LucaCappelletti94/bioinformatics_practice/blob/master/Notebooks/arr.png?raw=true">
</p>

(warning: I'm not an expert in biology)

The basic unit of all biological life is the cell, the major part of the heritable information of a cell is stored in the form of DNA molecules (called the cell's genome), a gene is a substring of the genome. Gene expression is the process by which the instructions in our DNA are converted into a functional product (such as protein) and it's summarized in the central dogma of molecular biology. 

There are two fundamental parts in central dogma:
1) Transcription: double helix of the DNA is opened, the nucleotides of the RNA are created complementary to those present on a DNA strand. The ribosomes inside the cell bind to RNA.
2) Translation: inside the ribosomes there is transfer RNA, which has three "pins" whose job is to 
read 3 letters of the m-RNA, in this manner the ribosomes create amminoacids. 

Genes also include parts of DNA that are not copied into RNA, each genes contains a sequence called  <b> promoters </b> which specifies under which conditions the RNA copies a part of the gene. Further, the concentration of any type of proteins in a cell, can be influenced by changing the efficiencies of the above steps. This is called <i> regulation </i> of expression. In addition to the general transcription factors, there are additional TFs which modify the probabilità or speed of transcription. They bind to short DNA motifs, caleed <b> enhancers </b> and <b> silencers </b>.

Therefore, gene expression involves non-coding regions of DNA called cis-regulatory:
- promoters: sequence of nucleotides, located near a gene, which represent the starting point of the transcription
- enhancers: DNA sequences that help induce transcription of a gene, but they're far from the gene itself (this makes more difficult the identification of these regions) 
<< The CRRs, through interactions with proteins and TFs, help specify the formation of different cell types and to respondo to changing physiological conditions. Deciphering the active CRRs in each cell type is a fundamental step to uncover the misregulations underlying numerous human genetic diseas >> 

### Dataset
<i> (retrieve_dataset.py, retrieve_sequences) </i>

- ENCODE (Encyclopedia of DNA Elements): thanks to epigenomic_datase, preprocessed epigenomic data for the 7 cell line (A549, GM12878, H1, HEK293, HepG2, K562, MCF-7) are available
- FANTOM5 (Functional Annotation of the Mammalian Genome): provides labels relative to CRRs for 250 different lines

In this work, I focues my attention on predicting enhancers and promoters regions in a single cell line A549

#### Labels and threshold
TO WRITE
#### Pre-processing 
TO WRITE
#### Correlations
TO WRITE
#### Features selection
TO WRITE
### Model and learning
TO DO
