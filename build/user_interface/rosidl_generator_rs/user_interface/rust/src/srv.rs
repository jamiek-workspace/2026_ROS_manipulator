#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};




// Corresponds to user_interface__srv__AddAndOdd_Request

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
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
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::AddAndOdd_Request::default())
  }
}

impl rosidl_runtime_rs::Message for AddAndOdd_Request {
  type RmwMsg = super::srv::rmw::AddAndOdd_Request;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        inta: msg.inta,
        intb: msg.intb,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      inta: msg.inta,
      intb: msg.intb,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      inta: msg.inta,
      intb: msg.intb,
    }
  }
}


// Corresponds to user_interface__srv__AddAndOdd_Response

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct AddAndOdd_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub sum: i32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub odd: std::string::String,

}



impl Default for AddAndOdd_Response {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::AddAndOdd_Response::default())
  }
}

impl rosidl_runtime_rs::Message for AddAndOdd_Response {
  type RmwMsg = super::srv::rmw::AddAndOdd_Response;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        sum: msg.sum,
        odd: msg.odd.as_str().into(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      sum: msg.sum,
        odd: msg.odd.as_str().into(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      sum: msg.sum,
      odd: msg.odd.to_string(),
    }
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


