// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from sobat_interfaces:msg/SobatHareket.idl
// generated code does not contain a copyright notice
#include "sobat_interfaces/msg/detail/sobat_hareket__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
sobat_interfaces__msg__SobatHareket__init(sobat_interfaces__msg__SobatHareket * msg)
{
  if (!msg) {
    return false;
  }
  // ileri
  // geri
  // sag
  // sol
  // yukari
  // asagi
  return true;
}

void
sobat_interfaces__msg__SobatHareket__fini(sobat_interfaces__msg__SobatHareket * msg)
{
  if (!msg) {
    return;
  }
  // ileri
  // geri
  // sag
  // sol
  // yukari
  // asagi
}

bool
sobat_interfaces__msg__SobatHareket__are_equal(const sobat_interfaces__msg__SobatHareket * lhs, const sobat_interfaces__msg__SobatHareket * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // ileri
  if (lhs->ileri != rhs->ileri) {
    return false;
  }
  // geri
  if (lhs->geri != rhs->geri) {
    return false;
  }
  // sag
  if (lhs->sag != rhs->sag) {
    return false;
  }
  // sol
  if (lhs->sol != rhs->sol) {
    return false;
  }
  // yukari
  if (lhs->yukari != rhs->yukari) {
    return false;
  }
  // asagi
  if (lhs->asagi != rhs->asagi) {
    return false;
  }
  return true;
}

bool
sobat_interfaces__msg__SobatHareket__copy(
  const sobat_interfaces__msg__SobatHareket * input,
  sobat_interfaces__msg__SobatHareket * output)
{
  if (!input || !output) {
    return false;
  }
  // ileri
  output->ileri = input->ileri;
  // geri
  output->geri = input->geri;
  // sag
  output->sag = input->sag;
  // sol
  output->sol = input->sol;
  // yukari
  output->yukari = input->yukari;
  // asagi
  output->asagi = input->asagi;
  return true;
}

sobat_interfaces__msg__SobatHareket *
sobat_interfaces__msg__SobatHareket__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sobat_interfaces__msg__SobatHareket * msg = (sobat_interfaces__msg__SobatHareket *)allocator.allocate(sizeof(sobat_interfaces__msg__SobatHareket), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(sobat_interfaces__msg__SobatHareket));
  bool success = sobat_interfaces__msg__SobatHareket__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
sobat_interfaces__msg__SobatHareket__destroy(sobat_interfaces__msg__SobatHareket * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    sobat_interfaces__msg__SobatHareket__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
sobat_interfaces__msg__SobatHareket__Sequence__init(sobat_interfaces__msg__SobatHareket__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sobat_interfaces__msg__SobatHareket * data = NULL;

  if (size) {
    data = (sobat_interfaces__msg__SobatHareket *)allocator.zero_allocate(size, sizeof(sobat_interfaces__msg__SobatHareket), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = sobat_interfaces__msg__SobatHareket__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        sobat_interfaces__msg__SobatHareket__fini(&data[i - 1]);
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
sobat_interfaces__msg__SobatHareket__Sequence__fini(sobat_interfaces__msg__SobatHareket__Sequence * array)
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
      sobat_interfaces__msg__SobatHareket__fini(&array->data[i]);
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

sobat_interfaces__msg__SobatHareket__Sequence *
sobat_interfaces__msg__SobatHareket__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sobat_interfaces__msg__SobatHareket__Sequence * array = (sobat_interfaces__msg__SobatHareket__Sequence *)allocator.allocate(sizeof(sobat_interfaces__msg__SobatHareket__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = sobat_interfaces__msg__SobatHareket__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
sobat_interfaces__msg__SobatHareket__Sequence__destroy(sobat_interfaces__msg__SobatHareket__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    sobat_interfaces__msg__SobatHareket__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
sobat_interfaces__msg__SobatHareket__Sequence__are_equal(const sobat_interfaces__msg__SobatHareket__Sequence * lhs, const sobat_interfaces__msg__SobatHareket__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!sobat_interfaces__msg__SobatHareket__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
sobat_interfaces__msg__SobatHareket__Sequence__copy(
  const sobat_interfaces__msg__SobatHareket__Sequence * input,
  sobat_interfaces__msg__SobatHareket__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(sobat_interfaces__msg__SobatHareket);
    sobat_interfaces__msg__SobatHareket * data =
      (sobat_interfaces__msg__SobatHareket *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!sobat_interfaces__msg__SobatHareket__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          sobat_interfaces__msg__SobatHareket__fini(&data[i]);
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
    if (!sobat_interfaces__msg__SobatHareket__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
