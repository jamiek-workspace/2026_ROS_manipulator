// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from user_interface:msg/UserInt.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "user_interface/msg/detail/user_int__rosidl_typesupport_introspection_c.h"
#include "user_interface/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "user_interface/msg/detail/user_int__functions.h"
#include "user_interface/msg/detail/user_int__struct.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/header.h"
// Member `header`
#include "std_msgs/msg/detail/header__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void user_interface__msg__UserInt__rosidl_typesupport_introspection_c__UserInt_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  user_interface__msg__UserInt__init(message_memory);
}

void user_interface__msg__UserInt__rosidl_typesupport_introspection_c__UserInt_fini_function(void * message_memory)
{
  user_interface__msg__UserInt__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember user_interface__msg__UserInt__rosidl_typesupport_introspection_c__UserInt_message_member_array[4] = {
  {
    "header",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(user_interface__msg__UserInt, header),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "user_int",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(user_interface__msg__UserInt, user_int),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "user_int2",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(user_interface__msg__UserInt, user_int2),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "user_int3",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(user_interface__msg__UserInt, user_int3),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers user_interface__msg__UserInt__rosidl_typesupport_introspection_c__UserInt_message_members = {
  "user_interface__msg",  // message namespace
  "UserInt",  // message name
  4,  // number of fields
  sizeof(user_interface__msg__UserInt),
  false,  // has_any_key_member_
  user_interface__msg__UserInt__rosidl_typesupport_introspection_c__UserInt_message_member_array,  // message members
  user_interface__msg__UserInt__rosidl_typesupport_introspection_c__UserInt_init_function,  // function to initialize message memory (memory has to be allocated)
  user_interface__msg__UserInt__rosidl_typesupport_introspection_c__UserInt_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t user_interface__msg__UserInt__rosidl_typesupport_introspection_c__UserInt_message_type_support_handle = {
  0,
  &user_interface__msg__UserInt__rosidl_typesupport_introspection_c__UserInt_message_members,
  get_message_typesupport_handle_function,
  &user_interface__msg__UserInt__get_type_hash,
  &user_interface__msg__UserInt__get_type_description,
  &user_interface__msg__UserInt__get_type_description_sources,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_user_interface
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, user_interface, msg, UserInt)() {
  user_interface__msg__UserInt__rosidl_typesupport_introspection_c__UserInt_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, std_msgs, msg, Header)();
  if (!user_interface__msg__UserInt__rosidl_typesupport_introspection_c__UserInt_message_type_support_handle.typesupport_identifier) {
    user_interface__msg__UserInt__rosidl_typesupport_introspection_c__UserInt_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &user_interface__msg__UserInt__rosidl_typesupport_introspection_c__UserInt_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
