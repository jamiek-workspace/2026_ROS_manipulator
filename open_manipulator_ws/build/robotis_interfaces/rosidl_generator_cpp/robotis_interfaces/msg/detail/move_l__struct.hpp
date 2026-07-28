// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from robotis_interfaces:msg/MoveL.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "robotis_interfaces/msg/move_l.hpp"


#ifndef ROBOTIS_INTERFACES__MSG__DETAIL__MOVE_L__STRUCT_HPP_
#define ROBOTIS_INTERFACES__MSG__DETAIL__MOVE_L__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <cstdint>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'pose'
#include "geometry_msgs/msg/detail/pose_stamped__struct.hpp"
// Member 'time_from_start'
#include "builtin_interfaces/msg/detail/duration__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__robotis_interfaces__msg__MoveL __attribute__((deprecated))
#else
# define DEPRECATED__robotis_interfaces__msg__MoveL __declspec(deprecated)
#endif

namespace robotis_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct MoveL_
{
  using Type = MoveL_<ContainerAllocator>;

  explicit MoveL_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : pose(_init),
    time_from_start(_init)
  {
    (void)_init;
  }

  explicit MoveL_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : pose(_alloc, _init),
    time_from_start(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _pose_type =
    geometry_msgs::msg::PoseStamped_<ContainerAllocator>;
  _pose_type pose;
  using _time_from_start_type =
    builtin_interfaces::msg::Duration_<ContainerAllocator>;
  _time_from_start_type time_from_start;

  // setters for named parameter idiom
  Type & set__pose(
    const geometry_msgs::msg::PoseStamped_<ContainerAllocator> & _arg)
  {
    this->pose = _arg;
    return *this;
  }
  Type & set__time_from_start(
    const builtin_interfaces::msg::Duration_<ContainerAllocator> & _arg)
  {
    this->time_from_start = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    robotis_interfaces::msg::MoveL_<ContainerAllocator> *;
  using ConstRawPtr =
    const robotis_interfaces::msg::MoveL_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<robotis_interfaces::msg::MoveL_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<robotis_interfaces::msg::MoveL_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      robotis_interfaces::msg::MoveL_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<robotis_interfaces::msg::MoveL_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      robotis_interfaces::msg::MoveL_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<robotis_interfaces::msg::MoveL_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<robotis_interfaces::msg::MoveL_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<robotis_interfaces::msg::MoveL_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__robotis_interfaces__msg__MoveL
    std::shared_ptr<robotis_interfaces::msg::MoveL_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__robotis_interfaces__msg__MoveL
    std::shared_ptr<robotis_interfaces::msg::MoveL_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const MoveL_ & other) const
  {
    if (this->pose != other.pose) {
      return false;
    }
    if (this->time_from_start != other.time_from_start) {
      return false;
    }
    return true;
  }
  bool operator!=(const MoveL_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct MoveL_

// alias to use template instance with default allocator
using MoveL =
  robotis_interfaces::msg::MoveL_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace robotis_interfaces

#endif  // ROBOTIS_INTERFACES__MSG__DETAIL__MOVE_L__STRUCT_HPP_
