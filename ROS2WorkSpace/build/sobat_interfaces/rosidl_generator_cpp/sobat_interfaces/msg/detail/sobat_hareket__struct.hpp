// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from sobat_interfaces:msg/SobatHareket.idl
// generated code does not contain a copyright notice

#ifndef SOBAT_INTERFACES__MSG__DETAIL__SOBAT_HAREKET__STRUCT_HPP_
#define SOBAT_INTERFACES__MSG__DETAIL__SOBAT_HAREKET__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__sobat_interfaces__msg__SobatHareket __attribute__((deprecated))
#else
# define DEPRECATED__sobat_interfaces__msg__SobatHareket __declspec(deprecated)
#endif

namespace sobat_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct SobatHareket_
{
  using Type = SobatHareket_<ContainerAllocator>;

  explicit SobatHareket_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->ileri = false;
      this->geri = false;
      this->sag = false;
      this->sol = false;
      this->yukari = false;
      this->asagi = false;
    }
  }

  explicit SobatHareket_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->ileri = false;
      this->geri = false;
      this->sag = false;
      this->sol = false;
      this->yukari = false;
      this->asagi = false;
    }
  }

  // field types and members
  using _ileri_type =
    bool;
  _ileri_type ileri;
  using _geri_type =
    bool;
  _geri_type geri;
  using _sag_type =
    bool;
  _sag_type sag;
  using _sol_type =
    bool;
  _sol_type sol;
  using _yukari_type =
    bool;
  _yukari_type yukari;
  using _asagi_type =
    bool;
  _asagi_type asagi;

  // setters for named parameter idiom
  Type & set__ileri(
    const bool & _arg)
  {
    this->ileri = _arg;
    return *this;
  }
  Type & set__geri(
    const bool & _arg)
  {
    this->geri = _arg;
    return *this;
  }
  Type & set__sag(
    const bool & _arg)
  {
    this->sag = _arg;
    return *this;
  }
  Type & set__sol(
    const bool & _arg)
  {
    this->sol = _arg;
    return *this;
  }
  Type & set__yukari(
    const bool & _arg)
  {
    this->yukari = _arg;
    return *this;
  }
  Type & set__asagi(
    const bool & _arg)
  {
    this->asagi = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    sobat_interfaces::msg::SobatHareket_<ContainerAllocator> *;
  using ConstRawPtr =
    const sobat_interfaces::msg::SobatHareket_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<sobat_interfaces::msg::SobatHareket_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<sobat_interfaces::msg::SobatHareket_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      sobat_interfaces::msg::SobatHareket_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<sobat_interfaces::msg::SobatHareket_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      sobat_interfaces::msg::SobatHareket_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<sobat_interfaces::msg::SobatHareket_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<sobat_interfaces::msg::SobatHareket_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<sobat_interfaces::msg::SobatHareket_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__sobat_interfaces__msg__SobatHareket
    std::shared_ptr<sobat_interfaces::msg::SobatHareket_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__sobat_interfaces__msg__SobatHareket
    std::shared_ptr<sobat_interfaces::msg::SobatHareket_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const SobatHareket_ & other) const
  {
    if (this->ileri != other.ileri) {
      return false;
    }
    if (this->geri != other.geri) {
      return false;
    }
    if (this->sag != other.sag) {
      return false;
    }
    if (this->sol != other.sol) {
      return false;
    }
    if (this->yukari != other.yukari) {
      return false;
    }
    if (this->asagi != other.asagi) {
      return false;
    }
    return true;
  }
  bool operator!=(const SobatHareket_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct SobatHareket_

// alias to use template instance with default allocator
using SobatHareket =
  sobat_interfaces::msg::SobatHareket_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace sobat_interfaces

#endif  // SOBAT_INTERFACES__MSG__DETAIL__SOBAT_HAREKET__STRUCT_HPP_
