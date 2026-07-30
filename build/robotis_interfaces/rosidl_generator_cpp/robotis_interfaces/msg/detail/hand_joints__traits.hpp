// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from robotis_interfaces:msg/HandJoints.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "robotis_interfaces/msg/hand_joints.hpp"


#ifndef ROBOTIS_INTERFACES__MSG__DETAIL__HAND_JOINTS__TRAITS_HPP_
#define ROBOTIS_INTERFACES__MSG__DETAIL__HAND_JOINTS__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "robotis_interfaces/msg/detail/hand_joints__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"
// Member 'joints'
#include "geometry_msgs/msg/detail/point32__traits.hpp"

namespace robotis_interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const HandJoints & msg,
  std::ostream & out)
{
  out << "{";
  // member: header
  {
    out << "header: ";
    to_flow_style_yaml(msg.header, out);
    out << ", ";
  }

  // member: joints
  {
    if (msg.joints.size() == 0) {
      out << "joints: []";
    } else {
      out << "joints: [";
      size_t pending_items = msg.joints.size();
      for (auto item : msg.joints) {
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
  const HandJoints & msg,
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

  // member: joints
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.joints.size() == 0) {
      out << "joints: []\n";
    } else {
      out << "joints:\n";
      for (auto item : msg.joints) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const HandJoints & msg, bool use_flow_style = false)
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
  const robotis_interfaces::msg::HandJoints & msg,
  std::ostream & out, size_t indentation = 0)
{
  robotis_interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use robotis_interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const robotis_interfaces::msg::HandJoints & msg)
{
  return robotis_interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<robotis_interfaces::msg::HandJoints>()
{
  return "robotis_interfaces::msg::HandJoints";
}

template<>
inline const char * name<robotis_interfaces::msg::HandJoints>()
{
  return "robotis_interfaces/msg/HandJoints";
}

template<>
struct has_fixed_size<robotis_interfaces::msg::HandJoints>
  : std::integral_constant<bool, has_fixed_size<geometry_msgs::msg::Point32>::value && has_fixed_size<std_msgs::msg::Header>::value> {};

template<>
struct has_bounded_size<robotis_interfaces::msg::HandJoints>
  : std::integral_constant<bool, has_bounded_size<geometry_msgs::msg::Point32>::value && has_bounded_size<std_msgs::msg::Header>::value> {};

template<>
struct is_message<robotis_interfaces::msg::HandJoints>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // ROBOTIS_INTERFACES__MSG__DETAIL__HAND_JOINTS__TRAITS_HPP_
