import json


class BaseObject:
    def __init__(self, data={}):
        if data:
            kwargs = data
            for k in kwargs:
                self.__setattr__(k, kwargs[k])

    def __to_dict__(self):
        obj = {}
        keys = dir(self)
        for key in keys:
            if not key.startswith('__'):
                value = self.__getattribute__(key)
                if value is not None:
                    if isinstance(value, str) or isinstance(value, int) or isinstance(value, dict) or isinstance(value, list) or isinstance(value, float) or isinstance(value, bool):
                        obj[key] = value
                    else:
                        obj[key] = value.__to_dict__()

        return obj

    def __to_json__(self):
        return json.dumps(self.__to_dict__())
