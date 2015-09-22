## INFO ########################################################################
##                                                                            ##
##                   Python and Cython Syntax Highlighters                    ##
##                   =====================================                    ##
##                                                                            ##
##                       Version: 2.0.00.071 (20141024)                       ##
##                            File: src/common.py                             ##
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

# Syntax Definition
syntax = {
    'name': '{NAME}',
    'comment': ('\n\t\tCopyright (C) 2013 - 2014 Peter Varo'
                '\n\t\t<http://github.com/petervaro/python>'
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
    'scopeName': 'source.{SCOPE}',
    # Patterns
    'patterns':
    {
#-- COMMENT -------------------------------------------------------------------#
        0x0000 :
        {
            'include': '#comment'
        },


#-- NUMBERS -------------------------------------------------------------------#
        0x0010:
        {
            'name' : 'constant.numeric.integer.binary.{SCOPE}',
            'match': r'\b0b[01]+'
        },

        0x0020:
        {
            'name' : 'constant.numeric.integer.hexadecimal.{SCOPE}',
            'match': r'\b0x\h+'
        },

        0x0030:
        {
            'name' : 'constant.numeric.integer.octal.{SCOPE}',
            'match': r'\b0o[0-7]+'
        },

        0x0040:
        {
            # .001  .1e6  .1E6  .1e+6  .1E+6  .1e-6  .1E-6
            'name' : 'constant.numeric.float_and_complex.decimal.floatnumber.{SCOPE}',
            'match': r'(?<=\W|^)\.\d+([eE][+-]?\d+)?[jJ]?'
        },

        0x0050:
        {
            # 1.  1.0  1.e10  1.1e6  1.1E6  1.1e+6  1.1E+6  1.1e-6  1.1E-6
            'name' : 'constant.numeric.float_and_complex.decimal.pointfloat.{SCOPE}',
            'match': r'\d+\.(\d*([eE][+-]?\d+)?)?[jJ]?(?=\W)'
        },

        0x0060:
        {
            # 1e6  1E6  1e+6  1E+6  1e-6  1E-6
            'name' : 'constant.numeric.float_and_complex.decimal.exponent.{SCOPE}',
            'match': r'(?<![\.\d])\d+[eE][+-]?\d+[jJ]?'
        },

        0x0070:
        {
            'name' : 'constant.numeric.integer_and_complex.decimal.{SCOPE}',
            'match': r'\b(?<!\.)([1-9]\d*|0)[jJ]?'
        },


#-- KEYWORDS ------------------------------------------------------------------#
        # 0x0080: storage.modifier.declaration

        # 0x0090: keyword.control.import_and_import_from

        # 0x00A0: keyword.control.flow_block_delimiters

        0x00B0:
        {
            'name' : 'keyword.operator.bool.logical.{SCOPE}',
            'match': r'\b(and|in|is|not|or)\b'
        },

        # 0x00C0: keyword.other


#-- OPERATORS -----------------------------------------------------------------#
        0x00D0:
        {
            'name' : 'keyword.operator.comparison.{SCOPE}',
            'match': r'<=|>=|==|<|>|!='
        },

        0x00E0:
        {
            'name' : 'keyword.operator.assignment.augmented.{SCOPE}',
            'match': r'\+=|-=|\*=|/=|//=|%=|&=|\|=|\^=|<<=|>>=|\*\*='
        },

        0x00F0:
        {
            'name' : 'keyword.operator.arithmetic.{SCOPE}',
            'match': r'\+|-|\*|\*\*|/|//|%|<<|>>|&|\||\^|~'
        },

        0x0100:
        {
            'name' : 'keyword.operator.value_and_annotation_assignment.{SCOPE}',
            'match': r'=|->'
        },


#-- CLASS ---------------------------------------------------------------------#
        # 0x0110: meta.class

#-- FUNCTION ------------------------------------------------------------------#
        # 0x0120: meta.function

#-- LAMBDA --------------------------------------------------------------------#
        0x0130:
        {
            'name' : 'meta.function.anonymous.{SCOPE}',
            'begin': r'\b(lambda)\b',
            'beginCaptures':
            {
                1: {'name': 'storage.type.function.anonymous.{SCOPE}'}
            },
            'patterns':
            [
                {
                    'begin': r'\s+',
                    'patterns':
                    [
                        # Keyword arguments
                        {
                            'begin': r'\b([a-zA-Z_]\w*)\s*(=)',
                            'beginCaptures':
                            {
                                1: {'name': 'variable.parameter.function.{SCOPE}'},
                                2: {'name': 'keyword.operator.assignment.{SCOPE}'}
                            },
                            'patterns':
                            [
                                {'include': '$self'}
                            ],
                            'end': r'(?=,|:)'
                        },
                        # Positional arguments
                        {
                            'name' : 'variable.parameter.function.{SCOPE}',
                            'match': r'\b[a-zA-Z_]\w*'
                        }
                    ],
                    'end': r'(?=:)'
                }
            ],
            'end': r':'
        },


#-- DECORATOR -----------------------------------------------------------------#
        # Decorator with arguments
        0x0140:
        {
            'name' : 'meta.function.decorator.with_arguments.{SCOPE}',
            'begin': r'^\s*(@\s*[a-zA-Z_]\w*(\.[a-zA-Z_]\w*)*)\s*\(',
            'beginCaptures':
            {
                1: {'name': 'support.function.decorator.{SCOPE}'}
            },
            'patterns':
            [
                {'include': '#keyword_arguments'},
                {'include': '$self'}
            ],
            'end': r'\)'
        },

        # Decorator without arguments
        0x0150:
        {
            'name' : 'meta.function.decorator.without_arguments.{SCOPE}',
            'begin': r'^\s*(@\s*[a-zA-Z_]\w*(\.[a-zA-Z_]\w*)*)',
            'beginCaptures':
            {
                1: {'name': 'support.function.decorator.{SCOPE}'}
            },
            'end': r'(?=\s|$\n?|#)'
        },


#-- CONSTANTS -----------------------------------------------------------------#
        # 0x0160: constant.language.word_like

        0x0170:
        {
            'name' : 'constant.language.symbol_like.{SCOPE}',
            'match': r'(?<=\W|^)\.\.\.(?=\W|$)'
        },


#-- STORAGES ------------------------------------------------------------------#
        # 0x0180: storage.type.function

        0x0190:
        {
            'name' : 'storage.type.class.{SCOPE}',
            'match': r'\b(class)\b'
        },


#-- BUILTINS ------------------------------------------------------------------#
        0x01A0:
        {
            'include': '#builtin_types'
        },

        0x01B0:
        {
            'include': '#builtin_functions'
        },

        0x01C0:
        {
            'include': '#builtin_exceptions'
        },


#-- MAGIC STUFFS --------------------------------------------------------------#
        0x01D0:
        {
            'include': '#magic_function_names'
        },

        0x01F0:
        {
            'include': '#magic_variable_names'
        },


#-- ETC -----------------------------------------------------------------------#
        0x0200:
        {
            'include': '#line_continuation'
        },

        0x0210:
        {
            'include': '#language_variables'
        },


#-- STRUCTURES ----------------------------------------------------------------#
        # LIST
        0x0220:
        {
            'name': 'meta.structure.list.{SCOPE}',
            'begin': r'\[',
            'patterns':
            [
                {
                    'begin': r'(?<=\[|,)\s*(?![\],])',
                    'patterns':
                    [
                        {'include': '$self'}
                    ],
                    'end'  : r'\s*(?:,|(?=\]))'
                }
            ],
            'end'  : r'\]'
        },

        # DICTIONARY
        0x0230:
        {
            'name': 'meta.structure.dictionary.{SCOPE}',
            'begin': r'\{',
            'patterns':
            [
                {
                    'begin': r'(?<=\{|,|^)\s*(?![,}])',
                    'patterns':
                    [
                        {'include': '$self'}
                    ],
                    'end'  : r'\s*(?:(?=\})|:)'
                },
                {
                    'begin': r'(?<=:|^)\s*',
                    'patterns':
                    [
                        {'include': '$self'}
                    ],
                    'end'  : r'\s*(?:(?=\})|,)'
                }
            ],
            'end'  : r'\}'
        },

        0x0240:
        # GROUPS, TUPLES
        {
            'name' : 'meta.structure.group.{SCOPE}',
            'begin': r'(?<=,|;|=|\+|-|\*|/|\||:|<|>|~|%|\^|\\)\s*\(',
            'patterns':
            [
                {'include': '$self'}
            ],
            'end': r'\)'
        },


#-- ACCESS --------------------------------------------------------------------#
        0x0250:
        {
            'name' : 'meta.function_call.{SCOPE}',
            'begin': r'(?<!:|,|;|\[|\{|\}|=|\+|-|\*|/|\||<|>|~|%|\^|\\|\n)\s*\(',
            'patterns':
            [
                {'include': '#keyword_arguments'},
                {'include': '$self'}
            ],
            'end': r'\)'
        },


#-- STRING --------------------------------------------------------------------#
        0x0260:
        {
            'include': '#string_quoted'
        }
    },

#-- REPOSITORY ----------------------------------------------------------------#
    'repository':
    {
#-- COMMENTS ------------------------------------------------------------------#
        'comment':
        {
            'name' : 'comment.line.hashmark.{SCOPE}',
            'match': r'#.*$\n?'
        },


#-- CLASS ---------------------------------------------------------------------#
        'class_entity_name':
        {
            'contentName': 'entity.name.type.class.{SCOPE}',
            'begin': r'(?=[a-zA-Z_]\w*)',
            'patterns':
            [
                {'include': '#entity_name_class'}
            ],
            'end': r'(?!\w)'
        },
        'class_inheritance':
        {
            'contentName': 'meta.class.inheritance.{SCOPE}',
            'begin': r'\(',
            'patterns':
            [
                {
                    'contentName': 'entity.other.inherited-class.{SCOPE}',
                    'begin': r'(?<=\(|,)\s*',
                    'patterns':
                    [
                        {'include': '$self'}
                    ],
                    'end': r'\s*(?:,|(?=\)))',
                    'endCaptures':
                    {
                        1: {'name': 'punctuation.separator.inheritance.{SCOPE}'}
                    }
                }
            ],
            'end': r'\)|:'
        },


#-- FUNCTION ------------------------------------------------------------------#
        'function_entity_name':
        {
            'contentName': 'entity.name.function.{SCOPE}',
            'begin': r'(?=[a-zA-Z_]\w*)',
            'patterns':
            [
                {'include': '#entity_name_function'}
            ],
            'end': r'(?!\w)'
        },
        'function_arguments':
        {
            'begin': r'\(',
            'patterns':
            [
                # 'Inline' comments
                {'include': '#comment'},
                # Keyword arguments
                {
                    'begin': r'\b([a-zA-Z_]\w*)\s*(=)',
                    'beginCaptures':
                    {
                        1: {'name': 'variable.parameter.function.{SCOPE}'},
                        2: {'name': 'keyword.operator.assignment.{SCOPE}'}
                    },
                    'patterns':
                    [
                        # Keyword assignment
                        {
                            'begin': r'(?<=(=))\s*',
                            'beginCaptures':
                            {
                                1: {'name': 'keyword.operator.assignment.{SCOPE}'}
                            },
                            'patterns':
                            [
                                {'include': '$self'}
                            ],
                            'end': r'(?=,|[\n)])',
                        },
                        # Annotation assignment (kwargs)
                        {
                            'begin': r'(?<=:)\s*',
                            'patterns':
                            [
                                {'include': '$self'}
                            ],
                            'end': r'(?=,|(=)|[\n)])',
                            'endCaptures':
                            {
                                1: {'name': 'keyword.operator.assignment.{SCOPE}'}
                            }
                        }
                    ],
                    'end': r'(?=,|[\n)])'
                },
                # Positional arguments
                {
                    'begin': r'\b([a-zA-Z_]\w*)\s*',
                    'beginCaptures':
                    {
                        1: {'name': 'variable.parameter.function.{SCOPE}'}
                    },
                    'patterns':
                    [
                        # Annotation assignment (args)
                        {
                            'begin': r'(?<=:)\s*',
                            'patterns':
                            [
                                {'include': '$self'}
                            ],
                            'end': r'(?=,|[\n)])',
                        }
                    ],
                    'end': r'(?=,|[\n)])'
                }
            ],
            'end': r'(?=\))'
        },
        'function_annotation':
        {
            'begin': r'(?<=\))\s*(->)\s*',
            'beginCaptures':
            {
                1: {'name': 'keyword.operator.annotation.assignment.{SCOPE}'}
            },
            'patterns':
            [
                {'include': '$self'}
            ],
            'end': r'(?=\s*:)'
        },


#-- BUILTINS ------------------------------------------------------------------#
        'builtin_exceptions':
        {
            'name' : 'support.type.exception.{SCOPE}',
            'match':
            (
                r'(?<!\.)\b('
                r'(Arithmetic|Buffer|Lookup|Assertion|Attribute|EOF|FloatingPoint|'
                r'Import|Index|Key|Memory|Name|NotImplemented|OS|Overflow|Reference|'
                r'Runtime|Syntax|Indentation|Tab|System|Type|UnboundLocal|Unicode|'
                r'Unicode(Encode|Decode|Translate)?|Value|ZeroDivision|'
                r'Environment|IO|VMS|Windows|BlockingIO|ChildProcess|'
                r'BrokenPipe|Connection(Aborted|Refused|Reset)?|'
                r'FileExists|FileNotFound|Interrupted|(Is|Not)ADirectory|'
                r'Permission|ProcessLookup|Timeout)Error|(User|Deprecation|'
                r'PendingDeprecation|Syntax|Runtime|Future|Import|Bytes|'
                r'Resource)Warning|(Base)?Exception|(Generator|System)Exit|'
                r'KeyboardInterrupt|StopIteration|Warning'
                r')\b'
            )
        },


#-- ENTITY --------------------------------------------------------------------#
        'entity_name_class':
        {
            'patterns':
            [
                {'include': '#illegal_names'},
                {'include': '#generic_names'}
            ]
        },
        'entity_name_function':
        {
            'patterns':
            [
                {'include': '#magic_function_names'},
                {'include': '#illegal_names'},
                {'include': '#generic_names'}
            ]
        },
        'generic_names':
        {
            'match': r'[a-zA-Z_]\w*'
        },


#-- KEYWORDS ------------------------------------------------------------------#
        'keyword_arguments':
        {
            'begin': r'\b([a-zA-Z_]\w*)\s*(=)(?!=)',
            'beginCaptures':
            {
                1: {'name': 'variable.parameter.function.{SCOPE}'},
                2: {'name': 'keyword.operator.assignment.{SCOPE}'}
            },
            'patterns':
            [
                {'include': '$self'}
            ],
            'end': r'(?=,|[\n)])'
        },


#-- MAGIC STUFFS --------------------------------------------------------------#
        # TODO: rearrange -> what is magic function and what is magic variable?
        'magic_variable_names':
        {
            'name' : 'support.variable.magic.{SCOPE}',
            'match':
            (
                r'\b__('
                r'all|annotations|bases|builtins|class|debug|dict|doc|file|'
                r'members|metaclass|mro|name|qualname|slots|weakref'
                r')__\b'
            )
        },
        # conventions
        'language_variables':
        {
            'name' : 'variable.language.{SCOPE}',
            'match': r'(?<!\.)\b(self|cls)\b'
        },
        'line_continuation':
        {
            'match': r'(\\)(.*)$\n?',
            'captures':
            {
                1: {'name': 'punctuation.separator.continuation.line.{SCOPE}'},
                2: {'name': 'invalid.illegal.unexpected_text.{SCOPE}'}
            }
        },


#-- STRING --------------------------------------------------------------------#
        # TODO: decide if source.sql and special words, like SELECT and INSERT needed
        'string_quoted':
        {
            # stringprefix:  "r"  | "u"  | "R"  | "U"  |
            # bytesprefix :  "b"  | "B"  | "br" | "Br" | "bR" |
            #                "BR" | "rb" | "rB" | "Rb" | "RB" |
            'patterns':
            [
                # Single BLOCK
                {
                    'name' : 'string.quoted.single.block.{SCOPE}',
                    'begin': r"([bBuU]?)'''",
                    'beginCaptures':
                    {
                        1: {'name': 'storage.type.string.prefix.{SCOPE}'}
                    },
                    'patterns':
                    [
                        {'include': '#string_patterns'}
                    ],
                    'end': r"'''"
                },
                {
                    'name' : 'string.quoted.single.block.{SCOPE}',
                    'begin': r"([rR][bB]|[bB][rR]|[rR])'''",
                    'beginCaptures':
                    {
                        1: {'name': 'storage.type.string.prefix.{SCOPE}'}
                    },
                    'patterns':
                    [
                        {'include': '#string_patterns'},
                        {'include': '#regular_expressions'},
                        {'include': '#comment'}
                    ],
                    'end': r"'''"
                },

                # Single LINE
                {
                    'name' : 'string.quoted.single.line.{SCOPE}',
                    'begin': r"([bBuU]?)'",
                    'beginCaptures':
                    {
                        1: {'name': 'storage.type.string.prefix.{SCOPE}'}
                    },
                    'patterns':
                    [
                        {'include': '#string_patterns'}
                    ],
                    'end': r"'|(\n)",
                    'endCaptures':
                    {
                        1: {'name': 'invalid.illegal.unclosed_string.{SCOPE}'}
                    }
                },
                {
                    'name' : 'string.quoted.single.line.{SCOPE}',
                    'begin': r"([rR][bB]|[bB][rR]|[rR])'",
                    'beginCaptures':
                    {
                        1: {'name': 'storage.type.string.prefix.{SCOPE}'}
                    },
                    'patterns':
                    [
                        {'include': '#string_patterns'},
                        {'include': '#regular_expressions'}
                    ],
                    'end': r"'|(\n)",
                    'endCaptures':
                    {
                        1: {'name': 'invalid.illegal.unclosed_string.{SCOPE}'}
                    }
                },

                # Double BLOCK
                {
                    'name' : 'string.quoted.double.block.{SCOPE}',
                    'begin': r'([bBuU]?)"""',
                    'beginCaptures':
                    {
                        1: {'name': 'storage.type.string.prefix.{SCOPE}'}
                    },
                    'patterns':
                    [
                        {'include': '#string_patterns'}
                    ],
                    'end': r'"""'
                },
                {
                    'name' : 'string.quoted.double.block.{SCOPE}',
                    'begin': r'([rR][bB]|[bB][rR]|[rR])"""',
                    'beginCaptures':
                    {
                        1: {'name': 'storage.type.string.prefix.{SCOPE}'}
                    },
                    'patterns':
                    [
                        {'include': '#string_patterns'},
                        {'include': '#regular_expressions'},
                        {'include': '#comment'}
                    ],
                    'end': r'"""'
                },

                # Double LINE
                {
                    'name' : 'string.quoted.double.line.{SCOPE}',
                    'begin': r'([bBuU]?)"',
                    'beginCaptures':
                    {
                        1: {'name': 'storage.type.string.prefix.{SCOPE}'}
                    },
                    'patterns':
                    [
                        {'include': '#string_patterns'}
                    ],
                    'end': r'"|(\n)',
                    'endCaptures':
                    {
                        1: {'name': 'invalid.illegal.unclosed_string.{SCOPE}'}
                    }
                },
                # {
                #     'name' : 'meta.format_attribute.format.{SCOPE}',
                #     'begin': r'(\.format)\s*\(',
                #     'beginCaptures':
                #     {
                #         1: {'name': 'invalid.illegal.none.{SCOPE}'}
                #     },
                #     'patterns':
                #     [
                #         {
                #             'name' : 'string.quoted.double.format.{SCOPE}',
                #             'begin': r'([uUbB]?)"',
                #             'beginCaptures':
                #             {
                #                 1: {'name': 'storage.type.string.prefix.{SCOPE}'}
                #             },
                #             'patterns':
                #             [
                #                 {'include': '#string_patterns'},
                #                 {'include': '#format_mini_language'}
                #             ],
                #             'end': r'"|(\n)',
                #             'endCaptures':
                #             {
                #                 1: {'name': 'invalid.illegal.unclosed_string.{SCOPE}'}
                #             }
                #         }
                #     ],
                #     'end': r'\)'
                # },
                # {
                #     'name' : 'string.quoted.double.format.{SCOPE}',
                #     'begin': r'([uUbB]?)"',
                #     'beginCaptures':
                #     {
                #         1: {'name': 'storage.type.string.prefix.{SCOPE}'}
                #     },
                #     'patterns':
                #     [
                #         {'include': '#string_patterns'},
                #         {'include': '#format_mini_language'}
                #     ],
                #     'end': r'"\.format',  # |(\n)',
                #     'endCaptures':
                #     {
                #         2: {'name': 'invalid.illegal.unclosed_string.{SCOPE}'}
                #     }
                # },
                {
                    'name' : 'string.quoted.double.line.{SCOPE}',
                    'begin': r'([rR][bB]|[bB][rR]|[rR])"',
                    'beginCaptures':
                    {
                        1: {'name': 'storage.type.string.prefix.{SCOPE}'}
                    },
                    'patterns':
                    [
                        {'include': '#string_patterns'},
                        {'include': '#regular_expressions'}
                    ],
                    'end': r'"|(\n)',
                    'endCaptures':
                    {
                        1: {'name': 'invalid.illegal.unclosed_string.{SCOPE}'}
                    }
                }
            ]
        },
        'string_patterns':
        {
            'patterns':
            [
                {'include': '#constant_placeholder'},
                {'include': '#escaped_characters'},
                {'include': '#escaped_unicode_characters'}
            ]
        },
        'constant_placeholder':
        {
            'name' : 'string.interpolated.placeholder.{SCOPE}',
            'match': r'%(\(\w+\))?#?0?-?[ ]?\+?(\d*|\*)(\.(\d*|\*))?[hlL]?[diouxXeEfFgGcrs%]'
        },
        'format_mini_language':
        {
            'patterns':
            [
                {
                    'name' : 'constant.other.placeholder.format.{SCOPE}',
                    'match': r'\{\}'
                }
            ]
        },
        'escaped_characters':
        {
            # escape:
            # hex          | octal  | newline   | double-quote |
            # single-quote | bell   | backspace | formfeed     |
            # line-feed    | return | tab       | vertical-tab | escape char
            'name' : 'constant.character.escaped.special.{SCOPE}',
            'match': r'\\(x\h{2}|[0-7]{3}|\n|\"|\'|a|b|f|n|r|t|v|\\)'
        },
        'escaped_unicode_characters':
        {
            # 16bit hex | 32bit hex | unicodename
            'name' : 'constant.character.escaped.{SCOPE}',
            'match': r'\\(u\h{4}|U\h{8}|N\{[a-zA-Z\s]+\})'
        },


#-- REGEX ---------------------------------------------------------------------#
        'regular_expressions':
        {
            'patterns':
            [
                {
                    # (?=  positive look-ahead)
                    # (?!  negative look-ahead)
                    # (?<= positive look-behind)
                    # (?<! negative look-behind)
                    # (?:  non-capturing)
                    # (?P<id> group)
                    # (?(id/name)yes-pattern|no-pattern)
                    'name' : 'constant.character.escape.{SCOPE}',
                    'match': r'(?<=\()\?(=|!|<=|<!|:|P<[a-zA-Z_]\w*?>|'
                             r'\(([1-9]\d?|[a-zA-Z_]\w*)\))'
                    # NOTE: the problem of making this to be a begin/end block
                    #       is that the patterns needs to include the multiline-
                    #       comments only if the expression is in multline
                    #       quotes otherwise it should be exclude it...
                },
                {
                    # (?P=this_is_a_group)
                    'name' : 'keyword.other.group_reference_name.regex.{SCOPE}',
                    'match': r'\((\?P=)([a-zA-Z_]\w*)\)',
                    'captures':
                    {
                        1: {'name': 'constant.character.escape.{SCOPE}'}
                    }
                },
                {
                    'name' : 'keyword.control.anchor.regex.{SCOPE}',
                    'match': r'\\[bBAZzG]|\^|\$'
                },
                {
                    # \number
                    'name' : 'keyword.other.group_reference_order.regex.{SCOPE}',
                    'match': r'\\[1-9]\d?'
                },
                {
                    # {2}, {2,}, {,2}, {2,3}, {2,3}?
                    'name' : 'keyword.operator.quantifier.regex.{SCOPE}',
                    'match': r'[?+*][?+]?|\{(\d+,\d+|\d+,|,\d+|\d+)\}\??'
                },
                {
                    'name' : 'keyword.operator.or.regex.{SCOPE}',
                    'match': r'\|'
                },
                {
                    # (?# comment)
                    'name' : 'comment.block.regex.{SCOPE}',
                    'begin': r'\(\?#',
                    'end'  : r'\)'
                },
                {
                    # flags: a: ASCII-only matching)
                    #        i: ignore case
                    #        L: locale dependent
                    #        m: multi-line
                    #        s: dot matches all
                    #        u: unicode
                    #        x: extended form (verbose)
                    'name' : 'keyword.other.option_toggle.regex.{SCOPE}',
                    'match': r'\(\?[aiLmsux]+\)'
                },
                {
                    'include': '#regular_expressions_escaped_characters'
                },
                {
                    'include': '#regular_expressions_character_classes'
                },
                {
                    'name' : 'keyword.operator.group.regex.{SCOPE}',
                    'match': r'[()]'
                }
            ]
        },
        'regular_expressions_character_classes':
        {
            'patterns':
            [
                {
                    # \w, \W, \s, \S, \d, \D, .
                    'name' : 'constant.character.character_class.regex.{SCOPE}',
                    'match': r'\\[wWsSdD]|\.'
                },
                {
                    # [set of characters]
                    'name' : 'constant.other.character_class.set.regex.{SCOPE}',
                    'begin': r'\[(\^)?(\](?=.*\]))?',
                    'beginCaptures':
                    {
                        1: {'name': 'keyword.operator.negation.regex.{SCOPE}'}
                    },
                    'patterns':
                    [
                        {
                            'name' : 'constant.character.escaped.special.regex.except.{SCOPE}',
                            'match': r'\[|\\\\|\\\]'
                        },
                        {'include': '#regular_expressions_character_classes'},
                        {'include': '#regular_expressions_escaped_characters'}
                    ],
                    'end': r'\]'
                }
            ]
        },
        'regular_expressions_escaped_characters':
        {
            'name' : 'constant.character.escaped.special.regex.{SCOPE}',
            'match': r'\\(\\|\?|\.|\*|\+|\{|\}|\||\(|\)|\[|\]|\^|\$)'
        }
    }
}
