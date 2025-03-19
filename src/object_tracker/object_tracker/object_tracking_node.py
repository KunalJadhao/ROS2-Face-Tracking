import cv2
import rclpy
from rclpy.node import Node
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import os

class FaceTracker(Node):
    def __init__(self):
        super().__init__("face_tracker")
        
        # Load Haar Cascade Classifier
        cascade_path = os.path.join(os.path.dirname(__file__), "haarcascade_frontalface_default.xml")
        self.face_cascade = cv2.CascadeClassifier(cascade_path)
        
        # ROS2 publisher
        self.publisher = self.create_publisher(Image, "tracked_image", 10)
        
        # Open camera
        self.cap = cv2.VideoCapture(0)
        self.bridge = CvBridge()
        self.timer = self.create_timer(0.1, self.process_frame)

    def process_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            self.get_logger().warn("Failed to capture frame")
            return
        
        # Convert frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = self.face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Draw rectangles around detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Show the video feed with face tracking
        cv2.imshow("Face Tracker", frame)
        cv2.waitKey(1)

        # Convert to ROS2 image and publish
        ros_image = self.bridge.cv2_to_imgmsg(frame, encoding="bgr8")
        self.publisher.publish(ros_image)

def main(args=None):
    rclpy.init(args=args)
    node = FaceTracker()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()

