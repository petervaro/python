## INFO ########################################################################
##                                                                            ##
##                   Python and Cython Syntax Highlighters                    ##
##                   =====================================                    ##
##                                                                            ##
##                       Version: 2.0.00.050 (20141007)                       ##
##                           File: src/comments.py                            ##
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

#------------------------------------------------------------------------------#
def generate_comments(scope, lines=None, blocks=None):
    # Build tmPreferences values
    suffix = ''
    values = []
    preference = {'name' : 'Comments',
                  'scope': 'source.{}'.format(scope),
                  'settings': {'shellVariables': values}}

    # If language has line comments
    if lines:
        suffix = '_2'
        values.append({'name' : 'TM_COMMENT_START',
                       'value': lines})

    # If langauge has block comments
    try:
        start, close = blocks
        values.append({'name' : 'TM_COMMENT_START{}'.format(suffix),
                       'value': start})
        values.append({'name' : 'TM_COMMENT_END{}'.format(suffix),
                       'value': close})
    except TypeError:
        pass

    # Return the new plist
    return preference
