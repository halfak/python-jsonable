from nose.tools import eq_

from .. import instance


def test_simple_repr():
    
    eq_(
        instance.simple_repr("Classname", 'foo', 5, herp=[5]),
        "Classname('foo', 5, herp=[5])"
    )
    
    eq_(
        instance.simple_repr("Classname",
                             ordered_kwargs=[('foo', "foo"),
                                             ('five', 5),
                                             ('herp', [5]),
                                             ('derp', 20)]),
        "Classname(foo='foo', five=5, herp=[5], derp=20)"
    )

def test_slots_repr():
    
    class AbstractSlottedItem:
        __slots__ = ('foo', 'five')
        def __init__(self, foo, five):
            self.foo = foo
            self.five = five
        
    
    class SubSlottedItem(AbstractSlottedItem):
        __slots__ = ('herp', 'derp')
        def __init__(self, foo, five, herp, derp):
            super().__init__(foo, five)
            self.herp = herp
            self.derp = derp
        
    
    eq_(
        instance.slots_repr(SubSlottedItem("foo", 5, [5], 20)),
        "SubSlottedItem(foo='foo', five=5, herp=[5], derp=20)"
    )

def test_slots_items():
    
    class AbstractSlottedItem:
        __slots__ = ('foo', 'five')
        def __init__(self, foo, five):
            self.foo = foo
            self.five = five
        

    class SubSlottedItem(AbstractSlottedItem):
        __slots__ = ('herp', 'derp')
        def __init__(self, foo, five, herp, derp):
            super().__init__(foo, five)
            self.herp = herp
            self.derp = derp
        
    
    eq_(
        list(instance.slots_items(SubSlottedItem("foo", 5, [5], 20))),
        [("foo", "foo"), ("five", 5), ("herp", [5]), ("derp", 20)]
    )

def test_slots_keys():
    
    class AbstractSlottedItem:
        __slots__ = ('foo', 'five')
        def __init__(self, foo, five):
            self.foo = foo
            self.five = five
        

    class SubSlottedItem(AbstractSlottedItem):
        __slots__ = ('herp', 'derp')
        def __init__(self, foo, five, herp, derp):
            super().__init__(foo, five)
            self.herp = herp
            self.derp = derp
        
    
    eq_(
        list(instance.slots_keys(SubSlottedItem("foo", 5, [5], 20))),
        ["foo", "five", "herp", "derp"]
    )
