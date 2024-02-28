// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from sobat_interfaces:msg/MesafeSensor.idl
// generated code does not contain a copyright notice
#include "sobat_interfaces/msg/detail/mesafe_sensor__rosidl_typesupport_fastrtps_cpp.hpp"
#include "sobat_interfaces/msg/detail/mesafe_sensor__struct.hpp"

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
  const sobat_interfaces::msg::MesafeSensor & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: mesafe_sensor1
  cdr << ros_message.mesafe_sensor1;
  // Member: mesafe_sensor2
  cdr << ros_message.mesafe_sensor2;
  // Member: mesafe_sensor3
  cdr << ros_message.mesafe_sensor3;
  // Member: mesafe_sensor4
  cdr << ros_message.mesafe_sensor4;
  // Member: mesafe_sensor5
  cdr << ros_message.mesafe_sensor5;
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_sobat_interfaces
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  sobat_interfaces::msg::MesafeSensor & ros_message)
{
  // Member: mesafe_sensor1
  cdr >> ros_message.mesafe_sensor1;

  // Member: mesafe_sensor2
  cdr >> ros_message.mesafe_sensor2;

  // Member: mesafe_sensor3
  cdr >> ros_message.mesafe_sensor3;

  // Member: mesafe_sensor4
  cdr >> ros_message.mesafe_sensor4;

  // Member: mesafe_sensor5
  cdr >> ros_message.mesafe_sensor5;

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_sobat_interfaces
get_serialized_size(
  const sobat_interfaces::msg::MesafeSensor & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: mesafe_sensor1
  {
    size_t item_size = sizeof(ros_message.mesafe_sensor1);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: mesafe_sensor2
  {
    size_t item_size = sizeof(ros_message.mesafe_sensor2);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: mesafe_sensor3
  {
    size_t item_size = sizeof(ros_message.mesafe_sensor3);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: mesafe_sensor4
  {
    size_t item_size = sizeof(ros_message.mesafe_sensor4);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: mesafe_sensor5
  {
    size_t item_size = sizeof(ros_message.mesafe_sensor5);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_sobat_interfaces
max_serialized_size_MesafeSensor(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;


  // Member: mesafe_sensor1
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: mesafe_sensor2
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: mesafe_sensor3
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: mesafe_sensor4
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: mesafe_sensor5
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  return current_alignment - initial_alignment;
}

static bool _MesafeSensor__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const sobat_interfaces::msg::MesafeSensor *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _MesafeSensor__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<sobat_interfaces::msg::MesafeSensor *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _MesafeSensor__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const sobat_interfaces::msg::MesafeSensor *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _MesafeSensor__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_MesafeSensor(full_bounded, 0);
}

static message_type_support_callbacks_t _MesafeSensor__callbacks = {
  "sobat_interfaces::msg",
  "MesafeSensor",
  _MesafeSensor__cdr_serialize,
  _MesafeSensor__cdr_deserialize,
  _MesafeSensor__get_serialized_size,
  _MesafeSensor__max_serialized_size
};

static rosidl_message_type_support_t _MesafeSensor__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_MesafeSensor__callbacks,
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
get_message_type_support_handle<sobat_interfaces::msg::MesafeSensor>()
{
  return &sobat_interfaces::msg::typesupport_fastrtps_cpp::_MesafeSensor__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, sobat_interfaces, msg, MesafeSensor)() {
  return &sobat_interfaces::msg::typesupport_fastrtps_cpp::_MesafeSensor__handle;
}

#ifdef __cplusplus
}
#endif
