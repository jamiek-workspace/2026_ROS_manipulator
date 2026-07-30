// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from user_interface:srv/AddAndOdd.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "user_interface/srv/add_and_odd.h"


#ifndef USER_INTERFACE__SRV__DETAIL__ADD_AND_ODD__STRUCT_H_
#define USER_INTERFACE__SRV__DETAIL__ADD_AND_ODD__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/AddAndOdd in the package user_interface.
typedef struct user_interface__srv__AddAndOdd_Request
{
  int32_t inta;
  int32_t intb;
} user_interface__srv__AddAndOdd_Request;

// Struct for a sequence of user_interface__srv__AddAndOdd_Request.
typedef struct user_interface__srv__AddAndOdd_Request__Sequence
{
  user_interface__srv__AddAndOdd_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} user_interface__srv__AddAndOdd_Request__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'odd'
#include "rosidl_runtime_c/string.h"

/// Struct defined in srv/AddAndOdd in the package user_interface.
typedef struct user_interface__srv__AddAndOdd_Response
{
  int32_t sum;
  rosidl_runtime_c__String odd;
} user_interface__srv__AddAndOdd_Response;

// Struct for a sequence of user_interface__srv__AddAndOdd_Response.
typedef struct user_interface__srv__AddAndOdd_Response__Sequence
{
  user_interface__srv__AddAndOdd_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} user_interface__srv__AddAndOdd_Response__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'info'
#include "service_msgs/msg/detail/service_event_info__struct.h"

// constants for array fields with an upper bound
// request
enum
{
  user_interface__srv__AddAndOdd_Event__request__MAX_SIZE = 1
};
// response
enum
{
  user_interface__srv__AddAndOdd_Event__response__MAX_SIZE = 1
};

/// Struct defined in srv/AddAndOdd in the package user_interface.
typedef struct user_interface__srv__AddAndOdd_Event
{
  service_msgs__msg__ServiceEventInfo info;
  user_interface__srv__AddAndOdd_Request__Sequence request;
  user_interface__srv__AddAndOdd_Response__Sequence response;
} user_interface__srv__AddAndOdd_Event;

// Struct for a sequence of user_interface__srv__AddAndOdd_Event.
typedef struct user_interface__srv__AddAndOdd_Event__Sequence
{
  user_interface__srv__AddAndOdd_Event * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} user_interface__srv__AddAndOdd_Event__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // USER_INTERFACE__SRV__DETAIL__ADD_AND_ODD__STRUCT_H_
