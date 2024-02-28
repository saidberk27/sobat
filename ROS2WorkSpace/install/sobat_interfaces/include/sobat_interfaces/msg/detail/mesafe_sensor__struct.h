// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from sobat_interfaces:msg/MesafeSensor.idl
// generated code does not contain a copyright notice

#ifndef SOBAT_INTERFACES__MSG__DETAIL__MESAFE_SENSOR__STRUCT_H_
#define SOBAT_INTERFACES__MSG__DETAIL__MESAFE_SENSOR__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in msg/MesafeSensor in the package sobat_interfaces.
typedef struct sobat_interfaces__msg__MesafeSensor
{
  float mesafe_sensor1;
  float mesafe_sensor2;
  float mesafe_sensor3;
  float mesafe_sensor4;
  float mesafe_sensor5;
} sobat_interfaces__msg__MesafeSensor;

// Struct for a sequence of sobat_interfaces__msg__MesafeSensor.
typedef struct sobat_interfaces__msg__MesafeSensor__Sequence
{
  sobat_interfaces__msg__MesafeSensor * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} sobat_interfaces__msg__MesafeSensor__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // SOBAT_INTERFACES__MSG__DETAIL__MESAFE_SENSOR__STRUCT_H_
