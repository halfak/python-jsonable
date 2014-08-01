from nose.tools import eq_

from ..jsonable import JSONable


def test_jsonable():
    
    class Foo(JSONable):
        __slots__ = ('herp', 'derp')
        def initialize(self, herp, derp):
            self.herp = herp
            self.derp = derp
        
    herp = 5
    derp = "test string"
    foo = Foo(herp, derp)
    
    eq_(foo.herp, herp)
    eq_(foo.derp, derp)
    eq_(foo, Foo(foo))
    eq_(foo, Foo(foo.to_json()))
