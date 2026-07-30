// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from robotis_interfaces:msg/HandPressures.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "robotis_interfaces/msg/hand_pressures.hpp"


#ifndef ROBOTIS_INTERFACES__MSG__DETAIL__HAND_PRESSURES__STRUCT_HPP_
#define ROBOTIS_INTERFACES__MSG__DETAIL__HAND_PRESSURES__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <cstdint>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.hpp"
// Member 'sensors'
#include "robotis_interfaces/msg/detail/tactile_sensor__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__robotis_interfaces__msg__HandPressures __attribute__((deprecated))
#else
# define DEPRECATED__robotis_interfaces__msg__HandPressures __declspec(deprecated)
#endif

namespace robotis_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct HandPressures_
{
  using Type = HandPressures_<ContainerAllocator>;

  explicit HandPressures_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->hand_name = "";
    }
  }

  explicit HandPressures_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init),
    hand_name(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->hand_name = "";
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _hand_name_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _hand_name_type hand_name;
  using _sensors_type =
    std::vector<robotis_interfaces::msg::TactileSensor_<ContainerAllocator>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<robotis_interfaces::msg::TactileSensor_<ContainerAllocator>>>;
  _sensors_type sensors;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__hand_name(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->hand_name = _arg;
    return *this;
  }
  Type & set__sensors(
    const std::vector<robotis_interfaces::msg::TactileSensor_<ContainerAllocator>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<robotis_interfaces::msg::TactileSensor_<ContainerAllocator>>> & _arg)
  {
    this->sensors = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    robotis_interfaces::msg::HandPressures_<ContainerAllocator> *;
  using ConstRawPtr =
    const robotis_interfaces::msg::HandPressures_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<robotis_interfaces::msg::HandPressures_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<robotis_interfaces::msg::HandPressures_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      robotis_interfaces::msg::HandPressures_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<robotis_interfaces::msg::HandPressures_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      robotis_interfaces::msg::HandPressures_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<robotis_interfaces::msg::HandPressures_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<robotis_interfaces::msg::HandPressures_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<robotis_interfaces::msg::HandPressures_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__robotis_interfaces__msg__HandPressures
    std::shared_ptr<robotis_interfaces::msg::HandPressures_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__robotis_interfaces__msg__HandPressures
    std::shared_ptr<robotis_interfaces::msg::HandPressures_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const HandPressures_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->hand_name != other.hand_name) {
      return false;
    }
    if (this->sensors != other.sensors) {
      return false;
    }
    return true;
  }
  bool operator!=(const HandPressures_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct HandPressures_

// alias to use template instance with default allocator
using HandPressures =
  robotis_interfaces::msg::HandPressures_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace robotis_interfaces

#endif  // ROBOTIS_INTERFACES__MSG__DETAIL__HAND_PRESSURES__STRUCT_HPP_
