// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from robotis_interfaces:msg/HandJoints.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "robotis_interfaces/msg/detail/hand_joints__functions.h"
#include "robotis_interfaces/msg/detail/hand_joints__struct.hpp"
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

void HandJoints_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) robotis_interfaces::msg::HandJoints(_init);
}

void HandJoints_fini_function(void * message_memory)
{
  auto typed_message = static_cast<robotis_interfaces::msg::HandJoints *>(message_memory);
  typed_message->~HandJoints();
}

size_t size_function__HandJoints__joints(const void * untyped_member)
{
  (void)untyped_member;
  return 21;
}

const void * get_const_function__HandJoints__joints(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::array<geometry_msgs::msg::Point32, 21> *>(untyped_member);
  return &member[index];
}

void * get_function__HandJoints__joints(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::array<geometry_msgs::msg::Point32, 21> *>(untyped_member);
  return &member[index];
}

void fetch_function__HandJoints__joints(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const geometry_msgs::msg::Point32 *>(
    get_const_function__HandJoints__joints(untyped_member, index));
  auto & value = *reinterpret_cast<geometry_msgs::msg::Point32 *>(untyped_value);
  value = item;
}

void assign_function__HandJoints__joints(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<geometry_msgs::msg::Point32 *>(
    get_function__HandJoints__joints(untyped_member, index));
  const auto & value = *reinterpret_cast<const geometry_msgs::msg::Point32 *>(untyped_value);
  item = value;
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember HandJoints_message_member_array[2] = {
  {
    "header",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<std_msgs::msg::Header>(),  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(robotis_interfaces::msg::HandJoints, header),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "joints",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<geometry_msgs::msg::Point32>(),  // members of sub message
    false,  // is key
    true,  // is array
    21,  // array size
    false,  // is upper bound
    offsetof(robotis_interfaces::msg::HandJoints, joints),  // bytes offset in struct
    nullptr,  // default value
    size_function__HandJoints__joints,  // size() function pointer
    get_const_function__HandJoints__joints,  // get_const(index) function pointer
    get_function__HandJoints__joints,  // get(index) function pointer
    fetch_function__HandJoints__joints,  // fetch(index, &value) function pointer
    assign_function__HandJoints__joints,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers HandJoints_message_members = {
  "robotis_interfaces::msg",  // message namespace
  "HandJoints",  // message name
  2,  // number of fields
  sizeof(robotis_interfaces::msg::HandJoints),
  false,  // has_any_key_member_
  HandJoints_message_member_array,  // message members
  HandJoints_init_function,  // function to initialize message memory (memory has to be allocated)
  HandJoints_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t HandJoints_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &HandJoints_message_members,
  get_message_typesupport_handle_function,
  &robotis_interfaces__msg__HandJoints__get_type_hash,
  &robotis_interfaces__msg__HandJoints__get_type_description,
  &robotis_interfaces__msg__HandJoints__get_type_description_sources,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace robotis_interfaces


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<robotis_interfaces::msg::HandJoints>()
{
  return &::robotis_interfaces::msg::rosidl_typesupport_introspection_cpp::HandJoints_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, robotis_interfaces, msg, HandJoints)() {
  return &::robotis_interfaces::msg::rosidl_typesupport_introspection_cpp::HandJoints_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
