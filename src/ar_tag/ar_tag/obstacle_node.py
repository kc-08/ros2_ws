import rclpy
from rclpy.node import Node 
import numpy as np
import cv2
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy, DurabilityPolicy
from px4_msgs.msg import TrajectorySetpoint

class ObstacleNode(Node):
    def __init__(self):
        super().__init__('Obstacle_avoider')
        #Constants
        self.CIRCLE_RADIUS = 1.101725
        self.BANNER_OUTER_HEIGHT = 1.16332
        self.BANNER_THICKNESS = 0.52705
        self.ARCH_INNER_HEIGHT = 1.84531
        self.ARCH_OUTER_HEIGHT = 2.14503
        self.ARCH_THICKNESS = self.ARCH_OUTER_HEIGHT - self.ARCH_INNER_HEIGHT
        self.ARCH_LENGTH = 2.11709
        self.KP_Z = 0.2


        #TEST VALUES NOT CORRECT
        self.tags = {98:'ct', 94: 'cl'} #ct = circle top; cb = circle bottom; cl = circle left; cr = circle right; b = banner; al = arch left; ar = arch left; at = arch top
        qos_profile = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            durability=DurabilityPolicy.TRANSIENT_LOCAL,
            history=HistoryPolicy.KEEP_LAST,
            depth=1
        )
        self.pose_sub = self.create_subscription(PoseStamped, '/mavros/local_position/pose', self.pose_callback, 10)
        self.vel_pub = self.create_publisher(TrajectorySetpoint, '/velocity', qos_profile)

    def pose_callback(self,msg):
        self.y = msg.pose.position.x
        self.z = msg.pose.position.y
        self.x = msg.pose.position.z
        tag_id = int(msg.header.frame_id)
        r = self.CIRCLE_RADIUS
        bh = self.BANNER_OUTER_HEIGHT
        ah = self.ARCH_INNER_HEIGHT
        al = self.ARCH_LENGTH
        tag_type = self.tags[tag_id]
        if tag_type == 'ct':
            z_des = r
        elif tag_type == 'cb':
            z_des = -r
        elif tag_type == 'b':
            z_des = ((bh-self.BANNER_THICKNESS)/2)+ self.BANNER_THICKNESS
        elif tag_type == 'at':
            z_des = (ah/2) + self.ARCH_THICKNESS
        elif tag_type in ['cl', 'cr',  'al', 'ar']:
            z_des = 0
        vz = self.KP_Z * (self.z - z_des)
        msg = TrajectorySetpoint()
        # msg.position = [float('nan'), float('nan'), float('nan')]
        # msg.acceleration = [float('nan'), float('nan'), float('nan')]
        # msg.yaw = float('nan')
        # msg.yawspeed = float('nan')
        msg.velocity = [0.0, 0.0, vz] #bd frame 
        msg.timestamp = int(self.get_clock().now().nanoseconds / 1000)
        self.vel_pub.publish(msg)
        
def main(args = None):
    rclpy.init()
    node = ObstacleNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
