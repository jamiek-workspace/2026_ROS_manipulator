// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from user_interface:action/Fibonacci.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "user_interface/action/fibonacci.hpp"


#ifndef USER_INTERFACE__ACTION__DETAIL__FIBONACCI__BUILDER_HPP_
#define USER_INTERFACE__ACTION__DETAIL__FIBONACCI__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "user_interface/action/detail/fibonacci__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace user_interface
{

namespace action
{

namespace builder
{

class Init_Fibonacci_Goal_step
{
public:
  Init_Fibonacci_Goal_step()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::user_interface::action::Fibonacci_Goal step(::user_interface::action::Fibonacci_Goal::_step_type arg)
  {
    msg_.step = std::move(arg);
    return std::move(msg_);
  }

private:
  ::user_interface::action::Fibonacci_Goal msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::user_interface::action::Fibonacci_Goal>()
{
  return user_interface::action::builder::Init_Fibonacci_Goal_step();
}

}  // namespace user_interface


namespace user_interface
{

namespace action
{

namespace builder
{

class Init_Fibonacci_Result_seq
{
public:
  explicit Init_Fibonacci_Result_seq(::user_interface::action::Fibonacci_Result & msg)
  : msg_(msg)
  {}
  ::user_interface::action::Fibonacci_Result seq(::user_interface::action::Fibonacci_Result::_seq_type arg)
  {
    msg_.seq = std::move(arg);
    return std::move(msg_);
  }

private:
  ::user_interface::action::Fibonacci_Result msg_;
};

class Init_Fibonacci_Result_header
{
public:
  Init_Fibonacci_Result_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Fibonacci_Result_seq header(::user_interface::action::Fibonacci_Result::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_Fibonacci_Result_seq(msg_);
  }

private:
  ::user_interface::action::Fibonacci_Result msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::user_interface::action::Fibonacci_Result>()
{
  return user_interface::action::builder::Init_Fibonacci_Result_header();
}

}  // namespace user_interface


namespace user_interface
{

namespace action
{

namespace builder
{

class Init_Fibonacci_Feedback_temp_seq
{
public:
  Init_Fibonacci_Feedback_temp_seq()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::user_interface::action::Fibonacci_Feedback temp_seq(::user_interface::action::Fibonacci_Feedback::_temp_seq_type arg)
  {
    msg_.temp_seq = std::move(arg);
    return std::move(msg_);
  }

private:
  ::user_interface::action::Fibonacci_Feedback msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::user_interface::action::Fibonacci_Feedback>()
{
  return user_interface::action::builder::Init_Fibonacci_Feedback_temp_seq();
}

}  // namespace user_interface


namespace user_interface
{

namespace action
{

namespace builder
{

class Init_Fibonacci_SendGoal_Request_goal
{
public:
  explicit Init_Fibonacci_SendGoal_Request_goal(::user_interface::action::Fibonacci_SendGoal_Request & msg)
  : msg_(msg)
  {}
  ::user_interface::action::Fibonacci_SendGoal_Request goal(::user_interface::action::Fibonacci_SendGoal_Request::_goal_type arg)
  {
    msg_.goal = std::move(arg);
    return std::move(msg_);
  }

private:
  ::user_interface::action::Fibonacci_SendGoal_Request msg_;
};

class Init_Fibonacci_SendGoal_Request_goal_id
{
public:
  Init_Fibonacci_SendGoal_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Fibonacci_SendGoal_Request_goal goal_id(::user_interface::action::Fibonacci_SendGoal_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_Fibonacci_SendGoal_Request_goal(msg_);
  }

private:
  ::user_interface::action::Fibonacci_SendGoal_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::user_interface::action::Fibonacci_SendGoal_Request>()
{
  return user_interface::action::builder::Init_Fibonacci_SendGoal_Request_goal_id();
}

}  // namespace user_interface


namespace user_interface
{

namespace action
{

namespace builder
{

class Init_Fibonacci_SendGoal_Response_stamp
{
public:
  explicit Init_Fibonacci_SendGoal_Response_stamp(::user_interface::action::Fibonacci_SendGoal_Response & msg)
  : msg_(msg)
  {}
  ::user_interface::action::Fibonacci_SendGoal_Response stamp(::user_interface::action::Fibonacci_SendGoal_Response::_stamp_type arg)
  {
    msg_.stamp = std::move(arg);
    return std::move(msg_);
  }

private:
  ::user_interface::action::Fibonacci_SendGoal_Response msg_;
};

class Init_Fibonacci_SendGoal_Response_accepted
{
public:
  Init_Fibonacci_SendGoal_Response_accepted()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Fibonacci_SendGoal_Response_stamp accepted(::user_interface::action::Fibonacci_SendGoal_Response::_accepted_type arg)
  {
    msg_.accepted = std::move(arg);
    return Init_Fibonacci_SendGoal_Response_stamp(msg_);
  }

private:
  ::user_interface::action::Fibonacci_SendGoal_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::user_interface::action::Fibonacci_SendGoal_Response>()
{
  return user_interface::action::builder::Init_Fibonacci_SendGoal_Response_accepted();
}

}  // namespace user_interface


namespace user_interface
{

namespace action
{

namespace builder
{

class Init_Fibonacci_SendGoal_Event_response
{
public:
  explicit Init_Fibonacci_SendGoal_Event_response(::user_interface::action::Fibonacci_SendGoal_Event & msg)
  : msg_(msg)
  {}
  ::user_interface::action::Fibonacci_SendGoal_Event response(::user_interface::action::Fibonacci_SendGoal_Event::_response_type arg)
  {
    msg_.response = std::move(arg);
    return std::move(msg_);
  }

private:
  ::user_interface::action::Fibonacci_SendGoal_Event msg_;
};

class Init_Fibonacci_SendGoal_Event_request
{
public:
  explicit Init_Fibonacci_SendGoal_Event_request(::user_interface::action::Fibonacci_SendGoal_Event & msg)
  : msg_(msg)
  {}
  Init_Fibonacci_SendGoal_Event_response request(::user_interface::action::Fibonacci_SendGoal_Event::_request_type arg)
  {
    msg_.request = std::move(arg);
    return Init_Fibonacci_SendGoal_Event_response(msg_);
  }

private:
  ::user_interface::action::Fibonacci_SendGoal_Event msg_;
};

class Init_Fibonacci_SendGoal_Event_info
{
public:
  Init_Fibonacci_SendGoal_Event_info()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Fibonacci_SendGoal_Event_request info(::user_interface::action::Fibonacci_SendGoal_Event::_info_type arg)
  {
    msg_.info = std::move(arg);
    return Init_Fibonacci_SendGoal_Event_request(msg_);
  }

private:
  ::user_interface::action::Fibonacci_SendGoal_Event msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::user_interface::action::Fibonacci_SendGoal_Event>()
{
  return user_interface::action::builder::Init_Fibonacci_SendGoal_Event_info();
}

}  // namespace user_interface


namespace user_interface
{

namespace action
{

namespace builder
{

class Init_Fibonacci_GetResult_Request_goal_id
{
public:
  Init_Fibonacci_GetResult_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::user_interface::action::Fibonacci_GetResult_Request goal_id(::user_interface::action::Fibonacci_GetResult_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::user_interface::action::Fibonacci_GetResult_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::user_interface::action::Fibonacci_GetResult_Request>()
{
  return user_interface::action::builder::Init_Fibonacci_GetResult_Request_goal_id();
}

}  // namespace user_interface


namespace user_interface
{

namespace action
{

namespace builder
{

class Init_Fibonacci_GetResult_Response_result
{
public:
  explicit Init_Fibonacci_GetResult_Response_result(::user_interface::action::Fibonacci_GetResult_Response & msg)
  : msg_(msg)
  {}
  ::user_interface::action::Fibonacci_GetResult_Response result(::user_interface::action::Fibonacci_GetResult_Response::_result_type arg)
  {
    msg_.result = std::move(arg);
    return std::move(msg_);
  }

private:
  ::user_interface::action::Fibonacci_GetResult_Response msg_;
};

class Init_Fibonacci_GetResult_Response_status
{
public:
  Init_Fibonacci_GetResult_Response_status()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Fibonacci_GetResult_Response_result status(::user_interface::action::Fibonacci_GetResult_Response::_status_type arg)
  {
    msg_.status = std::move(arg);
    return Init_Fibonacci_GetResult_Response_result(msg_);
  }

private:
  ::user_interface::action::Fibonacci_GetResult_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::user_interface::action::Fibonacci_GetResult_Response>()
{
  return user_interface::action::builder::Init_Fibonacci_GetResult_Response_status();
}

}  // namespace user_interface


namespace user_interface
{

namespace action
{

namespace builder
{

class Init_Fibonacci_GetResult_Event_response
{
public:
  explicit Init_Fibonacci_GetResult_Event_response(::user_interface::action::Fibonacci_GetResult_Event & msg)
  : msg_(msg)
  {}
  ::user_interface::action::Fibonacci_GetResult_Event response(::user_interface::action::Fibonacci_GetResult_Event::_response_type arg)
  {
    msg_.response = std::move(arg);
    return std::move(msg_);
  }

private:
  ::user_interface::action::Fibonacci_GetResult_Event msg_;
};

class Init_Fibonacci_GetResult_Event_request
{
public:
  explicit Init_Fibonacci_GetResult_Event_request(::user_interface::action::Fibonacci_GetResult_Event & msg)
  : msg_(msg)
  {}
  Init_Fibonacci_GetResult_Event_response request(::user_interface::action::Fibonacci_GetResult_Event::_request_type arg)
  {
    msg_.request = std::move(arg);
    return Init_Fibonacci_GetResult_Event_response(msg_);
  }

private:
  ::user_interface::action::Fibonacci_GetResult_Event msg_;
};

class Init_Fibonacci_GetResult_Event_info
{
public:
  Init_Fibonacci_GetResult_Event_info()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Fibonacci_GetResult_Event_request info(::user_interface::action::Fibonacci_GetResult_Event::_info_type arg)
  {
    msg_.info = std::move(arg);
    return Init_Fibonacci_GetResult_Event_request(msg_);
  }

private:
  ::user_interface::action::Fibonacci_GetResult_Event msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::user_interface::action::Fibonacci_GetResult_Event>()
{
  return user_interface::action::builder::Init_Fibonacci_GetResult_Event_info();
}

}  // namespace user_interface


namespace user_interface
{

namespace action
{

namespace builder
{

class Init_Fibonacci_FeedbackMessage_feedback
{
public:
  explicit Init_Fibonacci_FeedbackMessage_feedback(::user_interface::action::Fibonacci_FeedbackMessage & msg)
  : msg_(msg)
  {}
  ::user_interface::action::Fibonacci_FeedbackMessage feedback(::user_interface::action::Fibonacci_FeedbackMessage::_feedback_type arg)
  {
    msg_.feedback = std::move(arg);
    return std::move(msg_);
  }

private:
  ::user_interface::action::Fibonacci_FeedbackMessage msg_;
};

class Init_Fibonacci_FeedbackMessage_goal_id
{
public:
  Init_Fibonacci_FeedbackMessage_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Fibonacci_FeedbackMessage_feedback goal_id(::user_interface::action::Fibonacci_FeedbackMessage::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_Fibonacci_FeedbackMessage_feedback(msg_);
  }

private:
  ::user_interface::action::Fibonacci_FeedbackMessage msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::user_interface::action::Fibonacci_FeedbackMessage>()
{
  return user_interface::action::builder::Init_Fibonacci_FeedbackMessage_goal_id();
}

}  // namespace user_interface

#endif  // USER_INTERFACE__ACTION__DETAIL__FIBONACCI__BUILDER_HPP_
