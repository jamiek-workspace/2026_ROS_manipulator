// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from robotis_interfaces:msg/TactileSensor.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "robotis_interfaces/msg/tactile_sensor.hpp"


#ifndef ROBOTIS_INTERFACES__MSG__DETAIL__TACTILE_SENSOR__TRAITS_HPP_
#define ROBOTIS_INTERFACES__MSG__DETAIL__TACTILE_SENSOR__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "robotis_interfaces/msg/detail/tactile_sensor__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace robotis_interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const TactileSensor & msg,
  std::ostream & out)
{
  out << "{";
  // member: sensor_name
  {
    out << "sensor_name: ";
    rosidl_generator_traits::value_to_yaml(msg.sensor_name, out);
    out << ", ";
  }

  // member: pressure_names
  {
    if (msg.pressure_names.size() == 0) {
      out << "pressure_names: []";
    } else {
      out << "pressure_names: [";
      size_t pending_items = msg.pressure_names.size();
      for (auto item : msg.pressure_names) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: pressure_values
  {
    if (msg.pressure_values.size() == 0) {
      out << "pressure_values: []";
    } else {
      out << "pressure_values: [";
      size_t pending_items = msg.pressure_values.size();
      for (auto item : msg.pressure_values) {
        rosidl_generator_traits::value_to_yaml(item, out);
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
  const TactileSensor & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: sensor_name
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "sensor_name: ";
    rosidl_generator_traits::value_to_yaml(msg.sensor_name, out);
    out << "\n";
  }

  // member: pressure_names
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.pressure_names.size() == 0) {
      out << "pressure_names: []\n";
    } else {
      out << "pressure_names:\n";
      for (auto item : msg.pressure_names) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: pressure_values
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.pressure_values.size() == 0) {
      out << "pressure_values: []\n";
    } else {
      out << "pressure_values:\n";
      for (auto item : msg.pressure_values) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const TactileSensor & msg, bool use_flow_style = false)
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
  const robotis_interfaces::msg::TactileSensor & msg,
  std::ostream & out, size_t indentation = 0)
{
  robotis_interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use robotis_interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const robotis_interfaces::msg::TactileSensor & msg)
{
  return robotis_interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<robotis_interfaces::msg::TactileSensor>()
{
  return "robotis_interfaces::msg::TactileSensor";
}

template<>
inline const char * name<robotis_interfaces::msg::TactileSensor>()
{
  return "robotis_interfaces/msg/TactileSensor";
}

template<>
struct has_fixed_size<robotis_interfaces::msg::TactileSensor>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<robotis_interfaces::msg::TactileSensor>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<robotis_interfaces::msg::TactileSensor>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // ROBOTIS_INTERFACES__MSG__DETAIL__TACTILE_SENSOR__TRAITS_HPP_
