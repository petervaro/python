# Python and Cython language bundles

***THE MOST POPULAR (AND FEATURE RICH) PYTHON SYNTAX HIGHLIGHTER FOR SUBLIME
([OVER 11,000 DOWNLOADS!](https://sublime.wbond.net/packages/Python%203))***

This repo is about python 3.3+ and cython 0.19.1+ related bundles for Sublime
Text 2/3 and TextMate editors and for online usage.

![Preview](img/preview.png)

### Python 3.3

Python 3.3 is a truly powerful version of python, with a lot new and creative
features -- and some of them are actually bringing new or different syntaxes!
Unfortunately, the only available and default `tmLanguage` syntax-highlight
definition file is pretty old (only supports 2.x) and has several annoying bugs
and unfinished features -- not to mention, that the syntax of the new python
features brake the full highlighting of the entire code.

I belive, that a good syntax highlighter for software developers has to be as
much help as the auto-completion pop-up or a code linter script in a text
editor.

That's why I have implemented a new syntax definition from scratch that is
created especially for python 3.3 and above. I did this with pure python
structures, some converters and build scripts. *(I found editing `JSON` files
with their ugly double escape characters or editing `XML`/`tmLanguage`s directly
could be pretty annoying on the long run.)*

The end result is very flexible, dynamic, reuseable and easy to read and write
(syntax highlighted regexes -- with comments and variables). It is also simple
to maintain and pretty short too (the new version is only 35% of the old one)!

### Cython support

Unfortunately cython syntax highlighter definitions also lack of updated,
fully-working and 100% python compatible syntax definitions! I have created a
brand-new build-system to combine and convert the highlighter based on the
python one. With this tool, it is quite easy to keep up-to-date both the cython
and the python definitions, and as a plus, I only have to maintain a single
code-base. *Viva la* modularity!

### Highlight on web

***WORK IN PROGRESS***

Previously I wanted to support [`Rainbow.js`](http://craig.is/making/rainbows),
but unfortunately this project hasn't been updated for almost a year now, it
also has several very important, pending, open issues and without these the
proper "translation" from my syntax highlighters to a Rainbow one is impossible.

Thankfully, there is a new, and very actively developed tool, called the
[Ace Editor](http://ace.c9.io). I'm willing to support them, as they are
providing a more feature rich syntax highlighter system, they call it
`Ace Mode`. *(Further more, it is very similar to the `tmLanguage` system, and
they also provide a tool for automatic `Mode` generation from `tmLanguage`,
which is not perfect of course, as they claimed, but still better than
nothing!)*

> The old, Rainbow-compatible version is still available:
`etc/archive/js/Python.js`, but as before, it is still work-in-progress state,
and it is very unlikely that I will finish it and/or support it in the future.

### New is better

Below are some of the most important improvements:

- Added better number highlighting:
	- All types of floating point notations are working now;
	- All types of complex number notations are working now;
	- New types of binary and octal-number notations are supported;
	- Long integer is removed.
- The `...` syntax notation of `Ellipsis` is supported now.
- Declaration rules are extended with `nonlocal`.
- *Ex-statements-now-functions* (like `print`) are updated.
- New Exception highlighting added.
- Function annotations are now supported.
- Conventional-language variable `cls` added.
- Better regex support (multiline, grouping, comments and more are improved).
- String and byte literals:
	- Byte notation added;
	- Proper string prefixes added.
- All the unused built-in and magic functions/methods are now removed.
- All the unused keywords and notations are now removed.

### Future plans

- Support format mini-language in strings.
- Create a better Twilight-based theme file.

### Installation

***Via Package Control***

The fastest and easiest way to install these packages for Sublime Text is the
following:

1. Install [Package Control](https://sublime.wbond.net/installation)
2. Open `Tools` → `Command Palette`
3. Select `Package Control: Install Package`
4. Search for `Python 3` and `Cython+` packages and install them
5. Happy coding ;)

***Set as default***

After you installed the language definition file successfully, all you have to
do is assign the `.py` files to always open with this syntax highlighter. Go to

`View` → `Syntax` → `Open all with current extension as...` → `Python 3`

To remove this setting, you can always overwrite this preference.

***Manual installation***

Download the `tmLanguage` files from the python and Cython branches of this
repository. Navigate to your `Packages` folder and create a `Python3` and/or a
`Cython` folder(s) and copy the `tmLanguage` and sublime-build files into.

***Theme file***

*If you want to use my Work-In-Progress theme file: navigate to `Packages/User`
folder and copy `Gloom.tmTheme` into it. Then go to user-settings, and change
your old color theme to the new one.*

### Contribute

Any help is appreciated and more than welcome -- my goal is to make this the
*'de facto'* language bundle for python 3. If you want to submit a change,
please use the following conventions when editing the original python files:

- variables uses `underscore_separated_names`;
- all files uses 4 spaces for indentation;
- `=` and `:` operators are aligned if length of variable names are similar;
- `(`, `[` and `{` start a new line, if possible and reasonable;
- each line must fit in the width 80 columns (code, text, etc.);
- comment separators can be easily generated with the `src.utils.separator()`
function

### Appreciation

*Thank you very much Jon Clements for all the support and answers about python
and regexes in general, Kevin, Ffisegydd, Zero Piraeus and Poke for the support,
and of course thanks for all the wonderful members of the
[sopython](http://sopython.com) chat room! May the Cabbage be with us ;)*

### LICENSE

Copyright (C) 2013 - 2014 Peter Varo

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program, most likely a file in the root directory, called 'LICENSE'. If
not, see http://www.gnu.org/licenses.
