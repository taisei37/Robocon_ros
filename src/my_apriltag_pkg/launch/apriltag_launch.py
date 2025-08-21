from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # カメラノード（例: v4l2_camera）
        Node(
            package='v4l2_camera',
            executable='v4l2_camera_node',
            name='usb_cam',
            parameters=[{'video_device': '/dev/video0',
                         'image_size': [640, 480]}],
            output='screen'
        ),

        # AprilTag ノード
        Node(
            package='apriltag_ros',
            executable='apriltag_node',
            name='apriltag',
            remappings=[
                ('/image', '/image_raw'),
                ('/camera_info', '/camera_info')
            ],
            output='screen'
        ),
    ])

