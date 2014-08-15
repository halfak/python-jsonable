from . import instance


class SelfConstructor:
    
    def __new__(cls, *args, **kwargs):
        
        if len(args) == 1 and len(kwargs) == 0:
            if isinstance(args[0], cls):
                inst = args[0]
            else:
                inst = super().__new__(cls)
                inst.initialize(args[0])
        else:
            inst = super().__new__(cls)
            inst.initialize(*args, **kwargs)
        
        return inst
    
    def __init__(self, *args, **kwargs): pass
    
    def initialize(self, *args, **kwargs): raise NotImplementedError()
