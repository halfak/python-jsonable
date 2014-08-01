JSON-able data types
====================

This library provides and abstract base class ``JSONable`` which enables easy definition of trivially JSON-able python objects.

* **Installation:** ``pip install jsonable``

:Example:
    
    >>> from jsonable import JSONable
    >>>
    >>>
    >>> class Fruit(JSONable):
    ...     __slots__ = ('type', 'weight')
    ...
    ...     def initialize(self, type, weight):
    ...         self.type   = str(type)
    ...         self.weight = float(weight)
    ...
    >>> class Pie(JSONable):
    ...     __slots__ = ('fruit',)
    ...
    ...     def initialize(self, fruit):
    ...         self.fruit = [Fruit(f) for f in fruit]
    ...
    ...
    >>> pie = Pie([Fruit('apple', 10.3), Fruit('cherry', 2)])
    >>>
    >>> doc = pie.to_json()
    >>> doc
    {'fruit': [{'weight': 10.3, 'type': 'apple'}, {'weight': 2.0, 'type': 'cherry'}]}
    >>>
    >>> pie == Pie(doc)
    True
