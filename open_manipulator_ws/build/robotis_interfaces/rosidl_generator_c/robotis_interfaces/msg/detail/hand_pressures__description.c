// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from robotis_interfaces:msg/HandPressures.idl
// generated code does not contain a copyright notice

#include "robotis_interfaces/msg/detail/hand_pressures__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_robotis_interfaces
const rosidl_type_hash_t *
robotis_interfaces__msg__HandPressures__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0xc6, 0x2e, 0x92, 0x4c, 0x58, 0x95, 0x1d, 0xb5,
      0x92, 0xfd, 0xc6, 0x25, 0x78, 0x27, 0x29, 0xb6,
      0xd8, 0x18, 0x4a, 0xa1, 0xf0, 0x9c, 0x09, 0x65,
      0x11, 0x65, 0x1f, 0x41, 0xb1, 0x8a, 0xb6, 0x23,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types
#include "builtin_interfaces/msg/detail/time__functions.h"
#include "robotis_interfaces/msg/detail/tactile_sensor__functions.h"
#include "std_msgs/msg/detail/header__functions.h"

// Hashes for external referenced types
#ifndef NDEBUG
static const rosidl_type_hash_t builtin_interfaces__msg__Time__EXPECTED_HASH = {1, {
    0xb1, 0x06, 0x23, 0x5e, 0x25, 0xa4, 0xc5, 0xed,
    0x35, 0x09, 0x8a, 0xa0, 0xa6, 0x1a, 0x3e, 0xe9,
    0xc9, 0xb1, 0x8d, 0x19, 0x7f, 0x39, 0x8b, 0x0e,
    0x42, 0x06, 0xce, 0xa9, 0xac, 0xf9, 0xc1, 0x97,
  }};
static const rosidl_type_hash_t robotis_interfaces__msg__TactileSensor__EXPECTED_HASH = {1, {
    0x7b, 0x18, 0x28, 0x50, 0xc4, 0x49, 0x38, 0x4b,
    0xf0, 0x1e, 0x45, 0x53, 0x3f, 0xe9, 0x01, 0xdd,
    0x48, 0x3f, 0x0b, 0x00, 0xb6, 0x35, 0x06, 0xa5,
    0x28, 0x71, 0xea, 0x33, 0x5a, 0xaa, 0x4d, 0x48,
  }};
static const rosidl_type_hash_t std_msgs__msg__Header__EXPECTED_HASH = {1, {
    0xf4, 0x9f, 0xb3, 0xae, 0x2c, 0xf0, 0x70, 0xf7,
    0x93, 0x64, 0x5f, 0xf7, 0x49, 0x68, 0x3a, 0xc6,
    0xb0, 0x62, 0x03, 0xe4, 0x1c, 0x89, 0x1e, 0x17,
    0x70, 0x1b, 0x1c, 0xb5, 0x97, 0xce, 0x6a, 0x01,
  }};
#endif

static char robotis_interfaces__msg__HandPressures__TYPE_NAME[] = "robotis_interfaces/msg/HandPressures";
static char builtin_interfaces__msg__Time__TYPE_NAME[] = "builtin_interfaces/msg/Time";
static char robotis_interfaces__msg__TactileSensor__TYPE_NAME[] = "robotis_interfaces/msg/TactileSensor";
static char std_msgs__msg__Header__TYPE_NAME[] = "std_msgs/msg/Header";

// Define type names, field names, and default values
static char robotis_interfaces__msg__HandPressures__FIELD_NAME__header[] = "header";
static char robotis_interfaces__msg__HandPressures__FIELD_NAME__hand_name[] = "hand_name";
static char robotis_interfaces__msg__HandPressures__FIELD_NAME__sensors[] = "sensors";

static rosidl_runtime_c__type_description__Field robotis_interfaces__msg__HandPressures__FIELDS[] = {
  {
    {robotis_interfaces__msg__HandPressures__FIELD_NAME__header, 6, 6},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {std_msgs__msg__Header__TYPE_NAME, 19, 19},
    },
    {NULL, 0, 0},
  },
  {
    {robotis_interfaces__msg__HandPressures__FIELD_NAME__hand_name, 9, 9},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_STRING,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {robotis_interfaces__msg__HandPressures__FIELD_NAME__sensors, 7, 7},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE_UNBOUNDED_SEQUENCE,
      0,
      0,
      {robotis_interfaces__msg__TactileSensor__TYPE_NAME, 36, 36},
    },
    {NULL, 0, 0},
  },
};

static rosidl_runtime_c__type_description__IndividualTypeDescription robotis_interfaces__msg__HandPressures__REFERENCED_TYPE_DESCRIPTIONS[] = {
  {
    {builtin_interfaces__msg__Time__TYPE_NAME, 27, 27},
    {NULL, 0, 0},
  },
  {
    {robotis_interfaces__msg__TactileSensor__TYPE_NAME, 36, 36},
    {NULL, 0, 0},
  },
  {
    {std_msgs__msg__Header__TYPE_NAME, 19, 19},
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
robotis_interfaces__msg__HandPressures__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {robotis_interfaces__msg__HandPressures__TYPE_NAME, 36, 36},
      {robotis_interfaces__msg__HandPressures__FIELDS, 3, 3},
    },
    {robotis_interfaces__msg__HandPressures__REFERENCED_TYPE_DESCRIPTIONS, 3, 3},
  };
  if (!constructed) {
    assert(0 == memcmp(&builtin_interfaces__msg__Time__EXPECTED_HASH, builtin_interfaces__msg__Time__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[0].fields = builtin_interfaces__msg__Time__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&robotis_interfaces__msg__TactileSensor__EXPECTED_HASH, robotis_interfaces__msg__TactileSensor__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[1].fields = robotis_interfaces__msg__TactileSensor__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&std_msgs__msg__Header__EXPECTED_HASH, std_msgs__msg__Header__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[2].fields = std_msgs__msg__Header__get_type_description(NULL)->type_description.fields;
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "# Pressure readings for tactile sensors on a ROBOTIS Hand.\n"
  "\n"
  "# Standard header for timestamps and frame_id.\n"
  "std_msgs/Header header\n"
  "\n"
  "# Logical hand identifier, for example \"left\" or \"right\".\n"
  "string hand_name\n"
  "\n"
  "# Array of tactile sensor readings.\n"
  "TactileSensor[] sensors";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
robotis_interfaces__msg__HandPressures__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {robotis_interfaces__msg__HandPressures__TYPE_NAME, 36, 36},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 267, 267},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
robotis_interfaces__msg__HandPressures__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[4];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 4, 4};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *robotis_interfaces__msg__HandPressures__get_individual_type_description_source(NULL),
    sources[1] = *builtin_interfaces__msg__Time__get_individual_type_description_source(NULL);
    sources[2] = *robotis_interfaces__msg__TactileSensor__get_individual_type_description_source(NULL);
    sources[3] = *std_msgs__msg__Header__get_individual_type_description_source(NULL);
    constructed = true;
  }
  return &source_sequence;
}
