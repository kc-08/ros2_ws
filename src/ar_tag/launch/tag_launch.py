from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    AR_tag_detector_node = Node(
        package='ar_tag',
        executable='AR_tag_detector_node',
        output='screen'
    )

    obstacle_node = Node(
        package = 'ar_tag',
        executable = 'obstacle_node',
        output = 'screen'
    )

    return LaunchDescription([AR_tag_detector_node, obstacle_node])