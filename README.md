# ROS2 Face Tracking with OpenCV

![Project Demo](images/demo.gif)  
*A real-time face tracking system using ROS2 and OpenCV.*

## 🚀 Project Overview
This project implements a real-time **face tracking system** using **ROS2** and **OpenCV**. The system detects and tracks faces using the Haar Cascade Classifier and publishes the tracking data over ROS2 topics.

## 🛠 Features
- **Real-time Face Detection** using OpenCV's Haar Cascade
- **ROS2 Integration** for publishing detected face coordinates
- **Customizable Parameters** for detection sensitivity
- **Visualization** using OpenCV

---

## 📷 Demo
![Face Detection Output](images/face_tracking_output.png)
> *Face tracking in action*

## 🏗 Installation & Setup
### 1️⃣ Prerequisites
Ensure you have the following installed:
- **ROS2 Humble** (or your preferred ROS2 version)
- **Python 3.10+**
- **OpenCV**

### 2️⃣ Clone the Repository
```bash
git clone https://github.com/KunalJadhao/ROS2-Face-Tracking.git
cd ROS2-Face-Tracking
```

### 3️⃣ Build the ROS2 Package
```bash
colcon build --packages-select object_tracker
source install/setup.bash
```

### 4️⃣ Run the Face Tracker Node
```bash
ros2 run object_tracker face_tracker
```

---

## 📂 Directory Structure
```bash
ROS2-Face-Tracking/
├── object_tracking_ws/
│   ├── src/
│   │   ├── object_tracker/
│   │   │   ├── object_tracking_node.py
│   │   │   ├── haarcascade_frontalface_default.xml
│   │   │   ├── ...
│   ├── CMakeLists.txt
│   ├── package.xml
├── images/
│   ├── demo.gif
│   ├── face_tracking_output.png
├── README.md
```

---

## 🖼 Adding Images to README
To add images, follow these steps:
1. **Create an `images/` folder** in your repository.
2. **Add your screenshots or GIFs** to `images/`.
3. **Use this syntax in `README.md`**:
   ```markdown
   ![Description](![]()
)
   ```

---

## 📌 Future Enhancements
✅ Implement **hand tracking** alongside face tracking.  
✅ Improve **tracking accuracy** with deep learning models.  
✅ Integrate with **robotic movement** for real-world applications.  

---

## 📜 License
This project is licensed under the MIT License.

📢 **Contributions & Suggestions are Welcome!** 🚀
