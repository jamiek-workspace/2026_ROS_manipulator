// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from robotis_interfaces:msg/TactileSensor.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "robotis_interfaces/msg/detail/tactile_sensor__rosidl_typesupport_introspection_c.h"
#include "robotis_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "robotis_interfaces/msg/detail/tactile_sensor__functions.h"
#include "robotis_interfaces/msg/detail/tactile_sensor__struct.h"


// Include directives for member types
// Member `sensor_name`
// Member `pressure_names`
#include "rosidl_runtime_c/string_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void robotis_interfaces__msg__TactileSensor__rosidl_typesupport_introspection_c__TactileSensor_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  robotis_interfaces__msg__TactileSensor__init(message_memory);
}

void robotis_interfaces__msg__TactileSensor__rosidl_typesupport_introspection_c__TactileSensor_fini_function(void * message_memory)
{
  robotis_interfaces__msg__TactileSensor__fini(message_memory);
}

size_t robotis_interfaces__msg__TactileSensor__rosidl_typesupport_introspection_c__size_function__TactileSensor__pressure_names(
  const void * untyped_member)
{
  (void)untyped_member;
  return 9;
}

const void * robotis_interfaces__msg__TactileSensor__rosidl_typesupport_introspection_c__get_const_function__TactileSensor__pressure_names(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__String * member =
    (const rosidl_runtime_c__String *)(untyped_member);
  return &member[index];
}

void * robotis_interfaces__msg__TactileSensor__rosidl_typesupport_introspection_c__get_function__TactileSensor__pressure_names(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__String * member =
    (rosidl_runtime_c__String *)(untyped_member);
  return &member[index];
}

void robotis_interfaces__msg__TactileSensor__rosidl_typesupport_introspection_c__fetch_function__TactileSensor__pressure_names(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const rosidl_runtime_c__String * item =
    ((const rosidl_runtime_c__String *)
    robotis_interfaces__msg__TactileSensor__rosidl_typesupport_introspection_c__get_const_function__TactileSensor__pressure_names(untyped_member, index));
  rosidl_runtime_c__String * value =
    (rosidl_runtime_c__String *)(untyped_value);
  *value = *item;
}

void robotis_interfaces__msg__TactileSensor__rosidl_typesupport_introspection_c__assign_function__TactileSensor__pressure_names(
  void * untyped_member, size_t index, const void * untyped_value)
{
  rosidl_runtime_c__String * item =
    ((rosidl_runtime_c__String *)
    robotis_interfaces__msg__TactileSensor__rosidl_typesupport_introspection_c__get_function__TactileSensor__pressure_names(untyped_member, index));
  const rosidl_runtime_c__String * value =
    (const rosidl_runtime_c__String *)(untyped_value);
  *item = *value;
}

size_t robotis_interfaces__msg__TactileSensor__rosidl_typesupport_introspection_c__size_function__TactileSensor__pressure_values(
  const void * untyped_member)
{
  (void)untyped_member;
  return 9;
}

const void * robotis_interfaces__msg__TactileSensor__rosidl_typesupport_introspection_c__get_const_function__TactileSensor__pressure_values(
  const void * untyped_member, size_t index)
{
  const uint8_t * member =
    (const uint8_t *)(untyped_member);
  return &member[index];
}

void * robotis_interfaces__msg__TactileSensor__rosidl_typesupport_introspection_c__get_function__TactileSensor__pressure_values(
  void * untyped_member, size_t index)
{
  uint8_t * member =
    (uint8_t *)(untyped_member);
  return &member[index];
}

void robotis_interfaces__msg__TactileSensor__rosidl_typesupport_introspection_c__fetch_function__TactileSensor__pressure_values(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const uint8_t * item =
    ((const uint8_t *)
    robotis_interfaces__msg__TactileSensor__rosidl_typesupport_introspection_c__get_const_function__TactileSensor__pressure_values(untyped_member, index));
  uint8_t * value =
    (uint8_t *)(untyped_value);
  *value = *item;
}

void robotis_interfaces__msg__TactileSensor__rosidl_typesupport_introspection_c__assign_function__TactileSensor__pressure_values(
  void * untyped_member, size_t index, const void * untyped_value)
{
  uint8_t * item =
    ((uint8_t *)
    robotis_interfaces__msg__TactileSensor__rosidl_typesupport_introspection_c__get_function__TactileSensor__pressure_values(untyped_member, index));
  const uint8_t * value =
    (const uint8_t *)(untyped_value);
  *item = *value;
}

