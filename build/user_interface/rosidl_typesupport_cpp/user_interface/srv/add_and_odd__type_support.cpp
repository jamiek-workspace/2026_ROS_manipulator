// generated from rosidl_typesupport_cpp/resource/idl__type_support.cpp.em
// with input from user_interface:srv/AddAndOdd.idl
// generated code does not contain a copyright notice

#include "cstddef"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "user_interface/srv/detail/add_and_odd__functions.h"
#include "user_interface/srv/detail/add_and_odd__struct.hpp"
#include "rosidl_typesupport_cpp/identifier.hpp"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_c/type_support_map.h"
#include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
#include "rosidl_typesupport_cpp/visibility_control.h"
#include "rosidl_typesupport_interface/macros.h"

namespace user_interface
{

namespace srv
{

namespace rosidl_typesupport_cpp
{

typedef struct _AddAndOdd_Request_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _AddAndOdd_Request_type_support_ids_t;

static const _AddAndOdd_Request_type_support_ids_t _AddAndOdd_Request_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _AddAndOdd_Request_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _AddAndOdd_Request_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _AddAndOdd_Request_type_support_symbol_names_t _AddAndOdd_Request_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, user_interface, srv, AddAndOdd_Request)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, user_interface, srv, AddAndOdd_Request)),
  }
};

typedef struct _AddAndOdd_Request_type_support_data_t
{
  void * data[2];
} _AddAndOdd_Request_type_support_data_t;

static _AddAndOdd_Request_type_support_data_t _AddAndOdd_Request_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _AddAndOdd_Request_message_typesupport_map = {
  2,
  "user_interface",
  &_AddAndOdd_Request_message_typesupport_ids.typesupport_identifier[0],
  &_AddAndOdd_Request_message_typesupport_symbol_names.symbol_name[0],
  &_AddAndOdd_Request_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t AddAndOdd_Request_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_AddAndOdd_Request_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
  &user_interface__srv__AddAndOdd_Request__get_type_hash,
  &user_interface__srv__AddAndOdd_Request__get_type_description,
  &user_interface__srv__AddAndOdd_Request__get_type_description_sources,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace srv

}  // namespace user_interface

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<user_interface::srv::AddAndOdd_Request>()
{
  return &::user_interface::srv::rosidl_typesupport_cpp::AddAndOdd_Request_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, user_interface, srv, AddAndOdd_Request)() {
  return get_message_type_support_handle<user_interface::srv::AddAndOdd_Request>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "user_interface/srv/detail/add_and_odd__functions.h"
// already included above
// #include "user_interface/srv/detail/add_and_odd__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace user_interface
{

namespace srv
{

namespace rosidl_typesupport_cpp
{

typedef struct _AddAndOdd_Response_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _AddAndOdd_Response_type_support_ids_t;

static const _AddAndOdd_Response_type_support_ids_t _AddAndOdd_Response_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _AddAndOdd_Response_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _AddAndOdd_Response_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _AddAndOdd_Response_type_support_symbol_names_t _AddAndOdd_Response_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, user_interface, srv, AddAndOdd_Response)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, user_interface, srv, AddAndOdd_Response)),
  }
};

typedef struct _AddAndOdd_Response_type_support_data_t
{
  void * data[2];
} _AddAndOdd_Response_type_support_data_t;

static _AddAndOdd_Response_type_support_data_t _AddAndOdd_Response_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _AddAndOdd_Response_message_typesupport_map = {
  2,
  "user_interface",
  &_AddAndOdd_Response_message_typesupport_ids.typesupport_identifier[0],
  &_AddAndOdd_Response_message_typesupport_symbol_names.symbol_name[0],
  &_AddAndOdd_Response_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t AddAndOdd_Response_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_AddAndOdd_Response_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
  &user_interface__srv__AddAndOdd_Response__get_type_hash,
  &user_interface__srv__AddAndOdd_Response__get_type_description,
  &user_interface__srv__AddAndOdd_Response__get_type_description_sources,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace srv

}  // namespace user_interface

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<user_interface::srv::AddAndOdd_Response>()
{
  return &::user_interface::srv::rosidl_typesupport_cpp::AddAndOdd_Response_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, user_interface, srv, AddAndOdd_Response)() {
  return get_message_type_support_handle<user_interface::srv::AddAndOdd_Response>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "user_interface/srv/detail/add_and_odd__functions.h"
// already included above
// #include "user_interface/srv/detail/add_and_odd__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace user_interface
{

namespace srv
{

namespace rosidl_typesupport_cpp
{

typedef struct _AddAndOdd_Event_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _AddAndOdd_Event_type_support_ids_t;

static const _AddAndOdd_Event_type_support_ids_t _AddAndOdd_Event_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _AddAndOdd_Event_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _AddAndOdd_Event_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _AddAndOdd_Event_type_support_symbol_names_t _AddAndOdd_Event_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, user_interface, srv, AddAndOdd_Event)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, user_interface, srv, AddAndOdd_Event)),
  }
};

