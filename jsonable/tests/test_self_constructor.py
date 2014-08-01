from nose.tools import eq_

from ..self_constructor import SelfConstructor


def test_self_construction():
    
    class Foo(SelfConstructor):
        
        def initialize(self, herp, derp):
            self.herp = herp
            self.derp = derp
        
    herp = 5
    derp = "foo"
    foo = Foo(herp, derp)
    
    eq_(foo.herp, herp)
    eq_(foo.derp, derp)
    
    eq_(foo, Foo(foo))
