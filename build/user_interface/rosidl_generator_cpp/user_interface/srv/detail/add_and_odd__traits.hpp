// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from user_interface:srv/AddAndOdd.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "user_interface/srv/add_and_odd.hpp"


#ifndef USER_INTERFACE__SRV__DETAIL__ADD_AND_ODD__TRAITS_HPP_
#define USER_INTERFACE__SRV__DETAIL__ADD_AND_ODD__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "user_interface/srv/detail/add_and_odd__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace user_interface
{

namespace srv
{

inline void to_flow_style_yaml(
  const AddAndOdd_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: inta
  {
    out << "inta: ";
    rosidl_generator_traits::value_to_yaml(msg.inta, out);
    out << ", ";
  }

  // member: intb
  {
    out << "intb: ";
    rosidl_generator_traits::value_to_yaml(msg.intb, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const AddAndOdd_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: inta
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "inta: ";
    rosidl_generator_traits::value_to_yaml(msg.inta, out);
    out << "\n";
  }

  // member: intb
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "intb: ";
    rosidl_generator_traits::value_to_yaml(msg.intb, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const AddAndOdd_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace user_interface

namespace rosidl_generator_traits
{

[[deprecated("use user_interface::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const user_interface::srv::AddAndOdd_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  user_interface::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use user_interface::srv::to_yaml() instead")]]
inline std::string to_yaml(const user_interface::srv::AddAndOdd_Request & msg)
{
  return user_interface::srv::to_yaml(msg);
}

template<>
inline const char * data_type<user_interface::srv::AddAndOdd_Request>()
{
  return "user_interface::srv::AddAndOdd_Request";
}

template<>
inline const char * name<user_interface::srv::AddAndOdd_Request>()
{
  return "user_interface/srv/AddAndOdd_Request";
}

template<>
struct has_fixed_size<user_interface::srv::AddAndOdd_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<user_interface::srv::AddAndOdd_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<user_interface::srv::AddAndOdd_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace user_interface
{

namespace srv
{

inline void to_flow_style_yaml(
  const AddAndOdd_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: sum
  {
    out << "sum: ";
    rosidl_generator_traits::value_to_yaml(msg.sum, out);
    out << ", ";
  }

  // member: odd
  {
    out << "odd: ";
    rosidl_generator_traits::value_to_yaml(msg.odd, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const AddAndOdd_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: sum
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "sum: ";
    rosidl_generator_traits::value_to_yaml(msg.sum, out);
    out << "\n";
  }

  // member: odd
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "odd: ";
    rosidl_generator_traits::value_to_yaml(msg.odd, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const AddAndOdd_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace user_interface

namespace rosidl_generator_traits
{

[[deprecated("use user_interface::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const user_interface::srv::AddAndOdd_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  user_interface::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use user_interface::srv::to_yaml() instead")]]
inline std::string to_yaml(const user_interface::srv::AddAndOdd_Response & msg)
{
  return user_interface::srv::to_yaml(msg);
}

template<>
inline const char * data_type<user_interface::srv::AddAndOdd_Response>()
{
  return "user_interface::srv::AddAndOdd_Response";
}

template<>
inline const char * name<user_interface::srv::AddAndOdd_Response>()
{
  return "user_interface/srv/AddAndOdd_Response";
}

template<>
struct has_fixed_size<user_interface::srv::AddAndOdd_Response>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<user_interface::srv::AddAndOdd_Response>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<user_interface::srv::AddAndOdd_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'info'
#include "service_msgs/msg/detail/service_event_info__traits.hpp"

namespace user_interface
{

namespace srv
{

inline void to_flow_style_yaml(
  const AddAndOdd_Event & msg,
  std::ostream & out)
{
  out << "{";
  // member: info
  {
    out << "info: ";
    to_flow_style_yaml(msg.info, out);
    out << ", ";
  }

  // member: request
  {
    if (msg.request.size() == 0) {
      out << "request: []";
    } else {
      out << "request: [";
      size_t pending_items = msg.request.size();
      for (auto item : msg.request) {
        to_flow_style_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: response
  {
    if (msg.response.size() == 0) {
      out << "response: []";
    } else {
      out << "response: [";
      size_t pending_items = msg.response.size();
      for (auto item : msg.response) {
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
  const AddAndOdd_Event & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: info
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "info:\n";
    to_block_style_yaml(msg.info, out, indentation + 2);
  }

  // member: request
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.request.size() == 0) {
      out << "request: []\n";
    } else {
      out << "request:\n";
      for (auto item : msg.request) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }

  // member: response
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.response.size() == 0) {
      out << "response: []\n";
    } else {
      out << "response:\n";
      for (auto item : msg.response) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const AddAndOdd_Event & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace user_interface

namespace rosidl_generator_traits
{

[[deprecated("use user_interface::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const user_interface::srv::AddAndOdd_Event & msg,
  std::ostream & out, size_t indentation = 0)
{
  user_interface::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use user_interface::srv::to_yaml() instead")]]
inline std::string to_yaml(const user_interface::srv::AddAndOdd_Event & msg)
{
  return user_interface::srv::to_yaml(msg);
}

template<>
inline const char * data_type<user_interface::srv::AddAndOdd_Event>()
{
  return "user_interface::srv::AddAndOdd_Event";
}

template<>
inline const char * name<user_interface::srv::AddAndOdd_Event>()
{
  return "user_interface/srv/AddAndOdd_Event";
}

template<>
struct has_fixed_size<user_interface::srv::AddAndOdd_Event>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<user_interface::srv::AddAndOdd_Event>
  : std::integral_constant<bool, has_bounded_size<service_msgs::msg::ServiceEventInfo>::value && has_bounded_size<user_interface::srv::AddAndOdd_Request>::value && has_bounded_size<user_interface::srv::AddAndOdd_Response>::value> {};

template<>
struct is_message<user_interface::srv::AddAndOdd_Event>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<user_interface::srv::AddAndOdd>()
{
  return "user_interface::srv::AddAndOdd";
}

template<>
inline const char * name<user_interface::srv::AddAndOdd>()
{
  return "user_interface/srv/AddAndOdd";
}

template<>
struct has_fixed_size<user_interface::srv::AddAndOdd>
  : std::integral_constant<
    bool,
    has_fixed_size<user_interface::srv::AddAndOdd_Request>::value &&
    has_fixed_size<user_interface::srv::AddAndOdd_Response>::value
  >
{
};

template<>
struct has_bounded_size<user_interface::srv::AddAndOdd>
  : std::integral_constant<
    bool,
    has_bounded_size<user_interface::srv::AddAndOdd_Request>::value &&
    has_bounded_size<user_interface::srv::AddAndOdd_Response>::value
  >
{
};

template<>
struct is_service<user_interface::srv::AddAndOdd>
  : std::true_type
{
};

template<>
struct is_service_request<user_interface::srv::AddAndOdd_Request>
  : std::true_type
{
};

template<>
struct is_service_response<user_interface::srv::AddAndOdd_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // USER_INTERFACE__SRV__DETAIL__ADD_AND_ODD__TRAITS_HPP_
