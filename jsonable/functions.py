from collections import deque

JSON_TYPES = {str, int, float, type(None), bool}


def to_json(value):
    """
    Converts a value to a jsonable type.
    """
    if type(value) in JSON_TYPES:
        return value
    elif hasattr(value, "to_json"):
        return value.to_json()
    elif isinstance(value, list) or isinstance(value, set) or \
            isinstance(value, deque) or isinstance(value, tuple):
        return [to_json(v) for v in value]
    elif isinstance(value, dict):
        return {str(k): to_json(v) for k, v in value.items()}
    else:
        raise TypeError("{0} is not json serializable.".format(type(value)))
