// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from robotis_interfaces:msg/HandJoints.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "robotis_interfaces/msg/detail/hand_joints__rosidl_typesupport_introspection_c.h"
#include "robotis_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "robotis_interfaces/msg/detail/hand_joints__functions.h"
#include "robotis_interfaces/msg/detail/hand_joints__struct.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/header.h"
// Member `header`
#include "std_msgs/msg/detail/header__rosidl_typesupport_introspection_c.h"
// Member `joints`
#include "geometry_msgs/msg/point32.h"
// Member `joints`
#include "geometry_msgs/msg/detail/point32__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void robotis_interfaces__msg__HandJoints__rosidl_typesupport_introspection_c__HandJoints_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  robotis_interfaces__msg__HandJoints__init(message_memory);
}

void robotis_interfaces__msg__HandJoints__rosidl_typesupport_introspection_c__HandJoints_fini_function(void * message_memory)
{
  robotis_interfaces__msg__HandJoints__fini(message_memory);
}

size_t robotis_interfaces__msg__HandJoints__rosidl_typesupport_introspection_c__size_function__HandJoints__joints(
  const void * untyped_member)
{
  (void)untyped_member;
  return 21;
}

const void * robotis_interfaces__msg__HandJoints__rosidl_typesupport_introspection_c__get_const_function__HandJoints__joints(
  const void * untyped_member, size_t index)
{
  const geometry_msgs__msg__Point32 * member =
    (const geometry_msgs__msg__Point32 *)(untyped_member);
  return &member[index];
}

void * robotis_interfaces__msg__HandJoints__rosidl_typesupport_introspection_c__get_function__HandJoints__joints(
  void * untyped_member, size_t index)
{
  geometry_msgs__msg__Point32 * member =
    (geometry_msgs__msg__Point32 *)(untyped_member);
  return &member[index];
}

void robotis_interfaces__msg__HandJoints__rosidl_typesupport_introspection_c__fetch_function__HandJoints__joints(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const geometry_msgs__msg__Point32 * item =
    ((const geometry_msgs__msg__Point32 *)
    robotis_interfaces__msg__HandJoints__rosidl_typesupport_introspection_c__get_const_function__HandJoints__joints(untyped_member, index));
  geometry_msgs__msg__Point32 * value =
    (geometry_msgs__msg__Point32 *)(untyped_value);
  *value = *item;
}

void robotis_interfaces__msg__HandJoints__rosidl_typesupport_introspection_c__assign_function__HandJoints__joints(
  void * untyped_member, size_t index, const void * untyped_value)
{
  geometry_msgs__msg__Point32 * item =
    ((geometry_msgs__msg__Point32 *)
    robotis_interfaces__msg__HandJoints__rosidl_typesupport_introspection_c__get_function__HandJoints__joints(untyped_member, index));
  const geometry_msgs__msg__Point32 * value =
    (const geometry_msgs__msg__Point32 *)(untyped_value);
  *item = *value;
}

static rosidl_typesupport_introspection_c__MessageMember robotis_interfaces__msg__HandJoints__rosidl_typesupport_introspection_c__HandJoints_message_member_array[2] = {
  {
    "header",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(robotis_interfaces__msg__HandJoints, header),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "joints",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is key
    true,  // is array
    21,  // array size
    false,  // is upper bound
    offsetof(robotis_interfaces__msg__HandJoints, joints),  // bytes offset in struct
    NULL,  // default value
    robotis_interfaces__msg__HandJoints__rosidl_typesupport_introspection_c__size_function__HandJoints__joints,  // size() function pointer
    robotis_interfaces__msg__HandJoints__rosidl_typesupport_introspection_c__get_const_function__HandJoints__joints,  // get_const(index) function pointer
    robotis_interfaces__msg__HandJoints__rosidl_typesupport_introspection_c__get_function__HandJoints__joints,  // get(index) function pointer
    robotis_interfaces__msg__HandJoints__rosidl_typesupport_introspection_c__fetch_function__HandJoints__joints,  // fetch(index, &value) function pointer
    robotis_interfaces__msg__HandJoints__rosidl_typesupport_introspection_c__assign_function__HandJoints__joints,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers robotis_interfaces__msg__HandJoints__rosidl_typesupport_introspection_c__HandJoints_message_members = {
  "robotis_interfaces__msg",  // message namespace
  "HandJoints",  // message name
  2,  // number of fields
  sizeof(robotis_interfaces__msg__HandJoints),
  false,  // has_any_key_member_
  robotis_interfaces__msg__HandJoints__rosidl_typesupport_introspection_c__HandJoints_message_member_array,  // message members
  robotis_interfaces__msg__HandJoints__rosidl_typesupport_introspection_c__HandJoints_init_function,  // function to initialize message memory (memory has to be allocated)
  robotis_interfaces__msg__HandJoints__rosidl_typesupport_introspection_c__HandJoints_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t robotis_interfaces__msg__HandJoints__rosidl_typesupport_introspection_c__HandJoints_message_type_support_handle = {
  0,
  &robotis_interfaces__msg__HandJoints__rosidl_typesupport_introspection_c__HandJoints_message_members,
  get_message_typesupport_handle_function,
  &robotis_interfaces__msg__HandJoints__get_type_hash,
  &robotis_interfaces__msg__HandJoints__get_type_description,
  &robotis_interfaces__msg__HandJoints__get_type_description_sources,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_robotis_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robotis_interfaces, msg, HandJoints)() {
  robotis_interfaces__msg__HandJoints__rosidl_typesupport_introspection_c__HandJoints_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, std_msgs, msg, Header)();
  robotis_interfaces__msg__HandJoints__rosidl_typesupport_introspection_c__HandJoints_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, geometry_msgs, msg, Point32)();
  if (!robotis_interfaces__msg__HandJoints__rosidl_typesupport_introspection_c__HandJoints_message_type_support_handle.typesupport_identifier) {
    robotis_interfaces__msg__HandJoints__rosidl_typesupport_introspection_c__HandJoints_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &robotis_interfaces__msg__HandJoints__rosidl_typesupport_introspection_c__HandJoints_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
