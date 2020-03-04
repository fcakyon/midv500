***


# Convert MIDV-500 annotations to COCO instance segmentation format
This repo can be used to automatically download/unzip MIDV-500 dataset and convert the annotations into COCO instance segmentation format.

Then, dataset can be directly used in the training of Yolact, Detectron models etc.

## MIDV-500 Dataset
MIDV-500 consists of 500 video clips for 50 different identity document types with ground truth which allows to perform research in a wide scope of various document analysis problems.

You can find more detail on: [MIDV-500: A Dataset for Identity Documents Analysis and Recognition on Mobile Devices in Video Stream](https://arxiv.org/abs/1807.05786)

## Dependencies
Manually install Miniconda (Python3) for your OS:
https://docs.conda.io/en/latest/miniconda.html

Install Miniconda (Python3) by bash script on Linux:
>>sudo apt update --yes
>>sudo apt upgrade --yes
>>wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh
>>bash ~/miniconda.sh -b -p ~/miniconda 
>>rm ~/miniconda.sh

Inside the base project directory, open up a terminal/anaconda promt window 
and create environment:
>>conda env create -f environment.yml

After environment setup, run the tests to see if everything is ready:
>>python -m unittest

Tested both on Ubuntu and Windows.

## Run Instructions

In the base project directory, open up a terminal/anaconda promt window, and 
activate environment:
>>conda activate midv500tococo

Download dataset to "data/":
>>python download_dataset.py data/

Create coco annotations to coco/midv500.json using the dataset placed in "data/":
>>python convert_dataset.py data/ coco/midv500.json

## Citation
If you use MIDV-500 dataset in your work, you can cite
```
@article{arlazarov2019midv,
  title={MIDV-500: a dataset for identity document analysis and recognition on mobile devices in video stream},
  author={Arlazarov, Vladimir Viktorovich and Bulatov, Konstantin Bulatovich and Chernov, Timofey Sergeevich and Arlazarov, Vladimir Lvovich},
  journal={Компьютерная оптика},
  volume={43},
  number={5},
  year={2019},
  publisher={Федеральное государственное автономное образовательное учреждение высшего~…}
}
```

