#!/usr/bin/env python
# (c) 2018 CJ Associates
#
import json
from datetime import date
from singledispatch import singledispatch


class Parrot():
    def __init__(self, name, color):
        self._name = name
        self._color = color

    @property
    def name(self):
        return self._name

    @property
    def color(self):
        return self._color

parrots = [
    Parrot('Polly', 'green'),
    Parrot('Peggy', 'blue'),
    Parrot('Roger', 'red'),
]


data = {
    'spam': [1,2,3],
    'ham': ('a', 'b', 'c'),
    'date': date(2014, 8, 1),
    'parrots': parrots,
}

@singledispatch
def encode(obj):
    return obj


@encode.register(date)
def encode_date(date_obj):
    return date_obj.timetuple()

@encode.register(Parrot)
def encode_parrot(parrot_obj):
        return {'name': parrot_obj.name, 'color': parrot_obj.color}

# register other encoding functions here

print(json.dumps(data, default=encode, indent=4))

