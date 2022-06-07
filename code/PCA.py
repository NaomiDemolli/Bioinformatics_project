from tqdm.auto import tqdm
from sklearn.decomposition import PCA
import numpy as np
from retrieve_preprocessed_dataset import *
import pandas as pd
import matplotlib.pyplot as plt

epigenomes, labels, sequences = retrieve_preprocessed_dataset()

def pca(x: np.ndarray, n_components: int = 2) -> np.ndarray:
    return PCA(n_components=n_components, random_state=42).fit_transform(x)

tasks = {
    "x": [
        *[
            val.values
            for val in epigenomes.values()
        ],
        *[
            val.values
            for val in sequences.values()
        ]
    ],
    "y": [
        *[
            val.values.ravel()
            for val in labels.values()
        ],
        *[
            val.values.ravel()
            for val in labels.values()
        ]
    ],
    "titles": [
        "Epigenomes promoters",
        "Epigenomes enhancers",
        "Sequences promoters",
        "Sequences enhancers"
    ]
}

xs = tasks["x"]
ys = tasks["y"]
titles = tasks["titles"]

assert len(xs) == len(ys) == len(titles)

for x, y in zip(xs, ys):
    assert x.shape[0] == y.shape[0]


colors = np.array([
    "tab:blue",
    "tab:orange",
])

fig, axes = plt.subplots(nrows=1, ncols=4, figsize=(32, 8))

for x, y, title, axis in tqdm(zip(xs, ys, titles, axes.flatten()), desc="Computing PCAs", total=len(xs)):
    axis.scatter(*pca(x).T, s=1, color=colors[y.astype(int)])
    axis.xaxis.set_visible(False)
    axis.yaxis.set_visible(False)
    axis.set_title(f"PCA decomposition - {title}")
plt.savefig("./img/PCA decomposition")
plt.show()