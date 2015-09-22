import copy

from . import functions, instance
from .self_constructor import SelfConstructor

JSON_TYPES = {str, int, float, type(None), bool}


class Type(SelfConstructor):
    """
    Implements a simple class interface for trivially JSONable objects.

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
        >>>
        >>> pie == Pie(doc)
        True
    """
    def __new__(cls, *args, **kwargs):
        if len(args) == 1 and len(kwargs) == 0 and isinstance(args[0], dict):
            return cls.from_json(args[0])
        else:
            return super().__new__(cls, *args, **kwargs)

    def __hash__(self):
        return hash(tuple(instance.slots_values(self)))

    def __eq__(self, other):
        if other == None: return False
        try:
            for key in instance.slots_keys(self):
                    if getattr(self, key) != getattr(other, key): return False

            return True
        except KeyError or AttributeError:
            return False

    def __neq__(self, other):
        return not self.__eq__(other)

    def __str__(self): return self.__repr__()

    def __repr__(self):
        return instance.slots_repr(self)

    def to_json(self):
        return {k:functions.to_json(v)
                for k, v in instance.slots_items(self)
                if v is not None}

    def __getstate__(self):
        return self.to_json()

    def __getnewargs__(self):
        return (self.to_json(), )

    @classmethod
    def from_json(cls, doc):
        return cls(**doc)

    _from_json = from_json

JSONable = Type  # For backwards compatibility


class Base(Type):
    """
    Implements a simple JSONable datastructure for abstract classes.

    :Example:
        >>> from jsonable import JSONable, AbstractJSONable
        >>>
        >>> class Bowl(JSONable):
        ...     __slots__ = ('fruit',)
        ...     def initialize(self, fruit):
        ...         self.fruit = [Fruit(f) for f in fruit]
        ...
        >>>
        >>>
        >>> class Fruit(AbstractJSONable):
        ...     __slots__ = ('weight',)
        ...     def initialize(self, weight):
        ...         self.weight = float(weight) # lbs
        ...
        >>>
        >>> class Apple(Fruit):
        ...     __slots__ = ('variety',)
        ...     def initialize(self, weight, variety):
        ...         super().initialize(weight)
        ...         self.variety = str(variety)
        ...
        >>> Fruit.register(Apple)
        >>>
        >>> class Orange(Fruit):
        ...     __slots__ = ('radius',)
        ...     def initialize(self, weight, radius):
        ...         super().initialize(weight)
        ...         self.radius = float(radius) # in
        ...
        >>> Fruit.register(Orange)
        >>>
        >>> orange = Orange(10.1, 2.5)
        >>>
        >>> apple = Apple(9.2, "Honey Crisp")
        >>>
        >>> bowl = Bowl([apple, orange])
        >>>
        >>> doc = bowl.to_json()
        >>>
        >>> bowl == Bowl(doc)
        True
    """
    __slots__ = tuple()

    REGISTERED_SUB_CLASSES = {}
    CLASS_NAME_KEY = "__class__"

    def to_json(self):
        doc = super().to_json()
        doc[self.CLASS_NAME_KEY] = self.__class__.__name__
        return doc

    @classmethod
    def from_json(cls, doc):
        if cls.CLASS_NAME_KEY in doc:
            class_name = doc[cls.CLASS_NAME_KEY]
            if class_name in cls.REGISTERED_SUB_CLASSES:
                SubClass = cls.REGISTERED_SUB_CLASSES[class_name]
            elif class_name == cls.__name__:
                SubClass = cls
            else:
                raise KeyError(str(class_name) +
                               " is not a recognized subclass of " +
                               cls.__name__)

            new_doc = copy.copy(doc)
            del new_doc[cls.CLASS_NAME_KEY]
            return SubClass.from_json(new_doc)
        else:
            return cls._from_json(doc)

    @classmethod
    def get(cls, class_name):
        return cls.REGISTERED_SUB_CLASSES[class_name]

    @classmethod
    def register(cls, SubClass):
        cls.REGISTERED_SUB_CLASSES[SubClass.__name__] = SubClass

AbstractJSONable = Base # For backwards compatibilit
