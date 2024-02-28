// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from sobat_interfaces:msg/MesafeSensor.idl
// generated code does not contain a copyright notice

#ifndef SOBAT_INTERFACES__MSG__DETAIL__MESAFE_SENSOR__BUILDER_HPP_
#define SOBAT_INTERFACES__MSG__DETAIL__MESAFE_SENSOR__BUILDER_HPP_

#include "sobat_interfaces/msg/detail/mesafe_sensor__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace sobat_interfaces
{

namespace msg
{

namespace builder
{

class Init_MesafeSensor_mesafe_sensor5
{
public:
  explicit Init_MesafeSensor_mesafe_sensor5(::sobat_interfaces::msg::MesafeSensor & msg)
  : msg_(msg)
  {}
  ::sobat_interfaces::msg::MesafeSensor mesafe_sensor5(::sobat_interfaces::msg::MesafeSensor::_mesafe_sensor5_type arg)
  {
    msg_.mesafe_sensor5 = std::move(arg);
    return std::move(msg_);
  }

private:
  ::sobat_interfaces::msg::MesafeSensor msg_;
};

class Init_MesafeSensor_mesafe_sensor4
{
public:
  explicit Init_MesafeSensor_mesafe_sensor4(::sobat_interfaces::msg::MesafeSensor & msg)
  : msg_(msg)
  {}
  Init_MesafeSensor_mesafe_sensor5 mesafe_sensor4(::sobat_interfaces::msg::MesafeSensor::_mesafe_sensor4_type arg)
  {
    msg_.mesafe_sensor4 = std::move(arg);
    return Init_MesafeSensor_mesafe_sensor5(msg_);
  }

private:
  ::sobat_interfaces::msg::MesafeSensor msg_;
};

class Init_MesafeSensor_mesafe_sensor3
{
public:
  explicit Init_MesafeSensor_mesafe_sensor3(::sobat_interfaces::msg::MesafeSensor & msg)
  : msg_(msg)
  {}
  Init_MesafeSensor_mesafe_sensor4 mesafe_sensor3(::sobat_interfaces::msg::MesafeSensor::_mesafe_sensor3_type arg)
  {
    msg_.mesafe_sensor3 = std::move(arg);
    return Init_MesafeSensor_mesafe_sensor4(msg_);
  }

private:
  ::sobat_interfaces::msg::MesafeSensor msg_;
};

class Init_MesafeSensor_mesafe_sensor2
{
public:
  explicit Init_MesafeSensor_mesafe_sensor2(::sobat_interfaces::msg::MesafeSensor & msg)
  : msg_(msg)
  {}
  Init_MesafeSensor_mesafe_sensor3 mesafe_sensor2(::sobat_interfaces::msg::MesafeSensor::_mesafe_sensor2_type arg)
  {
    msg_.mesafe_sensor2 = std::move(arg);
    return Init_MesafeSensor_mesafe_sensor3(msg_);
  }

private:
  ::sobat_interfaces::msg::MesafeSensor msg_;
};

class Init_MesafeSensor_mesafe_sensor1
{
public:
  Init_MesafeSensor_mesafe_sensor1()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_MesafeSensor_mesafe_sensor2 mesafe_sensor1(::sobat_interfaces::msg::MesafeSensor::_mesafe_sensor1_type arg)
  {
    msg_.mesafe_sensor1 = std::move(arg);
    return Init_MesafeSensor_mesafe_sensor2(msg_);
  }

private:
  ::sobat_interfaces::msg::MesafeSensor msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::sobat_interfaces::msg::MesafeSensor>()
{
  return sobat_interfaces::msg::builder::Init_MesafeSensor_mesafe_sensor1();
}

}  // namespace sobat_interfaces

#endif  // SOBAT_INTERFACES__MSG__DETAIL__MESAFE_SENSOR__BUILDER_HPP_
