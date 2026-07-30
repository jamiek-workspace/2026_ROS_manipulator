// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from user_interface:srv/AddAndOdd.idl
// generated code does not contain a copyright notice
#include "user_interface/srv/detail/add_and_odd__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

bool
user_interface__srv__AddAndOdd_Request__init(user_interface__srv__AddAndOdd_Request * msg)
{
  if (!msg) {
    return false;
  }
  // inta
  // intb
  return true;
}

void
user_interface__srv__AddAndOdd_Request__fini(user_interface__srv__AddAndOdd_Request * msg)
{
  if (!msg) {
    return;
  }
  // inta
  // intb
}

bool
user_interface__srv__AddAndOdd_Request__are_equal(const user_interface__srv__AddAndOdd_Request * lhs, const user_interface__srv__AddAndOdd_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // inta
  if (lhs->inta != rhs->inta) {
    return false;
  }
  // intb
  if (lhs->intb != rhs->intb) {
    return false;
  }
  return true;
}

bool
user_interface__srv__AddAndOdd_Request__copy(
  const user_interface__srv__AddAndOdd_Request * input,
  user_interface__srv__AddAndOdd_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // inta
  output->inta = input->inta;
  // intb
  output->intb = input->intb;
  return true;
}

user_interface__srv__AddAndOdd_Request *
user_interface__srv__AddAndOdd_Request__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  user_interface__srv__AddAndOdd_Request * msg = (user_interface__srv__AddAndOdd_Request *)allocator.allocate(sizeof(user_interface__srv__AddAndOdd_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(user_interface__srv__AddAndOdd_Request));
  bool success = user_interface__srv__AddAndOdd_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
user_interface__srv__AddAndOdd_Request__destroy(user_interface__srv__AddAndOdd_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    user_interface__srv__AddAndOdd_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
user_interface__srv__AddAndOdd_Request__Sequence__init(user_interface__srv__AddAndOdd_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  user_interface__srv__AddAndOdd_Request * data = NULL;

  if (size) {
    if (size > SIZE_MAX / sizeof(user_interface__srv__AddAndOdd_Request)) {
      return false;
    }
    data = (user_interface__srv__AddAndOdd_Request *)allocator.zero_allocate(size, sizeof(user_interface__srv__AddAndOdd_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = user_interface__srv__AddAndOdd_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        user_interface__srv__AddAndOdd_Request__fini(&data[i - 1]);
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
user_interface__srv__AddAndOdd_Request__Sequence__fini(user_interface__srv__AddAndOdd_Request__Sequence * array)
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
      user_interface__srv__AddAndOdd_Request__fini(&array->data[i]);
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

user_interface__srv__AddAndOdd_Request__Sequence *
user_interface__srv__AddAndOdd_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  user_interface__srv__AddAndOdd_Request__Sequence * array = (user_interface__srv__AddAndOdd_Request__Sequence *)allocator.allocate(sizeof(user_interface__srv__AddAndOdd_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = user_interface__srv__AddAndOdd_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
user_interface__srv__AddAndOdd_Request__Sequence__destroy(user_interface__srv__AddAndOdd_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    user_interface__srv__AddAndOdd_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
user_interface__srv__AddAndOdd_Request__Sequence__are_equal(const user_interface__srv__AddAndOdd_Request__Sequence * lhs, const user_interface__srv__AddAndOdd_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!user_interface__srv__AddAndOdd_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
user_interface__srv__AddAndOdd_Request__Sequence__copy(
  const user_interface__srv__AddAndOdd_Request__Sequence * input,
  user_interface__srv__AddAndOdd_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    if (input->size > SIZE_MAX / sizeof(user_interface__srv__AddAndOdd_Request)) {
      return false;
    }
    const size_t allocation_size =
      input->size * sizeof(user_interface__srv__AddAndOdd_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    user_interface__srv__AddAndOdd_Request * data =
      (user_interface__srv__AddAndOdd_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!user_interface__srv__AddAndOdd_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          user_interface__srv__AddAndOdd_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!user_interface__srv__AddAndOdd_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `odd`
#include "rosidl_runtime_c/string_functions.h"

bool
user_interface__srv__AddAndOdd_Response__init(user_interface__srv__AddAndOdd_Response * msg)
{
  if (!msg) {
    return false;
  }
  // sum
  // odd
  if (!rosidl_runtime_c__String__init(&msg->odd)) {
    user_interface__srv__AddAndOdd_Response__fini(msg);
    return false;
  }
  return true;
}

void
user_interface__srv__AddAndOdd_Response__fini(user_interface__srv__AddAndOdd_Response * msg)
{
  if (!msg) {
    return;
  }
  // sum
  // odd
  rosidl_runtime_c__String__fini(&msg->odd);
}

bool
user_interface__srv__AddAndOdd_Response__are_equal(const user_interface__srv__AddAndOdd_Response * lhs, const user_interface__srv__AddAndOdd_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // sum
  if (lhs->sum != rhs->sum) {
    return false;
  }
  // odd
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->odd), &(rhs->odd)))
  {
    return false;
  }
  return true;
}

bool
user_interface__srv__AddAndOdd_Response__copy(
  const user_interface__srv__AddAndOdd_Response * input,
  user_interface__srv__AddAndOdd_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // sum
  output->sum = input->sum;
  // odd
  if (!rosidl_runtime_c__String__copy(
      &(input->odd), &(output->odd)))
  {
    return false;
  }
  return true;
}

user_interface__srv__AddAndOdd_Response *
user_interface__srv__AddAndOdd_Response__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  user_interface__srv__AddAndOdd_Response * msg = (user_interface__srv__AddAndOdd_Response *)allocator.allocate(sizeof(user_interface__srv__AddAndOdd_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(user_interface__srv__AddAndOdd_Response));
  bool success = user_interface__srv__AddAndOdd_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
user_interface__srv__AddAndOdd_Response__destroy(user_interface__srv__AddAndOdd_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    user_interface__srv__AddAndOdd_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
user_interface__srv__AddAndOdd_Response__Sequence__init(user_interface__srv__AddAndOdd_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  user_interface__srv__AddAndOdd_Response * data = NULL;

  if (size) {
    if (size > SIZE_MAX / sizeof(user_interface__srv__AddAndOdd_Response)) {
      return false;
    }
    data = (user_interface__srv__AddAndOdd_Response *)allocator.zero_allocate(size, sizeof(user_interface__srv__AddAndOdd_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = user_interface__srv__AddAndOdd_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        user_interface__srv__AddAndOdd_Response__fini(&data[i - 1]);
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
user_interface__srv__AddAndOdd_Response__Sequence__fini(user_interface__srv__AddAndOdd_Response__Sequence * array)
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
      user_interface__srv__AddAndOdd_Response__fini(&array->data[i]);
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

user_interface__srv__AddAndOdd_Response__Sequence *
user_interface__srv__AddAndOdd_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  user_interface__srv__AddAndOdd_Response__Sequence * array = (user_interface__srv__AddAndOdd_Response__Sequence *)allocator.allocate(sizeof(user_interface__srv__AddAndOdd_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = user_interface__srv__AddAndOdd_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
user_interface__srv__AddAndOdd_Response__Sequence__destroy(user_interface__srv__AddAndOdd_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    user_interface__srv__AddAndOdd_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
user_interface__srv__AddAndOdd_Response__Sequence__are_equal(const user_interface__srv__AddAndOdd_Response__Sequence * lhs, const user_interface__srv__AddAndOdd_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!user_interface__srv__AddAndOdd_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
user_interface__srv__AddAndOdd_Response__Sequence__copy(
  const user_interface__srv__AddAndOdd_Response__Sequence * input,
  user_interface__srv__AddAndOdd_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    if (input->size > SIZE_MAX / sizeof(user_interface__srv__AddAndOdd_Response)) {
      return false;
    }
    const size_t allocation_size =
      input->size * sizeof(user_interface__srv__AddAndOdd_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    user_interface__srv__AddAndOdd_Response * data =
      (user_interface__srv__AddAndOdd_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!user_interface__srv__AddAndOdd_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          user_interface__srv__AddAndOdd_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!user_interface__srv__AddAndOdd_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `info`
#include "service_msgs/msg/detail/service_event_info__functions.h"
// Member `request`
// Member `response`
// already included above
// #include "user_interface/srv/detail/add_and_odd__functions.h"

bool
user_interface__srv__AddAndOdd_Event__init(user_interface__srv__AddAndOdd_Event * msg)
{
  if (!msg) {
    return false;
  }
  // info
  if (!service_msgs__msg__ServiceEventInfo__init(&msg->info)) {
    user_interface__srv__AddAndOdd_Event__fini(msg);
    return false;
  }
  // request
  if (!user_interface__srv__AddAndOdd_Request__Sequence__init(&msg->request, 0)) {
    user_interface__srv__AddAndOdd_Event__fini(msg);
    return false;
  }
  // response
  if (!user_interface__srv__AddAndOdd_Response__Sequence__init(&msg->response, 0)) {
    user_interface__srv__AddAndOdd_Event__fini(msg);
    return false;
  }
  return true;
}

void
user_interface__srv__AddAndOdd_Event__fini(user_interface__srv__AddAndOdd_Event * msg)
{
  if (!msg) {
    return;
  }
  // info
  service_msgs__msg__ServiceEventInfo__fini(&msg->info);
  // request
  user_interface__srv__AddAndOdd_Request__Sequence__fini(&msg->request);
  // response
  user_interface__srv__AddAndOdd_Response__Sequence__fini(&msg->response);
}

bool
user_interface__srv__AddAndOdd_Event__are_equal(const user_interface__srv__AddAndOdd_Event * lhs, const user_interface__srv__AddAndOdd_Event * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // info
  if (!service_msgs__msg__ServiceEventInfo__are_equal(
      &(lhs->info), &(rhs->info)))
  {
    return false;
  }
  // request
  if (!user_interface__srv__AddAndOdd_Request__Sequence__are_equal(
      &(lhs->request), &(rhs->request)))
  {
    return false;
  }
  // response
  if (!user_interface__srv__AddAndOdd_Response__Sequence__are_equal(
      &(lhs->response), &(rhs->response)))
  {
    return false;
  }
  return true;
}

bool
user_interface__srv__AddAndOdd_Event__copy(
  const user_interface__srv__AddAndOdd_Event * input,
  user_interface__srv__AddAndOdd_Event * output)
{
  if (!input || !output) {
    return false;
  }
  // info
  if (!service_msgs__msg__ServiceEventInfo__copy(
      &(input->info), &(output->info)))
  {
    return false;
  }
  // request
  if (!user_interface__srv__AddAndOdd_Request__Sequence__copy(
      &(input->request), &(output->request)))
  {
    return false;
  }
  // response
  if (!user_interface__srv__AddAndOdd_Response__Sequence__copy(
      &(input->response), &(output->response)))
  {
    return false;
  }
  return true;
}

user_interface__srv__AddAndOdd_Event *
user_interface__srv__AddAndOdd_Event__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  user_interface__srv__AddAndOdd_Event * msg = (user_interface__srv__AddAndOdd_Event *)allocator.allocate(sizeof(user_interface__srv__AddAndOdd_Event), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(user_interface__srv__AddAndOdd_Event));
  bool success = user_interface__srv__AddAndOdd_Event__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
user_interface__srv__AddAndOdd_Event__destroy(user_interface__srv__AddAndOdd_Event * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    user_interface__srv__AddAndOdd_Event__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
user_interface__srv__AddAndOdd_Event__Sequence__init(user_interface__srv__AddAndOdd_Event__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  user_interface__srv__AddAndOdd_Event * data = NULL;

  if (size) {
    if (size > SIZE_MAX / sizeof(user_interface__srv__AddAndOdd_Event)) {
      return false;
    }
    data = (user_interface__srv__AddAndOdd_Event *)allocator.zero_allocate(size, sizeof(user_interface__srv__AddAndOdd_Event), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = user_interface__srv__AddAndOdd_Event__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        user_interface__srv__AddAndOdd_Event__fini(&data[i - 1]);
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
user_interface__srv__AddAndOdd_Event__Sequence__fini(user_interface__srv__AddAndOdd_Event__Sequence * array)
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
      user_interface__srv__AddAndOdd_Event__fini(&array->data[i]);
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

user_interface__srv__AddAndOdd_Event__Sequence *
user_interface__srv__AddAndOdd_Event__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  user_interface__srv__AddAndOdd_Event__Sequence * array = (user_interface__srv__AddAndOdd_Event__Sequence *)allocator.allocate(sizeof(user_interface__srv__AddAndOdd_Event__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = user_interface__srv__AddAndOdd_Event__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
user_interface__srv__AddAndOdd_Event__Sequence__destroy(user_interface__srv__AddAndOdd_Event__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    user_interface__srv__AddAndOdd_Event__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
user_interface__srv__AddAndOdd_Event__Sequence__are_equal(const user_interface__srv__AddAndOdd_Event__Sequence * lhs, const user_interface__srv__AddAndOdd_Event__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!user_interface__srv__AddAndOdd_Event__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
user_interface__srv__AddAndOdd_Event__Sequence__copy(
  const user_interface__srv__AddAndOdd_Event__Sequence * input,
  user_interface__srv__AddAndOdd_Event__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    if (input->size > SIZE_MAX / sizeof(user_interface__srv__AddAndOdd_Event)) {
      return false;
    }
    const size_t allocation_size =
      input->size * sizeof(user_interface__srv__AddAndOdd_Event);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    user_interface__srv__AddAndOdd_Event * data =
      (user_interface__srv__AddAndOdd_Event *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!user_interface__srv__AddAndOdd_Event__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          user_interface__srv__AddAndOdd_Event__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!user_interface__srv__AddAndOdd_Event__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
