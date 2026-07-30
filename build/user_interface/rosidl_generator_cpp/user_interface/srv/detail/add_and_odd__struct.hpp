// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from user_interface:srv/AddAndOdd.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "user_interface/srv/add_and_odd.hpp"


#ifndef USER_INTERFACE__SRV__DETAIL__ADD_AND_ODD__STRUCT_HPP_
#define USER_INTERFACE__SRV__DETAIL__ADD_AND_ODD__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <cstdint>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__user_interface__srv__AddAndOdd_Request __attribute__((deprecated))
#else
# define DEPRECATED__user_interface__srv__AddAndOdd_Request __declspec(deprecated)
#endif

namespace user_interface
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct AddAndOdd_Request_
{
  using Type = AddAndOdd_Request_<ContainerAllocator>;

  explicit AddAndOdd_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->inta = 0l;
      this->intb = 0l;
    }
  }

  explicit AddAndOdd_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->inta = 0l;
      this->intb = 0l;
    }
  }

  // field types and members
  using _inta_type =
    int32_t;
  _inta_type inta;
  using _intb_type =
    int32_t;
  _intb_type intb;

  // setters for named parameter idiom
  Type & set__inta(
    const int32_t & _arg)
  {
    this->inta = _arg;
    return *this;
  }
  Type & set__intb(
    const int32_t & _arg)
  {
    this->intb = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    user_interface::srv::AddAndOdd_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const user_interface::srv::AddAndOdd_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<user_interface::srv::AddAndOdd_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<user_interface::srv::AddAndOdd_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      user_interface::srv::AddAndOdd_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<user_interface::srv::AddAndOdd_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      user_interface::srv::AddAndOdd_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<user_interface::srv::AddAndOdd_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<user_interface::srv::AddAndOdd_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<user_interface::srv::AddAndOdd_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__user_interface__srv__AddAndOdd_Request
    std::shared_ptr<user_interface::srv::AddAndOdd_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__user_interface__srv__AddAndOdd_Request
    std::shared_ptr<user_interface::srv::AddAndOdd_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const AddAndOdd_Request_ & other) const
  {
    if (this->inta != other.inta) {
      return false;
    }
    if (this->intb != other.intb) {
      return false;
    }
    return true;
  }
  bool operator!=(const AddAndOdd_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct AddAndOdd_Request_

// alias to use template instance with default allocator
using AddAndOdd_Request =
  user_interface::srv::AddAndOdd_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace user_interface


#ifndef _WIN32
# define DEPRECATED__user_interface__srv__AddAndOdd_Response __attribute__((deprecated))
#else
# define DEPRECATED__user_interface__srv__AddAndOdd_Response __declspec(deprecated)
#endif

namespace user_interface
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct AddAndOdd_Response_
{
  using Type = AddAndOdd_Response_<ContainerAllocator>;

  explicit AddAndOdd_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->sum = 0l;
      this->odd = "";
    }
  }

  explicit AddAndOdd_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : odd(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->sum = 0l;
      this->odd = "";
    }
  }

  // field types and members
  using _sum_type =
    int32_t;
  _sum_type sum;
  using _odd_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _odd_type odd;

  // setters for named parameter idiom
  Type & set__sum(
    const int32_t & _arg)
  {
    this->sum = _arg;
    return *this;
  }
  Type & set__odd(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->odd = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    user_interface::srv::AddAndOdd_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const user_interface::srv::AddAndOdd_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<user_interface::srv::AddAndOdd_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<user_interface::srv::AddAndOdd_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      user_interface::srv::AddAndOdd_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<user_interface::srv::AddAndOdd_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      user_interface::srv::AddAndOdd_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<user_interface::srv::AddAndOdd_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<user_interface::srv::AddAndOdd_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<user_interface::srv::AddAndOdd_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__user_interface__srv__AddAndOdd_Response
    std::shared_ptr<user_interface::srv::AddAndOdd_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__user_interface__srv__AddAndOdd_Response
    std::shared_ptr<user_interface::srv::AddAndOdd_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const AddAndOdd_Response_ & other) const
  {
    if (this->sum != other.sum) {
      return false;
    }
    if (this->odd != other.odd) {
      return false;
    }
    return true;
  }
  bool operator!=(const AddAndOdd_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct AddAndOdd_Response_

// alias to use template instance with default allocator
using AddAndOdd_Response =
  user_interface::srv::AddAndOdd_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace user_interface


// Include directives for member types
// Member 'info'
#include "service_msgs/msg/detail/service_event_info__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__user_interface__srv__AddAndOdd_Event __attribute__((deprecated))
#else
# define DEPRECATED__user_interface__srv__AddAndOdd_Event __declspec(deprecated)
#endif

namespace user_interface
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct AddAndOdd_Event_
{
  using Type = AddAndOdd_Event_<ContainerAllocator>;

  explicit AddAndOdd_Event_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : info(_init)
  {
    (void)_init;
  }

  explicit AddAndOdd_Event_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : info(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _info_type =
    service_msgs::msg::ServiceEventInfo_<ContainerAllocator>;
  _info_type info;
  using _request_type =
    rosidl_runtime_cpp::BoundedVector<user_interface::srv::AddAndOdd_Request_<ContainerAllocator>, 1, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<user_interface::srv::AddAndOdd_Request_<ContainerAllocator>>>;
  _request_type request;
  using _response_type =
    rosidl_runtime_cpp::BoundedVector<user_interface::srv::AddAndOdd_Response_<ContainerAllocator>, 1, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<user_interface::srv::AddAndOdd_Response_<ContainerAllocator>>>;
  _response_type response;

  // setters for named parameter idiom
  Type & set__info(
    const service_msgs::msg::ServiceEventInfo_<ContainerAllocator> & _arg)
  {
    this->info = _arg;
    return *this;
  }
  Type & set__request(
    const rosidl_runtime_cpp::BoundedVector<user_interface::srv::AddAndOdd_Request_<ContainerAllocator>, 1, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<user_interface::srv::AddAndOdd_Request_<ContainerAllocator>>> & _arg)
  {
    this->request = _arg;
    return *this;
  }
  Type & set__response(
    const rosidl_runtime_cpp::BoundedVector<user_interface::srv::AddAndOdd_Response_<ContainerAllocator>, 1, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<user_interface::srv::AddAndOdd_Response_<ContainerAllocator>>> & _arg)
  {
    this->response = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    user_interface::srv::AddAndOdd_Event_<ContainerAllocator> *;
  using ConstRawPtr =
    const user_interface::srv::AddAndOdd_Event_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<user_interface::srv::AddAndOdd_Event_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<user_interface::srv::AddAndOdd_Event_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      user_interface::srv::AddAndOdd_Event_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<user_interface::srv::AddAndOdd_Event_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      user_interface::srv::AddAndOdd_Event_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<user_interface::srv::AddAndOdd_Event_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<user_interface::srv::AddAndOdd_Event_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<user_interface::srv::AddAndOdd_Event_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__user_interface__srv__AddAndOdd_Event
    std::shared_ptr<user_interface::srv::AddAndOdd_Event_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__user_interface__srv__AddAndOdd_Event
    std::shared_ptr<user_interface::srv::AddAndOdd_Event_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const AddAndOdd_Event_ & other) const
  {
    if (this->info != other.info) {
      return false;
    }
    if (this->request != other.request) {
      return false;
    }
    if (this->response != other.response) {
      return false;
    }
    return true;
  }
  bool operator!=(const AddAndOdd_Event_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct AddAndOdd_Event_

// alias to use template instance with default allocator
using AddAndOdd_Event =
  user_interface::srv::AddAndOdd_Event_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace user_interface

namespace user_interface
{

namespace srv
{

struct AddAndOdd
{
  using Request = user_interface::srv::AddAndOdd_Request;
  using Response = user_interface::srv::AddAndOdd_Response;
  using Event = user_interface::srv::AddAndOdd_Event;
};

}  // namespace srv

}  // namespace user_interface

#endif  // USER_INTERFACE__SRV__DETAIL__ADD_AND_ODD__STRUCT_HPP_
