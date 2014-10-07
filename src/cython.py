## INFO ########################################################################
##                                                                            ##
##                   Python and Cython Syntax Highlighters                    ##
##                   =====================================                    ##
##                                                                            ##
##                       Version: 2.0.00.015 (20141006)                       ##
##                            File: src/cython.py                             ##
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
syntax['fileTypes'] = ['pyx', 'pxi', 'pxd']
syntax['keyEquivalent'] = '^~C'

# Shebang
syntax['firstLineMatch'] = r'^#!/.*\bpython[\d.-]*\b'

# Folding marks for the TextEditor
syntax['foldingStartMarker'] = (r'^\s*((cp?)?def|class)\s+([.\w>]+)\s*(\((.*)\))?\s*:'
                                r'|\{\s*$|\(\s*$|\[\s*$|^\s*"""(?=.)(?!.*""")')
syntax['foldingStopMarker'] = r'^\s*$|^\s*\}|^\s*\]|^\s*\)|^\s*"""\s*$'

# Language ID
syntax['uuid'] = 'D085155B-E40A-40B3-8FEC-6865318CDEEA'

# Patterns
syntax['patterns'].update({
#-- COMMENT -------------------------------------------------------------------#
        # ALL ARE COMMON

#-- KEYWORDS ------------------------------------------------------------------#
        0x0080:
        {
            'name' : 'storage.modifier.declaration.{SCOPE}',
            'match':
            (
                r'\b(global|nonlocal|gil|nogil|extern|api|public|readonly|'
                r'const(\svolatile)?|inline)\b'
            )
        },

        0x0090:
        {
            'name' : 'keyword.control.import_and_import_from.{SCOPE}',
            'match': r'\b(cimport|include|extern|import|from)\b'
        },

        0x00A0:
        {
            'name' : 'keyword.control.flow_block_delimiters.{SCOPE}',
            'match':
            (
                r'\b(elif|else|except|finally|for|if|try|while|with|break|'
                r'continue|pass|raise|return|yield|IF|ELIF|ELSE|DEF)\b'
            )
        },

        0x00C0:
        {
            'name' : 'keyword.other.{SCOPE}',
            'match': r'\b(as|assert|by|del)\b'
        },


#-- OPERATORS -----------------------------------------------------------------#
        0x0101:
        {
            'name' : 'keyword.operator.type_test.{SCOPE}',
            'match': r'\?'
        },


#-- CLASS ---------------------------------------------------------------------#
        0x0110:
        {
            'name' : 'meta.class.{SCOPE}',
            'begin': r'^\s*(cdef\s+)?(class)\s+(?=[a-zA-Z_]\w*(\s*\()?)',
            'beginCaptures':
            {
                1: {'name': 'storage.type.class.definition.{SCOPE}'},
                2: {'name': 'storage.type.class.{SCOPE}'}
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
            'begin': r'^\s*((cp?)?def)\s+(?=[a-zA-Z_]\w*\s*\()',
            'beginCaptures':
            {
                1: {'name': 'storage.type.function.{SCOPE}'}
            },
            'patterns':
            [
                # TODO: highlight type declarations in functions!
                # Function name
                {'include': '#function_entity_name'},
                # Arguments
                {'include': '#function_arguments'},
                # Global Interpreter Lock
                {
                    'begin': r'\)\s*(nogil)\s*',
                    'beginCaptures':
                    {
                        1: {'name': 'storage.modifier.declaration.{SCOPE}'}
                    },
                    'end': r'\s*((->)|:|\n+)'
                },
                # Annotation assignment (function)
                {'include': '#function_annotation'}
            ],
            # todo: add illegal
            'end': r'(\s*:|\n+)',
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
            'match':
            (
                r'\b(NULL|None|True|False|Ellipsis|NotImplemented|'
                r'UNAME_SYSNAME|UNAME_NODENAME|UNAME_RELEASE|UNAME_VERSION|'
                r'UNAME_MACHINE|EXIT_FAILURE|EXIT_SUCCESS|RAND_MAX)\b'
            )
        },


#-- STORAGES ------------------------------------------------------------------#
        0x0180:
        {
            'name' : 'storage.type.function.{SCOPE}',
            'match': r'\b((c(p|type)?)?def|lambda)\b'
        },


#-- BUILTINS ------------------------------------------------------------------#
        0x01A1:
        {
            'include': '#c_types'
        },


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
                r'__import__|abort|(c|m|re)alloc|(ll?)?abs|all|any|ascii|bin|bsearch|'
                r'callable|chr|compile|delattr|dir|(ll?)?div|divmod|eval|exec|(_|at)?exit|'
                r'filter|format|free|getattr|getenv|globals|hasattr|hash|help|hex|id|'
                r'input|isinstance|issubclass|iter|len|locals|map|max|min|next|'
                r'oct|ord|pow|print|qsort|range|s?rand|repr|round|setattr|sizeof|'
                r'sorted|sum|system|vars|zip'
                r')\b'
            )
        },
        'builtin_types':
        {
            'name' : 'support.type.{SCOPE}',
            'match':
            (
                r'(?<!\.)\b('
                r'basestring|bool|buffer|bytearray|bytes|classmethod|complex|'
                r'dict|enumerate|file|frozenset|list|memoryview|object|open|'
                r'property|reversed|set|slice|staticmethod|str|super|tuple|type'
                r')\b'
            )
        },
        'c_types':
        {
            'name' : 'support.type.c_types.{SCOPE}',
            'match':
            (
                r'(?<!\.)\b('
                r'bint|(long\s)?double|enum|float|struct|union|void|const|fused|'
                r'((un)?signed\s)?(char|((short|long(\slong)?)\s)?int|short|long(\slong)?)'
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
                r'and|api|as|assert|break|by|class|continue|(c(p|type)?)?def|del|'
                r'elif|else|except|finally|for|from|global|if|import|in|is|lambda|'
                r'nonlocal|not|or|pass|public|raise|return|try|while|with|yield'
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
                r'dealloc|deepcopy|del|delattr|delete|delitem|dir|div|divmod|enter|'
                r'eq|exit|float|floor|floordiv|format|ge|get|getattr|getattribute|'
                r'getinitargs|getitem|getnewargs|getstate|gt|hash|hex|iadd|'
                r'iand|idiv|ifloordiv|ilshift|imul|index|c?init|instancecheck|'
                r'int|invert|ior|ipow|irshift|isub|iter|itruediv|ixor|le|len|'
                r'lshift|lt|metaclass|missing|mod|mul|ne|neg|new|next|oct|or|'
                r'pos|pow|prepare|radd|rand|rdiv|rdivmod|reduce|reduce_ex|'
                r'repr|reversed|rfloordiv|rlshift|rmod|rmul|ror|round|rpow|'
                r'rrshift|rshift|rsub|rtruediv|rxor|set|setattr|setitem|'
                r'setstate|signatures|str|sub|subclasscheck|subclasshook|truediv|'
                r'trunc|unicode|weakref|xor'
                r')__\b'
            )
        },


#-- STRING --------------------------------------------------------------------#
        # ALL ARE COMMON

#-- REGEX ---------------------------------------------------------------------#
        # ALL ARE COMMON
    })
