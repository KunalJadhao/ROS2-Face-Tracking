# ROS2 Face Tracking

## 📌 Overview
This project implements real-time face tracking using ROS2 and OpenCV. It utilizes Haarcascade classifiers to detect and track faces from a live camera feed.

## 🚀 Features
- Real-time face tracking using OpenCV.
- ROS2 integration for modularity and scalability.
- Customizable parameters for detection sensitivity.

## 🛠️ Installation
### 1️⃣ Prerequisites
Ensure you have the following installed:
- ROS2 Humble
- OpenCV
- Python 3.10 or later

### 2️⃣ Clone the Repository
```bash
git clone https://github.com/KunalJadhao/ROS2-Face-Tracking.git
cd ROS2-Face-Tracking
```

### 3️⃣ Build and Source the Package
```bash
colcon build --packages-select object_tracker
source install/setup.bash
```

## 🎯 Usage
To start the face tracking node, run:
```bash
ros2 run object_tracker face_tracker
```

## 📜 License
This project is open-source and available under the MIT License.
