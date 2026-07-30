# generated from rosidl_generator_py/resource/_idl.py.em
# with input from user_interface:srv/AddAndOdd.idl
# generated code does not contain a copyright notice

# This is being done at the module level and not on the instance level to avoid looking
# for the same variable multiple times on each instance. This variable is not supposed to
# change during runtime so it makes sense to only look for it once.
from os import getenv

ros_python_check_fields = getenv('ROS_PYTHON_CHECK_FIELDS', default='')


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_AddAndOdd_Request(type):
    """Metaclass of message 'AddAndOdd_Request'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('user_interface')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'user_interface.srv.AddAndOdd_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__add_and_odd__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__add_and_odd__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__add_and_odd__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__add_and_odd__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__add_and_odd__request

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class AddAndOdd_Request(metaclass=Metaclass_AddAndOdd_Request):
    """Message class 'AddAndOdd_Request'."""

    __slots__ = [
        '_inta',
        '_intb',
        '_check_fields',
    ]

    _fields_and_field_types = {
        'inta': 'int32',
        'intb': 'int32',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        if 'check_fields' in kwargs:
            self._check_fields = kwargs['check_fields']
        else:
            self._check_fields = ros_python_check_fields == '1'
        if self._check_fields:
            assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
                'Invalid arguments passed to constructor: %s' % \
                ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.inta = kwargs.get('inta', int())
        self.intb = kwargs.get('intb', int())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.get_fields_and_field_types().keys(), self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    if self._check_fields:
                        assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.inta != other.inta:
            return False
        if self.intb != other.intb:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def inta(self):
        """Message field 'inta'."""
        return self._inta

    @inta.setter
    def inta(self, value):
        if self._check_fields:
            assert \
                isinstance(value, int), \
                "The 'inta' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'inta' field must be an integer in [-2147483648, 2147483647]"
        self._inta = value

    @builtins.property
    def intb(self):
        """Message field 'intb'."""
        return self._intb

    @intb.setter
    def intb(self, value):
        if self._check_fields:
            assert \
                isinstance(value, int), \
                "The 'intb' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'intb' field must be an integer in [-2147483648, 2147483647]"
        self._intb = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_AddAndOdd_Response(type):
    """Metaclass of message 'AddAndOdd_Response'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('user_interface')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'user_interface.srv.AddAndOdd_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__add_and_odd__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__add_and_odd__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__add_and_odd__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__add_and_odd__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__add_and_odd__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class AddAndOdd_Response(metaclass=Metaclass_AddAndOdd_Response):
    """Message class 'AddAndOdd_Response'."""

    __slots__ = [
        '_sum',
        '_odd',
        '_check_fields',
    ]

    _fields_and_field_types = {
        'sum': 'int32',
        'odd': 'string',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, **kwargs):
        if 'check_fields' in kwargs:
            self._check_fields = kwargs['check_fields']
        else:
            self._check_fields = ros_python_check_fields == '1'
        if self._check_fields:
            assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
                'Invalid arguments passed to constructor: %s' % \
                ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.sum = kwargs.get('sum', int())
        self.odd = kwargs.get('odd', str())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.get_fields_and_field_types().keys(), self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    if self._check_fields:
                        assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.sum != other.sum:
            return False
        if self.odd != other.odd:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property  # noqa: A003
    def sum(self):  # noqa: A003
        """Message field 'sum'."""
        return self._sum

    @sum.setter  # noqa: A003
    def sum(self, value):  # noqa: A003
        if self._check_fields:
            assert \
                isinstance(value, int), \
                "The 'sum' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'sum' field must be an integer in [-2147483648, 2147483647]"
        self._sum = value

    @builtins.property
    def odd(self):
        """Message field 'odd'."""
        return self._odd

    @odd.setter
    def odd(self, value):
        if self._check_fields:
            assert \
                isinstance(value, str), \
                "The 'odd' field must be of type 'str'"
        self._odd = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_AddAndOdd_Event(type):
    """Metaclass of message 'AddAndOdd_Event'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('user_interface')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'user_interface.srv.AddAndOdd_Event')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__add_and_odd__event
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__add_and_odd__event
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__add_and_odd__event
            cls._TYPE_SUPPORT = module.type_support_msg__srv__add_and_odd__event
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__add_and_odd__event

            from service_msgs.msg import ServiceEventInfo
            if ServiceEventInfo.__class__._TYPE_SUPPORT is None:
                ServiceEventInfo.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class AddAndOdd_Event(metaclass=Metaclass_AddAndOdd_Event):
    """Message class 'AddAndOdd_Event'."""

    __slots__ = [
        '_info',
        '_request',
        '_response',
        '_check_fields',
    ]

    _fields_and_field_types = {
        'info': 'service_msgs/ServiceEventInfo',
        'request': 'sequence<user_interface/AddAndOdd_Request, 1>',
        'response': 'sequence<user_interface/AddAndOdd_Response, 1>',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['service_msgs', 'msg'], 'ServiceEventInfo'),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.NamespacedType(['user_interface', 'srv'], 'AddAndOdd_Request'), 1),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.NamespacedType(['user_interface', 'srv'], 'AddAndOdd_Response'), 1),  # noqa: E501
    )

    def __init__(self, **kwargs):
        if 'check_fields' in kwargs:
            self._check_fields = kwargs['check_fields']
        else:
            self._check_fields = ros_python_check_fields == '1'
        if self._check_fields:
            assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
                'Invalid arguments passed to constructor: %s' % \
                ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from service_msgs.msg import ServiceEventInfo
        self.info = kwargs.get('info', ServiceEventInfo())
        self.request = kwargs.get('request', [])
        self.response = kwargs.get('response', [])

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.get_fields_and_field_types().keys(), self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    if self._check_fields:
                        assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.info != other.info:
            return False
        if self.request != other.request:
            return False
        if self.response != other.response:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def info(self):
        """Message field 'info'."""
        return self._info

    @info.setter
    def info(self, value):
        if self._check_fields:
            from service_msgs.msg import ServiceEventInfo
            assert \
                isinstance(value, ServiceEventInfo), \
                "The 'info' field must be a sub message of type 'ServiceEventInfo'"
        self._info = value

    @builtins.property
    def request(self):
        """Message field 'request'."""
        return self._request

    @request.setter
    def request(self, value):
        if self._check_fields:
            from user_interface.srv import AddAndOdd_Request
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 len(value) <= 1 and
                 all(isinstance(v, AddAndOdd_Request) for v in value) and
                 True), \
                "The 'request' field must be a set or sequence with length <= 1 and each value of type 'AddAndOdd_Request'"
        self._request = value

    @builtins.property
    def response(self):
        """Message field 'response'."""
        return self._response

    @response.setter
    def response(self, value):
        if self._check_fields:
            from user_interface.srv import AddAndOdd_Response
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 len(value) <= 1 and
                 all(isinstance(v, AddAndOdd_Response) for v in value) and
                 True), \
                "The 'response' field must be a set or sequence with length <= 1 and each value of type 'AddAndOdd_Response'"
        self._response = value


class Metaclass_AddAndOdd(type):
    """Metaclass of service 'AddAndOdd'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('user_interface')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'user_interface.srv.AddAndOdd')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__add_and_odd

            from user_interface.srv import _add_and_odd
            if _add_and_odd.Metaclass_AddAndOdd_Request._TYPE_SUPPORT is None:
                _add_and_odd.Metaclass_AddAndOdd_Request.__import_type_support__()
            if _add_and_odd.Metaclass_AddAndOdd_Response._TYPE_SUPPORT is None:
                _add_and_odd.Metaclass_AddAndOdd_Response.__import_type_support__()
            if _add_and_odd.Metaclass_AddAndOdd_Event._TYPE_SUPPORT is None:
                _add_and_odd.Metaclass_AddAndOdd_Event.__import_type_support__()


class AddAndOdd(metaclass=Metaclass_AddAndOdd):
    from user_interface.srv._add_and_odd import AddAndOdd_Request as Request
    from user_interface.srv._add_and_odd import AddAndOdd_Response as Response
    from user_interface.srv._add_and_odd import AddAndOdd_Event as Event

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
