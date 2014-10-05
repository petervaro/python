#!/usr/bin/python3
# -*- coding: utf8 -*-

# this is a comment
0x12
0o2
0b0010101011110000
1
17256134
.3634
1.
0.12345689
1.e10
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

'some text %(name)s and all the other' % {'name': 'other_text'}

dict(hello=12)

'\x78ff'

r'[a-zA-Z_\]]'
r'[]]'
r'[[]'
r'[\\]]'
r'[\\]'
r'[^\\]'

pattern = r"""
# Capture shebang lines if any
([#]!.*?)*
# Capture opening block
(?P<opening>
    ((?P<line>{})+|({}))
        \s*INFO\s*(?P<pad>.))
    .*? # previous content of comment
# Capture closing block
(?P<closing>
    (?P=pad)\s*INFO\s*
        # if line comment:
        (?(line)
            # capture line closing
            (?P=line)+
        |# else:
            # capture block closing
            ({})))
"""

r'(\()'
r'\this\is\a\path'


import re
s = 'this is ]]]]]] text'
print(re.findall(r'[]]', s))

"hello {}".format("python")

#format("hello {}", 'python')
print(str.format("hello {}", 'python'))

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
'''(?<!\b|$)\d'''

a = r"""(?x)\d +  (?# the integral part)
            \.    (?# the decimal point)
            \d *  (?# some fractional digits)"""

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

def hello0() -> (i for i in range(10)):
    pass

def hello1(world):
    pass

def hello2(world) -> True:
    pass

def hello3(world, you):
    pass

def hello4(world, you) -> (12, 13, 14):
    pass

def hello5(world: None):
    pass

def hello6(world: None) -> True:
    pass

def hello7(world: None, you):
    pass

def hello8(world: None, you) -> (12, 13, 14):
    pass

def hello9(world: [None, 12], hex, help, jelp, huh: [12, 23, 45], huhu, hah):
    pass

def hello10(world: [None, 12]) -> True:
    pass

def hello11(world: None, you: range(1, 10, 2), a):
    pass

def hello12(world: None, you: [(1, 2), (3, 4), (5, 6)]) -> (12, 13, 14):
    pass

def hello13(world):
    pass

def hello14(world, come, on):
    pass

def hello15(world=12):
    pass

def decorator(func):
    return func

@decorator
def hello16(world=(12, 23)):
    pass

def deco(a, b):
    def wrap(func):
        pass
    return wrap

@deco(12**2, b=34)
def hello18(world, come, on=1, you=2):
    pass

def hello19(*args, **kwargs):
    pass

def hello20(world, come, *args, on=1, you=3, **kwargs):
    pass

def hello21(world: True):
    pass

def hello22(world: 0, come: 'on' = True, this: None = None, true: (True,) = True):
    pass

def hello23(world) -> None:
    pass

def hello24(world: 'nice to meet you' = 12, come: 'on you bastard' = 23) -> '':
    pass

def hello25(arg1,      # enable
            arg2,      # multiline
            arg3):     # comments
    pass

def hello26(arg1:'#', arg2='#', arg3:'#'='#'):
    pass

def hello26(arg1:'#',       # enable
            arg2='#',       # multiline
            arg3:'#'='#'):  # comments
    pass

def hello26(arg1:'#',              # enable
            arg2='#',              # multiline
            arg3:'#'='#') -> '#':  # comments
    pass

(lambda e, f, g: e + f + g)
lambda: 12**2
lambda alfa: True if alfa else False
lambda *args, **kwargs: None
lambda a=12, b=23: a+b
lambda a = [(1, 2), (3, 4)], b=[(5, 6)]: zip(a, b)
lambda a,b,c: None

global x
x = 2
def f():
    y = 10
    def ff():
        nonlocal y
        y**2


import math
math.sqrt(4)

from math import sqrt
sqrt(4)


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

def h() -> {i: j for i, j in [(1, 2), (3, 4), (5, 6)]}:
    pass

property
print(h.__annotations__['return'])
