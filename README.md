# Human detection in videos

The objective of the project is to show human presence in a given Youtube video (e.g. the [Dior - Eau de Parfum](https://www.youtube.com/watch?v=h4s0llOpKrU) commercial) by drawing bounding boxes around them on each frame.

The retained solution uses the [ImageAI](https://github.com/OlafenwaMoses/ImageAI) library and more specifically its [video detection](https://github.com/OlafenwaMoses/ImageAI#videodetection) class. This library enables quick usage of several pre-trained Deep Learning models for object detection such as ResNet (used as backbone of RetinaNet) which is found to perform best for this task (especially better than YOLOv3 and its lightweight variant tiny-YOLOv3). Note that such pre-trained models are released by ImageAI at https://github.com/OlafenwaMoses/ImageAI/releases.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. Its execution will generate a copy of the "Dior - Eau de Parfum" video in which detected humans are annotated on each frame.

### Prerequisites

There are two options available to get started:
1. Recommended: use Anaconda 3 and follow [Installing with conda](#installing-with-conda)
2. Alternatively, install Python 3.7.6 and pip in a virtual environment and follow [Installing with pip](#installing-with-pip)

In both cases, installation instructions must be performed at the root of a local copy of this repository:
```
git clone https://github.com/pauldmk/human_detection_video.git
cd human_detection_video
```

### Installing with conda

Create an environment with all requirements:
```
conda env create -f requirement.yml
```
Activate this environment:
```
conda activate video_detection_aive
```

### Installing with pip

Activate the previously created virtual environment and install requirements using pip:
```
pip install -r requirements.txt
```

## Execution

The code execution is done in one line:
```
python src/video_detection.py
```

It follows the following steps:
1. Download pre-trained Deep Learning model backbone
2. Download local copy of video
3. Perform object detection, using GPU if machine has a CUDA enabled GPU available (otherwise will run on CPU)

## Results

RetinaNet and a ResNet50 backbone are found to perform best, and perform annotation in about an hour on a basic CPU. 

Several detection threshold were attempted. A threshold of 60% gives visually satisfying results, but it is highly dependent on the use case. Besides, even with this manually tuned threshold, some frames feature false positives. On the upside, the annotation is overall of great quality, and even performs better than my human eye on some frames (e.g. at 0:17 with a blurred person in the background).

## Built with

- [ImageAI](https://github.com/OlafenwaMoses/ImageAI) to perform simple video detection
- [pytube](https://python-pytube.readthedocs.io/en/latest/user/quickstart.html) to download the video
