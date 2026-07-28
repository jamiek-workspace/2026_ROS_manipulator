// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from robotis_interfaces:msg/MoveL.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "robotis_interfaces/msg/move_l.hpp"


#ifndef ROBOTIS_INTERFACES__MSG__DETAIL__MOVE_L__TRAITS_HPP_
#define ROBOTIS_INTERFACES__MSG__DETAIL__MOVE_L__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "robotis_interfaces/msg/detail/move_l__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'pose'
#include "geometry_msgs/msg/detail/pose_stamped__traits.hpp"
// Member 'time_from_start'
#include "builtin_interfaces/msg/detail/duration__traits.hpp"

namespace robotis_interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const MoveL & msg,
  std::ostream & out)
{
  out << "{";
  // member: pose
  {
    out << "pose: ";
    to_flow_style_yaml(msg.pose, out);
    out << ", ";
  }

  // member: time_from_start
  {
    out << "time_from_start: ";
    to_flow_style_yaml(msg.time_from_start, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const MoveL & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: pose
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "pose:\n";
    to_block_style_yaml(msg.pose, out, indentation + 2);
  }

  // member: time_from_start
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "time_from_start:\n";
    to_block_style_yaml(msg.time_from_start, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const MoveL & msg, bool use_flow_style = false)
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
  const robotis_interfaces::msg::MoveL & msg,
  std::ostream & out, size_t indentation = 0)
{
  robotis_interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use robotis_interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const robotis_interfaces::msg::MoveL & msg)
{
  return robotis_interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<robotis_interfaces::msg::MoveL>()
{
  return "robotis_interfaces::msg::MoveL";
}

template<>
inline const char * name<robotis_interfaces::msg::MoveL>()
{
  return "robotis_interfaces/msg/MoveL";
}

template<>
struct has_fixed_size<robotis_interfaces::msg::MoveL>
  : std::integral_constant<bool, has_fixed_size<builtin_interfaces::msg::Duration>::value && has_fixed_size<geometry_msgs::msg::PoseStamped>::value> {};

template<>
struct has_bounded_size<robotis_interfaces::msg::MoveL>
  : std::integral_constant<bool, has_bounded_size<builtin_interfaces::msg::Duration>::value && has_bounded_size<geometry_msgs::msg::PoseStamped>::value> {};

template<>
struct is_message<robotis_interfaces::msg::MoveL>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // ROBOTIS_INTERFACES__MSG__DETAIL__MOVE_L__TRAITS_HPP_
