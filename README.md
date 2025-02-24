# Metal Surface Defect Detection Using SLF-YOLO Enhanced YOLOv8 Model

## Introduction

This repository contains the implementation code for the paper **"Metal Surface Defect Detection Using SLF-YOLO Enhanced YOLOv8 Model."** The project focuses on improving metal surface defect detection by enhancing the YOLOv8 model with the SLF-YOLO architecture.

## Repository Structure

- **`new_cfg/`** - Contains the proposed network configuration files from the paper.
- **`train.py`** - Script for training the SLF-YOLO model on a custom dataset.
- **`test.py`** - Script for testing the trained model on a custom dataset.
- **`README.md`** - This documentation file.

## Installation

To use this repository, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/zacianfans/SLF-YOLO.git
   cd SLF-YOLO
   ```

2. Install the required dependencies manually (ensure Python and necessary deep learning libraries are installed).

## Training

To train the model on your dataset, run:

```bash
python train.py --data your_dataset.yaml --cfg new_cfg/your_config.yaml --epochs 100 --batch-size 16
```

Make sure your dataset follows the YOLO format.

## Testing

To test the trained model, run:

```bash
python test.py --weights path/to/your/trained_model.pt --data your_dataset.yaml
```

## Dataset Preparation

Your dataset should be structured in the YOLO format, including:

```
- dataset/
  - images/
    - train/
    - val/
  - labels/
    - train/
    - val/
  - your_dataset.yaml
```

Ensure that `your_dataset.yaml` correctly points to the images and labels.


## Contact

For any issues or inquiries, please open an issue or contact [your email].

