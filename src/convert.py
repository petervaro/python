#!/usr/bin/env python3
## INFO ########################################################################
##                                                                            ##
##                   Python and Cython Syntax Highlighters                    ##
##                   =====================================                    ##
##                                                                            ##
##                       Version: 2.0.00.049 (20141007)                       ##
##                            File: src/convert.py                            ##
##                                                                            ##
##            For more information about the project, please visit            ##
##                   <https://github.com/petervaro/python>.                   ##
##                    Copyright (C) 2013 - 2014 Peter Varo                    ##
##                                                                            ##
##  This program is free software: you can redistribute it and/or modify it   ##
##   under the terms of the GNU General Public License as published by the    ##
##       Free Software Foundation, either version 3 of the License, or        ##
##                    (at your option) any later version.                     ##
##                                                                            ##
##    This program is distributed in the hope that it will be useful, but     ##
##         WITHOUT ANY WARRANTY; without even the implied warranty of         ##
##            MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.            ##
##            See the GNU General Public License for more details.            ##
##                                                                            ##
##     You should have received a copy of the GNU General Public License      ##
##     along with this program, most likely a file in the root directory,     ##
##        called 'LICENSE'. If not, see <http://www.gnu.org/licenses>.        ##
##                                                                            ##
######################################################################## INFO ##

# Import python modules
import plistlib
from os import makedirs
from copy import deepcopy
from itertools import cycle
from collections import OrderedDict
from os.path import join, expanduser

# Import user modules
from src.comments import generate_comments

# Module level constants
THEME_EXT = '.tmTheme'
LANG_EXT  = '.tmLanguage'
PREF_EXT  = '.tmPreferences'
NAME_KEYS = 'name', 'contentName', 'scopeName'


#------------------------------------------------------------------------------#
def _combinator(iterable1, iterable2):
    # Create 'OrderedSet's
    i1 = tuple(OrderedDict.fromkeys(iterable1))
    i2 = tuple(OrderedDict.fromkeys(iterable2))
    # Decide which one to repeat
    if len(i1) < len(i2):
        i1 = cycle(i1)
    else:
        i2 = cycle(i2)
    # Iterate through the values
    for value1, value2 in zip(i1, i2):
        yield value1, value2



#------------------------------------------------------------------------------#
def _replacer(data, name, scope):
    # If data is not the preferred container type
    if not isinstance(data, (dict, list)):
        return
    # If data is a dictionary
    try:
        for key, value in data.items():
            # If key is one of the name-keys
            if key in NAME_KEYS:
                data[key] = value.format(NAME=name, SCOPE=scope)
                continue
            # Convert integer dictionary keys into string literals
            elif isinstance(key, int):
                data[str(key)] = data.pop(key)
            # Recursion on sub-data
            _replacer(value, name, scope)
    # If data is a list
    except AttributeError:
        for item in data:
            # Recursion on sub-data
            _replacer(item, name, scope)


#------------------------------------------------------------------------------#
def _formatter(data, name):
    # If data is not the preferred container type
    if not isinstance(data, (dict, list)):
        return
    # If data is a dictionary
    try:
        for key, value in data.items():
            # If key is one of the name-keys
            if key in NAME_KEYS:
                data[key] = value.format(NAME=name)
            # If key is not a name-key
            else:
                # If value is a color-object
                try:
                    data[key] = value.to_hex()
                except AttributeError:
                    # Recursion on sub-data
                    _formatter(value, name)
    # If data is a list
    except AttributeError:
        for item in data:
            # Recursion on sub-data
            _formatter(item, name)



#------------------------------------------------------------------------------#
class TMFile:

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def __init__(self, name,
                       file=None,
                       path=None,
                       scope='',
                       test_name=None,
                       test_file=None,
                       test_path=None,
                       comments={}):
        # Store static values
        self._name  = name
        self._file  = file or name
        self._path  = path or os.getcwd()
        self._scope = scope
        self._test_name = test_name or name
        self._test_file = test_file or self._test_name
        self._test_path = test_path or self._path
        self._comments = comments
        # Create empty definitions
        self._definition = self._test_definition = {}


    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    # TODO: Add "Automatically Generated, Don't Change" label to files
    def write(self, kind):
        # If write comments-tmpreferences too
        comments = self._comments
        if comments:
            comment_name = 'Comments({})'.format(self._name) + PREF_EXT
            preference = generate_comments(self._scope, **comments)
        # Write work and/or test files to path(s)
        for definition, (file_path, file_name) in zip((self._definition, self._test_definition),
                                                      _combinator((self._path, self._test_path),
                                                                  (self._file, self._test_file))):
            # Create dirs if they don't exist
            real_path = expanduser(file_path)
            makedirs(real_path, exist_ok=True)
            # Create full path to file
            full_path = join(real_path, file_name + LANG_EXT)
            # Write out the property-list file
            with open(full_path, 'w+b') as file:
                plistlib.writePlist(definition, file)
                print('{} dictionary has been converted and placed:'.format(kind),
                      '\t{!r}'.format(full_path), sep='\n')
            if comments:
                full_path = join(real_path, comment_name)
                with open(full_path, 'w+b') as file:
                    plistlib.writePlist(preference, file)
                    print('Comments preference has been converted and placed:',
                          '\t{!r}'.format(full_path), sep='\n')



#------------------------------------------------------------------------------#
class Language(TMFile):

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def from_dict(self, definition):
        # If patterns is a dictionary or it does not exist
        try:
            patterns = definition.get('patterns', {})
            definition['patterns'] = [patterns[key] for key in sorted(patterns)]
        # If patterns is not a dictionary
        except TypeError:
            # If patterns is not a list
            if not isinstance(definition['patterns'], list):
                definition['patterns'] = []

        # If test-file is different than the working one
        if self._name != self._test_name:
            self._test_definition = test_definition = deepcopy(definition)
            _replacer(test_definition, self._test_name, self._scope)
        # If test-file is identical with the working one
        else:
            self._test_definition = definition

        # Format and store definition
        _replacer(definition, self._name, self._scope)
        self._definition = definition


    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def write(self):
        # Call parent's method
        super().write('Syntax')



#------------------------------------------------------------------------------#
class Theme(TMFile):

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def from_dict(self, definition):
        # If test-file is different than the working one
        if self._name != self._test_name:
            self._test_definition = test_definition = deepcopy(definition)
            _formatter(test_definition, self._test_name)
        # If test-file is identical with the working one
        else:
            self._test_definition = definition

        # Format and store definition
        _formatter(definition, self._name)
        self._definition = definition


    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def write(self, css=False):
        # Call parent's method
        super().write('Style')
        # If CSS output needed
        if css:
            pass
