// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__rosidl_typesupport_fastrtps_cpp.hpp.em
// with input from fizzbuzz_interfaces:msg/FizzBuzz.idl
// generated code does not contain a copyright notice

#ifndef FIZZBUZZ_INTERFACES__MSG__DETAIL__FIZZ_BUZZ__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
#define FIZZBUZZ_INTERFACES__MSG__DETAIL__FIZZ_BUZZ__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_

#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "fizzbuzz_interfaces/msg/rosidl_typesupport_fastrtps_cpp__visibility_control.h"
#include "fizzbuzz_interfaces/msg/detail/fizz_buzz__struct.hpp"

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

namespace fizzbuzz_interfaces
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_fizzbuzz_interfaces
cdr_serialize(
  const fizzbuzz_interfaces::msg::FizzBuzz & ros_message,
  eprosima::fastcdr::Cdr & cdr);

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_fizzbuzz_interfaces
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  fizzbuzz_interfaces::msg::FizzBuzz & ros_message);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_fizzbuzz_interfaces
get_serialized_size(
  const fizzbuzz_interfaces::msg::FizzBuzz & ros_message,
  size_t current_alignment);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_fizzbuzz_interfaces
max_serialized_size_FizzBuzz(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace fizzbuzz_interfaces

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_fizzbuzz_interfaces
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, fizzbuzz_interfaces, msg, FizzBuzz)();

#ifdef __cplusplus
}
#endif

#endif  // FIZZBUZZ_INTERFACES__MSG__DETAIL__FIZZ_BUZZ__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
