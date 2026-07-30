// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from user_interface:msg/UserInt.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "user_interface/msg/detail/user_int__struct.h"
#include "user_interface/msg/detail/user_int__functions.h"

ROSIDL_GENERATOR_C_IMPORT
bool std_msgs__msg__header__convert_from_py(PyObject * _pymsg, void * _ros_message);
ROSIDL_GENERATOR_C_IMPORT
PyObject * std_msgs__msg__header__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool user_interface__msg__user_int__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[37];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("user_interface.msg._user_int.UserInt", full_classname_dest, 36) == 0);
  }
  user_interface__msg__UserInt * ros_message = _ros_message;
  {  // header
    PyObject * field = PyObject_GetAttrString(_pymsg, "header");
    if (!field) {
      return false;
    }
    if (!std_msgs__msg__header__convert_from_py(field, &ros_message->header)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // user_int
    PyObject * field = PyObject_GetAttrString(_pymsg, "user_int");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->user_int = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // user_int2
    PyObject * field = PyObject_GetAttrString(_pymsg, "user_int2");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->user_int2 = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // user_int3
    PyObject * field = PyObject_GetAttrString(_pymsg, "user_int3");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->user_int3 = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * user_interface__msg__user_int__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of UserInt */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("user_interface.msg._user_int");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "UserInt");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  user_interface__msg__UserInt * ros_message = (user_interface__msg__UserInt *)raw_ros_message;
  {  // header
    PyObject * field = NULL;
    field = std_msgs__msg__header__convert_to_py(&ros_message->header);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "header", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // user_int
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->user_int);
    {
      int rc = PyObject_SetAttrString(_pymessage, "user_int", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // user_int2
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->user_int2);
    {
      int rc = PyObject_SetAttrString(_pymessage, "user_int2", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // user_int3
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->user_int3);
    {
      int rc = PyObject_SetAttrString(_pymessage, "user_int3", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
