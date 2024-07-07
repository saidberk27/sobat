// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from sobat_interfaces:msg/SobatHareket.idl
// generated code does not contain a copyright notice
#include "sobat_interfaces/msg/detail/sobat_hareket__rosidl_typesupport_fastrtps_cpp.hpp"
#include "sobat_interfaces/msg/detail/sobat_hareket__struct.hpp"

#include <limits>
#include <stdexcept>
#include <string>
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_fastrtps_cpp/identifier.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_fastrtps_cpp/wstring_conversion.hpp"
#include "fastcdr/Cdr.h"


// forward declaration of message dependencies and their conversion functions

namespace sobat_interfaces
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_sobat_interfaces
cdr_serialize(
  const sobat_interfaces::msg::SobatHareket & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: ileri
  cdr << (ros_message.ileri ? true : false);
  // Member: geri
  cdr << (ros_message.geri ? true : false);
  // Member: sag
  cdr << (ros_message.sag ? true : false);
  // Member: sol
  cdr << (ros_message.sol ? true : false);
  // Member: yukari
  cdr << (ros_message.yukari ? true : false);
  // Member: asagi
  cdr << (ros_message.asagi ? true : false);
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_sobat_interfaces
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  sobat_interfaces::msg::SobatHareket & ros_message)
{
  // Member: ileri
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.ileri = tmp ? true : false;
  }

  // Member: geri
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.geri = tmp ? true : false;
  }

  // Member: sag
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.sag = tmp ? true : false;
  }

  // Member: sol
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.sol = tmp ? true : false;
  }

  // Member: yukari
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.yukari = tmp ? true : false;
  }

  // Member: asagi
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.asagi = tmp ? true : false;
  }

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_sobat_interfaces
get_serialized_size(
  const sobat_interfaces::msg::SobatHareket & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: ileri
  {
    size_t item_size = sizeof(ros_message.ileri);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: geri
  {
    size_t item_size = sizeof(ros_message.geri);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: sag
  {
    size_t item_size = sizeof(ros_message.sag);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: sol
  {
    size_t item_size = sizeof(ros_message.sol);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: yukari
  {
    size_t item_size = sizeof(ros_message.yukari);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: asagi
  {
    size_t item_size = sizeof(ros_message.asagi);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_sobat_interfaces
max_serialized_size_SobatHareket(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;


  // Member: ileri
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: geri
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: sag
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: sol
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: yukari
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: asagi
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  return current_alignment - initial_alignment;
}

static bool _SobatHareket__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const sobat_interfaces::msg::SobatHareket *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _SobatHareket__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<sobat_interfaces::msg::SobatHareket *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _SobatHareket__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const sobat_interfaces::msg::SobatHareket *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _SobatHareket__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_SobatHareket(full_bounded, 0);
}

static message_type_support_callbacks_t _SobatHareket__callbacks = {
  "sobat_interfaces::msg",
  "SobatHareket",
  _SobatHareket__cdr_serialize,
  _SobatHareket__cdr_deserialize,
  _SobatHareket__get_serialized_size,
  _SobatHareket__max_serialized_size
};

static rosidl_message_type_support_t _SobatHareket__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_SobatHareket__callbacks,
  get_message_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace sobat_interfaces

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_sobat_interfaces
const rosidl_message_type_support_t *
get_message_type_support_handle<sobat_interfaces::msg::SobatHareket>()
{
  return &sobat_interfaces::msg::typesupport_fastrtps_cpp::_SobatHareket__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, sobat_interfaces, msg, SobatHareket)() {
  return &sobat_interfaces::msg::typesupport_fastrtps_cpp::_SobatHareket__handle;
}

#ifdef __cplusplus
}
#endif
