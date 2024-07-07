// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from sobat_interfaces:msg/SobatHareket.idl
// generated code does not contain a copyright notice

#ifndef SOBAT_INTERFACES__MSG__DETAIL__SOBAT_HAREKET__STRUCT_H_
#define SOBAT_INTERFACES__MSG__DETAIL__SOBAT_HAREKET__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in msg/SobatHareket in the package sobat_interfaces.
typedef struct sobat_interfaces__msg__SobatHareket
{
  bool ileri;
  bool geri;
  bool sag;
  bool sol;
  bool yukari;
  bool asagi;
} sobat_interfaces__msg__SobatHareket;

// Struct for a sequence of sobat_interfaces__msg__SobatHareket.
typedef struct sobat_interfaces__msg__SobatHareket__Sequence
{
  sobat_interfaces__msg__SobatHareket * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} sobat_interfaces__msg__SobatHareket__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // SOBAT_INTERFACES__MSG__DETAIL__SOBAT_HAREKET__STRUCT_H_
