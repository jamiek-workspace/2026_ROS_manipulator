// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from robotis_interfaces:msg/TactileSensor.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "robotis_interfaces/msg/tactile_sensor.h"


#ifndef ROBOTIS_INTERFACES__MSG__DETAIL__TACTILE_SENSOR__STRUCT_H_
#define ROBOTIS_INTERFACES__MSG__DETAIL__TACTILE_SENSOR__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

// Constants defined in the message

// Include directives for member types
// Member 'sensor_name'
// Member 'pressure_names'
#include "rosidl_runtime_c/string.h"

/// Struct defined in msg/TactileSensor in the package robotis_interfaces.
/**
  * TactileSensor.msg
 */
typedef struct robotis_interfaces__msg__TactileSensor
{
  /// Name of the tactile sensor source.
  rosidl_runtime_c__String sensor_name;
  /// Present pressure values (0-255) from the tactile sensor (3x3 grid base)
  /// Pressure indices are ordered from top to bottom, and from left to right within each row.
  rosidl_runtime_c__String pressure_names[9];
  uint8_t pressure_values[9];
} robotis_interfaces__msg__TactileSensor;

// Struct for a sequence of robotis_interfaces__msg__TactileSensor.
typedef struct robotis_interfaces__msg__TactileSensor__Sequence
{
  robotis_interfaces__msg__TactileSensor * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} robotis_interfaces__msg__TactileSensor__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ROBOTIS_INTERFACES__MSG__DETAIL__TACTILE_SENSOR__STRUCT_H_
