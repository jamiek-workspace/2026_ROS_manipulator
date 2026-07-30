#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};



// Corresponds to robotis_interfaces__msg__HandJoints
/// HandJoints.msg

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct HandJoints {
    /// Standard header for timestamps and frame_id.
    pub header: std_msgs::msg::Header,

    /// Fixed-size array of 21 Point32 structs.
    /// Point32 uses float32 for each coordinate, which is generally
    /// sufficient for non-critical robot localization and saves space
    /// compared to float64 (Point).
    pub joints: [geometry_msgs::msg::Point32; 21],

}



impl Default for HandJoints {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::HandJoints::default())
  }
}

impl rosidl_runtime_rs::Message for HandJoints {
  type RmwMsg = super::msg::rmw::HandJoints;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Owned(msg.header)).into_owned(),
        joints: msg.joints
          .map(|elem| geometry_msgs::msg::Point32::into_rmw_message(std::borrow::Cow::Owned(elem)).into_owned()),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Borrowed(&msg.header)).into_owned(),
        joints: msg.joints
          .iter()
          .map(|elem| geometry_msgs::msg::Point32::into_rmw_message(std::borrow::Cow::Borrowed(elem)).into_owned())
          .collect::<Vec<_>>()
          .try_into()
          .unwrap(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      header: std_msgs::msg::Header::from_rmw_message(msg.header),
      joints: msg.joints
        .map(geometry_msgs::msg::Point32::from_rmw_message),
    }
  }
}


// Corresponds to robotis_interfaces__msg__HandPressures
/// Pressure readings for tactile sensors on a ROBOTIS Hand.

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct HandPressures {
    /// Standard header for timestamps and frame_id.
    pub header: std_msgs::msg::Header,

    /// Logical hand identifier, for example "left" or "right".
    pub hand_name: std::string::String,

    /// Array of tactile sensor readings.
    pub sensors: Vec<super::msg::TactileSensor>,

}



impl Default for HandPressures {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::HandPressures::default())
  }
}

impl rosidl_runtime_rs::Message for HandPressures {
  type RmwMsg = super::msg::rmw::HandPressures;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Owned(msg.header)).into_owned(),
        hand_name: msg.hand_name.as_str().into(),
        sensors: msg.sensors
          .into_iter()
          .map(|elem| super::msg::TactileSensor::into_rmw_message(std::borrow::Cow::Owned(elem)).into_owned())
          .collect(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Borrowed(&msg.header)).into_owned(),
        hand_name: msg.hand_name.as_str().into(),
        sensors: msg.sensors
          .iter()
          .map(|elem| super::msg::TactileSensor::into_rmw_message(std::borrow::Cow::Borrowed(elem)).into_owned())
          .collect(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      header: std_msgs::msg::Header::from_rmw_message(msg.header),
      hand_name: msg.hand_name.to_string(),
      sensors: msg.sensors
          .into_iter()
          .map(super::msg::TactileSensor::from_rmw_message)
          .collect(),
    }
  }
}


// Corresponds to robotis_interfaces__msg__MoveL
/// Target end-effector pose for the linear move command.

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct MoveL {

    // This member is not documented.
    #[allow(missing_docs)]
    pub pose: geometry_msgs::msg::PoseStamped,

    /// Desired time to reach the target pose from the current pose.
    pub time_from_start: builtin_interfaces::msg::Duration,

}



impl Default for MoveL {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::MoveL::default())
  }
}

impl rosidl_runtime_rs::Message for MoveL {
  type RmwMsg = super::msg::rmw::MoveL;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        pose: geometry_msgs::msg::PoseStamped::into_rmw_message(std::borrow::Cow::Owned(msg.pose)).into_owned(),
        time_from_start: builtin_interfaces::msg::Duration::into_rmw_message(std::borrow::Cow::Owned(msg.time_from_start)).into_owned(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        pose: geometry_msgs::msg::PoseStamped::into_rmw_message(std::borrow::Cow::Borrowed(&msg.pose)).into_owned(),
        time_from_start: builtin_interfaces::msg::Duration::into_rmw_message(std::borrow::Cow::Borrowed(&msg.time_from_start)).into_owned(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      pose: geometry_msgs::msg::PoseStamped::from_rmw_message(msg.pose),
      time_from_start: builtin_interfaces::msg::Duration::from_rmw_message(msg.time_from_start),
    }
  }
}


// Corresponds to robotis_interfaces__msg__TactileSensor
/// TactileSensor.msg

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct TactileSensor {
    /// Name of the tactile sensor source.
    pub sensor_name: std::string::String,

    /// Present pressure values (0-255) from the tactile sensor (3x3 grid base)
    /// Pressure indices are ordered from top to bottom, and from left to right within each row.
    pub pressure_names: [std::string::String; 9],


    // This member is not documented.
    #[allow(missing_docs)]
    pub pressure_values: [u8; 9],

}



impl Default for TactileSensor {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::TactileSensor::default())
  }
}

impl rosidl_runtime_rs::Message for TactileSensor {
  type RmwMsg = super::msg::rmw::TactileSensor;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        sensor_name: msg.sensor_name.as_str().into(),
        pressure_names: msg.pressure_names
          .map(|elem| elem.as_str().into()),
        pressure_values: msg.pressure_values,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        sensor_name: msg.sensor_name.as_str().into(),
        pressure_names: msg.pressure_names
          .iter()
          .map(|elem| elem.as_str().into())
          .collect::<Vec<_>>()
          .try_into()
          .unwrap(),
        pressure_values: msg.pressure_values,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      sensor_name: msg.sensor_name.to_string(),
      pressure_names: msg.pressure_names
        .map(|elem| elem.to_string()),
      pressure_values: msg.pressure_values,
    }
  }
}