static rosidl_typesupport_introspection_c__MessageMember robotis_interfaces__msg__TactileSensor__rosidl_typesupport_introspection_c__TactileSensor_message_member_array[3] = {
  {
    "sensor_name",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(robotis_interfaces__msg__TactileSensor, sensor_name),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "pressure_names",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    true,  // is array
    9,  // array size
    false,  // is upper bound
    offsetof(robotis_interfaces__msg__TactileSensor, pressure_names),  // bytes offset in struct
    NULL,  // default value
    robotis_interfaces__msg__TactileSensor__rosidl_typesupport_introspection_c__size_function__TactileSensor__pressure_names,  // size() function pointer
    robotis_interfaces__msg__TactileSensor__rosidl_typesupport_introspection_c__get_const_function__TactileSensor__pressure_names,  // get_const(index) function pointer
    robotis_interfaces__msg__TactileSensor__rosidl_typesupport_introspection_c__get_function__TactileSensor__pressure_names,  // get(index) function pointer
    robotis_interfaces__msg__TactileSensor__rosidl_typesupport_introspection_c__fetch_function__TactileSensor__pressure_names,  // fetch(index, &value) function pointer
    robotis_interfaces__msg__TactileSensor__rosidl_typesupport_introspection_c__assign_function__TactileSensor__pressure_names,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "pressure_values",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    true,  // is array
    9,  // array size
    false,  // is upper bound
    offsetof(robotis_interfaces__msg__TactileSensor, pressure_values),  // bytes offset in struct
    NULL,  // default value
    robotis_interfaces__msg__TactileSensor__rosidl_typesupport_introspection_c__size_function__TactileSensor__pressure_values,  // size() function pointer
    robotis_interfaces__msg__TactileSensor__rosidl_typesupport_introspection_c__get_const_function__TactileSensor__pressure_values,  // get_const(index) function pointer
    robotis_interfaces__msg__TactileSensor__rosidl_typesupport_introspection_c__get_function__TactileSensor__pressure_values,  // get(index) function pointer
    robotis_interfaces__msg__TactileSensor__rosidl_typesupport_introspection_c__fetch_function__TactileSensor__pressure_values,  // fetch(index, &value) function pointer
    robotis_interfaces__msg__TactileSensor__rosidl_typesupport_introspection_c__assign_function__TactileSensor__pressure_values,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers robotis_interfaces__msg__TactileSensor__rosidl_typesupport_introspection_c__TactileSensor_message_members = {
  "robotis_interfaces__msg",  // message namespace
  "TactileSensor",  // message name
  3,  // number of fields
  sizeof(robotis_interfaces__msg__TactileSensor),
  false,  // has_any_key_member_
  robotis_interfaces__msg__TactileSensor__rosidl_typesupport_introspection_c__TactileSensor_message_member_array,  // message members
  robotis_interfaces__msg__TactileSensor__rosidl_typesupport_introspection_c__TactileSensor_init_function,  // function to initialize message memory (memory has to be allocated)
  robotis_interfaces__msg__TactileSensor__rosidl_typesupport_introspection_c__TactileSensor_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t robotis_interfaces__msg__TactileSensor__rosidl_typesupport_introspection_c__TactileSensor_message_type_support_handle = {
  0,
  &robotis_interfaces__msg__TactileSensor__rosidl_typesupport_introspection_c__TactileSensor_message_members,
  get_message_typesupport_handle_function,
  &robotis_interfaces__msg__TactileSensor__get_type_hash,
  &robotis_interfaces__msg__TactileSensor__get_type_description,
  &robotis_interfaces__msg__TactileSensor__get_type_description_sources,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_robotis_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robotis_interfaces, msg, TactileSensor)() {
  if (!robotis_interfaces__msg__TactileSensor__rosidl_typesupport_introspection_c__TactileSensor_message_type_support_handle.typesupport_identifier) {
    robotis_interfaces__msg__TactileSensor__rosidl_typesupport_introspection_c__TactileSensor_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &robotis_interfaces__msg__TactileSensor__rosidl_typesupport_introspection_c__TactileSensor_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
