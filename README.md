# Python and Cython language bundles

This package is about language related bundles for Python 3.3+ & Cython 0.19.1+

### Python 3.3 and Syntax Highlighter

A good syntax highlighter should be as great help for the developer as the
auto-complete popup or a linter in a text-editor.
Unfortunately for TextMate and SublimeText the only available syntax-highlighter
`.tmLanguage` file is pretty old, and only supports Python 2.x -- with a lot of
mistakes inside it.

Therefore I implemented a new syntax definition from scratch, but not in JSON or
XML, but as a Python dictionary, which enables a better syntax highlighted regex
editiong without the unnecessary double escaping and can be commented -- which
comments are not going to be inside the language file and the whole data is more
reuseable and dynamic than ever before.

### Cython support

Cython syntax highlighter definitions also lack of updated, well working syntax
definitions, so I also solved that problem, with extending the Python definition
file with the additional syntax notations.
So this new Cython definition is 100% compatible with the newest Python syntaxes
and also supports all the Cython notations, since it is literally a superset of
the Python language defintion.

### The new is better

It is shorter, and faster with less redundant and duplicated information in it,
and also easier to maintain, to edit, or to convert it to other formats.

### Added/Modified

- Added better number highlight:
	- all types of floating point notations
	- all types of complex number notations
	- new types of binary and octal number notations
- Extended constant support:
	- Ellipsis `...` notation added
- Declaration extended:
	- `nonlocal` added
- Exstatements, not functions (like `print`) added
- New exceptions added
- Function annotations are supported
- Language variable `cls` added
- Byte notation is added to strings

### Removed

- All the unused builtin and magic functions/methods removed
- Long integer removed

### Contribute

Every help is more than welcome!
If you want to submit a change, please use the following rules:

- This project uses 4 spaces as indentation
- `=` and `:` operators are aligned, if variable name's lengthes are similar
- `(`, `[` and `{` starts a new line, if possible
- Each line tries to fit in the width 80 columns

### MIT LICENSE

The MIT License (MIT)

Copyright (c) 2013 Peter Varo

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.