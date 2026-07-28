// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from robotis_interfaces:msg/TactileSensor.idl
// generated code does not contain a copyright notice
#include "robotis_interfaces/msg/detail/tactile_sensor__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <cstddef>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/serialization_helpers.hpp"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "robotis_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "robotis_interfaces/msg/detail/tactile_sensor__struct.h"
#include "robotis_interfaces/msg/detail/tactile_sensor__functions.h"
#include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif

#include "rosidl_runtime_c/string.h"  // pressure_names, sensor_name
#include "rosidl_runtime_c/string_functions.h"  // pressure_names, sensor_name

// forward declare type support functions


using _TactileSensor__ros_msg_type = robotis_interfaces__msg__TactileSensor;


ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_robotis_interfaces
bool cdr_serialize_robotis_interfaces__msg__TactileSensor(
  const robotis_interfaces__msg__TactileSensor * ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Field name: sensor_name
  {
    const rosidl_runtime_c__String * str = &ros_message->sensor_name;
    if (str->capacity == 0 || str->capacity <= str->size) {
      fprintf(stderr, "string capacity not greater than size\n");
      return false;
    }
    if (str->data[str->size] != '\0') {
      fprintf(stderr, "string not null-terminated\n");
      return false;
    }
    cdr << str->data;
  }

  // Field name: pressure_names
  {
    size_t size = 9;
    auto array_ptr = ros_message->pressure_names;
    for (size_t i = 0; i < size; ++i) {
      const rosidl_runtime_c__String * str = &array_ptr[i];
      if (str->capacity == 0 || str->capacity <= str->size) {
        fprintf(stderr, "string capacity not greater than size\n");
        return false;
      }
      if (str->data[str->size] != '\0') {
        fprintf(stderr, "string not null-terminated\n");
        return false;
      }
      cdr << str->data;
    }
  }

  // Field name: pressure_values
  {
    size_t size = 9;
    auto array_ptr = ros_message->pressure_values;
    cdr.serialize_array(array_ptr, size);
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_robotis_interfaces
bool cdr_deserialize_robotis_interfaces__msg__TactileSensor(
  eprosima::fastcdr::Cdr & cdr,
  robotis_interfaces__msg__TactileSensor * ros_message)
{
  // Field name: sensor_name
  {
    std::string tmp;
    cdr >> tmp;
    if (!ros_message->sensor_name.data) {
      rosidl_runtime_c__String__init(&ros_message->sensor_name);
    }
    bool succeeded = rosidl_runtime_c__String__assign(
      &ros_message->sensor_name,
      tmp.c_str());
    if (!succeeded) {
      fprintf(stderr, "failed to assign string into field 'sensor_name'\n");
      return false;
    }
  }

  // Field name: pressure_names
  {
    size_t size = 9;
    auto array_ptr = ros_message->pressure_names;
    for (size_t i = 0; i < size; ++i) {
      std::string tmp;
      cdr >> tmp;
      auto & ros_i = array_ptr[i];
      if (!ros_i.data) {
        rosidl_runtime_c__String__init(&ros_i);
      }
      bool succeeded = rosidl_runtime_c__String__assign(
        &ros_i,
        tmp.c_str());
      if (!succeeded) {
        fprintf(stderr, "failed to assign string into field 'pressure_names'\n");
        return false;
      }
    }
  }

  // Field name: pressure_values
  {
    size_t size = 9;
    auto array_ptr = ros_message->pressure_values;
    cdr.deserialize_array(array_ptr, size);
  }

  return true;
}  // NOLINT(readability/fn_size)


ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_robotis_interfaces
size_t get_serialized_size_robotis_interfaces__msg__TactileSensor(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _TactileSensor__ros_msg_type * ros_message = static_cast<const _TactileSensor__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Field name: sensor_name
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message->sensor_name.size + 1);

  // Field name: pressure_names
  {
    size_t array_size = 9;
    auto array_ptr = ros_message->pressure_names;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        (array_ptr[index].size + 1);
    }
  }

  // Field name: pressure_values
  {
    size_t array_size = 9;
    auto array_ptr = ros_message->pressure_values;
    (void)array_ptr;
    size_t item_size = sizeof(array_ptr[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}


ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_robotis_interfaces
size_t max_serialized_size_robotis_interfaces__msg__TactileSensor(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  size_t last_member_size = 0;
  (void)last_member_size;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;

  // Field name: sensor_name
  {
    size_t array_size = 1;
    full_bounded = false;
    is_plain = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }

  // Field name: pressure_names
  {
    size_t array_size = 9;
    full_bounded = false;
    is_plain = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }

  // Field name: pressure_values
  {
    size_t array_size = 9;
    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }


  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = robotis_interfaces__msg__TactileSensor;
    is_plain =
      (
      offsetof(DataType, pressure_values) +
      last_member_size
      ) == ret_val;
  }
  return ret_val;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_robotis_interfaces
bool cdr_serialize_key_robotis_interfaces__msg__TactileSensor(
  const robotis_interfaces__msg__TactileSensor * ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Field name: sensor_name
  {
    const rosidl_runtime_c__String * str = &ros_message->sensor_name;
    if (str->capacity == 0 || str->capacity <= str->size) {
      fprintf(stderr, "string capacity not greater than size\n");
      return false;
    }
    if (str->data[str->size] != '\0') {
      fprintf(stderr, "string not null-terminated\n");
      return false;
    }
    cdr << str->data;
  }

  // Field name: pressure_names
  {
    size_t size = 9;
    auto array_ptr = ros_message->pressure_names;
    for (size_t i = 0; i < size; ++i) {
      const rosidl_runtime_c__String * str = &array_ptr[i];
      if (str->capacity == 0 || str->capacity <= str->size) {
        fprintf(stderr, "string capacity not greater than size\n");
        return false;
      }
      if (str->data[str->size] != '\0') {
        fprintf(stderr, "string not null-terminated\n");
        return false;
      }
      cdr << str->data;
    }
  }

  // Field name: pressure_values
  {
    size_t size = 9;
    auto array_ptr = ros_message->pressure_values;
    cdr.serialize_array(array_ptr, size);
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_robotis_interfaces
size_t get_serialized_size_key_robotis_interfaces__msg__TactileSensor(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _TactileSensor__ros_msg_type * ros_message = static_cast<const _TactileSensor__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;

  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Field name: sensor_name
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message->sensor_name.size + 1);

  // Field name: pressure_names
  {
    size_t array_size = 9;
    auto array_ptr = ros_message->pressure_names;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        (array_ptr[index].size + 1);
    }
  }

  // Field name: pressure_values
  {
    size_t array_size = 9;
    auto array_ptr = ros_message->pressure_values;
    (void)array_ptr;
    size_t item_size = sizeof(array_ptr[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_robotis_interfaces
size_t max_serialized_size_key_robotis_interfaces__msg__TactileSensor(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  size_t last_member_size = 0;
  (void)last_member_size;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;
  // Field name: sensor_name
  {
    size_t array_size = 1;
    full_bounded = false;
    is_plain = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }

  // Field name: pressure_names
  {
    size_t array_size = 9;
    full_bounded = false;
    is_plain = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }

  // Field name: pressure_values
  {
    size_t array_size = 9;
    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = robotis_interfaces__msg__TactileSensor;
    is_plain =
      (
      offsetof(DataType, pressure_values) +
      last_member_size
      ) == ret_val;
  }
  return ret_val;
}


static bool _TactileSensor__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const robotis_interfaces__msg__TactileSensor * ros_message = static_cast<const robotis_interfaces__msg__TactileSensor *>(untyped_ros_message);
  (void)ros_message;
  return cdr_serialize_robotis_interfaces__msg__TactileSensor(ros_message, cdr);
}

static bool _TactileSensor__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  robotis_interfaces__msg__TactileSensor * ros_message = static_cast<robotis_interfaces__msg__TactileSensor *>(untyped_ros_message);
  (void)ros_message;
  return cdr_deserialize_robotis_interfaces__msg__TactileSensor(cdr, ros_message);
}

static uint32_t _TactileSensor__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_robotis_interfaces__msg__TactileSensor(
      untyped_ros_message, 0));
}

static size_t _TactileSensor__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_robotis_interfaces__msg__TactileSensor(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_TactileSensor = {
  "robotis_interfaces::msg",
  "TactileSensor",
  _TactileSensor__cdr_serialize,
  _TactileSensor__cdr_deserialize,
  _TactileSensor__get_serialized_size,
  _TactileSensor__max_serialized_size,
  nullptr
};

static rosidl_message_type_support_t _TactileSensor__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_TactileSensor,
  get_message_typesupport_handle_function,
  &robotis_interfaces__msg__TactileSensor__get_type_hash,
  &robotis_interfaces__msg__TactileSensor__get_type_description,
  &robotis_interfaces__msg__TactileSensor__get_type_description_sources,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, robotis_interfaces, msg, TactileSensor)() {
  return &_TactileSensor__type_support;
}

#if defined(__cplusplus)
}
#endif
