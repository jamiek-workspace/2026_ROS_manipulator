// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from robotis_interfaces:msg/TactileSensor.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "robotis_interfaces/msg/tactile_sensor.hpp"


#ifndef ROBOTIS_INTERFACES__MSG__DETAIL__TACTILE_SENSOR__BUILDER_HPP_
#define ROBOTIS_INTERFACES__MSG__DETAIL__TACTILE_SENSOR__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "robotis_interfaces/msg/detail/tactile_sensor__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace robotis_interfaces
{

namespace msg
{

namespace builder
{

class Init_TactileSensor_pressure_values
{
public:
  explicit Init_TactileSensor_pressure_values(::robotis_interfaces::msg::TactileSensor & msg)
  : msg_(msg)
  {}
  ::robotis_interfaces::msg::TactileSensor pressure_values(::robotis_interfaces::msg::TactileSensor::_pressure_values_type arg)
  {
    msg_.pressure_values = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robotis_interfaces::msg::TactileSensor msg_;
};

class Init_TactileSensor_pressure_names
{
public:
  explicit Init_TactileSensor_pressure_names(::robotis_interfaces::msg::TactileSensor & msg)
  : msg_(msg)
  {}
  Init_TactileSensor_pressure_values pressure_names(::robotis_interfaces::msg::TactileSensor::_pressure_names_type arg)
  {
    msg_.pressure_names = std::move(arg);
    return Init_TactileSensor_pressure_values(msg_);
  }

private:
  ::robotis_interfaces::msg::TactileSensor msg_;
};

class Init_TactileSensor_sensor_name
{
public:
  Init_TactileSensor_sensor_name()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_TactileSensor_pressure_names sensor_name(::robotis_interfaces::msg::TactileSensor::_sensor_name_type arg)
  {
    msg_.sensor_name = std::move(arg);
    return Init_TactileSensor_pressure_names(msg_);
  }

private:
  ::robotis_interfaces::msg::TactileSensor msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::robotis_interfaces::msg::TactileSensor>()
{
  return robotis_interfaces::msg::builder::Init_TactileSensor_sensor_name();
}

}  // namespace robotis_interfaces

#endif  // ROBOTIS_INTERFACES__MSG__DETAIL__TACTILE_SENSOR__BUILDER_HPP_
