// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from sobat_interfaces:msg/SobatHareket.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "sobat_interfaces/msg/detail/sobat_hareket__rosidl_typesupport_introspection_c.h"
#include "sobat_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "sobat_interfaces/msg/detail/sobat_hareket__functions.h"
#include "sobat_interfaces/msg/detail/sobat_hareket__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void SobatHareket__rosidl_typesupport_introspection_c__SobatHareket_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  sobat_interfaces__msg__SobatHareket__init(message_memory);
}

void SobatHareket__rosidl_typesupport_introspection_c__SobatHareket_fini_function(void * message_memory)
{
  sobat_interfaces__msg__SobatHareket__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember SobatHareket__rosidl_typesupport_introspection_c__SobatHareket_message_member_array[6] = {
  {
    "ileri",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sobat_interfaces__msg__SobatHareket, ileri),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "geri",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sobat_interfaces__msg__SobatHareket, geri),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "sag",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sobat_interfaces__msg__SobatHareket, sag),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "sol",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sobat_interfaces__msg__SobatHareket, sol),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "yukari",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sobat_interfaces__msg__SobatHareket, yukari),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "asagi",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sobat_interfaces__msg__SobatHareket, asagi),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers SobatHareket__rosidl_typesupport_introspection_c__SobatHareket_message_members = {
  "sobat_interfaces__msg",  // message namespace
  "SobatHareket",  // message name
  6,  // number of fields
  sizeof(sobat_interfaces__msg__SobatHareket),
  SobatHareket__rosidl_typesupport_introspection_c__SobatHareket_message_member_array,  // message members
  SobatHareket__rosidl_typesupport_introspection_c__SobatHareket_init_function,  // function to initialize message memory (memory has to be allocated)
  SobatHareket__rosidl_typesupport_introspection_c__SobatHareket_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t SobatHareket__rosidl_typesupport_introspection_c__SobatHareket_message_type_support_handle = {
  0,
  &SobatHareket__rosidl_typesupport_introspection_c__SobatHareket_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_sobat_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, sobat_interfaces, msg, SobatHareket)() {
  if (!SobatHareket__rosidl_typesupport_introspection_c__SobatHareket_message_type_support_handle.typesupport_identifier) {
    SobatHareket__rosidl_typesupport_introspection_c__SobatHareket_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &SobatHareket__rosidl_typesupport_introspection_c__SobatHareket_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
