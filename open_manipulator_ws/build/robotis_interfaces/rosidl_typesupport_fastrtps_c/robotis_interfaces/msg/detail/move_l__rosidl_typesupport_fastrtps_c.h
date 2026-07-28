// generated from rosidl_typesupport_fastrtps_c/resource/idl__rosidl_typesupport_fastrtps_c.h.em
// with input from robotis_interfaces:msg/MoveL.idl
// generated code does not contain a copyright notice
#ifndef ROBOTIS_INTERFACES__MSG__DETAIL__MOVE_L__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_
#define ROBOTIS_INTERFACES__MSG__DETAIL__MOVE_L__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_


#include <stddef.h>
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "robotis_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "robotis_interfaces/msg/detail/move_l__struct.h"
#include "fastcdr/Cdr.h"

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_robotis_interfaces
bool cdr_serialize_robotis_interfaces__msg__MoveL(
  const robotis_interfaces__msg__MoveL * ros_message,
  eprosima::fastcdr::Cdr & cdr);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_robotis_interfaces
bool cdr_deserialize_robotis_interfaces__msg__MoveL(
  eprosima::fastcdr::Cdr &,
  robotis_interfaces__msg__MoveL * ros_message);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_robotis_interfaces
size_t get_serialized_size_robotis_interfaces__msg__MoveL(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_robotis_interfaces
size_t max_serialized_size_robotis_interfaces__msg__MoveL(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_robotis_interfaces
bool cdr_serialize_key_robotis_interfaces__msg__MoveL(
  const robotis_interfaces__msg__MoveL * ros_message,
  eprosima::fastcdr::Cdr & cdr);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_robotis_interfaces
size_t get_serialized_size_key_robotis_interfaces__msg__MoveL(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_robotis_interfaces
size_t max_serialized_size_key_robotis_interfaces__msg__MoveL(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_robotis_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, robotis_interfaces, msg, MoveL)();

#ifdef __cplusplus
}
#endif

#endif  // ROBOTIS_INTERFACES__MSG__DETAIL__MOVE_L__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_
