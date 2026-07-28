// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from robotis_interfaces:msg/MoveL.idl
// generated code does not contain a copyright notice
#include "robotis_interfaces/msg/detail/move_l__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `pose`
#include "geometry_msgs/msg/detail/pose_stamped__functions.h"
// Member `time_from_start`
#include "builtin_interfaces/msg/detail/duration__functions.h"

bool
robotis_interfaces__msg__MoveL__init(robotis_interfaces__msg__MoveL * msg)
{
  if (!msg) {
    return false;
  }
  // pose
  if (!geometry_msgs__msg__PoseStamped__init(&msg->pose)) {
    robotis_interfaces__msg__MoveL__fini(msg);
    return false;
  }
  // time_from_start
  if (!builtin_interfaces__msg__Duration__init(&msg->time_from_start)) {
    robotis_interfaces__msg__MoveL__fini(msg);
    return false;
  }
  return true;
}

void
robotis_interfaces__msg__MoveL__fini(robotis_interfaces__msg__MoveL * msg)
{
  if (!msg) {
    return;
  }
  // pose
  geometry_msgs__msg__PoseStamped__fini(&msg->pose);
  // time_from_start
  builtin_interfaces__msg__Duration__fini(&msg->time_from_start);
}

bool
robotis_interfaces__msg__MoveL__are_equal(const robotis_interfaces__msg__MoveL * lhs, const robotis_interfaces__msg__MoveL * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // pose
  if (!geometry_msgs__msg__PoseStamped__are_equal(
      &(lhs->pose), &(rhs->pose)))
  {
    return false;
  }
  // time_from_start
  if (!builtin_interfaces__msg__Duration__are_equal(
      &(lhs->time_from_start), &(rhs->time_from_start)))
  {
    return false;
  }
  return true;
}

bool
robotis_interfaces__msg__MoveL__copy(
  const robotis_interfaces__msg__MoveL * input,
  robotis_interfaces__msg__MoveL * output)
{
  if (!input || !output) {
    return false;
  }
  // pose
  if (!geometry_msgs__msg__PoseStamped__copy(
      &(input->pose), &(output->pose)))
  {
    return false;
  }
  // time_from_start
  if (!builtin_interfaces__msg__Duration__copy(
      &(input->time_from_start), &(output->time_from_start)))
  {
    return false;
  }
  return true;
}

robotis_interfaces__msg__MoveL *
robotis_interfaces__msg__MoveL__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  robotis_interfaces__msg__MoveL * msg = (robotis_interfaces__msg__MoveL *)allocator.allocate(sizeof(robotis_interfaces__msg__MoveL), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(robotis_interfaces__msg__MoveL));
  bool success = robotis_interfaces__msg__MoveL__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
robotis_interfaces__msg__MoveL__destroy(robotis_interfaces__msg__MoveL * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    robotis_interfaces__msg__MoveL__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
robotis_interfaces__msg__MoveL__Sequence__init(robotis_interfaces__msg__MoveL__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  robotis_interfaces__msg__MoveL * data = NULL;

  if (size) {
    if (size > SIZE_MAX / sizeof(robotis_interfaces__msg__MoveL)) {
      return false;
    }
    data = (robotis_interfaces__msg__MoveL *)allocator.zero_allocate(size, sizeof(robotis_interfaces__msg__MoveL), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = robotis_interfaces__msg__MoveL__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        robotis_interfaces__msg__MoveL__fini(&data[i - 1]);
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
robotis_interfaces__msg__MoveL__Sequence__fini(robotis_interfaces__msg__MoveL__Sequence * array)
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
      robotis_interfaces__msg__MoveL__fini(&array->data[i]);
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

robotis_interfaces__msg__MoveL__Sequence *
robotis_interfaces__msg__MoveL__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  robotis_interfaces__msg__MoveL__Sequence * array = (robotis_interfaces__msg__MoveL__Sequence *)allocator.allocate(sizeof(robotis_interfaces__msg__MoveL__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = robotis_interfaces__msg__MoveL__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
robotis_interfaces__msg__MoveL__Sequence__destroy(robotis_interfaces__msg__MoveL__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    robotis_interfaces__msg__MoveL__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
robotis_interfaces__msg__MoveL__Sequence__are_equal(const robotis_interfaces__msg__MoveL__Sequence * lhs, const robotis_interfaces__msg__MoveL__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!robotis_interfaces__msg__MoveL__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
robotis_interfaces__msg__MoveL__Sequence__copy(
  const robotis_interfaces__msg__MoveL__Sequence * input,
  robotis_interfaces__msg__MoveL__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    if (input->size > SIZE_MAX / sizeof(robotis_interfaces__msg__MoveL)) {
      return false;
    }
    const size_t allocation_size =
      input->size * sizeof(robotis_interfaces__msg__MoveL);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    robotis_interfaces__msg__MoveL * data =
      (robotis_interfaces__msg__MoveL *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!robotis_interfaces__msg__MoveL__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          robotis_interfaces__msg__MoveL__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!robotis_interfaces__msg__MoveL__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
