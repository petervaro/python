# this is a comment
0x12
0o2
0b0010101011110000
1
17256134
.3634
1.
0.12345689
1.23e10
1.23e+10
1.23e-10
1.23E10
1.23E+10
1.23E-10
10e12
10e+12
10e-12
10E12
10E+12
10E-12
10j
10.j
3.14j
10.j
10j
.001j
1e100j
3.14e-10j
print(.012)
hello12 = .344
hello_12 = 12.

True
False
None
Ellipsis
NotImplemented
[...]
...


r'raw'
u'unicode.'
rB'raw byte' + Br'raw byte'
'\b\r\n\t\v\'\"'
'''hello\x78'''
'hello\x78'
'''\\'''
"hello\x78"
"""khj
"""


r'[a-z]'

r'^hello$'
r'a{4,}b'
r'a+?(?#this is a comment)'

r'(?<!\b|$)\d'

{
    'hello':
    {
        'you':
        {
            'little':
            {
                'somebody':
                (
                    r'x{2}',
                    r'\u78ff'
                )
            }
        }
    }
}

def hello():
    pass

def hello() -> (i for i in range(10)):
    pass

def hello(world):
    pass

def hello(world) -> True:
    pass

def hello(world, you):
    pass

def hello(world, you) -> (12, 13, 14):
    pass

def hello(world: None):
    pass

def hello(world: None) -> True:
    pass

def hello(world: None, you):
    pass

def hello(world: None, you) -> (12, 13, 14):
    pass

def hello(world: [None, 12], hex, help, jelp, huh: [12, 23, 45], huhu, hah):
    pass

def hello(world: [None, 12]) -> True:
    pass

def hello(world: None, you: range(1, 10, 2), a):
    pass

def hello(world: None, you: [(1, 2), (3, 4), (5, 6)]) -> (12, 13, 14):
    pass

def hello(world):
    pass

def hello(world, come, on):
    pass

def hello(world=12):
    pass

def hello(world=(12, 23)):
    pass

def hello(world, come=0, on=1):
    pass

def hello(world, come, on=1, you=2):
    pass

def hello(*args, **kwargs):
    pass

def hello(world, come, *args, on=1, you=3, **kwargs):
    pass

def hello(world: True):
    pass

def hello(world: 0, come: 'on' = True, this: None = None, true: (True,) = True):
    pass

def hello(world) -> None:
    pass

def hello(world: 'nice to meet you' = 12, come: 'on you bastard' = 23) -> '':
    pass

(lambda e, f, g: e + f + g)
lambda: 12**2
lambda alfa: True if alfa else False
lambda *args, **kwargs: None
lambda a=12, b=23: a+b
lambda a = [(1, 2), (3, 4)], b=[(5, 6)]: zip(a,b)

global x
x = 2
def f():
    y = 10
    def ff():
        nonlocal y

import math
from math import sqrt

if x >= 1:
    print()
elif not x:
    print()
else:
    print()

class Hello:
    def __init__(self, other):
        pass
    def testing(self):
        self.a = NotImplemented
    def hahaha(cls, b):
        cls.var = b

class World(object):  # this is some comment
    def __init__(self, other):
        pass
    def testing(self):
        self.a = NotImplemented
    def hahaha(cls, b):
        cls.var = b

class Python(list, Hello, World):
    def __init__(self, other):
        pass
    def testing(self):
        self.a = NotImplemented
    def hahaha(cls, b):
        cls.var = b

class Spam(metaclass=type):
    def __init__(self, other):
        pass
    def testing(self):
        self.a = NotImplemented
    def hahaha(cls, b):
        cls.var = b

class Hey():
    def __init__(self, other):
        pass
    def testing(self):
        self.a = NotImplemented
    def hahaha(cls, b):
        cls.var = b

string = 'abcde'

def mul_str(s: 'string', n: 'multiplier' = 'hello') -> 'doubled each string':
    return ''.join(c*n for c in s)

print(mul_str.__annotations__)

def func(some, arguments, *args, other='keywords', **kwargs):
    pass

def life(*, hello, world):
    print(hello, world)

life(hello='a', world='b')

def h() -> {i:j for i,j in [(1, 2), (3, 4), (5, 6)]}:
    pass

print(h.__annotations__['return'])
