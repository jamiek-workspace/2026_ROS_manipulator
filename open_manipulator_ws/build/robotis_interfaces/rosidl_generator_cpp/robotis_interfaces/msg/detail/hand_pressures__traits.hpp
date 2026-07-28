// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from robotis_interfaces:msg/HandPressures.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "robotis_interfaces/msg/hand_pressures.hpp"


#ifndef ROBOTIS_INTERFACES__MSG__DETAIL__HAND_PRESSURES__TRAITS_HPP_
#define ROBOTIS_INTERFACES__MSG__DETAIL__HAND_PRESSURES__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "robotis_interfaces/msg/detail/hand_pressures__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"
// Member 'sensors'
#include "robotis_interfaces/msg/detail/tactile_sensor__traits.hpp"

namespace robotis_interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const HandPressures & msg,
  std::ostream & out)
{
  out << "{";
  // member: header
  {
    out << "header: ";
    to_flow_style_yaml(msg.header, out);
    out << ", ";
  }

  // member: hand_name
  {
    out << "hand_name: ";
    rosidl_generator_traits::value_to_yaml(msg.hand_name, out);
    out << ", ";
  }

  // member: sensors
  {
    if (msg.sensors.size() == 0) {
      out << "sensors: []";
    } else {
      out << "sensors: [";
      size_t pending_items = msg.sensors.size();
      for (auto item : msg.sensors) {
        to_flow_style_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const HandPressures & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: header
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "header:\n";
    to_block_style_yaml(msg.header, out, indentation + 2);
  }

  // member: hand_name
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "hand_name: ";
    rosidl_generator_traits::value_to_yaml(msg.hand_name, out);
    out << "\n";
  }

  // member: sensors
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.sensors.size() == 0) {
      out << "sensors: []\n";
    } else {
      out << "sensors:\n";
      for (auto item : msg.sensors) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const HandPressures & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace robotis_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use robotis_interfaces::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const robotis_interfaces::msg::HandPressures & msg,
  std::ostream & out, size_t indentation = 0)
{
  robotis_interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use robotis_interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const robotis_interfaces::msg::HandPressures & msg)
{
  return robotis_interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<robotis_interfaces::msg::HandPressures>()
{
  return "robotis_interfaces::msg::HandPressures";
}

template<>
inline const char * name<robotis_interfaces::msg::HandPressures>()
{
  return "robotis_interfaces/msg/HandPressures";
}

template<>
struct has_fixed_size<robotis_interfaces::msg::HandPressures>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<robotis_interfaces::msg::HandPressures>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<robotis_interfaces::msg::HandPressures>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // ROBOTIS_INTERFACES__MSG__DETAIL__HAND_PRESSURES__TRAITS_HPP_
