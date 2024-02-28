# generated from rosidl_generator_py/resource/_idl.py.em
# with input from sobat_interfaces:msg/MesafeSensor.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_MesafeSensor(type):
    """Metaclass of message 'MesafeSensor'."""

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
            module = import_type_support('sobat_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'sobat_interfaces.msg.MesafeSensor')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__mesafe_sensor
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__mesafe_sensor
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__mesafe_sensor
            cls._TYPE_SUPPORT = module.type_support_msg__msg__mesafe_sensor
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__mesafe_sensor

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class MesafeSensor(metaclass=Metaclass_MesafeSensor):
    """Message class 'MesafeSensor'."""

    __slots__ = [
        '_mesafe_sensor1',
        '_mesafe_sensor2',
        '_mesafe_sensor3',
        '_mesafe_sensor4',
        '_mesafe_sensor5',
    ]

    _fields_and_field_types = {
        'mesafe_sensor1': 'float',
        'mesafe_sensor2': 'float',
        'mesafe_sensor3': 'float',
        'mesafe_sensor4': 'float',
        'mesafe_sensor5': 'float',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.mesafe_sensor1 = kwargs.get('mesafe_sensor1', float())
        self.mesafe_sensor2 = kwargs.get('mesafe_sensor2', float())
        self.mesafe_sensor3 = kwargs.get('mesafe_sensor3', float())
        self.mesafe_sensor4 = kwargs.get('mesafe_sensor4', float())
        self.mesafe_sensor5 = kwargs.get('mesafe_sensor5', float())

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
        if self.mesafe_sensor1 != other.mesafe_sensor1:
            return False
        if self.mesafe_sensor2 != other.mesafe_sensor2:
            return False
        if self.mesafe_sensor3 != other.mesafe_sensor3:
            return False
        if self.mesafe_sensor4 != other.mesafe_sensor4:
            return False
        if self.mesafe_sensor5 != other.mesafe_sensor5:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @property
    def mesafe_sensor1(self):
        """Message field 'mesafe_sensor1'."""
        return self._mesafe_sensor1

    @mesafe_sensor1.setter
    def mesafe_sensor1(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'mesafe_sensor1' field must be of type 'float'"
        self._mesafe_sensor1 = value

    @property
    def mesafe_sensor2(self):
        """Message field 'mesafe_sensor2'."""
        return self._mesafe_sensor2

    @mesafe_sensor2.setter
    def mesafe_sensor2(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'mesafe_sensor2' field must be of type 'float'"
        self._mesafe_sensor2 = value

    @property
    def mesafe_sensor3(self):
        """Message field 'mesafe_sensor3'."""
        return self._mesafe_sensor3

    @mesafe_sensor3.setter
    def mesafe_sensor3(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'mesafe_sensor3' field must be of type 'float'"
        self._mesafe_sensor3 = value

    @property
    def mesafe_sensor4(self):
        """Message field 'mesafe_sensor4'."""
        return self._mesafe_sensor4

    @mesafe_sensor4.setter
    def mesafe_sensor4(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'mesafe_sensor4' field must be of type 'float'"
        self._mesafe_sensor4 = value

    @property
    def mesafe_sensor5(self):
        """Message field 'mesafe_sensor5'."""
        return self._mesafe_sensor5

    @mesafe_sensor5.setter
    def mesafe_sensor5(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'mesafe_sensor5' field must be of type 'float'"
        self._mesafe_sensor5 = value
