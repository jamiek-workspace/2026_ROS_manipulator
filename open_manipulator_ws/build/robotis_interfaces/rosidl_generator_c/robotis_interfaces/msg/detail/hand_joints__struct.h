// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from robotis_interfaces:msg/HandJoints.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "robotis_interfaces/msg/hand_joints.h"


#ifndef ROBOTIS_INTERFACES__MSG__DETAIL__HAND_JOINTS__STRUCT_H_
#define ROBOTIS_INTERFACES__MSG__DETAIL__HAND_JOINTS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

// Constants defined in the message

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.h"
// Member 'joints'
#include "geometry_msgs/msg/detail/point32__struct.h"

/// Struct defined in msg/HandJoints in the package robotis_interfaces.
/**
  * HandJoints.msg
 */
typedef struct robotis_interfaces__msg__HandJoints
{
  /// Standard header for timestamps and frame_id.
  std_msgs__msg__Header header;
  /// Fixed-size array of 21 Point32 structs.
  /// Point32 uses float32 for each coordinate, which is generally
  /// sufficient for non-critical robot localization and saves space
  /// compared to float64 (Point).
  geometry_msgs__msg__Point32 joints[21];
} robotis_interfaces__msg__HandJoints;

// Struct for a sequence of robotis_interfaces__msg__HandJoints.
typedef struct robotis_interfaces__msg__HandJoints__Sequence
{
  robotis_interfaces__msg__HandJoints * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} robotis_interfaces__msg__HandJoints__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ROBOTIS_INTERFACES__MSG__DETAIL__HAND_JOINTS__STRUCT_H_
