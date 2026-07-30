// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from robotis_interfaces:msg/HandJoints.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "robotis_interfaces/msg/hand_joints.hpp"


#ifndef ROBOTIS_INTERFACES__MSG__DETAIL__HAND_JOINTS__STRUCT_HPP_
#define ROBOTIS_INTERFACES__MSG__DETAIL__HAND_JOINTS__STRUCT_HPP_

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
// Member 'joints'
#include "geometry_msgs/msg/detail/point32__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__robotis_interfaces__msg__HandJoints __attribute__((deprecated))
#else
# define DEPRECATED__robotis_interfaces__msg__HandJoints __declspec(deprecated)
#endif

namespace robotis_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct HandJoints_
{
  using Type = HandJoints_<ContainerAllocator>;

  explicit HandJoints_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->joints.fill(geometry_msgs::msg::Point32_<ContainerAllocator>{_init});
    }
  }

  explicit HandJoints_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init),
    joints(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->joints.fill(geometry_msgs::msg::Point32_<ContainerAllocator>{_alloc, _init});
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _joints_type =
    std::array<geometry_msgs::msg::Point32_<ContainerAllocator>, 21>;
  _joints_type joints;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__joints(
    const std::array<geometry_msgs::msg::Point32_<ContainerAllocator>, 21> & _arg)
  {
    this->joints = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    robotis_interfaces::msg::HandJoints_<ContainerAllocator> *;
  using ConstRawPtr =
    const robotis_interfaces::msg::HandJoints_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<robotis_interfaces::msg::HandJoints_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<robotis_interfaces::msg::HandJoints_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      robotis_interfaces::msg::HandJoints_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<robotis_interfaces::msg::HandJoints_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      robotis_interfaces::msg::HandJoints_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<robotis_interfaces::msg::HandJoints_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<robotis_interfaces::msg::HandJoints_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<robotis_interfaces::msg::HandJoints_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__robotis_interfaces__msg__HandJoints
    std::shared_ptr<robotis_interfaces::msg::HandJoints_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__robotis_interfaces__msg__HandJoints
    std::shared_ptr<robotis_interfaces::msg::HandJoints_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const HandJoints_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->joints != other.joints) {
      return false;
    }
    return true;
  }
  bool operator!=(const HandJoints_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct HandJoints_

// alias to use template instance with default allocator
using HandJoints =
  robotis_interfaces::msg::HandJoints_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace robotis_interfaces

#endif  // ROBOTIS_INTERFACES__MSG__DETAIL__HAND_JOINTS__STRUCT_HPP_
