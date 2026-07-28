// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from robotis_interfaces:msg/HandJoints.idl
// generated code does not contain a copyright notice
#include "robotis_interfaces/msg/detail/hand_joints__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"
// Member `joints`
#include "geometry_msgs/msg/detail/point32__functions.h"

bool
robotis_interfaces__msg__HandJoints__init(robotis_interfaces__msg__HandJoints * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    robotis_interfaces__msg__HandJoints__fini(msg);
    return false;
  }
  // joints
  for (size_t i = 0; i < 21; ++i) {
    if (!geometry_msgs__msg__Point32__init(&msg->joints[i])) {
      robotis_interfaces__msg__HandJoints__fini(msg);
      return false;
    }
  }
  return true;
}

void
robotis_interfaces__msg__HandJoints__fini(robotis_interfaces__msg__HandJoints * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // joints
  for (size_t i = 0; i < 21; ++i) {
    geometry_msgs__msg__Point32__fini(&msg->joints[i]);
  }
}

bool
robotis_interfaces__msg__HandJoints__are_equal(const robotis_interfaces__msg__HandJoints * lhs, const robotis_interfaces__msg__HandJoints * rhs)
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
  // joints
  for (size_t i = 0; i < 21; ++i) {
    if (!geometry_msgs__msg__Point32__are_equal(
        &(lhs->joints[i]), &(rhs->joints[i])))
    {
      return false;
    }
  }
  return true;
}

bool
robotis_interfaces__msg__HandJoints__copy(
  const robotis_interfaces__msg__HandJoints * input,
  robotis_interfaces__msg__HandJoints * output)
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
  // joints
  for (size_t i = 0; i < 21; ++i) {
    if (!geometry_msgs__msg__Point32__copy(
        &(input->joints[i]), &(output->joints[i])))
    {
      return false;
    }
  }
  return true;
}

robotis_interfaces__msg__HandJoints *
robotis_interfaces__msg__HandJoints__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  robotis_interfaces__msg__HandJoints * msg = (robotis_interfaces__msg__HandJoints *)allocator.allocate(sizeof(robotis_interfaces__msg__HandJoints), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(robotis_interfaces__msg__HandJoints));
  bool success = robotis_interfaces__msg__HandJoints__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
robotis_interfaces__msg__HandJoints__destroy(robotis_interfaces__msg__HandJoints * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    robotis_interfaces__msg__HandJoints__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
robotis_interfaces__msg__HandJoints__Sequence__init(robotis_interfaces__msg__HandJoints__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  robotis_interfaces__msg__HandJoints * data = NULL;

  if (size) {
    if (size > SIZE_MAX / sizeof(robotis_interfaces__msg__HandJoints)) {
      return false;
    }
    data = (robotis_interfaces__msg__HandJoints *)allocator.zero_allocate(size, sizeof(robotis_interfaces__msg__HandJoints), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = robotis_interfaces__msg__HandJoints__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        robotis_interfaces__msg__HandJoints__fini(&data[i - 1]);
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
robotis_interfaces__msg__HandJoints__Sequence__fini(robotis_interfaces__msg__HandJoints__Sequence * array)
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
      robotis_interfaces__msg__HandJoints__fini(&array->data[i]);
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

robotis_interfaces__msg__HandJoints__Sequence *
robotis_interfaces__msg__HandJoints__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  robotis_interfaces__msg__HandJoints__Sequence * array = (robotis_interfaces__msg__HandJoints__Sequence *)allocator.allocate(sizeof(robotis_interfaces__msg__HandJoints__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = robotis_interfaces__msg__HandJoints__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
robotis_interfaces__msg__HandJoints__Sequence__destroy(robotis_interfaces__msg__HandJoints__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    robotis_interfaces__msg__HandJoints__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
robotis_interfaces__msg__HandJoints__Sequence__are_equal(const robotis_interfaces__msg__HandJoints__Sequence * lhs, const robotis_interfaces__msg__HandJoints__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!robotis_interfaces__msg__HandJoints__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
robotis_interfaces__msg__HandJoints__Sequence__copy(
  const robotis_interfaces__msg__HandJoints__Sequence * input,
  robotis_interfaces__msg__HandJoints__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    if (input->size > SIZE_MAX / sizeof(robotis_interfaces__msg__HandJoints)) {
      return false;
    }
    const size_t allocation_size =
      input->size * sizeof(robotis_interfaces__msg__HandJoints);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    robotis_interfaces__msg__HandJoints * data =
      (robotis_interfaces__msg__HandJoints *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!robotis_interfaces__msg__HandJoints__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          robotis_interfaces__msg__HandJoints__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!robotis_interfaces__msg__HandJoints__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