typedef struct _AddAndOdd_Event_type_support_data_t
{
  void * data[2];
} _AddAndOdd_Event_type_support_data_t;

static _AddAndOdd_Event_type_support_data_t _AddAndOdd_Event_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _AddAndOdd_Event_message_typesupport_map = {
  2,
  "user_interface",
  &_AddAndOdd_Event_message_typesupport_ids.typesupport_identifier[0],
  &_AddAndOdd_Event_message_typesupport_symbol_names.symbol_name[0],
  &_AddAndOdd_Event_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t AddAndOdd_Event_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_AddAndOdd_Event_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
  &user_interface__srv__AddAndOdd_Event__get_type_hash,
  &user_interface__srv__AddAndOdd_Event__get_type_description,
  &user_interface__srv__AddAndOdd_Event__get_type_description_sources,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace srv

}  // namespace user_interface

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<user_interface::srv::AddAndOdd_Event>()
{
  return &::user_interface::srv::rosidl_typesupport_cpp::AddAndOdd_Event_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, user_interface, srv, AddAndOdd_Event)() {
  return get_message_type_support_handle<user_interface::srv::AddAndOdd_Event>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
#include "rosidl_runtime_c/service_type_support_struct.h"
#include "rosidl_typesupport_cpp/service_type_support.hpp"
// already included above
// #include "user_interface/srv/detail/add_and_odd__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
#include "rosidl_typesupport_cpp/service_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace user_interface
{

namespace srv
{

namespace rosidl_typesupport_cpp
{

typedef struct _AddAndOdd_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _AddAndOdd_type_support_ids_t;

static const _AddAndOdd_type_support_ids_t _AddAndOdd_service_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _AddAndOdd_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _AddAndOdd_type_support_symbol_names_t;
#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _AddAndOdd_type_support_symbol_names_t _AddAndOdd_service_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, user_interface, srv, AddAndOdd)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, user_interface, srv, AddAndOdd)),
  }
};

typedef struct _AddAndOdd_type_support_data_t
{
  void * data[2];
} _AddAndOdd_type_support_data_t;

static _AddAndOdd_type_support_data_t _AddAndOdd_service_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _AddAndOdd_service_typesupport_map = {
  2,
  "user_interface",
  &_AddAndOdd_service_typesupport_ids.typesupport_identifier[0],
  &_AddAndOdd_service_typesupport_symbol_names.symbol_name[0],
  &_AddAndOdd_service_typesupport_data.data[0],
};

static const rosidl_service_type_support_t AddAndOdd_service_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_AddAndOdd_service_typesupport_map),
  ::rosidl_typesupport_cpp::get_service_typesupport_handle_function,
  ::rosidl_typesupport_cpp::get_message_type_support_handle<user_interface::srv::AddAndOdd_Request>(),
  ::rosidl_typesupport_cpp::get_message_type_support_handle<user_interface::srv::AddAndOdd_Response>(),
  ::rosidl_typesupport_cpp::get_message_type_support_handle<user_interface::srv::AddAndOdd_Event>(),
  &::rosidl_typesupport_cpp::service_create_event_message<user_interface::srv::AddAndOdd>,
  &::rosidl_typesupport_cpp::service_destroy_event_message<user_interface::srv::AddAndOdd>,
  &user_interface__srv__AddAndOdd__get_type_hash,
  &user_interface__srv__AddAndOdd__get_type_description,
  &user_interface__srv__AddAndOdd__get_type_description_sources,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace srv

}  // namespace user_interface

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_service_type_support_t *
get_service_type_support_handle<user_interface::srv::AddAndOdd>()
{
  return &::user_interface::srv::rosidl_typesupport_cpp::AddAndOdd_service_type_support_handle;
}

}  // namespace rosidl_typesupport_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_cpp, user_interface, srv, AddAndOdd)() {
  return ::rosidl_typesupport_cpp::get_service_type_support_handle<user_interface::srv::AddAndOdd>();
}

#ifdef __cplusplus
}
#endif
