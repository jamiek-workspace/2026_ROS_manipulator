// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from robotis_interfaces:msg/HandJoints.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "robotis_interfaces/msg/hand_joints.hpp"


#ifndef ROBOTIS_INTERFACES__MSG__DETAIL__HAND_JOINTS__BUILDER_HPP_
#define ROBOTIS_INTERFACES__MSG__DETAIL__HAND_JOINTS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "robotis_interfaces/msg/detail/hand_joints__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace robotis_interfaces
{

namespace msg
{

namespace builder
{

class Init_HandJoints_joints
{
public:
  explicit Init_HandJoints_joints(::robotis_interfaces::msg::HandJoints & msg)
  : msg_(msg)
  {}
  ::robotis_interfaces::msg::HandJoints joints(::robotis_interfaces::msg::HandJoints::_joints_type arg)
  {
    msg_.joints = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robotis_interfaces::msg::HandJoints msg_;
};

class Init_HandJoints_header
{
public:
  Init_HandJoints_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_HandJoints_joints header(::robotis_interfaces::msg::HandJoints::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_HandJoints_joints(msg_);
  }

private:
  ::robotis_interfaces::msg::HandJoints msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::robotis_interfaces::msg::HandJoints>()
{
  return robotis_interfaces::msg::builder::Init_HandJoints_header();
}

}  // namespace robotis_interfaces

#endif  // ROBOTIS_INTERFACES__MSG__DETAIL__HAND_JOINTS__BUILDER_HPP_
