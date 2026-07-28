// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from robotis_interfaces:msg/HandPressures.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "robotis_interfaces/msg/hand_pressures.h"


#ifndef ROBOTIS_INTERFACES__MSG__DETAIL__HAND_PRESSURES__STRUCT_H_
#define ROBOTIS_INTERFACES__MSG__DETAIL__HAND_PRESSURES__STRUCT_H_

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
// Member 'hand_name'
#include "rosidl_runtime_c/string.h"
// Member 'sensors'
#include "robotis_interfaces/msg/detail/tactile_sensor__struct.h"

/// Struct defined in msg/HandPressures in the package robotis_interfaces.
/**
  * Pressure readings for tactile sensors on a ROBOTIS Hand.
 */
typedef struct robotis_interfaces__msg__HandPressures
{
  /// Standard header for timestamps and frame_id.
  std_msgs__msg__Header header;
  /// Logical hand identifier, for example "left" or "right".
  rosidl_runtime_c__String hand_name;
  /// Array of tactile sensor readings.
  robotis_interfaces__msg__TactileSensor__Sequence sensors;
} robotis_interfaces__msg__HandPressures;

// Struct for a sequence of robotis_interfaces__msg__HandPressures.
typedef struct robotis_interfaces__msg__HandPressures__Sequence
{
  robotis_interfaces__msg__HandPressures * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} robotis_interfaces__msg__HandPressures__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ROBOTIS_INTERFACES__MSG__DETAIL__HAND_PRESSURES__STRUCT_H_
