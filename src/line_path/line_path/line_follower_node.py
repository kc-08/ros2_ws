import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from px4_msgs.msg import VehicleLocalPosition
import numpy as np
import cv2

class LineFollowerNode(Node):
    def __init__(self):
        super().__init__('line_follower')
        self.height = 1

        self.position_sub = self.create_subscription(VehicleLocalPosition, '/fmu/out/vehicle_local_position', self.height_callback, 10)
        # self.image_sub = self.create_subscription(Image, '/camera/image_raw', self.image_callback, 10)
        self.line_pub = self.create_publisher(Image, '/camera/line_reg', 10)

    # def height_callback(self, msg):
    #     height = msg.z
    #     self.height = height


    def image_callback(self, msg):
        h = self.height
        img = msg.data
        kernel = np.ones((3,3), np.uint8)
        cols, rows = img.shape[:2]
        threshold_img = cv2.threshold(img, 240, 255, cv2.THRESH_BINARY)
        threshold_img = cv2.dilate(threshold_img, kernel, iterations = 3)
        contours = cv2.findContours(threshold_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        usable_contours = []
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area >= rows*cols*h*0.1:
                usable_contours.append(cnt)
        cnt_only_image = np.zeros((rows, cols, 3), np.uint8)
        cnt_only_image = cv2.drawContours(cnt_only_image, usable_contours, -1, (255,255,255), 3)
        white_line = np.argwhere(cnt_only_image)
        x_data = white_line[:,1]
        y_data = white_line[:,0]
        x_mean = np.mean(x_data)
        y_mean = np.mean(y_data)
        xy_mean = np.mean((x_data*y_data))
        x_squared_mean = np.mean((x_data**2))
        m = (x_mean*y_mean - xy_mean)/(x_mean*x_mean - x_squared_mean)
        b = y_mean -m*x_mean
        y1 = max(0, min(b, cols))
        y2 = max(0, min(m*rows+b, cols))
        x1 = (y1-b)/m
        x2 = (y2-b)/m
        cv2.line(threshold_img, (x1,y1), (x2,y2), (0,0,255), 2)



def main(args = None):
    rclpy.init()
    node = LineFollowerNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()