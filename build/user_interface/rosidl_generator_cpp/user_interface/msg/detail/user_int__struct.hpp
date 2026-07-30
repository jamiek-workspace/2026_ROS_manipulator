// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from user_interface:msg/UserInt.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "user_interface/msg/user_int.hpp"


#ifndef USER_INTERFACE__MSG__DETAIL__USER_INT__STRUCT_HPP_
#define USER_INTERFACE__MSG__DETAIL__USER_INT__STRUCT_HPP_

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

#ifndef _WIN32
# define DEPRECATED__user_interface__msg__UserInt __attribute__((deprecated))
#else
# define DEPRECATED__user_interface__msg__UserInt __declspec(deprecated)
#endif

namespace user_interface
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct UserInt_
{
  using Type = UserInt_<ContainerAllocator>;

  explicit UserInt_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->user_int = 0l;
      this->user_int2 = 0l;
      this->user_int3 = 0l;
    }
  }

  explicit UserInt_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->user_int = 0l;
      this->user_int2 = 0l;
      this->user_int3 = 0l;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _user_int_type =
    int32_t;
  _user_int_type user_int;
  using _user_int2_type =
    int32_t;
  _user_int2_type user_int2;
  using _user_int3_type =
    int32_t;
  _user_int3_type user_int3;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__user_int(
    const int32_t & _arg)
  {
    this->user_int = _arg;
    return *this;
  }
  Type & set__user_int2(
    const int32_t & _arg)
  {
    this->user_int2 = _arg;
    return *this;
  }
  Type & set__user_int3(
    const int32_t & _arg)
  {
    this->user_int3 = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    user_interface::msg::UserInt_<ContainerAllocator> *;
  using ConstRawPtr =
    const user_interface::msg::UserInt_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<user_interface::msg::UserInt_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<user_interface::msg::UserInt_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      user_interface::msg::UserInt_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<user_interface::msg::UserInt_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      user_interface::msg::UserInt_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<user_interface::msg::UserInt_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<user_interface::msg::UserInt_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<user_interface::msg::UserInt_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__user_interface__msg__UserInt
    std::shared_ptr<user_interface::msg::UserInt_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__user_interface__msg__UserInt
    std::shared_ptr<user_interface::msg::UserInt_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const UserInt_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->user_int != other.user_int) {
      return false;
    }
    if (this->user_int2 != other.user_int2) {
      return false;
    }
    if (this->user_int3 != other.user_int3) {
      return false;
    }
    return true;
  }
  bool operator!=(const UserInt_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct UserInt_

// alias to use template instance with default allocator
using UserInt =
  user_interface::msg::UserInt_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace user_interface

#endif  // USER_INTERFACE__MSG__DETAIL__USER_INT__STRUCT_HPP_
