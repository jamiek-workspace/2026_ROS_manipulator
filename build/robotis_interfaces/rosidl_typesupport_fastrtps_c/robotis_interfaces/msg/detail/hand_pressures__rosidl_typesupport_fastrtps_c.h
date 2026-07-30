// generated from rosidl_typesupport_fastrtps_c/resource/idl__rosidl_typesupport_fastrtps_c.h.em
// with input from robotis_interfaces:msg/HandPressures.idl
// generated code does not contain a copyright notice
#ifndef ROBOTIS_INTERFACES__MSG__DETAIL__HAND_PRESSURES__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_
#define ROBOTIS_INTERFACES__MSG__DETAIL__HAND_PRESSURES__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_


#include <stddef.h>
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "robotis_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "robotis_interfaces/msg/detail/hand_pressures__struct.h"
#include "fastcdr/Cdr.h"

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_robotis_interfaces
bool cdr_serialize_robotis_interfaces__msg__HandPressures(
  const robotis_interfaces__msg__HandPressures * ros_message,
  eprosima::fastcdr::Cdr & cdr);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_robotis_interfaces
bool cdr_deserialize_robotis_interfaces__msg__HandPressures(
  eprosima::fastcdr::Cdr &,
  robotis_interfaces__msg__HandPressures * ros_message);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_robotis_interfaces
size_t get_serialized_size_robotis_interfaces__msg__HandPressures(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_robotis_interfaces
size_t max_serialized_size_robotis_interfaces__msg__HandPressures(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_robotis_interfaces
bool cdr_serialize_key_robotis_interfaces__msg__HandPressures(
  const robotis_interfaces__msg__HandPressures * ros_message,
  eprosima::fastcdr::Cdr & cdr);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_robotis_interfaces
size_t get_serialized_size_key_robotis_interfaces__msg__HandPressures(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_robotis_interfaces
size_t max_serialized_size_key_robotis_interfaces__msg__HandPressures(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_robotis_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, robotis_interfaces, msg, HandPressures)();

#ifdef __cplusplus
}
#endif

#endif  // ROBOTIS_INTERFACES__MSG__DETAIL__HAND_PRESSURES__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_
