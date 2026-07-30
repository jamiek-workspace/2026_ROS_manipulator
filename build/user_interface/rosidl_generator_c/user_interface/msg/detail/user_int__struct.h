// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from user_interface:msg/UserInt.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "user_interface/msg/user_int.h"


#ifndef USER_INTERFACE__MSG__DETAIL__USER_INT__STRUCT_H_
#define USER_INTERFACE__MSG__DETAIL__USER_INT__STRUCT_H_

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

/// Struct defined in msg/UserInt in the package user_interface.
typedef struct user_interface__msg__UserInt
{
  std_msgs__msg__Header header;
  int32_t user_int;
  int32_t user_int2;
  int32_t user_int3;
} user_interface__msg__UserInt;

// Struct for a sequence of user_interface__msg__UserInt.
typedef struct user_interface__msg__UserInt__Sequence
{
  user_interface__msg__UserInt * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} user_interface__msg__UserInt__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // USER_INTERFACE__MSG__DETAIL__USER_INT__STRUCT_H_
