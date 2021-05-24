### lidar_gmapping_noodom.launch

Gmapping launch file using only the Velodyne VLP-16 LIDAR

Requires the ekf_localization node to be active

### cartographer_demo.launch

Cartographer launch file using only the Velodyne VLP-16 LIDAR

Requires the ekf_localization node to be active

### zed_rtabmap_tutA2.launch

RTABMap using only the ZED2 stereo camera. Odometry is published rtabmap.

zed_no_tf.launch must be launched to avoid duplicate map to odom transforms.

ekf_localization node must be killed to avoid duplicate map to odom transforms.
