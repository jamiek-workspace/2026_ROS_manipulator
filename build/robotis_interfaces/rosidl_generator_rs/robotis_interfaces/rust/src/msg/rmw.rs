#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};


#[link(name = "robotis_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__robotis_interfaces__msg__HandJoints() -> *const std::ffi::c_void;
}

#[link(name = "robotis_interfaces__rosidl_generator_c")]
extern "C" {
    fn robotis_interfaces__msg__HandJoints__init(msg: *mut HandJoints) -> bool;
    fn robotis_interfaces__msg__HandJoints__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<HandJoints>, size: usize) -> bool;
    fn robotis_interfaces__msg__HandJoints__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<HandJoints>);
    fn robotis_interfaces__msg__HandJoints__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<HandJoints>, out_seq: *mut rosidl_runtime_rs::Sequence<HandJoints>) -> bool;
}

// Corresponds to robotis_interfaces__msg__HandJoints
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]

/// HandJoints.msg

#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct HandJoints {
    /// Standard header for timestamps and frame_id.
    pub header: std_msgs::msg::rmw::Header,

    /// Fixed-size array of 21 Point32 structs.
    /// Point32 uses float32 for each coordinate, which is generally
    /// sufficient for non-critical robot localization and saves space
    /// compared to float64 (Point).
    pub joints: [geometry_msgs::msg::rmw::Point32; 21],

}



impl Default for HandJoints {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !robotis_interfaces__msg__HandJoints__init(&mut msg as *mut _) {
        panic!("Call to robotis_interfaces__msg__HandJoints__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for HandJoints {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { robotis_interfaces__msg__HandJoints__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { robotis_interfaces__msg__HandJoints__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { robotis_interfaces__msg__HandJoints__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for HandJoints {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for HandJoints where Self: Sized {
  const TYPE_NAME: &'static str = "robotis_interfaces/msg/HandJoints";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__robotis_interfaces__msg__HandJoints() }
  }
}


#[link(name = "robotis_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__robotis_interfaces__msg__HandPressures() -> *const std::ffi::c_void;
}

#[link(name = "robotis_interfaces__rosidl_generator_c")]
extern "C" {
    fn robotis_interfaces__msg__HandPressures__init(msg: *mut HandPressures) -> bool;
    fn robotis_interfaces__msg__HandPressures__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<HandPressures>, size: usize) -> bool;
    fn robotis_interfaces__msg__HandPressures__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<HandPressures>);
    fn robotis_interfaces__msg__HandPressures__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<HandPressures>, out_seq: *mut rosidl_runtime_rs::Sequence<HandPressures>) -> bool;
}

// Corresponds to robotis_interfaces__msg__HandPressures
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]

/// Pressure readings for tactile sensors on a ROBOTIS Hand.

#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct HandPressures {
    /// Standard header for timestamps and frame_id.
    pub header: std_msgs::msg::rmw::Header,

    /// Logical hand identifier, for example "left" or "right".
    pub hand_name: rosidl_runtime_rs::String,

    /// Array of tactile sensor readings.
    pub sensors: rosidl_runtime_rs::Sequence<super::super::msg::rmw::TactileSensor>,

}



impl Default for HandPressures {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !robotis_interfaces__msg__HandPressures__init(&mut msg as *mut _) {
        panic!("Call to robotis_interfaces__msg__HandPressures__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for HandPressures {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { robotis_interfaces__msg__HandPressures__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { robotis_interfaces__msg__HandPressures__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { robotis_interfaces__msg__HandPressures__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for HandPressures {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for HandPressures where Self: Sized {
  const TYPE_NAME: &'static str = "robotis_interfaces/msg/HandPressures";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__robotis_interfaces__msg__HandPressures() }
  }
}


#[link(name = "robotis_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__robotis_interfaces__msg__MoveL() -> *const std::ffi::c_void;
}

#[link(name = "robotis_interfaces__rosidl_generator_c")]
extern "C" {
    fn robotis_interfaces__msg__MoveL__init(msg: *mut MoveL) -> bool;
    fn robotis_interfaces__msg__MoveL__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<MoveL>, size: usize) -> bool;
    fn robotis_interfaces__msg__MoveL__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<MoveL>);
    fn robotis_interfaces__msg__MoveL__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<MoveL>, out_seq: *mut rosidl_runtime_rs::Sequence<MoveL>) -> bool;
}

// Corresponds to robotis_interfaces__msg__MoveL
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]

/// Target end-effector pose for the linear move command.

#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct MoveL {

    // This member is not documented.
    #[allow(missing_docs)]
    pub pose: geometry_msgs::msg::rmw::PoseStamped,

    /// Desired time to reach the target pose from the current pose.
    pub time_from_start: builtin_interfaces::msg::rmw::Duration,

}



impl Default for MoveL {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !robotis_interfaces__msg__MoveL__init(&mut msg as *mut _) {
        panic!("Call to robotis_interfaces__msg__MoveL__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for MoveL {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { robotis_interfaces__msg__MoveL__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { robotis_interfaces__msg__MoveL__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { robotis_interfaces__msg__MoveL__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for MoveL {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for MoveL where Self: Sized {
  const TYPE_NAME: &'static str = "robotis_interfaces/msg/MoveL";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__robotis_interfaces__msg__MoveL() }
  }
}


#[link(name = "robotis_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__robotis_interfaces__msg__TactileSensor() -> *const std::ffi::c_void;
}

#[link(name = "robotis_interfaces__rosidl_generator_c")]
extern "C" {
    fn robotis_interfaces__msg__TactileSensor__init(msg: *mut TactileSensor) -> bool;
    fn robotis_interfaces__msg__TactileSensor__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<TactileSensor>, size: usize) -> bool;
    fn robotis_interfaces__msg__TactileSensor__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<TactileSensor>);
    fn robotis_interfaces__msg__TactileSensor__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<TactileSensor>, out_seq: *mut rosidl_runtime_rs::Sequence<TactileSensor>) -> bool;
}

// Corresponds to robotis_interfaces__msg__TactileSensor
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]

/// TactileSensor.msg

#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct TactileSensor {
    /// Name of the tactile sensor source.
    pub sensor_name: rosidl_runtime_rs::String,

    /// Present pressure values (0-255) from the tactile sensor (3x3 grid base)
    /// Pressure indices are ordered from top to bottom, and from left to right within each row.
    pub pressure_names: [rosidl_runtime_rs::String; 9],


    // This member is not documented.
    #[allow(missing_docs)]
    pub pressure_values: [u8; 9],

}



impl Default for TactileSensor {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !robotis_interfaces__msg__TactileSensor__init(&mut msg as *mut _) {
        panic!("Call to robotis_interfaces__msg__TactileSensor__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for TactileSensor {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { robotis_interfaces__msg__TactileSensor__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { robotis_interfaces__msg__TactileSensor__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { robotis_interfaces__msg__TactileSensor__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for TactileSensor {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for TactileSensor where Self: Sized {
  const TYPE_NAME: &'static str = "robotis_interfaces/msg/TactileSensor";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__robotis_interfaces__msg__TactileSensor() }
  }
}


