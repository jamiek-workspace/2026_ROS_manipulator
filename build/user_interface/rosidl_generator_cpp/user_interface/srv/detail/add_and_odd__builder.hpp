// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from user_interface:srv/AddAndOdd.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "user_interface/srv/add_and_odd.hpp"


#ifndef USER_INTERFACE__SRV__DETAIL__ADD_AND_ODD__BUILDER_HPP_
#define USER_INTERFACE__SRV__DETAIL__ADD_AND_ODD__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "user_interface/srv/detail/add_and_odd__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace user_interface
{

namespace srv
{

namespace builder
{

class Init_AddAndOdd_Request_intb
{
public:
  explicit Init_AddAndOdd_Request_intb(::user_interface::srv::AddAndOdd_Request & msg)
  : msg_(msg)
  {}
  ::user_interface::srv::AddAndOdd_Request intb(::user_interface::srv::AddAndOdd_Request::_intb_type arg)
  {
    msg_.intb = std::move(arg);
    return std::move(msg_);
  }

private:
  ::user_interface::srv::AddAndOdd_Request msg_;
};

class Init_AddAndOdd_Request_inta
{
public:
  Init_AddAndOdd_Request_inta()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_AddAndOdd_Request_intb inta(::user_interface::srv::AddAndOdd_Request::_inta_type arg)
  {
    msg_.inta = std::move(arg);
    return Init_AddAndOdd_Request_intb(msg_);
  }

private:
  ::user_interface::srv::AddAndOdd_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::user_interface::srv::AddAndOdd_Request>()
{
  return user_interface::srv::builder::Init_AddAndOdd_Request_inta();
}

}  // namespace user_interface


namespace user_interface
{

namespace srv
{

namespace builder
{

class Init_AddAndOdd_Response_odd
{
public:
  explicit Init_AddAndOdd_Response_odd(::user_interface::srv::AddAndOdd_Response & msg)
  : msg_(msg)
  {}
  ::user_interface::srv::AddAndOdd_Response odd(::user_interface::srv::AddAndOdd_Response::_odd_type arg)
  {
    msg_.odd = std::move(arg);
    return std::move(msg_);
  }

private:
  ::user_interface::srv::AddAndOdd_Response msg_;
};

class Init_AddAndOdd_Response_sum
{
public:
  Init_AddAndOdd_Response_sum()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_AddAndOdd_Response_odd sum(::user_interface::srv::AddAndOdd_Response::_sum_type arg)
  {
    msg_.sum = std::move(arg);
    return Init_AddAndOdd_Response_odd(msg_);
  }

private:
  ::user_interface::srv::AddAndOdd_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::user_interface::srv::AddAndOdd_Response>()
{
  return user_interface::srv::builder::Init_AddAndOdd_Response_sum();
}

}  // namespace user_interface


namespace user_interface
{

namespace srv
{

namespace builder
{

class Init_AddAndOdd_Event_response
{
public:
  explicit Init_AddAndOdd_Event_response(::user_interface::srv::AddAndOdd_Event & msg)
  : msg_(msg)
  {}
  ::user_interface::srv::AddAndOdd_Event response(::user_interface::srv::AddAndOdd_Event::_response_type arg)
  {
    msg_.response = std::move(arg);
    return std::move(msg_);
  }

private:
  ::user_interface::srv::AddAndOdd_Event msg_;
};

class Init_AddAndOdd_Event_request
{
public:
  explicit Init_AddAndOdd_Event_request(::user_interface::srv::AddAndOdd_Event & msg)
  : msg_(msg)
  {}
  Init_AddAndOdd_Event_response request(::user_interface::srv::AddAndOdd_Event::_request_type arg)
  {
    msg_.request = std::move(arg);
    return Init_AddAndOdd_Event_response(msg_);
  }

private:
  ::user_interface::srv::AddAndOdd_Event msg_;
};

class Init_AddAndOdd_Event_info
{
public:
  Init_AddAndOdd_Event_info()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_AddAndOdd_Event_request info(::user_interface::srv::AddAndOdd_Event::_info_type arg)
  {
    msg_.info = std::move(arg);
    return Init_AddAndOdd_Event_request(msg_);
  }

private:
  ::user_interface::srv::AddAndOdd_Event msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::user_interface::srv::AddAndOdd_Event>()
{
  return user_interface::srv::builder::Init_AddAndOdd_Event_info();
}

}  // namespace user_interface

#endif  // USER_INTERFACE__SRV__DETAIL__ADD_AND_ODD__BUILDER_HPP_
