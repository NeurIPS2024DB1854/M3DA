# M3DA
M3DA: Benchmark for Unsupervised Domain Adaptation in 3D Medical Image Segmentation

## Install

```
git clone https://github.com/NeurIPS2024DB1854/M3DA.git
cd M3DA && pip install -e .
```

## Getting started

### 1. Downloading data

We use four source datasets in our benchmark: AMOS, BraTS2021, CC359, and LIDC.
As a unifying interface to access the data, we use [AMID](https://github.com/neuro-ml/amid/),
so you can follow the guides on data downloading from the latter lib:

- Follow the docstring of the [AMOS class](https://github.com/neuro-ml/amid/blob/master/amid/amos/dataset.py)
- Follow the docstring of the [BraTS2021 class](https://github.com/neuro-ml/amid/blob/master/amid/brats2021.py)
- Follow the docstring of the [CC359 class](https://github.com/neuro-ml/amid/blob/master/amid/cc359/dataset.py)
- Follow the docstring of the [LIDC class](https://github.com/neuro-ml/amid/blob/master/amid/lidc/dataset.py)

### 2. Configuring repo

Insert paths to the raw datasets (downloaded at the previous step) in [m3da/config.py](m3da/config.py), e.g.,
```
PATH_AMOS22_RAW = "path/to/downloaded/amos22"
# etc.
```

### 3. Importing and using datasets

Every DA task has

1. _dataset class instance_: `dataset_*`. 
This instance has methods `image` and `mask` to get 3D image and the corresponding segmentation mask items.

2. _tuple with the task split_: `split_*`.
All splits are organized as `[source_ids: list, target_train_ids: list, target_test_ids: list]`.

3. _tuple with labels_: `labels_*`. It enumerates all segmentation classes in the selected task.
For instance, CC359 has a background and three foreground classes to segment, so `labels_t1f = (0, 1, 2, 3)`.

4. _int indicating the background label_: `background_lbl_*`.
This item explicitly indicates what label corresponds to the background. For now, it is always `0`.

Usage example:

```
from m3da.bench.task06_t1f import dataset_t1f, split_t1f, labels_t1f, background_lbl_t1f

x_source = dataset_t1f.image(split_t1f[0][0])
y_source = dataset_t1f.mask(split_t1f[0][0])

x_target_train = dataset_t1f.image(split_t1f[1][0])
# y_target_train = dataset_t1f.mask(split_t1f[1][0])  # (not needed in UDA setup, but sometimes available)

x_target_test = dataset_t1f.image(split_t1f[2][0])
y_target_test = dataset_t1f.mask(split_t1f[2][0])  # (for testing purposes only)
```


