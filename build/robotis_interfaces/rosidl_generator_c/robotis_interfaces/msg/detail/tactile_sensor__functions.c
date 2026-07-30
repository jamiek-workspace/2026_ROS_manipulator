// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from robotis_interfaces:msg/TactileSensor.idl
// generated code does not contain a copyright notice
#include "robotis_interfaces/msg/detail/tactile_sensor__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `sensor_name`
// Member `pressure_names`
#include "rosidl_runtime_c/string_functions.h"

bool
robotis_interfaces__msg__TactileSensor__init(robotis_interfaces__msg__TactileSensor * msg)
{
  if (!msg) {
    return false;
  }
  // sensor_name
  if (!rosidl_runtime_c__String__init(&msg->sensor_name)) {
    robotis_interfaces__msg__TactileSensor__fini(msg);
    return false;
  }
  // pressure_names
  for (size_t i = 0; i < 9; ++i) {
    if (!rosidl_runtime_c__String__init(&msg->pressure_names[i])) {
      robotis_interfaces__msg__TactileSensor__fini(msg);
      return false;
    }
  }
  // pressure_values
  return true;
}

void
robotis_interfaces__msg__TactileSensor__fini(robotis_interfaces__msg__TactileSensor * msg)
{
  if (!msg) {
    return;
  }
  // sensor_name
  rosidl_runtime_c__String__fini(&msg->sensor_name);
  // pressure_names
  for (size_t i = 0; i < 9; ++i) {
    rosidl_runtime_c__String__fini(&msg->pressure_names[i]);
  }
  // pressure_values
}

bool
robotis_interfaces__msg__TactileSensor__are_equal(const robotis_interfaces__msg__TactileSensor * lhs, const robotis_interfaces__msg__TactileSensor * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // sensor_name
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->sensor_name), &(rhs->sensor_name)))
  {
    return false;
  }
  // pressure_names
  for (size_t i = 0; i < 9; ++i) {
    if (!rosidl_runtime_c__String__are_equal(
        &(lhs->pressure_names[i]), &(rhs->pressure_names[i])))
    {
      return false;
    }
  }
  // pressure_values
  for (size_t i = 0; i < 9; ++i) {
    if (lhs->pressure_values[i] != rhs->pressure_values[i]) {
      return false;
    }
  }
  return true;
}

bool
robotis_interfaces__msg__TactileSensor__copy(
  const robotis_interfaces__msg__TactileSensor * input,
  robotis_interfaces__msg__TactileSensor * output)
{
  if (!input || !output) {
    return false;
  }
  // sensor_name
  if (!rosidl_runtime_c__String__copy(
      &(input->sensor_name), &(output->sensor_name)))
  {
    return false;
  }
  // pressure_names
  for (size_t i = 0; i < 9; ++i) {
    if (!rosidl_runtime_c__String__copy(
        &(input->pressure_names[i]), &(output->pressure_names[i])))
    {
      return false;
    }
  }
  // pressure_values
  for (size_t i = 0; i < 9; ++i) {
    output->pressure_values[i] = input->pressure_values[i];
  }
  return true;
}

robotis_interfaces__msg__TactileSensor *
robotis_interfaces__msg__TactileSensor__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  robotis_interfaces__msg__TactileSensor * msg = (robotis_interfaces__msg__TactileSensor *)allocator.allocate(sizeof(robotis_interfaces__msg__TactileSensor), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(robotis_interfaces__msg__TactileSensor));
  bool success = robotis_interfaces__msg__TactileSensor__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
robotis_interfaces__msg__TactileSensor__destroy(robotis_interfaces__msg__TactileSensor * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    robotis_interfaces__msg__TactileSensor__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
robotis_interfaces__msg__TactileSensor__Sequence__init(robotis_interfaces__msg__TactileSensor__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  robotis_interfaces__msg__TactileSensor * data = NULL;

  if (size) {
    if (size > SIZE_MAX / sizeof(robotis_interfaces__msg__TactileSensor)) {
      return false;
    }
    data = (robotis_interfaces__msg__TactileSensor *)allocator.zero_allocate(size, sizeof(robotis_interfaces__msg__TactileSensor), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = robotis_interfaces__msg__TactileSensor__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        robotis_interfaces__msg__TactileSensor__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
robotis_interfaces__msg__TactileSensor__Sequence__fini(robotis_interfaces__msg__TactileSensor__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      robotis_interfaces__msg__TactileSensor__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

robotis_interfaces__msg__TactileSensor__Sequence *
robotis_interfaces__msg__TactileSensor__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  robotis_interfaces__msg__TactileSensor__Sequence * array = (robotis_interfaces__msg__TactileSensor__Sequence *)allocator.allocate(sizeof(robotis_interfaces__msg__TactileSensor__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = robotis_interfaces__msg__TactileSensor__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
robotis_interfaces__msg__TactileSensor__Sequence__destroy(robotis_interfaces__msg__TactileSensor__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    robotis_interfaces__msg__TactileSensor__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
robotis_interfaces__msg__TactileSensor__Sequence__are_equal(const robotis_interfaces__msg__TactileSensor__Sequence * lhs, const robotis_interfaces__msg__TactileSensor__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!robotis_interfaces__msg__TactileSensor__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
robotis_interfaces__msg__TactileSensor__Sequence__copy(
  const robotis_interfaces__msg__TactileSensor__Sequence * input,
  robotis_interfaces__msg__TactileSensor__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    if (input->size > SIZE_MAX / sizeof(robotis_interfaces__msg__TactileSensor)) {
      return false;
    }
    const size_t allocation_size =
      input->size * sizeof(robotis_interfaces__msg__TactileSensor);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    robotis_interfaces__msg__TactileSensor * data =
      (robotis_interfaces__msg__TactileSensor *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!robotis_interfaces__msg__TactileSensor__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          robotis_interfaces__msg__TactileSensor__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!robotis_interfaces__msg__TactileSensor__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
