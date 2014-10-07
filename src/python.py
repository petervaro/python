## INFO ########################################################################
##                                                                            ##
##                   Python and Cython Syntax Highlighters                    ##
##                   =====================================                    ##
##                                                                            ##
##                       Version: 2.0.00.015 (20141006)                       ##
##                            File: src/python.py                             ##
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

#-- CHEATSHEET ----------------------------------------------------------------#
# HOWTO: http://sublimetext.info/docs/en/reference/syntaxdefs.html
# REGEX: http://manual.macromates.com/en/regular_expressions

# Import python modules
from copy import deepcopy

# Import user modules
from src.common import syntax as original

# Syntax Definition
syntax = deepcopy(original)

# Auto-recognition
syntax['fileTypes'] = ['py']
syntax['keyEquivalent'] = '^~P'

# Shebang
syntax['firstLineMatch'] = r'^#!/.*\bpython[\d.-]*\b'

# Folding marks for the TextEditor
syntax['foldingStartMarker'] = (r'^\s*(def|class)\s+([.\w>]+)\s*(\((.*)\))?\s*:'
                                r'|\{\s*$|\(\s*$|\[\s*$|^\s*"""(?=.)(?!.*""")')
syntax['foldingStopMarker'] = r'^\s*$|^\s*\}|^\s*\]|^\s*\)|^\s*"""\s*$'

# Language ID
syntax['uuid'] = '851B1429-B8B4-4C1E-8030-399BDA994393'

# Patterns
syntax['patterns'].update({
#-- COMMENT -------------------------------------------------------------------#
        # ALL ARE COMMON

#-- KEYWORDS ------------------------------------------------------------------#
        0x0080:
        {
            'name' : 'storage.modifier.declaration.{SCOPE}',
            'match': r'\b(global|nonlocal)\b'
        },

        0x0090:
        {
            'name' : 'keyword.control.import_and_import_from.{SCOPE}',
            'match': r'\b(import|from)\b'
        },

        0x00A0:
        {
            'name' : 'keyword.control.flow_block_delimiters.{SCOPE}',
            'match':
            (
                r'\b(elif|else|except|finally|for|if|try|while|'
                r'with|break|continue|pass|raise|return|yield)\b'
            )
        },

        0x00C0:
        {
            'name' : 'keyword.other.{SCOPE}',
            'match': r'\b(as|assert|del)\b'
        },


#-- OPERATORS -----------------------------------------------------------------#
        # ALL ARE COMMON

#-- CLASS ---------------------------------------------------------------------#
        0x0110:
        {
            'name' : 'meta.class.{SCOPE}',
            'begin': r'^\s*(class)\s+(?=[a-zA-Z_]\w*(\s*\()?)',
            'beginCaptures':
            {
                1: {'name': 'storage.type.class.{SCOPE}'}
            },
            'patterns':
            [
                {'include': '#class_entity_name'},
                {'include': '#class_inheritance'}
            ],
            'end'  : r'(\)?\s*:|\s+([\w#\s:]+))',
            'endCaptures':
            {
                3: {'name': 'invalid.illegal.missing_section_begin.{SCOPE}'}
            }
        },


#-- FUNCTION ------------------------------------------------------------------#
        0x0120:
        {
            'name' : 'meta.function.{SCOPE}',
            'begin': r'^\s*(def)\s+(?=[a-zA-Z_]\w*\s*\()',
            'beginCaptures':
            {
                1: {'name': 'storage.type.function.{SCOPE}'}
            },
            'patterns':
            [
                # Function name
                {'include': '#function_entity_name'},
                # Arguments
                {'include': '#function_arguments'},
                # Annotation assignment (function)
                {'include': '#function_annotation'}
            ],
            # TODO: add illegal
            'end': r'(\s*:)',
            'endCaptures':
            {
                2: {'name': 'invalid.illegal.missing_section_begin.{SCOPE}'}
            }
        },


#-- LAMBDA --------------------------------------------------------------------#
        # ALL ARE COMMON

#-- DECORATOR -----------------------------------------------------------------#
        # ALL ARE COMMONE

#-- CONSTANTS -----------------------------------------------------------------#
        0x0160:
        {
            'name' : 'constant.language.word_like.{SCOPE}',
            'match': r'\b(None|True|False|Ellipsis|NotImplemented)\b'
        },


#-- STORAGES ------------------------------------------------------------------#
        0x0180:
        {
            'name' : 'storage.type.function.{SCOPE}',
            'match': r'\b(def|lambda)\b'
        },


#-- BUILTINS ------------------------------------------------------------------#
        # ALL ARE COMMON

#-- MAGIC STUFFS --------------------------------------------------------------#
        # ALL ARE COMMON

#-- ETC -----------------------------------------------------------------------#
        # ALL ARE COMMON

#-- STRUCTURES ----------------------------------------------------------------#
        # ALL ARE COMMON

#-- ACCESS --------------------------------------------------------------------#
        # ALL ARE COMMON

#-- STRING --------------------------------------------------------------------#
        # ALL ARE COMMON
    })


