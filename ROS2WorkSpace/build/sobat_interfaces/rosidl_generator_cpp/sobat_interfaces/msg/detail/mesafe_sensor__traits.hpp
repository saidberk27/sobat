// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from sobat_interfaces:msg/MesafeSensor.idl
// generated code does not contain a copyright notice

#ifndef SOBAT_INTERFACES__MSG__DETAIL__MESAFE_SENSOR__TRAITS_HPP_
#define SOBAT_INTERFACES__MSG__DETAIL__MESAFE_SENSOR__TRAITS_HPP_

#include "sobat_interfaces/msg/detail/mesafe_sensor__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<sobat_interfaces::msg::MesafeSensor>()
{
  return "sobat_interfaces::msg::MesafeSensor";
}

template<>
inline const char * name<sobat_interfaces::msg::MesafeSensor>()
{
  return "sobat_interfaces/msg/MesafeSensor";
}

template<>
struct has_fixed_size<sobat_interfaces::msg::MesafeSensor>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<sobat_interfaces::msg::MesafeSensor>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<sobat_interfaces::msg::MesafeSensor>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // SOBAT_INTERFACES__MSG__DETAIL__MESAFE_SENSOR__TRAITS_HPP_
