from . import instance
from .self_constructor import SelfConstructor

JSON_TYPES = {str, int, float, type(None)}

class JSONable(SelfConstructor):
    def __new__(cls, *args, **kwargs):
        if len(args) == 1 and len(kwargs) == 0 and isinstance(args[0], dict):
            return cls.from_json(args[0])
        else:
            return super().__new__(cls, *args, **kwargs)
    
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
        return util.instance.slots_repr(self)
    
    def to_json(self):
        return {k:self._to_json(v) for k, v in instance.slots_items(self)}
    
    @classmethod
    def _to_json(cls, value):
        
        if type(value) in JSON_TYPES:
            return value
        elif hasattr(value, "to_json"):
            return value.to_json()
        elif isinstance(value, list):
            return [cls._to_json(v) for v in value]
        elif isinstance(value, dict):
            return {str(k):cls._to_json(v) for k,v in value.items()}
        else:
            raise TypeError("{0} is not json serializable.".format(type(value)))

    @classmethod
    def from_json(cls, doc):
        return cls(**doc)
