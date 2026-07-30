// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from user_interface:msg/UserInt.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "user_interface/msg/user_int.hpp"


#ifndef USER_INTERFACE__MSG__DETAIL__USER_INT__BUILDER_HPP_
#define USER_INTERFACE__MSG__DETAIL__USER_INT__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "user_interface/msg/detail/user_int__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace user_interface
{

namespace msg
{

namespace builder
{

class Init_UserInt_user_int3
{
public:
  explicit Init_UserInt_user_int3(::user_interface::msg::UserInt & msg)
  : msg_(msg)
  {}
  ::user_interface::msg::UserInt user_int3(::user_interface::msg::UserInt::_user_int3_type arg)
  {
    msg_.user_int3 = std::move(arg);
    return std::move(msg_);
  }

private:
  ::user_interface::msg::UserInt msg_;
};

class Init_UserInt_user_int2
{
public:
  explicit Init_UserInt_user_int2(::user_interface::msg::UserInt & msg)
  : msg_(msg)
  {}
  Init_UserInt_user_int3 user_int2(::user_interface::msg::UserInt::_user_int2_type arg)
  {
    msg_.user_int2 = std::move(arg);
    return Init_UserInt_user_int3(msg_);
  }

private:
  ::user_interface::msg::UserInt msg_;
};

class Init_UserInt_user_int
{
public:
  explicit Init_UserInt_user_int(::user_interface::msg::UserInt & msg)
  : msg_(msg)
  {}
  Init_UserInt_user_int2 user_int(::user_interface::msg::UserInt::_user_int_type arg)
  {
    msg_.user_int = std::move(arg);
    return Init_UserInt_user_int2(msg_);
  }

private:
  ::user_interface::msg::UserInt msg_;
};

class Init_UserInt_header
{
public:
  Init_UserInt_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_UserInt_user_int header(::user_interface::msg::UserInt::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_UserInt_user_int(msg_);
  }

private:
  ::user_interface::msg::UserInt msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::user_interface::msg::UserInt>()
{
  return user_interface::msg::builder::Init_UserInt_header();
}

}  // namespace user_interface

#endif  // USER_INTERFACE__MSG__DETAIL__USER_INT__BUILDER_HPP_
