# Python and Cython language bundles

This repo is about Python 3.3+ and Cython 0.19.1+ related bundles for Sublime
Text 2/3 and TextMate editors and for web presentations.

### Python 3.3

Python 3.3 is a truly powerful version of python, with a lot new and creative
features inside! Sadly, the only available `tmLanguage` syntax-highlight
definition file is pretty old (only supports 2.x) and buggy -- and the some of
the new features' syntaxes brake the full syntax highlighting of the code, not
to mention the lack of new keywords.

I do belive, that a good syntax highlighter for software developers has to be as
much help as an auto-complete popup or a code linter script in a text editor.

That's why I implemented a new syntax definition, started from scratch and
created especially for Python 3.3 and above. I did this with a python
dictionary plus a little converter script and not in `JSON` (ugly double escape
characters -- *Ouch!*) nor in `XML`/`tmLanguage` (com'n is there anyone, who
likes to read-and-write that?). The result is a dynamic, reuseable, easy to read
(syntax highlighted regexes - comments and variables!) and easy to maintain and
also pretty short syntax definition!

### Cython support

Unfortunately cython syntax highlighter definitions are also lack of updated,
fully working and 100% python compatible syntax definitions! To solve this
problem I created the cython defintion file as an extension of the python
definition -- so any time, the python syntax is changing, the cython will
change also!

Now, it is literally a super-set of python!

### Highlight on web

After used to the syntax highlight in the text editor, sharing the code online
with the same colors and highlights is evident! Thanks to Craig Campbell and his
amazing [`Rainbow.js`](http://craig.is/making/rainbows/) it is also possible!

### New is better

- Added better number highlight:
	- all types of floating point notations are working now
	- all types of complex number notations are working now
	- new types of binary and octal number notations are supported
	- long integer is removed
- List of constants are supported:
	- the `...` syntax notation of `Ellipsis` is supported now
- Declaration rules are extended:
	- `nonlocal` added
- Ex-statements-now-functions (like `print` or `exec`) are supported
- New exceptions added
- Function annotations are supported
- Language variable `cls` added
- Byte notation is added to strings
- Format mini-language is supported in strings
- All the unused builtin and magic functions/methods are removed

### Contribute

Every help is appreciated and more than welcome -- my goal is to make the
*'defacto'* language bundle for python 3+. If you want to submit a change,
please use the following conventions:

- variables uses `underscore_separated_names`,
- all files uses 4 spaces for indentation,
- `=` and `:` operators are aligned if length of variable names are similar
- `(`, `[` and `{` start a new line, if possible and reasonable
- each line tries to fit in the width 80 columns
- comment separators are generated with the `separator()` function

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