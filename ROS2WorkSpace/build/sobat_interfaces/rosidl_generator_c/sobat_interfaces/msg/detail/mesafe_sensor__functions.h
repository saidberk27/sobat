// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from sobat_interfaces:msg/MesafeSensor.idl
// generated code does not contain a copyright notice

#ifndef SOBAT_INTERFACES__MSG__DETAIL__MESAFE_SENSOR__FUNCTIONS_H_
#define SOBAT_INTERFACES__MSG__DETAIL__MESAFE_SENSOR__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "sobat_interfaces/msg/rosidl_generator_c__visibility_control.h"

#include "sobat_interfaces/msg/detail/mesafe_sensor__struct.h"

/// Initialize msg/MesafeSensor message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * sobat_interfaces__msg__MesafeSensor
 * )) before or use
 * sobat_interfaces__msg__MesafeSensor__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_sobat_interfaces
bool
sobat_interfaces__msg__MesafeSensor__init(sobat_interfaces__msg__MesafeSensor * msg);

/// Finalize msg/MesafeSensor message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_sobat_interfaces
void
sobat_interfaces__msg__MesafeSensor__fini(sobat_interfaces__msg__MesafeSensor * msg);

/// Create msg/MesafeSensor message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * sobat_interfaces__msg__MesafeSensor__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_sobat_interfaces
sobat_interfaces__msg__MesafeSensor *
sobat_interfaces__msg__MesafeSensor__create();

/// Destroy msg/MesafeSensor message.
/**
 * It calls
 * sobat_interfaces__msg__MesafeSensor__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_sobat_interfaces
void
sobat_interfaces__msg__MesafeSensor__destroy(sobat_interfaces__msg__MesafeSensor * msg);

/// Check for msg/MesafeSensor message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_sobat_interfaces
bool
sobat_interfaces__msg__MesafeSensor__are_equal(const sobat_interfaces__msg__MesafeSensor * lhs, const sobat_interfaces__msg__MesafeSensor * rhs);

/// Copy a msg/MesafeSensor message.
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
ROSIDL_GENERATOR_C_PUBLIC_sobat_interfaces
bool
sobat_interfaces__msg__MesafeSensor__copy(
  const sobat_interfaces__msg__MesafeSensor * input,
  sobat_interfaces__msg__MesafeSensor * output);

/// Initialize array of msg/MesafeSensor messages.
/**
 * It allocates the memory for the number of elements and calls
 * sobat_interfaces__msg__MesafeSensor__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_sobat_interfaces
bool
sobat_interfaces__msg__MesafeSensor__Sequence__init(sobat_interfaces__msg__MesafeSensor__Sequence * array, size_t size);

/// Finalize array of msg/MesafeSensor messages.
/**
 * It calls
 * sobat_interfaces__msg__MesafeSensor__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_sobat_interfaces
void
sobat_interfaces__msg__MesafeSensor__Sequence__fini(sobat_interfaces__msg__MesafeSensor__Sequence * array);

/// Create array of msg/MesafeSensor messages.
/**
 * It allocates the memory for the array and calls
 * sobat_interfaces__msg__MesafeSensor__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_sobat_interfaces
sobat_interfaces__msg__MesafeSensor__Sequence *
sobat_interfaces__msg__MesafeSensor__Sequence__create(size_t size);

/// Destroy array of msg/MesafeSensor messages.
/**
 * It calls
 * sobat_interfaces__msg__MesafeSensor__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_sobat_interfaces
void
sobat_interfaces__msg__MesafeSensor__Sequence__destroy(sobat_interfaces__msg__MesafeSensor__Sequence * array);

/// Check for msg/MesafeSensor message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_sobat_interfaces
bool
sobat_interfaces__msg__MesafeSensor__Sequence__are_equal(const sobat_interfaces__msg__MesafeSensor__Sequence * lhs, const sobat_interfaces__msg__MesafeSensor__Sequence * rhs);

/// Copy an array of msg/MesafeSensor messages.
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
ROSIDL_GENERATOR_C_PUBLIC_sobat_interfaces
bool
sobat_interfaces__msg__MesafeSensor__Sequence__copy(
  const sobat_interfaces__msg__MesafeSensor__Sequence * input,
  sobat_interfaces__msg__MesafeSensor__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // SOBAT_INTERFACES__MSG__DETAIL__MESAFE_SENSOR__FUNCTIONS_H_
