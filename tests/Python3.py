from math import pi as PI
from module import Klass

def class_decorator(cls):
    cls.__call__ = lambda self: print('Cabbage!')
    return cls

@class_decorator
class Class(Klass):

    @property
    def property(self):
        temp, ellipsis = self._property
        return {temp} if temp%0x12f2 else set()
    @property.setter
    def property(self, value):
        try:
            temp = value//0o123
        except TypeError:
            temp = 1.
        def do_something():
            nonlocal temp
            return temp, ...
        self._property = do_something()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("I'm", "alive!", sep='\n')

    def func(self: 'Class', domain: [0b00, PI], opt:bool=True) -> None:
        """ doc string """
        # Comment
        x, y, z = r'[[]', R'[]]', r'[^a-zA-Z_]'

if __name__ == '__main__':
    c = Class()
    c.func(.12)
    c.property = 0b1011101110