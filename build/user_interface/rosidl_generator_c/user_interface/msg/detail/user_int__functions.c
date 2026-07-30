// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from user_interface:msg/UserInt.idl
// generated code does not contain a copyright notice
#include "user_interface/msg/detail/user_int__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"

bool
user_interface__msg__UserInt__init(user_interface__msg__UserInt * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    user_interface__msg__UserInt__fini(msg);
    return false;
  }
  // user_int
  // user_int2
  // user_int3
  return true;
}

void
user_interface__msg__UserInt__fini(user_interface__msg__UserInt * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // user_int
  // user_int2
  // user_int3
}

bool
user_interface__msg__UserInt__are_equal(const user_interface__msg__UserInt * lhs, const user_interface__msg__UserInt * rhs)
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
  // user_int
  if (lhs->user_int != rhs->user_int) {
    return false;
  }
  // user_int2
  if (lhs->user_int2 != rhs->user_int2) {
    return false;
  }
  // user_int3
  if (lhs->user_int3 != rhs->user_int3) {
    return false;
  }
  return true;
}

bool
user_interface__msg__UserInt__copy(
  const user_interface__msg__UserInt * input,
  user_interface__msg__UserInt * output)
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
  // user_int
  output->user_int = input->user_int;
  // user_int2
  output->user_int2 = input->user_int2;
  // user_int3
  output->user_int3 = input->user_int3;
  return true;
}

user_interface__msg__UserInt *
user_interface__msg__UserInt__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  user_interface__msg__UserInt * msg = (user_interface__msg__UserInt *)allocator.allocate(sizeof(user_interface__msg__UserInt), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(user_interface__msg__UserInt));
  bool success = user_interface__msg__UserInt__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
user_interface__msg__UserInt__destroy(user_interface__msg__UserInt * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    user_interface__msg__UserInt__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
user_interface__msg__UserInt__Sequence__init(user_interface__msg__UserInt__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  user_interface__msg__UserInt * data = NULL;

  if (size) {
    if (size > SIZE_MAX / sizeof(user_interface__msg__UserInt)) {
      return false;
    }
    data = (user_interface__msg__UserInt *)allocator.zero_allocate(size, sizeof(user_interface__msg__UserInt), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = user_interface__msg__UserInt__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        user_interface__msg__UserInt__fini(&data[i - 1]);
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
user_interface__msg__UserInt__Sequence__fini(user_interface__msg__UserInt__Sequence * array)
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
      user_interface__msg__UserInt__fini(&array->data[i]);
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

user_interface__msg__UserInt__Sequence *
user_interface__msg__UserInt__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  user_interface__msg__UserInt__Sequence * array = (user_interface__msg__UserInt__Sequence *)allocator.allocate(sizeof(user_interface__msg__UserInt__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = user_interface__msg__UserInt__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
user_interface__msg__UserInt__Sequence__destroy(user_interface__msg__UserInt__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    user_interface__msg__UserInt__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
user_interface__msg__UserInt__Sequence__are_equal(const user_interface__msg__UserInt__Sequence * lhs, const user_interface__msg__UserInt__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!user_interface__msg__UserInt__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
user_interface__msg__UserInt__Sequence__copy(
  const user_interface__msg__UserInt__Sequence * input,
  user_interface__msg__UserInt__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    if (input->size > SIZE_MAX / sizeof(user_interface__msg__UserInt)) {
      return false;
    }
    const size_t allocation_size =
      input->size * sizeof(user_interface__msg__UserInt);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    user_interface__msg__UserInt * data =
      (user_interface__msg__UserInt *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!user_interface__msg__UserInt__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          user_interface__msg__UserInt__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!user_interface__msg__UserInt__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
