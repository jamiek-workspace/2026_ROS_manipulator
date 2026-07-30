// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from robotis_interfaces:msg/HandPressures.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "robotis_interfaces/msg/detail/hand_pressures__functions.h"
#include "robotis_interfaces/msg/detail/hand_pressures__struct.hpp"
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

void HandPressures_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) robotis_interfaces::msg::HandPressures(_init);
}

void HandPressures_fini_function(void * message_memory)
{
  auto typed_message = static_cast<robotis_interfaces::msg::HandPressures *>(message_memory);
  typed_message->~HandPressures();
}

size_t size_function__HandPressures__sensors(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<robotis_interfaces::msg::TactileSensor> *>(untyped_member);
  return member->size();
}

const void * get_const_function__HandPressures__sensors(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<robotis_interfaces::msg::TactileSensor> *>(untyped_member);
  return &member[index];
}

void * get_function__HandPressures__sensors(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<robotis_interfaces::msg::TactileSensor> *>(untyped_member);
  return &member[index];
}

void fetch_function__HandPressures__sensors(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const robotis_interfaces::msg::TactileSensor *>(
    get_const_function__HandPressures__sensors(untyped_member, index));
  auto & value = *reinterpret_cast<robotis_interfaces::msg::TactileSensor *>(untyped_value);
  value = item;
}

void assign_function__HandPressures__sensors(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<robotis_interfaces::msg::TactileSensor *>(
    get_function__HandPressures__sensors(untyped_member, index));
  const auto & value = *reinterpret_cast<const robotis_interfaces::msg::TactileSensor *>(untyped_value);
  item = value;
}

void resize_function__HandPressures__sensors(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<robotis_interfaces::msg::TactileSensor> *>(untyped_member);
  member->resize(size);
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember HandPressures_message_member_array[3] = {
  {
    "header",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<std_msgs::msg::Header>(),  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(robotis_interfaces::msg::HandPressures, header),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "hand_name",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(robotis_interfaces::msg::HandPressures, hand_name),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "sensors",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<robotis_interfaces::msg::TactileSensor>(),  // members of sub message
    false,  // is key
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(robotis_interfaces::msg::HandPressures, sensors),  // bytes offset in struct
    nullptr,  // default value
    size_function__HandPressures__sensors,  // size() function pointer
    get_const_function__HandPressures__sensors,  // get_const(index) function pointer
    get_function__HandPressures__sensors,  // get(index) function pointer
    fetch_function__HandPressures__sensors,  // fetch(index, &value) function pointer
    assign_function__HandPressures__sensors,  // assign(index, value) function pointer
    resize_function__HandPressures__sensors  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers HandPressures_message_members = {
  "robotis_interfaces::msg",  // message namespace
  "HandPressures",  // message name
  3,  // number of fields
  sizeof(robotis_interfaces::msg::HandPressures),
  false,  // has_any_key_member_
  HandPressures_message_member_array,  // message members
  HandPressures_init_function,  // function to initialize message memory (memory has to be allocated)
  HandPressures_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t HandPressures_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &HandPressures_message_members,
  get_message_typesupport_handle_function,
  &robotis_interfaces__msg__HandPressures__get_type_hash,
  &robotis_interfaces__msg__HandPressures__get_type_description,
  &robotis_interfaces__msg__HandPressures__get_type_description_sources,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace robotis_interfaces


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<robotis_interfaces::msg::HandPressures>()
{
  return &::robotis_interfaces::msg::rosidl_typesupport_introspection_cpp::HandPressures_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, robotis_interfaces, msg, HandPressures)() {
  return &::robotis_interfaces::msg::rosidl_typesupport_introspection_cpp::HandPressures_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
