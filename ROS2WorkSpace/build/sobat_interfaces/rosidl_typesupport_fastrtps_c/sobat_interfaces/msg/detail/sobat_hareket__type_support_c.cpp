// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from sobat_interfaces:msg/SobatHareket.idl
// generated code does not contain a copyright notice
#include "sobat_interfaces/msg/detail/sobat_hareket__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "sobat_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "sobat_interfaces/msg/detail/sobat_hareket__struct.h"
#include "sobat_interfaces/msg/detail/sobat_hareket__functions.h"
#include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif


// forward declare type support functions


using _SobatHareket__ros_msg_type = sobat_interfaces__msg__SobatHareket;

static bool _SobatHareket__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _SobatHareket__ros_msg_type * ros_message = static_cast<const _SobatHareket__ros_msg_type *>(untyped_ros_message);
  // Field name: ileri
  {
    cdr << (ros_message->ileri ? true : false);
  }

  // Field name: geri
  {
    cdr << (ros_message->geri ? true : false);
  }

  // Field name: sag
  {
    cdr << (ros_message->sag ? true : false);
  }

  // Field name: sol
  {
    cdr << (ros_message->sol ? true : false);
  }

  // Field name: yukari
  {
    cdr << (ros_message->yukari ? true : false);
  }

  // Field name: asagi
  {
    cdr << (ros_message->asagi ? true : false);
  }

  return true;
}

static bool _SobatHareket__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _SobatHareket__ros_msg_type * ros_message = static_cast<_SobatHareket__ros_msg_type *>(untyped_ros_message);
  // Field name: ileri
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->ileri = tmp ? true : false;
  }

  // Field name: geri
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->geri = tmp ? true : false;
  }

  // Field name: sag
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->sag = tmp ? true : false;
  }

  // Field name: sol
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->sol = tmp ? true : false;
  }

  // Field name: yukari
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->yukari = tmp ? true : false;
  }

  // Field name: asagi
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->asagi = tmp ? true : false;
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_sobat_interfaces
size_t get_serialized_size_sobat_interfaces__msg__SobatHareket(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _SobatHareket__ros_msg_type * ros_message = static_cast<const _SobatHareket__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name ileri
  {
    size_t item_size = sizeof(ros_message->ileri);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name geri
  {
    size_t item_size = sizeof(ros_message->geri);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name sag
  {
    size_t item_size = sizeof(ros_message->sag);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name sol
  {
    size_t item_size = sizeof(ros_message->sol);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name yukari
  {
    size_t item_size = sizeof(ros_message->yukari);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name asagi
  {
    size_t item_size = sizeof(ros_message->asagi);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _SobatHareket__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_sobat_interfaces__msg__SobatHareket(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_sobat_interfaces
size_t max_serialized_size_sobat_interfaces__msg__SobatHareket(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;

  // member: ileri
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: geri
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: sag
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: sol
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: yukari
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: asagi
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  return current_alignment - initial_alignment;
}

static size_t _SobatHareket__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_sobat_interfaces__msg__SobatHareket(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_SobatHareket = {
  "sobat_interfaces::msg",
  "SobatHareket",
  _SobatHareket__cdr_serialize,
  _SobatHareket__cdr_deserialize,
  _SobatHareket__get_serialized_size,
  _SobatHareket__max_serialized_size
};

static rosidl_message_type_support_t _SobatHareket__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_SobatHareket,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, sobat_interfaces, msg, SobatHareket)() {
  return &_SobatHareket__type_support;
}

#if defined(__cplusplus)
}
#endif
