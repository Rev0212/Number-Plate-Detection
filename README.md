# Number Plate Detection Project

## Overview

The Number Plate Detection Project utilizes OpenCV to perform real-time detection of vehicle license plates using a webcam. This project is designed to provide a robust and flexible solution for capturing and recording license plates, which can be integrated into various applications, including:

- **Automatic License Plate Recognition (ALPR)**: Ideal for integrating into broader ALPR systems for automatic vehicle tracking and identification.
- **Parking Management Systems**: Useful for monitoring and managing parking spaces by detecting and recording the number plates of parked vehicles.
- **Security Systems**: Enhances surveillance systems by capturing and logging vehicle number plates for security and access control.

### Key Features

- **Real-Time Detection**: Continuously processes the video feed from a webcam to detect and display number plates as they appear.
- **Save Detected Plates**: Allows users to save images of detected number plates to a specified directory with a simple key press.
- **User Controls**: Easy-to-use controls for saving images (`s` key) and exiting the application (`q` key).
- **Dynamic Path Handling**: Configurable paths for saving images and loading the Haar cascade file, ensuring flexibility in deployment.

### How It Works

1. **Load Haar Cascade**: The project uses a pre-trained Haar cascade classifier to detect number plates. This classifier is a machine learning model trained to identify specific patterns associated with license plates.
2. **Capture Video Feed**: Accesses the webcam to capture the live video feed.
3. **Process Frames**: Each frame is converted to grayscale and processed to detect number plates.
4. **Display Results**: Detected number plates are highlighted with bounding boxes and labels. The region of interest (ROI) can also be displayed separately.
5. **Save Images**: Detected number plates can be saved to a specified directory when the user presses the 's' key.

### Use Cases

- **Automated Toll Systems**: Can be used in toll collection systems to automatically record and verify vehicle registrations.
- **Traffic Monitoring**: Suitable for traffic monitoring systems to log the license plates of vehicles passing through specific locations.
- **Fleet Management**: Assists in monitoring and managing fleet vehicles by recording their number plates during routine checks.

### Getting Started

To get started with the Number Plate Detection Project, follow the setup instructions provided in this README. Ensure you have the Haar cascade file and a functional webcam to test the detection capabilities.

# Number Plate Detection Project Setup

```bash
# Clone the Repository
git clone <repository-url>
cd number_plate_detection_project

# Install Required Dependencies
pip install -r requirements.txt

# Prepare Haar Cascade File
# Download the Haar cascade file for number plate detection.
# Place the haarcascade_russian_plate_number.xml file in the haarcascades/ directory of your project.
# You can download this file from OpenCV's GitHub repository or other sources online.

# Create Save Directory
# Ensure the directory for saving images exists. This directory will be used to store captured images of detected number plates.
mkdir -p data/saved_images

# Run the Detection Script
# Execute the main script to start the number plate detection.
python src/main.py

### Controls
Save Detected Number Plate: Press the s key to save an image of the detected number plate to the data/saved_images/ directory.
Quit Application: Press the q key to exit the application.


```
