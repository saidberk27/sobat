// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__rosidl_typesupport_fastrtps_cpp.hpp.em
// with input from sobat_interfaces:msg/MesafeSensor.idl
// generated code does not contain a copyright notice

#ifndef SOBAT_INTERFACES__MSG__DETAIL__MESAFE_SENSOR__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
#define SOBAT_INTERFACES__MSG__DETAIL__MESAFE_SENSOR__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_

#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "sobat_interfaces/msg/rosidl_typesupport_fastrtps_cpp__visibility_control.h"
#include "sobat_interfaces/msg/detail/mesafe_sensor__struct.hpp"

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

#include "fastcdr/Cdr.h"

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
  eprosima::fastcdr::Cdr & cdr);

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_sobat_interfaces
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  sobat_interfaces::msg::MesafeSensor & ros_message);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_sobat_interfaces
get_serialized_size(
  const sobat_interfaces::msg::MesafeSensor & ros_message,
  size_t current_alignment);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_sobat_interfaces
max_serialized_size_MesafeSensor(
  bool & full_bounded,
  size_t current_alignment);

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace sobat_interfaces

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_sobat_interfaces
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, sobat_interfaces, msg, MesafeSensor)();

#ifdef __cplusplus
}
#endif

#endif  // SOBAT_INTERFACES__MSG__DETAIL__MESAFE_SENSOR__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
