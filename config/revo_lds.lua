-- Copyright 2016 The Cartographer Authors
--
-- Licensed under the Apache License, Version 2.0 (the "License");
-- you may not use this file except in compliance with the License.
-- You may obtain a copy of the License at
--
--      http://www.apache.org/licenses/LICENSE-2.0
--
-- Unless required by applicable law or agreed to in writing, software
-- distributed under the License is distributed on an "AS IS" BASIS,
-- WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
-- See the License for the specific language governing permissions and
-- limitations under the License.

include "map_builder.lua"
include "trajectory_builder.lua"

options = {
  map_builder = MAP_BUILDER,
  trajectory_builder = TRAJECTORY_BUILDER,
  map_frame = "map",
  tracking_frame = "base_link", -- imu_link, If you are using gazebo, use 'base_footprint' (libgazebo_ros_imu's bug)
  published_frame = "odom",
  odom_frame = "odom",
  provide_odom_frame = false,
  publish_frame_projected_to_2d = true,
  use_odometry = true,--sdsd
  use_nav_sat = false,
  use_landmarks = false,
  num_laser_scans = 1,
  num_multi_echo_laser_scans = 0,
  num_subdivisions_per_laser_scan = 1,
  num_point_clouds = 0,
  lookup_transform_timeout_sec = 0.5,--0.2
  submap_publish_period_sec = 0.8,
  pose_publish_period_sec = 5e-3,
  trajectory_publish_period_sec = 30e-3,
  rangefinder_sampling_ratio = 1.,
  odometry_sampling_ratio = 1.,
  fixed_frame_pose_sampling_ratio = 1.,
  imu_sampling_ratio = 1.,
  landmarks_sampling_ratio = 1.,
}
-- 2d建图
MAP_BUILDER.use_trajectory_builder_2d = true
-- 设置成4线程
MAP_BUILDER.num_background_threads = 6
-- 激光雷达最小范围
TRAJECTORY_BUILDER_2D.min_range = 0.3
-- 激光雷达最大范围
TRAJECTORY_BUILDER_2D.max_range = 5
-- 替换max_range 更远的范围
TRAJECTORY_BUILDER_2D.missing_data_ray_length = 5.

-- -- TRAJECTORY_BUILDER_2D.num_accumulated_range_data
-- -- 使用imu数据
TRAJECTORY_BUILDER_2D.use_imu_data = false  --sdsd
TRAJECTORY_BUILDER_2D.use_online_correlative_scan_matching = true
TRAJECTORY_BUILDER_2D.motion_filter.max_angle_radians = math.rad(0.1)
-- 设置偏离代价
TRAJECTORY_BUILDER_2D.ceres_scan_matcher.translation_weight = 1e3
-- 扫描匹配分数阈值，低于设定阈值则补考虑建图
POSE_GRAPH.constraint_builder.min_score = 0.65
-- 低于设定阈值的全局定位不受信任
POSE_GRAPH.constraint_builder.global_localization_min_score = 0.7
-- 每n个节点进行一次优化，设置为0则关闭后端优化
POSE_GRAPH.optimize_every_n_nodes = 60


--pure_localization
-- POSE_GRAPH.optimize_every_n_nodes = 40
-- MAP_BUILDER.num_background_threads = 4
-- POSE_GRAPH.global_sampling_ratio = 0.003
-- POSE_GRAPH.constraint_builder.sampling_ratio = 0.3
-- POSE_GRAPH.constraint_builder.min_score = 0.85
-- POSE_GRAPH.global_constraint_search_after_n_seconds = 30
-- --pure_localization end
-- -- POSE_GRAPH.optimization_problem.log_solver_summary = true

-- MAP_BUILDER.use_trajectory_builder_2d = true

-- TRAJECTORY_BUILDER_2D.submaps.num_range_data = 45
-- TRAJECTORY_BUILDER_2D.min_range = 0.5
-- TRAJECTORY_BUILDER_2D.max_range = 15.
-- TRAJECTORY_BUILDER_2D.missing_data_ray_length = 1.
-- TRAJECTORY_BUILDER_2D.use_imu_data = false
-- --重力常数
-- TRAJECTORY_BUILDER_2D.imu_gravity_time_constant = 9.7883

-- TRAJECTORY_BUILDER_2D.use_online_correlative_scan_matching = true
-- TRAJECTORY_BUILDER_2D.real_time_correlative_scan_matcher.linear_search_window = 0.1
-- --TRAJECTORY_BUILDER_2D.real_time_correlative_scan_matcher.angular_search_window = math.rad(45.)
-- TRAJECTORY_BUILDER_2D.real_time_correlative_scan_matcher.translation_delta_cost_weight = 10.
-- TRAJECTORY_BUILDER_2D.real_time_correlative_scan_matcher.rotation_delta_cost_weight = 1e-1

-- --扫描匹配器可以在不影响分数的情况下自由地前后移动匹配项。我们希望通过使扫描匹配器支付更多费用来偏离这种情况，
-- --从而对这种情况进行惩罚。控制它的两个参数是TRAJECTORY_BUILDER_2D.ceres_scan_matcher.translation_weight和
-- --rotation_weight。越高，将结果从先前移开，换句话说，就越昂贵：扫描匹配必须在要接受的另一个位置产生更高的分数。
-- --TRAJECTORY_BUILDER_2D.ceres_scan_matcher.translation_weight = 2e2
-- --TRAJECTORY_BUILDER_2D.ceres_scan_matcher.rotation_weight = 4e2


-- POSE_GRAPH.optimization_problem.huber_scale = 1e2
--odom
-- POSE_GRAPH.optimization_problem.initial_pose_translation_weight = 1e5
-- POSE_GRAPH.optimization_problem.initial_pose_rotation_weight = 1e5
-- POSE_GRAPH.optimization_problem.odometry_translation_weight = 1e5
-- POSE_GRAPH.optimization_problem.odometry_rotation_weight = 1e1



return options
