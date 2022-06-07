import pandas as pd

def retrieve_preprocessed_dataset():
    promoters = pd.read_csv('./pre_processed_dataset/epigenomes_promoters.csv', index_col = [0,1,2,3])
    enhancers = pd.read_csv('./pre_processed_dataset/epigenomes_enhancers.csv', index_col = [0,1,2,3])
    promoters_labels = pd.read_csv('./pre_processed_dataset/labels_promoters.csv', index_col = [0,1,2,3])
    enhancers_labels = pd.read_csv('./pre_processed_dataset/labels_enhancers.csv', index_col = [0,1,2,3])
    enhancers_sequences = pd.read_csv('./pre_processed_dataset/sequence_enhancers.csv', index_col = [0])
    promoters_sequences = pd.read_csv('./pre_processed_dataset/sequence_promoters.csv', index_col = [0])

    epigenomes = {
        "promoters": promoters,
        "enhancers": enhancers
    }

    labels = {
        "promoters": promoters_labels,
        "enhancers": enhancers_labels
    }

    sequences = {
        "promoters": promoters_sequences,
        "enhancers": enhancers_sequences
    }

    return epigenomes, labels, sequences

def retrieve_epigenomes_labels():
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

    return epigenomes, labels
