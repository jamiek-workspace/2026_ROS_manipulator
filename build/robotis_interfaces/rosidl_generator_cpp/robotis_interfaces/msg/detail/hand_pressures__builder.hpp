// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from robotis_interfaces:msg/HandPressures.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "robotis_interfaces/msg/hand_pressures.hpp"


#ifndef ROBOTIS_INTERFACES__MSG__DETAIL__HAND_PRESSURES__BUILDER_HPP_
#define ROBOTIS_INTERFACES__MSG__DETAIL__HAND_PRESSURES__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "robotis_interfaces/msg/detail/hand_pressures__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace robotis_interfaces
{

namespace msg
{

namespace builder
{

class Init_HandPressures_sensors
{
public:
  explicit Init_HandPressures_sensors(::robotis_interfaces::msg::HandPressures & msg)
  : msg_(msg)
  {}
  ::robotis_interfaces::msg::HandPressures sensors(::robotis_interfaces::msg::HandPressures::_sensors_type arg)
  {
    msg_.sensors = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robotis_interfaces::msg::HandPressures msg_;
};

class Init_HandPressures_hand_name
{
public:
  explicit Init_HandPressures_hand_name(::robotis_interfaces::msg::HandPressures & msg)
  : msg_(msg)
  {}
  Init_HandPressures_sensors hand_name(::robotis_interfaces::msg::HandPressures::_hand_name_type arg)
  {
    msg_.hand_name = std::move(arg);
    return Init_HandPressures_sensors(msg_);
  }

private:
  ::robotis_interfaces::msg::HandPressures msg_;
};

class Init_HandPressures_header
{
public:
  Init_HandPressures_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_HandPressures_hand_name header(::robotis_interfaces::msg::HandPressures::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_HandPressures_hand_name(msg_);
  }

private:
  ::robotis_interfaces::msg::HandPressures msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::robotis_interfaces::msg::HandPressures>()
{
  return robotis_interfaces::msg::builder::Init_HandPressures_header();
}

}  // namespace robotis_interfaces

#endif  // ROBOTIS_INTERFACES__MSG__DETAIL__HAND_PRESSURES__BUILDER_HPP_
