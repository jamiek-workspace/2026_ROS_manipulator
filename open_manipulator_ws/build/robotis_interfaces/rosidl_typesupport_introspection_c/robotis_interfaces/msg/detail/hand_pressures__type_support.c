// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from robotis_interfaces:msg/HandPressures.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "robotis_interfaces/msg/detail/hand_pressures__rosidl_typesupport_introspection_c.h"
#include "robotis_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "robotis_interfaces/msg/detail/hand_pressures__functions.h"
#include "robotis_interfaces/msg/detail/hand_pressures__struct.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/header.h"
// Member `header`
#include "std_msgs/msg/detail/header__rosidl_typesupport_introspection_c.h"
// Member `hand_name`
#include "rosidl_runtime_c/string_functions.h"
// Member `sensors`
#include "robotis_interfaces/msg/tactile_sensor.h"
// Member `sensors`
#include "robotis_interfaces/msg/detail/tactile_sensor__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void robotis_interfaces__msg__HandPressures__rosidl_typesupport_introspection_c__HandPressures_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  robotis_interfaces__msg__HandPressures__init(message_memory);
}

void robotis_interfaces__msg__HandPressures__rosidl_typesupport_introspection_c__HandPressures_fini_function(void * message_memory)
{
  robotis_interfaces__msg__HandPressures__fini(message_memory);
}

size_t robotis_interfaces__msg__HandPressures__rosidl_typesupport_introspection_c__size_function__HandPressures__sensors(
  const void * untyped_member)
{
  const robotis_interfaces__msg__TactileSensor__Sequence * member =
    (const robotis_interfaces__msg__TactileSensor__Sequence *)(untyped_member);
  return member->size;
}

const void * robotis_interfaces__msg__HandPressures__rosidl_typesupport_introspection_c__get_const_function__HandPressures__sensors(
  const void * untyped_member, size_t index)
{
  const robotis_interfaces__msg__TactileSensor__Sequence * member =
    (const robotis_interfaces__msg__TactileSensor__Sequence *)(untyped_member);
  return &member->data[index];
}

void * robotis_interfaces__msg__HandPressures__rosidl_typesupport_introspection_c__get_function__HandPressures__sensors(
  void * untyped_member, size_t index)
{
  robotis_interfaces__msg__TactileSensor__Sequence * member =
    (robotis_interfaces__msg__TactileSensor__Sequence *)(untyped_member);
  return &member->data[index];
}

void robotis_interfaces__msg__HandPressures__rosidl_typesupport_introspection_c__fetch_function__HandPressures__sensors(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const robotis_interfaces__msg__TactileSensor * item =
    ((const robotis_interfaces__msg__TactileSensor *)
    robotis_interfaces__msg__HandPressures__rosidl_typesupport_introspection_c__get_const_function__HandPressures__sensors(untyped_member, index));
  robotis_interfaces__msg__TactileSensor * value =
    (robotis_interfaces__msg__TactileSensor *)(untyped_value);
  *value = *item;
}

void robotis_interfaces__msg__HandPressures__rosidl_typesupport_introspection_c__assign_function__HandPressures__sensors(
  void * untyped_member, size_t index, const void * untyped_value)
{
  robotis_interfaces__msg__TactileSensor * item =
    ((robotis_interfaces__msg__TactileSensor *)
    robotis_interfaces__msg__HandPressures__rosidl_typesupport_introspection_c__get_function__HandPressures__sensors(untyped_member, index));
  const robotis_interfaces__msg__TactileSensor * value =
    (const robotis_interfaces__msg__TactileSensor *)(untyped_value);
  *item = *value;
}

bool robotis_interfaces__msg__HandPressures__rosidl_typesupport_introspection_c__resize_function__HandPressures__sensors(
  void * untyped_member, size_t size)
{
  robotis_interfaces__msg__TactileSensor__Sequence * member =
    (robotis_interfaces__msg__TactileSensor__Sequence *)(untyped_member);
  robotis_interfaces__msg__TactileSensor__Sequence__fini(member);
  return robotis_interfaces__msg__TactileSensor__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember robotis_interfaces__msg__HandPressures__rosidl_typesupport_introspection_c__HandPressures_message_member_array[3] = {
  {
    "header",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(robotis_interfaces__msg__HandPressures, header),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "hand_name",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(robotis_interfaces__msg__HandPressures, hand_name),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "sensors",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is key
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(robotis_interfaces__msg__HandPressures, sensors),  // bytes offset in struct
    NULL,  // default value
    robotis_interfaces__msg__HandPressures__rosidl_typesupport_introspection_c__size_function__HandPressures__sensors,  // size() function pointer
    robotis_interfaces__msg__HandPressures__rosidl_typesupport_introspection_c__get_const_function__HandPressures__sensors,  // get_const(index) function pointer
    robotis_interfaces__msg__HandPressures__rosidl_typesupport_introspection_c__get_function__HandPressures__sensors,  // get(index) function pointer
    robotis_interfaces__msg__HandPressures__rosidl_typesupport_introspection_c__fetch_function__HandPressures__sensors,  // fetch(index, &value) function pointer
    robotis_interfaces__msg__HandPressures__rosidl_typesupport_introspection_c__assign_function__HandPressures__sensors,  // assign(index, value) function pointer
    robotis_interfaces__msg__HandPressures__rosidl_typesupport_introspection_c__resize_function__HandPressures__sensors  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers robotis_interfaces__msg__HandPressures__rosidl_typesupport_introspection_c__HandPressures_message_members = {
  "robotis_interfaces__msg",  // message namespace
  "HandPressures",  // message name
  3,  // number of fields
  sizeof(robotis_interfaces__msg__HandPressures),
  false,  // has_any_key_member_
  robotis_interfaces__msg__HandPressures__rosidl_typesupport_introspection_c__HandPressures_message_member_array,  // message members
  robotis_interfaces__msg__HandPressures__rosidl_typesupport_introspection_c__HandPressures_init_function,  // function to initialize message memory (memory has to be allocated)
  robotis_interfaces__msg__HandPressures__rosidl_typesupport_introspection_c__HandPressures_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t robotis_interfaces__msg__HandPressures__rosidl_typesupport_introspection_c__HandPressures_message_type_support_handle = {
  0,
  &robotis_interfaces__msg__HandPressures__rosidl_typesupport_introspection_c__HandPressures_message_members,
  get_message_typesupport_handle_function,
  &robotis_interfaces__msg__HandPressures__get_type_hash,
  &robotis_interfaces__msg__HandPressures__get_type_description,
  &robotis_interfaces__msg__HandPressures__get_type_description_sources,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_robotis_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robotis_interfaces, msg, HandPressures)() {
  robotis_interfaces__msg__HandPressures__rosidl_typesupport_introspection_c__HandPressures_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, std_msgs, msg, Header)();
  robotis_interfaces__msg__HandPressures__rosidl_typesupport_introspection_c__HandPressures_message_member_array[2].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robotis_interfaces, msg, TactileSensor)();
  if (!robotis_interfaces__msg__HandPressures__rosidl_typesupport_introspection_c__HandPressures_message_type_support_handle.typesupport_identifier) {
    robotis_interfaces__msg__HandPressures__rosidl_typesupport_introspection_c__HandPressures_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &robotis_interfaces__msg__HandPressures__rosidl_typesupport_introspection_c__HandPressures_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
