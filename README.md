# Real-Time Surveillance Object Detection and Multi-Object Tracking

## Overview

This repository contains a computer vision pipeline for real-time object detection and multi-object tracking in surveillance environments. The system combines YOLOv8 for object detection with DeepSORT for persistent object tracking, enabling accurate monitoring of moving objects across video frames.

The repository also includes dataset preprocessing and annotation management utilities used during model development and training.

> **Note:** This repository contains representative implementations of detection, tracking, and data preprocessing modules. The complete deployment environment and proprietary assets associated with the original project are not publicly available due to institutional ownership and confidentiality restrictions.

---

## Features

* Real-time object detection using YOLOv8
* Multi-object tracking with DeepSORT
* Persistent object identity assignment across frames
* Custom YOLOv8 model training pipeline
* Dataset validation and cleanup utilities
* YOLO annotation preprocessing tools
* Video output generation with tracking visualization
* Scalable surveillance analytics workflow

---

## System Architecture

```text
Input Video
     │
     ▼
YOLOv8 Detection
     │
     ▼
Bounding Boxes
     │
     ▼
DeepSORT Tracker
     │
     ▼
Object Association
     │
     ▼
Persistent Track IDs
     │
     ▼
Visualization & Analytics
     │
     ▼
Output Video
```

---

## Repository Structure

```text
Real-Time-Surveillance-Tracking/
│
├── training/
│   └── train_yolov8.py
│
├── tracking/
│   └── yolo_deepsort_tracking.py
│
├── preprocessing/
│   ├── update_class_labels.py
│   ├── convert_to_single_class.py
│   └── dataset_cleanup.py
│
├── results/
│   ├── sample_detection.jpg
│   ├── tracking_demo.gif
│   └── output_video.mp4
│
├── requirements.txt
└── README.md
```

---

## Modules

### YOLOv8 Training

Train a custom object detection model on a labeled dataset.

**Capabilities**

* Custom dataset training
* GPU acceleration support
* Transfer learning from pretrained YOLOv8 weights
* Performance monitoring during training

---

### YOLOv8 + DeepSORT Tracking

Perform real-time detection and multi-object tracking on video streams.

**Capabilities**

* Object detection in each frame
* Persistent identity tracking
* Motion continuity handling
* Real-time visualization
* Video output generation

---

### Annotation Management

Utilities for modifying YOLO label files.

**Capabilities**

* Class remapping
* Single-class conversion
* Batch annotation processing

---

### Dataset Cleanup

Ensures dataset consistency by removing unmatched images and labels.

**Capabilities**

* Detect missing annotations
* Remove orphan image files
* Remove orphan label files
* Improve dataset quality

---

## Technologies Used

| Technology | Purpose                   |
| ---------- | ------------------------- |
| Python     | Core development language |
| YOLOv8     | Object detection          |
| DeepSORT   | Multi-object tracking     |
| OpenCV     | Video processing          |
| NumPy      | Numerical operations      |
| PyTorch    | Deep learning framework   |

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/Real-Time-Surveillance-Tracking.git
cd Real-Time-Surveillance-Tracking
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Requirements

```text
ultralytics
opencv-python
deep-sort-realtime
numpy
torch
torchvision
```

---

## Usage

### Train YOLOv8 Model

```bash
python training/train_yolov8.py
```

### Run Tracking

```bash
python tracking/yolo_deepsort_tracking.py
```

### Clean Dataset

```bash
python preprocessing/dataset_cleanup.py
```

### Update Class Labels

```bash
python preprocessing/update_class_labels.py
```

---

## Applications

* Smart Surveillance Systems
* Campus Security Monitoring
* Traffic Monitoring
* Public Safety Analytics
* Intelligent Video Analytics
* Defense Surveillance Research

---

## Future Improvements

* Multi-camera tracking
* Cross-camera identity association
* Real-time anomaly detection
* Edge deployment optimization
* Distributed surveillance analytics
* Transformer-based tracking models

---

## Disclaimer

This repository contains representative implementations of object detection, tracking, and preprocessing components developed during research and experimentation in intelligent surveillance systems. Certain project assets, deployment configurations, and proprietary components are not included due to confidentiality and ownership restrictions.

---



