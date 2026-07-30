// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from robotis_interfaces:msg/HandPressures.idl
// generated code does not contain a copyright notice
#include "robotis_interfaces/msg/detail/hand_pressures__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"
// Member `hand_name`
#include "rosidl_runtime_c/string_functions.h"
// Member `sensors`
#include "robotis_interfaces/msg/detail/tactile_sensor__functions.h"

bool
robotis_interfaces__msg__HandPressures__init(robotis_interfaces__msg__HandPressures * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    robotis_interfaces__msg__HandPressures__fini(msg);
    return false;
  }
  // hand_name
  if (!rosidl_runtime_c__String__init(&msg->hand_name)) {
    robotis_interfaces__msg__HandPressures__fini(msg);
    return false;
  }
  // sensors
  if (!robotis_interfaces__msg__TactileSensor__Sequence__init(&msg->sensors, 0)) {
    robotis_interfaces__msg__HandPressures__fini(msg);
    return false;
  }
  return true;
}

void
robotis_interfaces__msg__HandPressures__fini(robotis_interfaces__msg__HandPressures * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // hand_name
  rosidl_runtime_c__String__fini(&msg->hand_name);
  // sensors
  robotis_interfaces__msg__TactileSensor__Sequence__fini(&msg->sensors);
}

bool
robotis_interfaces__msg__HandPressures__are_equal(const robotis_interfaces__msg__HandPressures * lhs, const robotis_interfaces__msg__HandPressures * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__are_equal(
      &(lhs->header), &(rhs->header)))
  {
    return false;
  }
  // hand_name
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->hand_name), &(rhs->hand_name)))
  {
    return false;
  }
  // sensors
  if (!robotis_interfaces__msg__TactileSensor__Sequence__are_equal(
      &(lhs->sensors), &(rhs->sensors)))
  {
    return false;
  }
  return true;
}

bool
robotis_interfaces__msg__HandPressures__copy(
  const robotis_interfaces__msg__HandPressures * input,
  robotis_interfaces__msg__HandPressures * output)
{
  if (!input || !output) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__copy(
      &(input->header), &(output->header)))
  {
    return false;
  }
  // hand_name
  if (!rosidl_runtime_c__String__copy(
      &(input->hand_name), &(output->hand_name)))
  {
    return false;
  }
  // sensors
  if (!robotis_interfaces__msg__TactileSensor__Sequence__copy(
      &(input->sensors), &(output->sensors)))
  {
    return false;
  }
  return true;
}

robotis_interfaces__msg__HandPressures *
robotis_interfaces__msg__HandPressures__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  robotis_interfaces__msg__HandPressures * msg = (robotis_interfaces__msg__HandPressures *)allocator.allocate(sizeof(robotis_interfaces__msg__HandPressures), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(robotis_interfaces__msg__HandPressures));
  bool success = robotis_interfaces__msg__HandPressures__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
robotis_interfaces__msg__HandPressures__destroy(robotis_interfaces__msg__HandPressures * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    robotis_interfaces__msg__HandPressures__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
robotis_interfaces__msg__HandPressures__Sequence__init(robotis_interfaces__msg__HandPressures__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  robotis_interfaces__msg__HandPressures * data = NULL;

  if (size) {
    if (size > SIZE_MAX / sizeof(robotis_interfaces__msg__HandPressures)) {
      return false;
    }
    data = (robotis_interfaces__msg__HandPressures *)allocator.zero_allocate(size, sizeof(robotis_interfaces__msg__HandPressures), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = robotis_interfaces__msg__HandPressures__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        robotis_interfaces__msg__HandPressures__fini(&data[i - 1]);
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
robotis_interfaces__msg__HandPressures__Sequence__fini(robotis_interfaces__msg__HandPressures__Sequence * array)
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
      robotis_interfaces__msg__HandPressures__fini(&array->data[i]);
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

robotis_interfaces__msg__HandPressures__Sequence *
robotis_interfaces__msg__HandPressures__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  robotis_interfaces__msg__HandPressures__Sequence * array = (robotis_interfaces__msg__HandPressures__Sequence *)allocator.allocate(sizeof(robotis_interfaces__msg__HandPressures__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = robotis_interfaces__msg__HandPressures__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
robotis_interfaces__msg__HandPressures__Sequence__destroy(robotis_interfaces__msg__HandPressures__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    robotis_interfaces__msg__HandPressures__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
robotis_interfaces__msg__HandPressures__Sequence__are_equal(const robotis_interfaces__msg__HandPressures__Sequence * lhs, const robotis_interfaces__msg__HandPressures__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!robotis_interfaces__msg__HandPressures__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
robotis_interfaces__msg__HandPressures__Sequence__copy(
  const robotis_interfaces__msg__HandPressures__Sequence * input,
  robotis_interfaces__msg__HandPressures__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    if (input->size > SIZE_MAX / sizeof(robotis_interfaces__msg__HandPressures)) {
      return false;
    }
    const size_t allocation_size =
      input->size * sizeof(robotis_interfaces__msg__HandPressures);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    robotis_interfaces__msg__HandPressures * data =
      (robotis_interfaces__msg__HandPressures *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!robotis_interfaces__msg__HandPressures__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          robotis_interfaces__msg__HandPressures__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!robotis_interfaces__msg__HandPressures__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
