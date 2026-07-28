// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from robotis_interfaces:msg/HandPressures.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "robotis_interfaces/msg/hand_pressures.h"


#ifndef ROBOTIS_INTERFACES__MSG__DETAIL__HAND_PRESSURES__FUNCTIONS_H_
#define ROBOTIS_INTERFACES__MSG__DETAIL__HAND_PRESSURES__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/action_type_support_struct.h"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_runtime_c/service_type_support_struct.h"
#include "rosidl_runtime_c/type_description/type_description__struct.h"
#include "rosidl_runtime_c/type_description/type_source__struct.h"
#include "rosidl_runtime_c/type_hash.h"
#include "rosidl_runtime_c/visibility_control.h"
#include "robotis_interfaces/msg/rosidl_generator_c__visibility_control.h"

#include "robotis_interfaces/msg/detail/hand_pressures__struct.h"

/// Initialize msg/HandPressures message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * robotis_interfaces__msg__HandPressures
 * )) before or use
 * robotis_interfaces__msg__HandPressures__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_robotis_interfaces
bool
robotis_interfaces__msg__HandPressures__init(robotis_interfaces__msg__HandPressures * msg);

/// Finalize msg/HandPressures message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_robotis_interfaces
void
robotis_interfaces__msg__HandPressures__fini(robotis_interfaces__msg__HandPressures * msg);

/// Create msg/HandPressures message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * robotis_interfaces__msg__HandPressures__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_robotis_interfaces
robotis_interfaces__msg__HandPressures *
robotis_interfaces__msg__HandPressures__create(void);

/// Destroy msg/HandPressures message.
/**
 * It calls
 * robotis_interfaces__msg__HandPressures__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_robotis_interfaces
void
robotis_interfaces__msg__HandPressures__destroy(robotis_interfaces__msg__HandPressures * msg);

/// Check for msg/HandPressures message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_robotis_interfaces
bool
robotis_interfaces__msg__HandPressures__are_equal(const robotis_interfaces__msg__HandPressures * lhs, const robotis_interfaces__msg__HandPressures * rhs);

/// Copy a msg/HandPressures message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_robotis_interfaces
bool
robotis_interfaces__msg__HandPressures__copy(
  const robotis_interfaces__msg__HandPressures * input,
  robotis_interfaces__msg__HandPressures * output);

/// Retrieve pointer to the hash of the description of this type.
ROSIDL_GENERATOR_C_PUBLIC_robotis_interfaces
const rosidl_type_hash_t *
robotis_interfaces__msg__HandPressures__get_type_hash(
  const rosidl_message_type_support_t * type_support);

/// Retrieve pointer to the description of this type.
ROSIDL_GENERATOR_C_PUBLIC_robotis_interfaces
const rosidl_runtime_c__type_description__TypeDescription *
robotis_interfaces__msg__HandPressures__get_type_description(
  const rosidl_message_type_support_t * type_support);

/// Retrieve pointer to the single raw source text that defined this type.
ROSIDL_GENERATOR_C_PUBLIC_robotis_interfaces
const rosidl_runtime_c__type_description__TypeSource *
robotis_interfaces__msg__HandPressures__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support);

/// Retrieve pointer to the recursive raw sources that defined the description of this type.
ROSIDL_GENERATOR_C_PUBLIC_robotis_interfaces
const rosidl_runtime_c__type_description__TypeSource__Sequence *
robotis_interfaces__msg__HandPressures__get_type_description_sources(
  const rosidl_message_type_support_t * type_support);

/// Initialize array of msg/HandPressures messages.
/**
 * It allocates the memory for the number of elements and calls
 * robotis_interfaces__msg__HandPressures__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_robotis_interfaces
bool
robotis_interfaces__msg__HandPressures__Sequence__init(robotis_interfaces__msg__HandPressures__Sequence * array, size_t size);

/// Finalize array of msg/HandPressures messages.
/**
 * It calls
 * robotis_interfaces__msg__HandPressures__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_robotis_interfaces
void
robotis_interfaces__msg__HandPressures__Sequence__fini(robotis_interfaces__msg__HandPressures__Sequence * array);

/// Create array of msg/HandPressures messages.
/**
 * It allocates the memory for the array and calls
 * robotis_interfaces__msg__HandPressures__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_robotis_interfaces
robotis_interfaces__msg__HandPressures__Sequence *
robotis_interfaces__msg__HandPressures__Sequence__create(size_t size);

/// Destroy array of msg/HandPressures messages.
/**
 * It calls
 * robotis_interfaces__msg__HandPressures__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_robotis_interfaces
void
robotis_interfaces__msg__HandPressures__Sequence__destroy(robotis_interfaces__msg__HandPressures__Sequence * array);

/// Check for msg/HandPressures message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_robotis_interfaces
bool
robotis_interfaces__msg__HandPressures__Sequence__are_equal(const robotis_interfaces__msg__HandPressures__Sequence * lhs, const robotis_interfaces__msg__HandPressures__Sequence * rhs);

/// Copy an array of msg/HandPressures messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_robotis_interfaces
bool
robotis_interfaces__msg__HandPressures__Sequence__copy(
  const robotis_interfaces__msg__HandPressures__Sequence * input,
  robotis_interfaces__msg__HandPressures__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // ROBOTIS_INTERFACES__MSG__DETAIL__HAND_PRESSURES__FUNCTIONS_H_
