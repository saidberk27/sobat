# generated from rosidl_generator_py/resource/_idl.py.em
# with input from sobat_interfaces:msg/SobatHareket.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_SobatHareket(type):
    """Metaclass of message 'SobatHareket'."""

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
                'sobat_interfaces.msg.SobatHareket')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__sobat_hareket
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__sobat_hareket
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__sobat_hareket
            cls._TYPE_SUPPORT = module.type_support_msg__msg__sobat_hareket
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__sobat_hareket

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class SobatHareket(metaclass=Metaclass_SobatHareket):
    """Message class 'SobatHareket'."""

    __slots__ = [
        '_ileri',
        '_geri',
        '_sag',
        '_sol',
        '_yukari',
        '_asagi',
    ]

    _fields_and_field_types = {
        'ileri': 'boolean',
        'geri': 'boolean',
        'sag': 'boolean',
        'sol': 'boolean',
        'yukari': 'boolean',
        'asagi': 'boolean',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.ileri = kwargs.get('ileri', bool())
        self.geri = kwargs.get('geri', bool())
        self.sag = kwargs.get('sag', bool())
        self.sol = kwargs.get('sol', bool())
        self.yukari = kwargs.get('yukari', bool())
        self.asagi = kwargs.get('asagi', bool())

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
        if self.ileri != other.ileri:
            return False
        if self.geri != other.geri:
            return False
        if self.sag != other.sag:
            return False
        if self.sol != other.sol:
            return False
        if self.yukari != other.yukari:
            return False
        if self.asagi != other.asagi:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @property
    def ileri(self):
        """Message field 'ileri'."""
        return self._ileri

    @ileri.setter
    def ileri(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'ileri' field must be of type 'bool'"
        self._ileri = value

    @property
    def geri(self):
        """Message field 'geri'."""
        return self._geri

    @geri.setter
    def geri(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'geri' field must be of type 'bool'"
        self._geri = value

    @property
    def sag(self):
        """Message field 'sag'."""
        return self._sag

    @sag.setter
    def sag(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'sag' field must be of type 'bool'"
        self._sag = value

    @property
    def sol(self):
        """Message field 'sol'."""
        return self._sol

    @sol.setter
    def sol(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'sol' field must be of type 'bool'"
        self._sol = value

    @property
    def yukari(self):
        """Message field 'yukari'."""
        return self._yukari

    @yukari.setter
    def yukari(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'yukari' field must be of type 'bool'"
        self._yukari = value

    @property
    def asagi(self):
        """Message field 'asagi'."""
        return self._asagi

    @asagi.setter
    def asagi(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'asagi' field must be of type 'bool'"
        self._asagi = value
