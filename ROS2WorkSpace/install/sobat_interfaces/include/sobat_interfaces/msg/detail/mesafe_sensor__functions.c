// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from sobat_interfaces:msg/MesafeSensor.idl
// generated code does not contain a copyright notice
#include "sobat_interfaces/msg/detail/mesafe_sensor__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
sobat_interfaces__msg__MesafeSensor__init(sobat_interfaces__msg__MesafeSensor * msg)
{
  if (!msg) {
    return false;
  }
  // mesafe_sensor1
  // mesafe_sensor2
  // mesafe_sensor3
  // mesafe_sensor4
  // mesafe_sensor5
  return true;
}

void
sobat_interfaces__msg__MesafeSensor__fini(sobat_interfaces__msg__MesafeSensor * msg)
{
  if (!msg) {
    return;
  }
  // mesafe_sensor1
  // mesafe_sensor2
  // mesafe_sensor3
  // mesafe_sensor4
  // mesafe_sensor5
}

bool
sobat_interfaces__msg__MesafeSensor__are_equal(const sobat_interfaces__msg__MesafeSensor * lhs, const sobat_interfaces__msg__MesafeSensor * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // mesafe_sensor1
  if (lhs->mesafe_sensor1 != rhs->mesafe_sensor1) {
    return false;
  }
  // mesafe_sensor2
  if (lhs->mesafe_sensor2 != rhs->mesafe_sensor2) {
    return false;
  }
  // mesafe_sensor3
  if (lhs->mesafe_sensor3 != rhs->mesafe_sensor3) {
    return false;
  }
  // mesafe_sensor4
  if (lhs->mesafe_sensor4 != rhs->mesafe_sensor4) {
    return false;
  }
  // mesafe_sensor5
  if (lhs->mesafe_sensor5 != rhs->mesafe_sensor5) {
    return false;
  }
  return true;
}

bool
sobat_interfaces__msg__MesafeSensor__copy(
  const sobat_interfaces__msg__MesafeSensor * input,
  sobat_interfaces__msg__MesafeSensor * output)
{
  if (!input || !output) {
    return false;
  }
  // mesafe_sensor1
  output->mesafe_sensor1 = input->mesafe_sensor1;
  // mesafe_sensor2
  output->mesafe_sensor2 = input->mesafe_sensor2;
  // mesafe_sensor3
  output->mesafe_sensor3 = input->mesafe_sensor3;
  // mesafe_sensor4
  output->mesafe_sensor4 = input->mesafe_sensor4;
  // mesafe_sensor5
  output->mesafe_sensor5 = input->mesafe_sensor5;
  return true;
}

sobat_interfaces__msg__MesafeSensor *
sobat_interfaces__msg__MesafeSensor__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sobat_interfaces__msg__MesafeSensor * msg = (sobat_interfaces__msg__MesafeSensor *)allocator.allocate(sizeof(sobat_interfaces__msg__MesafeSensor), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(sobat_interfaces__msg__MesafeSensor));
  bool success = sobat_interfaces__msg__MesafeSensor__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
sobat_interfaces__msg__MesafeSensor__destroy(sobat_interfaces__msg__MesafeSensor * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    sobat_interfaces__msg__MesafeSensor__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
sobat_interfaces__msg__MesafeSensor__Sequence__init(sobat_interfaces__msg__MesafeSensor__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sobat_interfaces__msg__MesafeSensor * data = NULL;

  if (size) {
    data = (sobat_interfaces__msg__MesafeSensor *)allocator.zero_allocate(size, sizeof(sobat_interfaces__msg__MesafeSensor), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = sobat_interfaces__msg__MesafeSensor__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        sobat_interfaces__msg__MesafeSensor__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
sobat_interfaces__msg__MesafeSensor__Sequence__fini(sobat_interfaces__msg__MesafeSensor__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      sobat_interfaces__msg__MesafeSensor__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

sobat_interfaces__msg__MesafeSensor__Sequence *
sobat_interfaces__msg__MesafeSensor__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sobat_interfaces__msg__MesafeSensor__Sequence * array = (sobat_interfaces__msg__MesafeSensor__Sequence *)allocator.allocate(sizeof(sobat_interfaces__msg__MesafeSensor__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = sobat_interfaces__msg__MesafeSensor__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
sobat_interfaces__msg__MesafeSensor__Sequence__destroy(sobat_interfaces__msg__MesafeSensor__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    sobat_interfaces__msg__MesafeSensor__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
sobat_interfaces__msg__MesafeSensor__Sequence__are_equal(const sobat_interfaces__msg__MesafeSensor__Sequence * lhs, const sobat_interfaces__msg__MesafeSensor__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!sobat_interfaces__msg__MesafeSensor__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
sobat_interfaces__msg__MesafeSensor__Sequence__copy(
  const sobat_interfaces__msg__MesafeSensor__Sequence * input,
  sobat_interfaces__msg__MesafeSensor__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(sobat_interfaces__msg__MesafeSensor);
    sobat_interfaces__msg__MesafeSensor * data =
      (sobat_interfaces__msg__MesafeSensor *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!sobat_interfaces__msg__MesafeSensor__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          sobat_interfaces__msg__MesafeSensor__fini(&data[i]);
        }
        free(data);
        return false;
      }
    }
    output->data = data;
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!sobat_interfaces__msg__MesafeSensor__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
