import abc
import typing as typ
from collections import namedtuple


PropVal = typ.Union[typ.List[str], typ.Mapping[str, str]]


###############################################################################
#                                   DA Types                                  #
###############################################################################
class DType(abc.ABC):

    def __init__(self, t: typ.Union[type, None] = None) -> None:
        self._origin = t
        self._value = None  # type: typ.Any

    def value(self) -> typ.Any:
        return self._value


class DInt(DType):

    def __init__(self, value: int = 0) -> None:
        DType.__init__(self, int)
        self._value = value

    def __int__(self) -> int:
        return self._value

    def __add__(self, other: typ.Union['DInt', int]) -> 'DInt':
        if isinstance(other, int):
            return DInt(self._value + other)
        else:
            return DInt(self._value + other.value())  # type: ignore

    def __radd__(self, other: typ.Union['DInt', int]) -> 'DInt':
        return self.__add__(other)

    def __eq__(self, o: typ.Union['DInt', int]) -> bool:
        if isinstance(o, int):
            return self._value == o
        else:
            return self._value == o.value()

    def __mul__(self, o: typ.Union['DInt', int]) -> 'DInt':
        if isinstance(o, int):
            return DInt(self._value * o)
        else:
            return DInt(self._value * o.value())

    def __rmul__(self, o) -> 'DInt':
        return self.__mul__(o)

    def __str__(self) -> str:
        return str(self._value)


class DStr(DType):

    def __init__(self, value: str = "") -> None:
        DType.__init__(self, str)
        self._value = value

    def __str__(self) -> str:
        return self._value

    def __eq__(self, o: typ.Union['DStr', str]) -> bool:
        if isinstance(o, str):
            return self._value == o
        else:
            return self._value == o.value()


class DList(DType):

    def __init__(self, value: typ.List = None) -> None:
        DType.__init__(self, list)
        if value is None:
            value = []
        self._value = value

    def __getitem__(self, index: int) -> typ.Any:
        """
        This method no need to do any real operation, it just a description
        that to say get something from DList
        """

    def __setitem__(self, key: int, value: typ.Any) -> None:
        """
        This method no need to do any real operation, it just a description
        that to say set something from DList
        """

    def __eq__(self, o) -> bool:
        return True


class DDict(DType):

    def __init__(self, value: typ.Dict = None) -> None:
        DType.__init__(self, dict)
        if value is None:
            value = {}
        self._value = value

    def __getitem__(self, index: int) -> typ.Any:
        """
        This method no need to do any real operation, it just a description
        that to say get something from DDict
        """

    def __setitem__(self, key: int, value: typ.Any) -> None:
        """
        This method no need to do any real operation, it just a description
        that to say set something from DDict
        """

    def __eq__(self, o) -> bool:
        return True


class DTuple(DType):

    def __init__(self, value: typ.Tuple = None) -> None:
        DType.__init__(self, tuple)
        if value is None:
            value = ()
        self._value = value

    def __getitem__(self, index: int) -> typ.Any:
        """
        This method no need to do any real operation, it just a description
        that to say get something from DTuple
        """


class DNone(DType):

    def __init__(self) -> None:
        DType.__init__(self, None)
        self._value = None

    def __eq__(self, o) -> bool:
        return True


###############################################################################
#                                  Operation                                  #
###############################################################################
# opargs :: typ.Tuple[DType]
opTuple = namedtuple("opTuple", "opcode opargs")
opParameter = typ.List[typ.Tuple[str, typ.Type[DType]]]
opRet = typ.Tuple[str, typ.Type[DType]]


def argsCheck(opargs: typ.List[DType], para: opParameter) -> bool:
    """
    To check that opargs of opTuple is match with opParameter.
    """
    length = len(opargs)
    if length != len(para):
        return False

    for i in range(length):
        if type(opargs[i]) != para[i][1]:
            return False

    return True


def paraMatch(para1: opParameter, para2: opParameter) -> bool:
    """
    Two opParameter is equal iff their types is equal.
    """
    length = len(para1)
    if length != len(para2):
        return False

    # If two parameter's type is equal then
    # these two parameter is equal
    for i in range(length):
        if para1[i][1] != para2[i][1]:
            return False

    return True
