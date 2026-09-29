# Object Detection and Tracking

A real-time Object Detection and Tracking project developed using **Python, OpenCV, and YOLO11**. The system detects objects in webcam/video input and tracks them across consecutive frames using unique tracking IDs.

## Features

* Real-time object detection
* Object tracking with unique IDs
* Bounding boxes around detected objects
* Confidence-based detection
* Supports webcam and video files
* Real-time display using OpenCV
* Press **Q** to quit

## Technologies Used

* Python
* OpenCV
* Ultralytics YOLO11
* NumPy

## Project Structure

```text
Object-Detection-Tracking/
│
├── App.py
├── requirements.txt
├── README.md
└── videos/
    └── sample.mp4
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/SnehaSingh2504/CodeAlpha_Object_Detection_Tracking.git
```

### 2. Open the project folder

```bash
cd CodeAlpha_Object_Detection_Tracking
```

### 3. Install the required libraries

```bash
pip install -r requirements.txt
```

## How to Run

### Using Webcam

```bash
python App.py
```

The default source is the system webcam.

### Using a Video File

```bash
python App.py --source sample.mp4
```

## How It Works

1. OpenCV captures frames from the webcam or video file.
2. The YOLO11 pretrained model processes each frame.
3. Objects are detected using bounding boxes.
4. The tracking system maintains object identities across frames.
5. The processed frames are displayed in real time.
6. Press **Q** to stop the program.

## Model

The project uses the **YOLO11 Nano (`yolo11n.pt`)** pretrained model from Ultralytics.

If the model file is not available locally, Ultralytics can download it when the application is run.

## Internship Task

This project was developed as part of an internship task on **Object Detection and Tracking**.

## Author

**Sneha Singh**

GitHub: [SnehaSingh2504](https://github.com/SnehaSingh2504)
