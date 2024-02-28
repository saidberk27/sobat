// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from sobat_interfaces:msg/MesafeSensor.idl
// generated code does not contain a copyright notice

#ifndef SOBAT_INTERFACES__MSG__DETAIL__MESAFE_SENSOR__STRUCT_HPP_
#define SOBAT_INTERFACES__MSG__DETAIL__MESAFE_SENSOR__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__sobat_interfaces__msg__MesafeSensor __attribute__((deprecated))
#else
# define DEPRECATED__sobat_interfaces__msg__MesafeSensor __declspec(deprecated)
#endif

namespace sobat_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct MesafeSensor_
{
  using Type = MesafeSensor_<ContainerAllocator>;

  explicit MesafeSensor_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->mesafe_sensor1 = 0.0f;
      this->mesafe_sensor2 = 0.0f;
      this->mesafe_sensor3 = 0.0f;
      this->mesafe_sensor4 = 0.0f;
      this->mesafe_sensor5 = 0.0f;
    }
  }

  explicit MesafeSensor_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->mesafe_sensor1 = 0.0f;
      this->mesafe_sensor2 = 0.0f;
      this->mesafe_sensor3 = 0.0f;
      this->mesafe_sensor4 = 0.0f;
      this->mesafe_sensor5 = 0.0f;
    }
  }

  // field types and members
  using _mesafe_sensor1_type =
    float;
  _mesafe_sensor1_type mesafe_sensor1;
  using _mesafe_sensor2_type =
    float;
  _mesafe_sensor2_type mesafe_sensor2;
  using _mesafe_sensor3_type =
    float;
  _mesafe_sensor3_type mesafe_sensor3;
  using _mesafe_sensor4_type =
    float;
  _mesafe_sensor4_type mesafe_sensor4;
  using _mesafe_sensor5_type =
    float;
  _mesafe_sensor5_type mesafe_sensor5;

  // setters for named parameter idiom
  Type & set__mesafe_sensor1(
    const float & _arg)
  {
    this->mesafe_sensor1 = _arg;
    return *this;
  }
  Type & set__mesafe_sensor2(
    const float & _arg)
  {
    this->mesafe_sensor2 = _arg;
    return *this;
  }
  Type & set__mesafe_sensor3(
    const float & _arg)
  {
    this->mesafe_sensor3 = _arg;
    return *this;
  }
  Type & set__mesafe_sensor4(
    const float & _arg)
  {
    this->mesafe_sensor4 = _arg;
    return *this;
  }
  Type & set__mesafe_sensor5(
    const float & _arg)
  {
    this->mesafe_sensor5 = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    sobat_interfaces::msg::MesafeSensor_<ContainerAllocator> *;
  using ConstRawPtr =
    const sobat_interfaces::msg::MesafeSensor_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<sobat_interfaces::msg::MesafeSensor_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<sobat_interfaces::msg::MesafeSensor_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      sobat_interfaces::msg::MesafeSensor_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<sobat_interfaces::msg::MesafeSensor_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      sobat_interfaces::msg::MesafeSensor_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<sobat_interfaces::msg::MesafeSensor_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<sobat_interfaces::msg::MesafeSensor_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<sobat_interfaces::msg::MesafeSensor_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__sobat_interfaces__msg__MesafeSensor
    std::shared_ptr<sobat_interfaces::msg::MesafeSensor_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__sobat_interfaces__msg__MesafeSensor
    std::shared_ptr<sobat_interfaces::msg::MesafeSensor_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const MesafeSensor_ & other) const
  {
    if (this->mesafe_sensor1 != other.mesafe_sensor1) {
      return false;
    }
    if (this->mesafe_sensor2 != other.mesafe_sensor2) {
      return false;
    }
    if (this->mesafe_sensor3 != other.mesafe_sensor3) {
      return false;
    }
    if (this->mesafe_sensor4 != other.mesafe_sensor4) {
      return false;
    }
    if (this->mesafe_sensor5 != other.mesafe_sensor5) {
      return false;
    }
    return true;
  }
  bool operator!=(const MesafeSensor_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct MesafeSensor_

// alias to use template instance with default allocator
using MesafeSensor =
  sobat_interfaces::msg::MesafeSensor_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace sobat_interfaces

#endif  // SOBAT_INTERFACES__MSG__DETAIL__MESAFE_SENSOR__STRUCT_HPP_
