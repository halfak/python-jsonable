from collections import deque

from nose.tools import eq_

from ..functions import to_json
from ..type import Type


def test_to_json():

    # Basic JSON types
    eq_(to_json(5), 5)
    eq_(to_json(5.5), 5.5)
    eq_(to_json("five"), "five")
    eq_(to_json(True), True)
    eq_(to_json(None), None)

    # Iterable types
    eq_(to_json(["foo", 5.5]), ["foo", 5.5])
    eq_(to_json(("foo", 5.5)), ["foo", 5.5])
    eq_(set(to_json({"foo", 5.5})), {"foo", 5.5})
    eq_(to_json(deque(["foo", 5.5])), ["foo", 5.5])

    # Dict type
    eq_(to_json({"foo": 5.5}), {"foo": 5.5})

    # jsonable.Type
    class Foo(Type):
        __slots__ = ('bar',)

        def initialize(self, bar):
            self.bar = int(bar)

    foo = Foo(5)
    eq_(to_json(foo), foo.to_json())
