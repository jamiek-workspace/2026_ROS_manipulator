# generated from rosidl_cmake/cmake/rosidl_cmake_aggregate_target-extras.cmake.in

# Create a convenience aggregate target user_interface::user_interface
# that links all generated interface targets, so downstream packages can use
# a single modern CMake target name instead of ${user_interface_TARGETS}.
if(user_interface_TARGETS AND NOT TARGET user_interface::user_interface)
  add_library(user_interface::user_interface INTERFACE IMPORTED)
  set_target_properties(user_interface::user_interface PROPERTIES
    INTERFACE_LINK_LIBRARIES "${user_interface_TARGETS}")
endif()