#-- REPOSITORY ----------------------------------------------------------------#
syntax['repository'].update({
#-- COMMENTS ------------------------------------------------------------------#
        # ALL ARE COMMON

#-- CLASS ---------------------------------------------------------------------#
        # ALL ARE COMMON

#-- FUNCTION ------------------------------------------------------------------#
        # ALL ARE COMMON

#-- BUILTINS ------------------------------------------------------------------#
        # TODO: rearrange -> what is builtin function and what is builtin type?
        'builtin_functions':
        {
            'name' : 'support.function.builtin.{SCOPE}',
            'match':
            (
                r'(?<!\.)\b('
                r'__import__|abs|all|any|ascii|bin|callable|chr|compile|delattr|'
                r'dir|divmod|eval|exec|filter|format|getattr|globals|hasattr|hash|'
                r'help|hex|id|input|isinstance|issubclass|iter|len|locals|map|max|'
                r'min|next|oct|ord|pow|print|range|repr|round|setattr|sorted|sum|'
                r'vars|zip'
                r')\b'
            )
        },
        'builtin_types':
        {
            'name' : 'support.type.{SCOPE}',
            'match':
            (
                r'(?<!\.)\b('
                r'basestring|bool|bytearray|bytes|classmethod|complex|dict|'
                r'enumerate|float|frozenset|int|list|memoryview|object|open|'
                r'property|reversed|set|slice|staticmethod|str|super|tuple|type'
                r')\b'
            )
        },


#-- ENTITY --------------------------------------------------------------------#
        'illegal_names':
        {
            'name' : 'invalid.illegal_names.name.{SCOPE}',
            'match':
            (
                r'\b('
                r'and|as|assert|break|class|continue|def|del|elif|else|except|'
                r'finally|for|from|global|if|import|in|is|lambda|nonlocal|not|'
                r'or|pass|raise|return|try|while|with|yield'
                r')\b'
            )
        },


#-- KEYWORDS ------------------------------------------------------------------#
        # ALL ARE COMMON

#-- MAGIC STUFFS --------------------------------------------------------------#
        # TODO: rearrange -> what is magic function and what is magic variable?
        'magic_function_names':
        {
            'name' : 'support.function.magic.{SCOPE}',
            'match':
            (
                r'\b__('
                r'abs|add|and|bool|bytes|call|ceil|complex|contains|copy|'
                r'deepcopy|del|delattr|delete|delitem|dir|div|divmod|enter|eq|'
                r'exit|float|floor|floordiv|format|ge|get|getattr|getattribute|'
                r'getinitargs|getitem|getnewargs|getstate|gt|hash|hex|iadd|'
                r'iand|idiv|ifloordiv|ilshift|imul|index|init|instancecheck|'
                r'int|invert|ior|ipow|irshift|isub|iter|itruediv|ixor|le|len|'
                r'lshift|lt|metaclass|missing|mod|mul|ne|neg|new|next|oct|or|'
                r'pos|pow|prepare|radd|rand|rdiv|rdivmod|reduce|reduce_ex|'
                r'repr|reversed|rfloordiv|rlshift|rmod|rmul|ror|round|rpow|'
                r'rrshift|rshift|rsub|rtruediv|rxor|set|setattr|setitem|'
                r'setstate|sizeof|str|sub|subclasscheck|subclasshook|truediv|'
                r'trunc|unicode|weakref|xor'
                r')__\b'
            )
        },


#-- STRING --------------------------------------------------------------------#
        # ALL ARE COMMON

#-- REGEX ---------------------------------------------------------------------#
        # ALL ARE COMMON
    })
