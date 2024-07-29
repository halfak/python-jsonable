from collections import deque

from ..functions import to_json
from ..type import Type


def test_to_json():

    # Basic JSON types
    assert to_json(5) == 5
    assert to_json(5.5) == 5.5
    assert to_json("five") == "five"
    assert to_json(True) == True
    assert to_json(None) == None

    # Iterable types
    assert to_json(["foo", 5.5]) == ["foo", 5.5]
    assert to_json(("foo", 5.5)) == ["foo", 5.5]
    assert set(to_json({"foo", 5.5})) == {"foo", 5.5}
    assert to_json(deque(["foo", 5.5])) == ["foo", 5.5]

    # Dict type
    assert to_json({"foo": 5.5}) == {"foo": 5.5}

    # jsonable.Type
    class Foo(Type):
        __slots__ = ('bar',)

        def initialize(self, bar):
            self.bar = int(bar)

    foo = Foo(5)
    assert to_json(foo) == foo.to_json()
