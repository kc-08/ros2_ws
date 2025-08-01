# generated from rosidl_generator_py/resource/_idl.py.em
# with input from fizzbuzz_interfaces:msg/FizzBuzz.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_FizzBuzz(type):
    """Metaclass of message 'FizzBuzz'."""

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
            module = import_type_support('fizzbuzz_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'fizzbuzz_interfaces.msg.FizzBuzz')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__fizz_buzz
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__fizz_buzz
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__fizz_buzz
            cls._TYPE_SUPPORT = module.type_support_msg__msg__fizz_buzz
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__fizz_buzz

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class FizzBuzz(metaclass=Metaclass_FizzBuzz):
    """Message class 'FizzBuzz'."""

    __slots__ = [
        '_fizzbuzz',
        '_fizz_ratio',
        '_buzz_ratio',
        '_fizzbuzz_ratio',
        '_number_total',
    ]

    _fields_and_field_types = {
        'fizzbuzz': 'string',
        'fizz_ratio': 'float',
        'buzz_ratio': 'float',
        'fizzbuzz_ratio': 'float',
        'number_total': 'int32',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.fizzbuzz = kwargs.get('fizzbuzz', str())
        self.fizz_ratio = kwargs.get('fizz_ratio', float())
        self.buzz_ratio = kwargs.get('buzz_ratio', float())
        self.fizzbuzz_ratio = kwargs.get('fizzbuzz_ratio', float())
        self.number_total = kwargs.get('number_total', int())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
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
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.fizzbuzz != other.fizzbuzz:
            return False
        if self.fizz_ratio != other.fizz_ratio:
            return False
        if self.buzz_ratio != other.buzz_ratio:
            return False
        if self.fizzbuzz_ratio != other.fizzbuzz_ratio:
            return False
        if self.number_total != other.number_total:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def fizzbuzz(self):
        """Message field 'fizzbuzz'."""
        return self._fizzbuzz

    @fizzbuzz.setter
    def fizzbuzz(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'fizzbuzz' field must be of type 'str'"
        self._fizzbuzz = value

    @builtins.property
    def fizz_ratio(self):
        """Message field 'fizz_ratio'."""
        return self._fizz_ratio

    @fizz_ratio.setter
    def fizz_ratio(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'fizz_ratio' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'fizz_ratio' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._fizz_ratio = value

    @builtins.property
    def buzz_ratio(self):
        """Message field 'buzz_ratio'."""
        return self._buzz_ratio

    @buzz_ratio.setter
    def buzz_ratio(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'buzz_ratio' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'buzz_ratio' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._buzz_ratio = value

    @builtins.property
    def fizzbuzz_ratio(self):
        """Message field 'fizzbuzz_ratio'."""
        return self._fizzbuzz_ratio

    @fizzbuzz_ratio.setter
    def fizzbuzz_ratio(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'fizzbuzz_ratio' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'fizzbuzz_ratio' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._fizzbuzz_ratio = value

    @builtins.property
    def number_total(self):
        """Message field 'number_total'."""
        return self._number_total

    @number_total.setter
    def number_total(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'number_total' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'number_total' field must be an integer in [-2147483648, 2147483647]"
        self._number_total = value
