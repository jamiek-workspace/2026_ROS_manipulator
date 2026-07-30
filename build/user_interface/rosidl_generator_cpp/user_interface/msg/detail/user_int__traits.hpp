// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from user_interface:msg/UserInt.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "user_interface/msg/user_int.hpp"


#ifndef USER_INTERFACE__MSG__DETAIL__USER_INT__TRAITS_HPP_
#define USER_INTERFACE__MSG__DETAIL__USER_INT__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "user_interface/msg/detail/user_int__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"

namespace user_interface
{

namespace msg
{

inline void to_flow_style_yaml(
  const UserInt & msg,
  std::ostream & out)
{
  out << "{";
  // member: header
  {
    out << "header: ";
    to_flow_style_yaml(msg.header, out);
    out << ", ";
  }

  // member: user_int
  {
    out << "user_int: ";
    rosidl_generator_traits::value_to_yaml(msg.user_int, out);
    out << ", ";
  }

  // member: user_int2
  {
    out << "user_int2: ";
    rosidl_generator_traits::value_to_yaml(msg.user_int2, out);
    out << ", ";
  }

  // member: user_int3
  {
    out << "user_int3: ";
    rosidl_generator_traits::value_to_yaml(msg.user_int3, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const UserInt & msg,
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

  // member: user_int
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "user_int: ";
    rosidl_generator_traits::value_to_yaml(msg.user_int, out);
    out << "\n";
  }

  // member: user_int2
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "user_int2: ";
    rosidl_generator_traits::value_to_yaml(msg.user_int2, out);
    out << "\n";
  }

  // member: user_int3
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "user_int3: ";
    rosidl_generator_traits::value_to_yaml(msg.user_int3, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const UserInt & msg, bool use_flow_style = false)
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

}  // namespace user_interface

namespace rosidl_generator_traits
{

[[deprecated("use user_interface::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const user_interface::msg::UserInt & msg,
  std::ostream & out, size_t indentation = 0)
{
  user_interface::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use user_interface::msg::to_yaml() instead")]]
inline std::string to_yaml(const user_interface::msg::UserInt & msg)
{
  return user_interface::msg::to_yaml(msg);
}

template<>
inline const char * data_type<user_interface::msg::UserInt>()
{
  return "user_interface::msg::UserInt";
}

template<>
inline const char * name<user_interface::msg::UserInt>()
{
  return "user_interface/msg/UserInt";
}

template<>
struct has_fixed_size<user_interface::msg::UserInt>
  : std::integral_constant<bool, has_fixed_size<std_msgs::msg::Header>::value> {};

template<>
struct has_bounded_size<user_interface::msg::UserInt>
  : std::integral_constant<bool, has_bounded_size<std_msgs::msg::Header>::value> {};

template<>
struct is_message<user_interface::msg::UserInt>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // USER_INTERFACE__MSG__DETAIL__USER_INT__TRAITS_HPP_
