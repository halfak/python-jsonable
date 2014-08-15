import pickle

from nose.tools import eq_

from ..jsonable import AbstractJSONable, JSONable


class ExampleJSONable(JSONable):
    __slots__ = ('foo', 'bar')
    def initialize(self, foo, bar):
        self.foo = foo
        self.bar = bar

def test_construction_and_variables():
    
    class Bar(JSONable):
        __slots__ = ('subherp', 'subderp')
        def initialize(self, subherp, subderp):
            self.subherp = subherp
            self.subderp = subderp
    
    class Foo(JSONable):
        __slots__ = ('herp', 'bars')
        def initialize(self, herp, bars):
            self.herp = herp
            self.bars = list(Bar(b) for b in bars)
        
    herp = 5
    bars = [Bar("string", 334.34), Bar(False, {"derp": 3.1})]
    foo = Foo(herp, bars)
    
    eq_(foo.herp, herp)
    eq_(foo.bars, bars)
    eq_(foo, Foo(foo))
    eq_(foo, Foo(foo.to_json()))
    

def test_pickle():
    bar = ExampleJSONable("wat", "herp")

    eq_(bar, pickle.loads(pickle.dumps(bar)))


def test_repr():
    
    class Bar(JSONable):
        __slots__ = ('subherp', 'subderp')
        def initialize(self, subherp, subderp):
            self.subherp = subherp
            self.subderp = subderp
        
    
    bar = Bar(1, "two")
    eq_(
        repr(bar),
        "Bar(subherp=1, subderp='two')"
    )

def test_abstract_construction_and_variables():
    
    class Bowl(JSONable):
        __slots__ = ('fruit',)
        def initialize(self, fruit):
            self.fruit = [Fruit(f) for f in fruit]
        
    
    
    class Fruit(AbstractJSONable):
        __slots__ = ('weight',)
        def initialize(self, weight):
            self.weight = float(weight) # lbs
            
    
    class Apple(Fruit):
        __slots__ = ('variety',)
        def initialize(self, weight, variety):
            super().initialize(weight)
            self.variety = str(variety)
        
    
    class Orange(Fruit):
        __slots__ = ('radius',)
        def initialize(self, weight, radius):
            super().initialize(weight)
            self.radius = float(radius) # in
            
        
    orange = Orange(10.1, 2.5)
    apple = Apple(9.2, "Honey Crisp")
    
    bowl = Bowl([apple, orange])
    print(bowl.to_json())
    
    
    fruit = Fruit(21.1)
    eq_(fruit, Fruit(fruit.to_json()))
