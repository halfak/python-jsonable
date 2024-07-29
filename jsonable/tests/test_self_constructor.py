from ..self_constructor import SelfConstructor


def test_self_construction():
    
    class Foo(SelfConstructor):
        
        def initialize(self, herp, derp):
            self.herp = herp
            self.derp = derp
        
    herp = 5
    derp = "foo"
    foo = Foo(herp, derp)
    
    assert foo.herp == herp
    assert foo.derp == derp
    
    assert foo == Foo(foo)
