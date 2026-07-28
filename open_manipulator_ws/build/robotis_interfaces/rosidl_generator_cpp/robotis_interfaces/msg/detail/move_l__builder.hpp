// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from robotis_interfaces:msg/MoveL.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "robotis_interfaces/msg/move_l.hpp"


#ifndef ROBOTIS_INTERFACES__MSG__DETAIL__MOVE_L__BUILDER_HPP_
#define ROBOTIS_INTERFACES__MSG__DETAIL__MOVE_L__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "robotis_interfaces/msg/detail/move_l__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace robotis_interfaces
{

namespace msg
{

namespace builder
{

class Init_MoveL_time_from_start
{
public:
  explicit Init_MoveL_time_from_start(::robotis_interfaces::msg::MoveL & msg)
  : msg_(msg)
  {}
  ::robotis_interfaces::msg::MoveL time_from_start(::robotis_interfaces::msg::MoveL::_time_from_start_type arg)
  {
    msg_.time_from_start = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robotis_interfaces::msg::MoveL msg_;
};

class Init_MoveL_pose
{
public:
  Init_MoveL_pose()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_MoveL_time_from_start pose(::robotis_interfaces::msg::MoveL::_pose_type arg)
  {
    msg_.pose = std::move(arg);
    return Init_MoveL_time_from_start(msg_);
  }

private:
  ::robotis_interfaces::msg::MoveL msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::robotis_interfaces::msg::MoveL>()
{
  return robotis_interfaces::msg::builder::Init_MoveL_pose();
}

}  // namespace robotis_interfaces

#endif  // ROBOTIS_INTERFACES__MSG__DETAIL__MOVE_L__BUILDER_HPP_
