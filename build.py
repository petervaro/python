#!/usr/bin/env python3
## INFO ########################################################################
##                                                                            ##
##                   Python and Cython Syntax Highlighters                    ##
##                   =====================================                    ##
##                                                                            ##
##                       Version: 2.0.00.081 (20141101)                       ##
##                               File: build.py                               ##
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
from os.path import join

# Module level constants
CURRENT_DIR = '.'
LANG_PATH  = join(CURRENT_DIR, 'langs')
THEME_PATH = join(CURRENT_DIR, 'themes')

# Import cutils modules
try:
    import cutils.ccom
    import cutils.clic
    import cutils.cver

    # Update version
    cutils.cver.version(CURRENT_DIR, sub_max=9, rev_max=99, build_max=999)
    # Collect all special comments
    cutils.ccom.collect(CURRENT_DIR)
    # Update header comments
    cutils.clic.header(CURRENT_DIR)
except ImportError:
    print('[WARNING] cutils modules are missing: '
          'install it from http://www.cutils.org')

# Import tmtools modules
try:
    from tmtools.convert import Language, Theme
except ImportError:
    from sys import exit
    print('[ ERROR ] tmtools modules are missing: '
          'install it from http://github.com/petervaro/tmtools')
    exit(-1)

#------------------------------------------------------------------------------#
# Import user modules
from src.python  import syntax as py_syntax
from src.cython  import syntax as cy_syntax
from src.gloom   import style  as gl_style

# I/O Details of languages and themes
py_details = {'name' : 'Python3',
              'path' : LANG_PATH,
              'scope': 'python.3',
              'comments' : {'lines': '# '},
              'test_name': 'Python3_TEST',
              'test_path': '~/Library/Application Support/Sublime Text 3/'
                           'Packages/User/Python3_TEST'}

cy_details = {'name' : 'Cython',
              'path' : LANG_PATH,
              'scope': 'cython',
              'comments' : {'lines': '# '},
              'test_name': 'Cython_TEST',
              'test_path': '~/Library/Application Support/Sublime Text 3/'
                           'Packages/User/Cython_TEST'}

gl_details = {'name': 'Gloom',
              'path': THEME_PATH,
              'test_name': 'Gloom_TEST',
              'test_path': '~/Library/Application Support/Sublime Text 3/'
                           'Packages/User/Gloom_TEST'}

# NOTE: Old path to theme files => DO NOT SUPPORT IT:
# '~/Library/Application Support/Sublime Text 3/Packages/Color Scheme - Default'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# Process language files
for details, syntax in zip((py_details, cy_details), (py_syntax, cy_syntax)):
    # Setup names and locations
    lang = Language(**details)
    # Convert and save language file
    lang.from_dict(syntax)
    lang.write()

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# Setup names and locations
theme = Theme(**gl_details)
# Convert and save theme file
theme.from_dict(gl_style)
theme.write()
