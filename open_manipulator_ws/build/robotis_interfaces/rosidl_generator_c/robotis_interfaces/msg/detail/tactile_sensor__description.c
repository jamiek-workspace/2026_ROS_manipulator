// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from robotis_interfaces:msg/TactileSensor.idl
// generated code does not contain a copyright notice

#include "robotis_interfaces/msg/detail/tactile_sensor__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_robotis_interfaces
const rosidl_type_hash_t *
robotis_interfaces__msg__TactileSensor__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x7b, 0x18, 0x28, 0x50, 0xc4, 0x49, 0x38, 0x4b,
      0xf0, 0x1e, 0x45, 0x53, 0x3f, 0xe9, 0x01, 0xdd,
      0x48, 0x3f, 0x0b, 0x00, 0xb6, 0x35, 0x06, 0xa5,
      0x28, 0x71, 0xea, 0x33, 0x5a, 0xaa, 0x4d, 0x48,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types

// Hashes for external referenced types
#ifndef NDEBUG
#endif

static char robotis_interfaces__msg__TactileSensor__TYPE_NAME[] = "robotis_interfaces/msg/TactileSensor";

// Define type names, field names, and default values
static char robotis_interfaces__msg__TactileSensor__FIELD_NAME__sensor_name[] = "sensor_name";
static char robotis_interfaces__msg__TactileSensor__FIELD_NAME__pressure_names[] = "pressure_names";
static char robotis_interfaces__msg__TactileSensor__FIELD_NAME__pressure_values[] = "pressure_values";

static rosidl_runtime_c__type_description__Field robotis_interfaces__msg__TactileSensor__FIELDS[] = {
  {
    {robotis_interfaces__msg__TactileSensor__FIELD_NAME__sensor_name, 11, 11},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_STRING,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {robotis_interfaces__msg__TactileSensor__FIELD_NAME__pressure_names, 14, 14},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_STRING_ARRAY,
      9,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {robotis_interfaces__msg__TactileSensor__FIELD_NAME__pressure_values, 15, 15},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_UINT8_ARRAY,
      9,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
robotis_interfaces__msg__TactileSensor__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {robotis_interfaces__msg__TactileSensor__TYPE_NAME, 36, 36},
      {robotis_interfaces__msg__TactileSensor__FIELDS, 3, 3},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "# TactileSensor.msg\n"
  "\n"
  "# Name of the tactile sensor source.\n"
  "string sensor_name\n"
  "\n"
  "# Present pressure values (0-255) from the tactile sensor (3x3 grid base)\n"
  "# Pressure indices are ordered from top to bottom, and from left to right within each row.\n"
  "string[9] pressure_names\n"
  "uint8[9] pressure_values";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
robotis_interfaces__msg__TactileSensor__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {robotis_interfaces__msg__TactileSensor__TYPE_NAME, 36, 36},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 293, 293},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
robotis_interfaces__msg__TactileSensor__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *robotis_interfaces__msg__TactileSensor__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}
