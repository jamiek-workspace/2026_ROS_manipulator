# generated from rosidl_cmake/cmake/rosidl_cmake_aggregate_target-extras.cmake.in

# Create a convenience aggregate target robotis_interfaces::robotis_interfaces
# that links all generated interface targets, so downstream packages can use
# a single modern CMake target name instead of ${robotis_interfaces_TARGETS}.
if(robotis_interfaces_TARGETS AND NOT TARGET robotis_interfaces::robotis_interfaces)
  add_library(robotis_interfaces::robotis_interfaces INTERFACE IMPORTED)
  set_target_properties(robotis_interfaces::robotis_interfaces PROPERTIES
    INTERFACE_LINK_LIBRARIES "${robotis_interfaces_TARGETS}")
endif()
