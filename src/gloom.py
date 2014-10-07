## INFO ########################################################################
##                                                                            ##
##                   Python and Cython Syntax Highlighters                    ##
##                   =====================================                    ##
##                                                                            ##
##                       Version: 2.0.00.036 (20141007)                       ##
##                             File: src/gloom.py                             ##
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

# Import user modules
from src.utils import hsba

# Keyword constants
bg = 'background'
fg = 'foreground'
name   = 'name'
scope  = 'scope'
prefs  = 'settings'
font   = 'fontStyle'
bold   = 'bold'
italic = 'italic'

#------------------------------------------------------------------------------#
style = {
    'author': 'Peter Varo (c)2013-2014',
    'comment': ('\n\t\tCopyright (C) 2013 - 2014 Peter Varo'
                '\n\t\t<http://github.com/petervaro/python>'
                '\n'
                '\n\t\tBased on the Twilight theme of Michael Sheets.'
                '\n'
                '\n\t\tThis program is free software: you can redistribute it'
                '\n\t\tand/or modify it under the terms of the GNU General'
                '\n\t\tPublic License as published by the Free Software'
                '\n\t\tFoundation, either version 3 of the License, or (at your'
                '\n\t\toption) any later version.'
                '\n'
                '\n\t\tThis program is distributed in the hope that it will be'
                '\n\t\tuseful, but WITHOUT ANY WARRANTY; without even the'
                '\n\t\timplied warranty of MERCHANTABILITY or FITNESS FOR A'
                '\n\t\tPARTICULAR PURPOSE. See the GNU General Public License'
                '\n\t\tfor more details.'
                '\n'
                '\n\t\tYou should have received a copy of the GNU General Public'
                '\n\t\tLicense along with this program, most likely a file in'
                '\n\t\tthe root directory, called "LICENSE". If not, see'
                '\n\t\t<http://www.gnu.org/licenses>.'
                '\n\t'),
    'uuid': '5E10F479-14B9-4DC1-B26C-557B2BB3FAE',
    name : '{NAME}',
    prefs:
    [
        {
            prefs:
            {
                bg             : hsba(0, 0, .08),
                fg             : hsba(0, 0, .95),
                'caret'        : hsba(0, 0, .65),
                'invisibles'   : hsba(0, 0, 1, .10),
                'lineHighlight': hsba(0, 0, 1, .04),
                'selection'    : hsba(0, 0, 1, .08)
            }
        },
        {
            name  : 'Comment',
            scope : 'comment',
            prefs :
            {
                fg  : hsba(0, 0, .35),
                font: italic
            }
        },
        {
            name : 'Constant',
            scope: 'constant',
            prefs:
            {
                fg: hsba(15, .65, .80)
            }
        },
        {
            name : 'Entity',
            scope: 'entity',
            prefs:
            {
                fg: hsba(30, .60, .60)
            }
        },
        {
            name : 'Keyword',
            scope: 'keyword',
            prefs:
            {
                fg: hsba(40, .50, .80)
            }
        },
        {
            name : 'Storage',
            scope: 'storage',
            prefs:
            {
                fg: hsba(50, .40, .95)
            }
        },
        {
            name : 'String',
            scope: 'string',
            prefs:
            {
                fg: hsba(75, .30, .60)
            }
        },
        {
            name : 'Support',
            scope: 'support',
            prefs:
            {
                fg: hsba(295, .15, .60)
            }
        },
        {
            name : 'Variable',
            scope: 'variable',
            prefs:
            {
                fg: hsba(220, .30, .65)
            }
        },
        {
            name : 'Invalid Deprecated',
            scope: 'invalid.deprecated',
            prefs:
            {
                bg: hsba(10, .25, .80, .25)
            }
        },
        {
            name : 'Invalid Illegal',
            scope: 'invalid.illegal',
            prefs:
            {
                bg: hsba(300, .50, .35, .60)
            }
        },


#-- DETAILS -------------------------------------------------------------------#
        {
            name : 'Entity Inherited Class',
            scope: 'entity.other.inherited-class',
            prefs:
            {
                fg: hsba(25, .70, .60),
                font: italic
            }
        },
        {
            name : 'String Constant',
            scope: 'string constant',
            prefs:
            {
                fg: hsba(75, .30, .95)
            }
        },
        {
            name : 'String Interpolated',
            scope: 'string.interpolated',
            prefs:
            {
                fg: hsba(120, .10, .85)
            }
        },
        {
            name : 'Support Function',
            scope: 'support.function',
            prefs:
            {
                fg: hsba(55, .40, .85)
            }
        },
        {
            name : 'Constant Character Escape',
            scope: 'constant.character.escape',
            prefs:
            {
                fg: hsba(30, .75, .80)
            }
        },
        {
            name : 'Storage Modifier',
            scope: 'storage.modifier',
            prefs:
            {
                fg: hsba(30, .55, .80)
            }
        },


#-- LINTER --------------------------------------------------------------------#
        {
            name : 'SublimeLinter Annotations',
            scope: 'sublimelinter.annotations',
            prefs:
            {
                bg: hsba(60, .33, 1.0),
                fg: hsba(0, 0, 1)
            }
        },
        {
            name : 'SublimeLinter Error Outline',
            scope: 'sublimelinter.outline.illegal',
            prefs:
            {
                bg: hsba(20, .80, .60),
                fg: hsba(0, 0, 1)
            }
        },
        {
            name : 'SublimeLinter Error Underline',
            scope: 'sublimelinter.underline.illegal',
            prefs:
            {
                bg: hsba(20, .80, .95)
            }
        },
        {
            name : 'SublimeLinter Warning Outline',
            scope: 'sublimelinter.outline.warning',
            prefs:
            {
                bg: hsba(40, .50, .50),
                fg: hsba(0, 0, 1)
            }
        },
        {
            name : 'SublimeLinter Warning Underline',
            scope: 'sublimelinter.underline.warning',
            prefs:
            {
                bg: hsba(40, .50, .85)
            }
        },
        {
            name : 'SublimeLinter Violation Outline',
            scope: 'sublimelinter.outline.violation',
            prefs:
            {
                bg: hsba(75, .40, .35),
                fg: hsba(0, 0, 1)
            }
        },
        {
            name : 'SublimeLinter Violation Underline',
            scope: 'sublimelinter.underline.violation',
            prefs:
            {
                bg: hsba(75, .40, .70)
            }
        }
    ]
}
