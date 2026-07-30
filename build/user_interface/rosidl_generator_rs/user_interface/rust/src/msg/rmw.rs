#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};


#[link(name = "user_interface__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__user_interface__msg__UserInt() -> *const std::ffi::c_void;
}

#[link(name = "user_interface__rosidl_generator_c")]
extern "C" {
    fn user_interface__msg__UserInt__init(msg: *mut UserInt) -> bool;
    fn user_interface__msg__UserInt__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<UserInt>, size: usize) -> bool;
    fn user_interface__msg__UserInt__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<UserInt>);
    fn user_interface__msg__UserInt__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<UserInt>, out_seq: *mut rosidl_runtime_rs::Sequence<UserInt>) -> bool;
}

// Corresponds to user_interface__msg__UserInt
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct UserInt {

    // This member is not documented.
    #[allow(missing_docs)]
    pub header: std_msgs::msg::rmw::Header,


    // This member is not documented.
    #[allow(missing_docs)]
    pub user_int: i32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub user_int2: i32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub user_int3: i32,

}



impl Default for UserInt {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !user_interface__msg__UserInt__init(&mut msg as *mut _) {
        panic!("Call to user_interface__msg__UserInt__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for UserInt {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { user_interface__msg__UserInt__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { user_interface__msg__UserInt__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { user_interface__msg__UserInt__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for UserInt {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for UserInt where Self: Sized {
  const TYPE_NAME: &'static str = "user_interface/msg/UserInt";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__user_interface__msg__UserInt() }
  }
}


