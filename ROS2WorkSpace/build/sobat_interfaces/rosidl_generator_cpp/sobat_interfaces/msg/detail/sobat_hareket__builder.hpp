// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from sobat_interfaces:msg/SobatHareket.idl
// generated code does not contain a copyright notice

#ifndef SOBAT_INTERFACES__MSG__DETAIL__SOBAT_HAREKET__BUILDER_HPP_
#define SOBAT_INTERFACES__MSG__DETAIL__SOBAT_HAREKET__BUILDER_HPP_

#include "sobat_interfaces/msg/detail/sobat_hareket__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace sobat_interfaces
{

namespace msg
{

namespace builder
{

class Init_SobatHareket_asagi
{
public:
  explicit Init_SobatHareket_asagi(::sobat_interfaces::msg::SobatHareket & msg)
  : msg_(msg)
  {}
  ::sobat_interfaces::msg::SobatHareket asagi(::sobat_interfaces::msg::SobatHareket::_asagi_type arg)
  {
    msg_.asagi = std::move(arg);
    return std::move(msg_);
  }

private:
  ::sobat_interfaces::msg::SobatHareket msg_;
};

class Init_SobatHareket_yukari
{
public:
  explicit Init_SobatHareket_yukari(::sobat_interfaces::msg::SobatHareket & msg)
  : msg_(msg)
  {}
  Init_SobatHareket_asagi yukari(::sobat_interfaces::msg::SobatHareket::_yukari_type arg)
  {
    msg_.yukari = std::move(arg);
    return Init_SobatHareket_asagi(msg_);
  }

private:
  ::sobat_interfaces::msg::SobatHareket msg_;
};

class Init_SobatHareket_sol
{
public:
  explicit Init_SobatHareket_sol(::sobat_interfaces::msg::SobatHareket & msg)
  : msg_(msg)
  {}
  Init_SobatHareket_yukari sol(::sobat_interfaces::msg::SobatHareket::_sol_type arg)
  {
    msg_.sol = std::move(arg);
    return Init_SobatHareket_yukari(msg_);
  }

private:
  ::sobat_interfaces::msg::SobatHareket msg_;
};

class Init_SobatHareket_sag
{
public:
  explicit Init_SobatHareket_sag(::sobat_interfaces::msg::SobatHareket & msg)
  : msg_(msg)
  {}
  Init_SobatHareket_sol sag(::sobat_interfaces::msg::SobatHareket::_sag_type arg)
  {
    msg_.sag = std::move(arg);
    return Init_SobatHareket_sol(msg_);
  }

private:
  ::sobat_interfaces::msg::SobatHareket msg_;
};

class Init_SobatHareket_geri
{
public:
  explicit Init_SobatHareket_geri(::sobat_interfaces::msg::SobatHareket & msg)
  : msg_(msg)
  {}
  Init_SobatHareket_sag geri(::sobat_interfaces::msg::SobatHareket::_geri_type arg)
  {
    msg_.geri = std::move(arg);
    return Init_SobatHareket_sag(msg_);
  }

private:
  ::sobat_interfaces::msg::SobatHareket msg_;
};

class Init_SobatHareket_ileri
{
public:
  Init_SobatHareket_ileri()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_SobatHareket_geri ileri(::sobat_interfaces::msg::SobatHareket::_ileri_type arg)
  {
    msg_.ileri = std::move(arg);
    return Init_SobatHareket_geri(msg_);
  }

private:
  ::sobat_interfaces::msg::SobatHareket msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::sobat_interfaces::msg::SobatHareket>()
{
  return sobat_interfaces::msg::builder::Init_SobatHareket_ileri();
}

}  // namespace sobat_interfaces

#endif  // SOBAT_INTERFACES__MSG__DETAIL__SOBAT_HAREKET__BUILDER_HPP_
