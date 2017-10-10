# Python >= 3.5
from typing import Dict, NamedTuple


class TaskMeta(type):
    def __new__(mcl, name, bases, dict_):
        if "__fields__" in dict_:
            base_namedtuple = NamedTuple(name, dict_["__fields__"])
            dict_["__slots__"] = []
            bases = bases + (base_namedtuple,)
        return super().__new__(mcl, name, bases, dict_)


class BaseStruct(metaclass=TaskMeta):
    def as_dict(self) -> Dict:
        return self._asdict()

    @classmethod
    def from_dict(cls, data: Dict):
        return cls(**data)


class Person(BaseStruct):
    __fields__ = [
        ('name', str),
        ('age', int),
    ]


guido = Person.from_dict({
    'name': 'Guido',
    'age': 61,
})


print(guido)
