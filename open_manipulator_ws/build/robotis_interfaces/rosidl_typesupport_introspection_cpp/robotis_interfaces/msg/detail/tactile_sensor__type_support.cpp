// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from robotis_interfaces:msg/TactileSensor.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "robotis_interfaces/msg/detail/tactile_sensor__functions.h"
#include "robotis_interfaces/msg/detail/tactile_sensor__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace robotis_interfaces
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void TactileSensor_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) robotis_interfaces::msg::TactileSensor(_init);
}

void TactileSensor_fini_function(void * message_memory)
{
  auto typed_message = static_cast<robotis_interfaces::msg::TactileSensor *>(message_memory);
  typed_message->~TactileSensor();
}

size_t size_function__TactileSensor__pressure_names(const void * untyped_member)
{
  (void)untyped_member;
  return 9;
}

const void * get_const_function__TactileSensor__pressure_names(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::array<std::string, 9> *>(untyped_member);
  return &member[index];
}

void * get_function__TactileSensor__pressure_names(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::array<std::string, 9> *>(untyped_member);
  return &member[index];
}

void fetch_function__TactileSensor__pressure_names(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const std::string *>(
    get_const_function__TactileSensor__pressure_names(untyped_member, index));
  auto & value = *reinterpret_cast<std::string *>(untyped_value);
  value = item;
}

void assign_function__TactileSensor__pressure_names(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<std::string *>(
    get_function__TactileSensor__pressure_names(untyped_member, index));
  const auto & value = *reinterpret_cast<const std::string *>(untyped_value);
  item = value;
}

size_t size_function__TactileSensor__pressure_values(const void * untyped_member)
{
  (void)untyped_member;
  return 9;
}

const void * get_const_function__TactileSensor__pressure_values(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::array<uint8_t, 9> *>(untyped_member);
  return &member[index];
}

void * get_function__TactileSensor__pressure_values(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::array<uint8_t, 9> *>(untyped_member);
  return &member[index];
}

void fetch_function__TactileSensor__pressure_values(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const uint8_t *>(
    get_const_function__TactileSensor__pressure_values(untyped_member, index));
  auto & value = *reinterpret_cast<uint8_t *>(untyped_value);
  value = item;
}

void assign_function__TactileSensor__pressure_values(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<uint8_t *>(
    get_function__TactileSensor__pressure_values(untyped_member, index));
  const auto & value = *reinterpret_cast<const uint8_t *>(untyped_value);
  item = value;
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember TactileSensor_message_member_array[3] = {
  {
    "sensor_name",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(robotis_interfaces::msg::TactileSensor, sensor_name),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "pressure_names",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is key
    true,  // is array
    9,  // array size
    false,  // is upper bound
    offsetof(robotis_interfaces::msg::TactileSensor, pressure_names),  // bytes offset in struct
    nullptr,  // default value
    size_function__TactileSensor__pressure_names,  // size() function pointer
    get_const_function__TactileSensor__pressure_names,  // get_const(index) function pointer
    get_function__TactileSensor__pressure_names,  // get(index) function pointer
    fetch_function__TactileSensor__pressure_names,  // fetch(index, &value) function pointer
    assign_function__TactileSensor__pressure_names,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "pressure_values",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is key
    true,  // is array
    9,  // array size
    false,  // is upper bound
    offsetof(robotis_interfaces::msg::TactileSensor, pressure_values),  // bytes offset in struct
    nullptr,  // default value
    size_function__TactileSensor__pressure_values,  // size() function pointer
    get_const_function__TactileSensor__pressure_values,  // get_const(index) function pointer
    get_function__TactileSensor__pressure_values,  // get(index) function pointer
    fetch_function__TactileSensor__pressure_values,  // fetch(index, &value) function pointer
    assign_function__TactileSensor__pressure_values,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers TactileSensor_message_members = {
  "robotis_interfaces::msg",  // message namespace
  "TactileSensor",  // message name
  3,  // number of fields
  sizeof(robotis_interfaces::msg::TactileSensor),
  false,  // has_any_key_member_
  TactileSensor_message_member_array,  // message members
  TactileSensor_init_function,  // function to initialize message memory (memory has to be allocated)
  TactileSensor_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t TactileSensor_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &TactileSensor_message_members,
  get_message_typesupport_handle_function,
  &robotis_interfaces__msg__TactileSensor__get_type_hash,
  &robotis_interfaces__msg__TactileSensor__get_type_description,
  &robotis_interfaces__msg__TactileSensor__get_type_description_sources,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace robotis_interfaces


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<robotis_interfaces::msg::TactileSensor>()
{
  return &::robotis_interfaces::msg::rosidl_typesupport_introspection_cpp::TactileSensor_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, robotis_interfaces, msg, TactileSensor)() {
  return &::robotis_interfaces::msg::rosidl_typesupport_introspection_cpp::TactileSensor_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
