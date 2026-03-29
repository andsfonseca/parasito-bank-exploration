# ParasitoBank Explorarion

This repository contains an exploration notebook for the ParasitoBank dataset, which is a dataset of images. The goal of this repository is to provide an overview of the dataset, including sample visualization and their annotations.

## Description 

This dataset contains 779 images of the visual field from fresh fecal samples analyzed under the microscope. These images were acquired using a Motorola G84 cellphone at resolutions of 3,072 x 3,072 pixels and 3,072 x 4,080 pixels. Parasite content was labeled by outlining regions, resulting in a total of 1,620 intestinal parasites, with a particular focus on intestinal protozoa. Through image processing, non-informative and noisy regions that did not provide relevant information within the visual field were removed, yielding images with an approximately 1:1 aspect ratio and a resolution of 2,100 x 2,100 pixels. The labeling information was organized in a JSON file following the “Common Objects in Context” (COCO) format, which was combined with the folder containing the images into a compressed file.

## Download do Dataset

A version of the dataset was created on [Hugging Face](https://huggingface.co/datasets/andsfonseca/parasito-bank), which can be accessed and downloaded using the Hugging Face `datasets` library. The code to load the dataset is as follows:

```python
from datasets import load_dataset

ds = load_dataset("andsfonseca/parasito-bank")
```

### Manual Data Download

The original dataset can also be downloaded manually via Mendeley Data: [https://data.mendeley.com/datasets/2h6z8s5m9c/1](https://data.mendeley.com/datasets/2h6z8s5m9c/1).

> If you choose to download it manually, to run the notebooks you will need to organize the files following the repository structure described below, placing the images and the JSON file inside the `data/raw/` folder.

## Estrutura do Repositório

```
parasito-bank/
├── data/                        <-- Folder to store dataset data
│   ├── raw/                     <-- Downloaded raw data
│   │   ├── images/              <-- Original images
│   │   └── ParasitoBank.json    <-- COCO annotations
│   └── interim/                 <-- Processed data
|      └── train.parquet         <-- Dataset in Parquet format
├── notebooks/                   <-- Folder for notebooks
│   └── exploration.ipynb        <-- Dataset exploration notebook
├── src/                         <-- Source code folder
│   └── dataset/                 <-- Dataset-related code
|       └── converter.py         <-- Code to convert the dataset to Parquet format
└── requirements.txt             <-- Project dependencies
```

## Structure

Each row has two fields:

| field | type | description |
|-------|------|-------------|
| `image` | `Image` | Microscopy image |
| `objects` | `Sequence` | List of annotations for that image |

`objects` sub-fields:

| sub-field | type | description |
|-----------|------|-------------|
| `bbox` | `Sequence(float32)` | Bounding box in COCO format `[x, y, width, height]` |
| `label` | `ClassLabel` | 0-based class index (names embedded in schema) |
| `area` | `float32` | Bounding box area in pixels² |

## Labels

| id | label |
|----|------|
| 0 | chillomastix |
| 1 | giardia |
| 2 | entamoebaColi |
| 3 | entamoebaHart |
| 4 | endolimaxNana |
| 5 | iodamoeba |
| 6 | blastocystis |
| 7 | complejoEntamoeba |
| 8 | coccidia |
| 9 | ascarisLumbricoides |
| 10 | taenia |
| 11 | tricocefalo |
| 12 | strongyloides |

## Notebooks

A detailed exploration of the dataset can be found in the `notebooks/exploration.ipynb` notebook, which includes loading the dataset, visualizing samples, and analyzing class distributions.

## Attribution

This dataset is derived from [ParasitoBank: Dataset of helminths and protozoa in coprology samples](https://data.mendeley.com/datasets/725hpzpwzf/1).

Original dataset authors: Jader Alejandro Muñoz Galindez, Luis Reinel Vásquez Arteaga, Rubiel Vargas-Canas

Use the following citation when referring to this dataset:

```tex
Muñoz Galindez, Jader Alejandro; Vásquez Arteaga, Luis Reinel; Vargas-Canas, Rubiel (2024), “ParasitoBank: Dataset of helminths and protozoa in coprology samples”, Mendeley Data, V1, doi: 10.17632/725hpzpwzf.1
```

License: CC BY 4.0  
https://creativecommons.org/licenses/by/4.0/

## Disclaimer

This dataset is a redistribution of ParasitoBank.
We do not claim ownership of the original data.

The code in this repository is licensed under the MIT License. See `LICENSE` for more details.

## Issues

Feel free to submit issues and enhancement requests.

## Contribution

1. Fork the project
2. Create a _branch_ for your modification (`git checkout -b my-new-resource`)
3. Do the _commit_ (`git commit -am 'Adding a new resource...'`)
4. _Push_ (`git push origin my-new-resource`)
5. Create a new _Pull Request_ 
