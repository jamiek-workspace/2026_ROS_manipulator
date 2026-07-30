#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};



#[link(name = "user_interface__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__user_interface__srv__AddAndOdd_Request() -> *const std::ffi::c_void;
}

#[link(name = "user_interface__rosidl_generator_c")]
extern "C" {
    fn user_interface__srv__AddAndOdd_Request__init(msg: *mut AddAndOdd_Request) -> bool;
    fn user_interface__srv__AddAndOdd_Request__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<AddAndOdd_Request>, size: usize) -> bool;
    fn user_interface__srv__AddAndOdd_Request__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<AddAndOdd_Request>);
    fn user_interface__srv__AddAndOdd_Request__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<AddAndOdd_Request>, out_seq: *mut rosidl_runtime_rs::Sequence<AddAndOdd_Request>) -> bool;
}

// Corresponds to user_interface__srv__AddAndOdd_Request
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct AddAndOdd_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub inta: i32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub intb: i32,

}



impl Default for AddAndOdd_Request {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !user_interface__srv__AddAndOdd_Request__init(&mut msg as *mut _) {
        panic!("Call to user_interface__srv__AddAndOdd_Request__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for AddAndOdd_Request {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { user_interface__srv__AddAndOdd_Request__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { user_interface__srv__AddAndOdd_Request__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { user_interface__srv__AddAndOdd_Request__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for AddAndOdd_Request {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for AddAndOdd_Request where Self: Sized {
  const TYPE_NAME: &'static str = "user_interface/srv/AddAndOdd_Request";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__user_interface__srv__AddAndOdd_Request() }
  }
}


#[link(name = "user_interface__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__user_interface__srv__AddAndOdd_Response() -> *const std::ffi::c_void;
}

#[link(name = "user_interface__rosidl_generator_c")]
extern "C" {
    fn user_interface__srv__AddAndOdd_Response__init(msg: *mut AddAndOdd_Response) -> bool;
    fn user_interface__srv__AddAndOdd_Response__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<AddAndOdd_Response>, size: usize) -> bool;
    fn user_interface__srv__AddAndOdd_Response__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<AddAndOdd_Response>);
    fn user_interface__srv__AddAndOdd_Response__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<AddAndOdd_Response>, out_seq: *mut rosidl_runtime_rs::Sequence<AddAndOdd_Response>) -> bool;
}

// Corresponds to user_interface__srv__AddAndOdd_Response
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct AddAndOdd_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub sum: i32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub odd: rosidl_runtime_rs::String,

}



impl Default for AddAndOdd_Response {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !user_interface__srv__AddAndOdd_Response__init(&mut msg as *mut _) {
        panic!("Call to user_interface__srv__AddAndOdd_Response__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for AddAndOdd_Response {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { user_interface__srv__AddAndOdd_Response__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { user_interface__srv__AddAndOdd_Response__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { user_interface__srv__AddAndOdd_Response__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for AddAndOdd_Response {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for AddAndOdd_Response where Self: Sized {
  const TYPE_NAME: &'static str = "user_interface/srv/AddAndOdd_Response";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__user_interface__srv__AddAndOdd_Response() }
  }
}






#[link(name = "user_interface__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_service_type_support_handle__user_interface__srv__AddAndOdd() -> *const std::ffi::c_void;
}

// Corresponds to user_interface__srv__AddAndOdd
#[allow(missing_docs, non_camel_case_types)]
pub struct AddAndOdd;

impl rosidl_runtime_rs::Service for AddAndOdd {
    type Request = AddAndOdd_Request;
    type Response = AddAndOdd_Response;

    fn get_type_support() -> *const std::ffi::c_void {
        // SAFETY: No preconditions for this function.
        unsafe { rosidl_typesupport_c__get_service_type_support_handle__user_interface__srv__AddAndOdd() }
    }
}


