import inspect
from itertools import chain


def simple_repr(class_name, *args, ordered_kwargs=None, **kwargs):
    class_name = str(class_name)
    ordered_kwargs = ordered_kwargs or []
    
    arguments = [repr(arg) for arg in args]
    arguments.extend("{0}={1}".format(k, repr(v)) for k, v in ordered_kwargs)
    arguments.extend("{0}={1}".format(k, repr(v)) for k, v in kwargs.items())
    
    return "{0}({1})".format(class_name, ", ".join(arguments))

def unique(l):
    seen = set()
    for i in l:
        if i not in seen:
            yield i
            seen.add(i)

def slots_repr(instance):
    
    return simple_repr(
        instance.__class__.__name__,
        ordered_kwargs = slots_items(instance)
    )

def slots_items(instance):
    for key in slots_keys(instance):
        yield key, getattr(instance, key)

def slots_values(instance):
    for key in slots_keys(instance):
        yield getattr(instance, key)

def slots_keys(instance):
    cls = instance.__class__
    
    return unique(chain(*(getattr(cls, '__slots__', [])
                     for cls in reversed(instance.__class__.__mro__))))
