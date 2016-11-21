from module import Klass
from math   import pi as PI
from matrix import MAT1, MAT2

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
        def do_something(m):
            nonlocal temp
            return temp, ...

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("I'm", "alive!", sep='\n')

    async def func(self     : 'Class',
                   callback : 'callable'
                   domain   : [0b00, PI],
                   opt      : bool=True) -> None:

        """ doc string """

        self._property = await callback(MAT1 @ MAT2)

        # Highlighted regular expression
        # syntax:re
        r'''(?<!\d+)
            \s*?\W # multiline regex comment
            \d$'''
        x, y, z, path = r'[[]', R'[]]', r'[^a-zA-Z_]', r'C:\Users\Wilson\new'
        # end:re

        # Unhighlighted regular expression
        r'''(?<!\d+)
            \s*?\W # regex comment
            \d$'''
        x, y, z, path = r'[[]', R'[]]', r'[^a-zA-Z_]', r'C:\Users\Wilson\new'

        # syntax:fmt
        '{.property:{fill}>+#023,.34} => {:0>16b} {{{!r}}}' # highlighted
        # end:fmt

        '{.property:{fill}>+#023,.34} => {:0>16b} {{{!r}}}' # not highlighted

        # syntax:tmp
        '$$ and $identifier and ${identifier}' # highlighted
        # end:tmp

        '$$ and $identifier and ${identifier}' # not highlighted

        # syntax:old
        '%d %f %#0-23X' # highlighted
        # end:old

        '%d %f %#0-23X' # not highlighted

        # Format string
        f'{self.method(x, y, z, {"a": 97})!a:>>12} => {u:0>16b} {{{v!r}}}'


if __name__ == '__main__':
    c = Class()
    c.func(.12)
    c.property = 0b1011101110
