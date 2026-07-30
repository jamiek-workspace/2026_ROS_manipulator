// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from robotis_interfaces:msg/MoveL.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "robotis_interfaces/msg/detail/move_l__rosidl_typesupport_introspection_c.h"
#include "robotis_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "robotis_interfaces/msg/detail/move_l__functions.h"
#include "robotis_interfaces/msg/detail/move_l__struct.h"


// Include directives for member types
// Member `pose`
#include "geometry_msgs/msg/pose_stamped.h"
// Member `pose`
#include "geometry_msgs/msg/detail/pose_stamped__rosidl_typesupport_introspection_c.h"
// Member `time_from_start`
#include "builtin_interfaces/msg/duration.h"
// Member `time_from_start`
#include "builtin_interfaces/msg/detail/duration__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void robotis_interfaces__msg__MoveL__rosidl_typesupport_introspection_c__MoveL_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  robotis_interfaces__msg__MoveL__init(message_memory);
}

void robotis_interfaces__msg__MoveL__rosidl_typesupport_introspection_c__MoveL_fini_function(void * message_memory)
{
  robotis_interfaces__msg__MoveL__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember robotis_interfaces__msg__MoveL__rosidl_typesupport_introspection_c__MoveL_message_member_array[2] = {
  {
    "pose",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(robotis_interfaces__msg__MoveL, pose),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "time_from_start",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(robotis_interfaces__msg__MoveL, time_from_start),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers robotis_interfaces__msg__MoveL__rosidl_typesupport_introspection_c__MoveL_message_members = {
  "robotis_interfaces__msg",  // message namespace
  "MoveL",  // message name
  2,  // number of fields
  sizeof(robotis_interfaces__msg__MoveL),
  false,  // has_any_key_member_
  robotis_interfaces__msg__MoveL__rosidl_typesupport_introspection_c__MoveL_message_member_array,  // message members
  robotis_interfaces__msg__MoveL__rosidl_typesupport_introspection_c__MoveL_init_function,  // function to initialize message memory (memory has to be allocated)
  robotis_interfaces__msg__MoveL__rosidl_typesupport_introspection_c__MoveL_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t robotis_interfaces__msg__MoveL__rosidl_typesupport_introspection_c__MoveL_message_type_support_handle = {
  0,
  &robotis_interfaces__msg__MoveL__rosidl_typesupport_introspection_c__MoveL_message_members,
  get_message_typesupport_handle_function,
  &robotis_interfaces__msg__MoveL__get_type_hash,
  &robotis_interfaces__msg__MoveL__get_type_description,
  &robotis_interfaces__msg__MoveL__get_type_description_sources,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_robotis_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robotis_interfaces, msg, MoveL)() {
  robotis_interfaces__msg__MoveL__rosidl_typesupport_introspection_c__MoveL_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, geometry_msgs, msg, PoseStamped)();
  robotis_interfaces__msg__MoveL__rosidl_typesupport_introspection_c__MoveL_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, builtin_interfaces, msg, Duration)();
  if (!robotis_interfaces__msg__MoveL__rosidl_typesupport_introspection_c__MoveL_message_type_support_handle.typesupport_identifier) {
    robotis_interfaces__msg__MoveL__rosidl_typesupport_introspection_c__MoveL_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &robotis_interfaces__msg__MoveL__rosidl_typesupport_introspection_c__MoveL_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
