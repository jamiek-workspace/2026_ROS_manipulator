// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from robotis_interfaces:msg/MoveL.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "robotis_interfaces/msg/move_l.h"


#ifndef ROBOTIS_INTERFACES__MSG__DETAIL__MOVE_L__STRUCT_H_
#define ROBOTIS_INTERFACES__MSG__DETAIL__MOVE_L__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

// Constants defined in the message

// Include directives for member types
// Member 'pose'
#include "geometry_msgs/msg/detail/pose_stamped__struct.h"
// Member 'time_from_start'
#include "builtin_interfaces/msg/detail/duration__struct.h"

/// Struct defined in msg/MoveL in the package robotis_interfaces.
/**
  * Target end-effector pose for the linear move command.
 */
typedef struct robotis_interfaces__msg__MoveL
{
  geometry_msgs__msg__PoseStamped pose;
  /// Desired time to reach the target pose from the current pose.
  builtin_interfaces__msg__Duration time_from_start;
} robotis_interfaces__msg__MoveL;

// Struct for a sequence of robotis_interfaces__msg__MoveL.
typedef struct robotis_interfaces__msg__MoveL__Sequence
{
  robotis_interfaces__msg__MoveL * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} robotis_interfaces__msg__MoveL__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ROBOTIS_INTERFACES__MSG__DETAIL__MOVE_L__STRUCT_H_
