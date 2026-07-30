// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from robotis_interfaces:msg/TactileSensor.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "robotis_interfaces/msg/tactile_sensor.hpp"


#ifndef ROBOTIS_INTERFACES__MSG__DETAIL__TACTILE_SENSOR__STRUCT_HPP_
#define ROBOTIS_INTERFACES__MSG__DETAIL__TACTILE_SENSOR__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <cstdint>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__robotis_interfaces__msg__TactileSensor __attribute__((deprecated))
#else
# define DEPRECATED__robotis_interfaces__msg__TactileSensor __declspec(deprecated)
#endif

namespace robotis_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct TactileSensor_
{
  using Type = TactileSensor_<ContainerAllocator>;

  explicit TactileSensor_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->sensor_name = "";
      std::fill<typename std::array<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>, 9>::iterator, std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>(this->pressure_names.begin(), this->pressure_names.end(), "");
      std::fill<typename std::array<uint8_t, 9>::iterator, uint8_t>(this->pressure_values.begin(), this->pressure_values.end(), 0);
    }
  }

  explicit TactileSensor_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : sensor_name(_alloc),
    pressure_names(_alloc),
    pressure_values(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->sensor_name = "";
      std::fill<typename std::array<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>, 9>::iterator, std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>(this->pressure_names.begin(), this->pressure_names.end(), "");
      std::fill<typename std::array<uint8_t, 9>::iterator, uint8_t>(this->pressure_values.begin(), this->pressure_values.end(), 0);
    }
  }

  // field types and members
  using _sensor_name_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _sensor_name_type sensor_name;
  using _pressure_names_type =
    std::array<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>, 9>;
  _pressure_names_type pressure_names;
  using _pressure_values_type =
    std::array<uint8_t, 9>;
  _pressure_values_type pressure_values;

  // setters for named parameter idiom
  Type & set__sensor_name(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->sensor_name = _arg;
    return *this;
  }
  Type & set__pressure_names(
    const std::array<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>, 9> & _arg)
  {
    this->pressure_names = _arg;
    return *this;
  }
  Type & set__pressure_values(
    const std::array<uint8_t, 9> & _arg)
  {
    this->pressure_values = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    robotis_interfaces::msg::TactileSensor_<ContainerAllocator> *;
  using ConstRawPtr =
    const robotis_interfaces::msg::TactileSensor_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<robotis_interfaces::msg::TactileSensor_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<robotis_interfaces::msg::TactileSensor_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      robotis_interfaces::msg::TactileSensor_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<robotis_interfaces::msg::TactileSensor_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      robotis_interfaces::msg::TactileSensor_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<robotis_interfaces::msg::TactileSensor_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<robotis_interfaces::msg::TactileSensor_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<robotis_interfaces::msg::TactileSensor_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__robotis_interfaces__msg__TactileSensor
    std::shared_ptr<robotis_interfaces::msg::TactileSensor_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__robotis_interfaces__msg__TactileSensor
    std::shared_ptr<robotis_interfaces::msg::TactileSensor_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const TactileSensor_ & other) const
  {
    if (this->sensor_name != other.sensor_name) {
      return false;
    }
    if (this->pressure_names != other.pressure_names) {
      return false;
    }
    if (this->pressure_values != other.pressure_values) {
      return false;
    }
    return true;
  }
  bool operator!=(const TactileSensor_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct TactileSensor_

// alias to use template instance with default allocator
using TactileSensor =
  robotis_interfaces::msg::TactileSensor_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace robotis_interfaces

#endif  // ROBOTIS_INTERFACES__MSG__DETAIL__TACTILE_SENSOR__STRUCT_HPP_
