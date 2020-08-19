[![Downloads](https://pepy.tech/badge/midv500)](https://pepy.tech/project/midv500)
[![PyPI version](https://badge.fury.io/py/midv500.svg)](https://badge.fury.io/py/midv500)
![CI](https://github.com/fcakyon/midv500/workflows/CI/badge.svg)

## Download and convert MIDV-500 datasets into COCO instance segmentation format
Automatically download/unzip [MIDV-500](https://arxiv.org/abs/1807.05786) and [MIDV-2019](https://arxiv.org/abs/1910.04009) datasets and convert the annotations into COCO instance segmentation format.

Then, dataset can be directly used in the training of Yolact, Detectron type of models.

## MIDV-500 Datasets
MIDV-500 consists of 500 video clips for 50 different identity document types including 17 ID cards, 14 passports, 13 driving licences and 6 other identity documents of different countries with ground truth which allows to perform research in a wide scope of various document analysis problems. Additionally, MIDV-2019 dataset contains distorted and low light images in it.

<img width="1000" alt="teaser" src="./figures/midv500.png">

You can find more detail on papers:

[MIDV-500: A Dataset for Identity Documents Analysis and Recognition on Mobile Devices in Video Stream](https://arxiv.org/abs/1807.05786)

[MIDV-2019: Challenges of the modern mobile-based document OCR](https://arxiv.org/abs/1910.04009)


## Getting started
### Installation
```console
pip install midv500
```

### Usage

- Import package:

```python
import midv500
```

- Download and unzip desired version of the dataset:

```python
# set directory for dataset to be downloaded
dataset_dir = 'midv500_data/'

# download and unzip the base midv500 dataset
dataset_name = "midv500"
midv500.download_dataset(dataset_dir, dataset_name)

# or download and unzip the midv2019 dataset that includes low light images
dataset_name = "midv2019"
midv500.download_dataset(dataset_dir, dataset_name)

# or download and unzip both midv500 and midv2019 datasets
dataset_name = "all"
midv500.download_dataset(dataset_dir, dataset_name)
```

- Convert downloaded dataset to coco format:

```python
# set directory for coco annotations to be saved
export_dir = 'midv500_data/'

# set the desired name of the coco file, coco file will be exported as "filename + '_coco.json'"
filename = 'midv500'

# convert midv500 annotations to coco format
midv500.convert_to_coco(dataset_dir, export_dir, filename)
```
