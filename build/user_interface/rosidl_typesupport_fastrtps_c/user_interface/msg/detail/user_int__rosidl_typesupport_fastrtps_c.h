// generated from rosidl_typesupport_fastrtps_c/resource/idl__rosidl_typesupport_fastrtps_c.h.em
// with input from user_interface:msg/UserInt.idl
// generated code does not contain a copyright notice
#ifndef USER_INTERFACE__MSG__DETAIL__USER_INT__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_
#define USER_INTERFACE__MSG__DETAIL__USER_INT__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_


#include <stddef.h>
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "user_interface/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "user_interface/msg/detail/user_int__struct.h"
#include "fastcdr/Cdr.h"

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_user_interface
bool cdr_serialize_user_interface__msg__UserInt(
  const user_interface__msg__UserInt * ros_message,
  eprosima::fastcdr::Cdr & cdr);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_user_interface
bool cdr_deserialize_user_interface__msg__UserInt(
  eprosima::fastcdr::Cdr &,
  user_interface__msg__UserInt * ros_message);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_user_interface
size_t get_serialized_size_user_interface__msg__UserInt(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_user_interface
size_t max_serialized_size_user_interface__msg__UserInt(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_user_interface
bool cdr_serialize_key_user_interface__msg__UserInt(
  const user_interface__msg__UserInt * ros_message,
  eprosima::fastcdr::Cdr & cdr);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_user_interface
size_t get_serialized_size_key_user_interface__msg__UserInt(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_user_interface
size_t max_serialized_size_key_user_interface__msg__UserInt(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_user_interface
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, user_interface, msg, UserInt)();

#ifdef __cplusplus
}
#endif

#endif  // USER_INTERFACE__MSG__DETAIL__USER_INT__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_
