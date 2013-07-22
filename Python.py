#!/usr/bin/python3
# -*- coding: utf8 -*-

#-- CHEASHEET -----------------------------------------------------------------#
# HOWTO: http://sublimetext.info/docs/en/reference/syntaxdefs.html
# REGEX: http://manual.macromates.com/en/regular_expressions

# Syntax Definition
syntax = {
    'name': 'Python 3',
    'comment': '\n\t\tWritten by Peter Varo (c)2013\n\t\thttp://github.com/petervaro/Python3\n\t',
    'scopeName': 'source.python',
    'fileTypes': ['py'],
    'keyEquivalent': '^~P',
    # hashbang
    'firstLineMatch': r'^#!/.*\bpython[\d.-]*\b',
    # Folding marks for the TextEditor
    'foldingStartMarker':
        r'^\s*(def|class)\s+([.\w>]+)\s*(\((.*)\))?\s*:|\{\s*$|\(\s*$|\[\s*$|^\s*"""(?=.)(?!.*""")',
    'foldingStopMarker':
        r'^\s*$|^\s*\}|^\s*\]|^\s*\)|^\s*"""\s*$',
    # Patterns
    'patterns':
    [
#-- COMMENT -------------------------------------------------------------------#
        {
            'name' : 'comment.line.hashmark.python',
            'match': r'#.*$\n?'
        },


#-- NUMBERS -------------------------------------------------------------------#
        {
            'name' : 'constant.numeric.integer.binary.python',
            'match': r'\b0b[01]+'
        },
        {
            'name' : 'constant.numeric.integer.hexadecimal.python',
            'match': r'\b0x\h+'
        },
        {
            'name' : 'constant.numeric.integer.octal.python',
            'match': r'\b0o[0-7]+'
        },
        {
            # .001  .1e6  .1E6  .1e+6  .1E+6  .1e-6  .1E-6
            'name' : 'constant.numeric.float_and_complex.decimal.floatnumber.python',
            'match': r'(?<=\W|^)\.\d+([eE][+-]?\d+)?[jJ]?'
        },
        {
            # 1.  1.0  1.1e6  1.1E6  1.1e+6  1.1E+6  1.1e-6  1.1E-6
            'name' : 'constant.numeric.float_and_complex.decimal.pointfloat.python',
            'match': r'\d+\.(\d+([eE][+-]?\d+)?)?[jJ]?'
        },
        {
            # 1e6  1E6  1e+6  1E+6  1e-6  1E-6
            'name' : 'constant.numeric.float_and_complex.decimal.exponent.python',
            'match': r'(?<![\.\d])\d+[eE][+-]?\d+[jJ]?'
        },
        {
            'name' : 'constant.numeric.integer_and_complex.decimal.python',
            'match': r'\b(?<!\.)([1-9]\d*|0)[jJ]?'
        },


#-- KEYWORDS ------------------------------------------------------------------#
        {
            'name' : 'storage.modifier.declaration.python',
            'match': r'\b(global|nonlocal)\b'
        },
        {
            'name' : 'keyword.control.import_and_import_from.python',
            'match': r'\b(import|from)\b'
        },
        {
            'name' : 'keyword.control.flow_block_delimiters.python',
            'match':
            (
                r'\b(elif|else|except|finally|for|if|try|while|'
                r'with|break|continue|pass|raise|return|yield)\b'
            )
        },
        {
            'name' : 'keyword.operator.bool.logical.python',
            'match': r'\b(and|in|is|not|or)\b'
        },
        {
            'name' : 'keyword.other.python',
            'match': r'\b(as|assert|del)\b'
        },


#-- OPERATORS -----------------------------------------------------------------#
        {
            'name' : 'keyword.operator.comparison.python',
            'match': r'<=|>=|==|<|>|!='
        },
        {
            'name' : 'keyword.operator.assignment.augmented.python',
            'match': r'\+=|-=|\*=|/=|//=|%=|&=|\|=|\^=|<<=|>>=|\*\*='
        },
        {
            'name' : 'keyword.operator.arithmetic.python',
            'match': r'\+|-|\*|\*\*|/|//|%|<<|>>|&|\||\^|~'
        },
        {
            'name' : 'keyword.operator.value_and_annotation_assignment.python',
            'match': r'=|->'
        },


#-- CLASS ---------------------------------------------------------------------#
        {
            'name' : 'meta.class.python',
            'begin': r'^\s*(class)\s+(?=[a-zA-Z_]\w*(\s*\()?)',
            'beginCaptures':
            {
                1: {'name': 'storage.type.class.python'}
            },
            'patterns':
            [
                {
                    'contentName': 'entity.name.type.class.python',
                    'begin': r'(?=[a-zA-Z_]\w*)',
                    'patterns':
                    [
                        {'include': '#entity_name_class'}
                    ],
                    'end': r'(?!\w)'
                },
                {
                    'contentName': 'meta.class.inheritance.python',
                    'begin': r'\(',
                    'patterns':
                    [
                        {
                            'contentName': 'entity.other.inherited-class.python',
                            'begin': r'(?<=\(|,)\s*',
                            'patterns':
                            [
                                {'include': '$self'}
                            ],
                            'end': r'\s*(?:,|(?=\)))',
                            'endCaptures':
                            {
                                1: {'name': 'punctuation.separator.inheritance.python'}
                            }
                        }
                    ],
                    'end': r'\)|:'
                }
            ],
            'end'  : r'(\)?\s*:|\s+([\w#\s:]+))',
            'endCaptures':
            {
                3: {'name': 'invalid.illegal.missing_section_begin.python'}
            }
        },


#-- FUNCTION ------------------------------------------------------------------#
        {
            'name' : 'meta.function.python',
            'begin': r'^\s*(def)\s+(?=[a-zA-Z_]\w*\s*\()',
            'beginCaptures':
            {
                1: {'name': 'storage.type.function.python'}
            },
            'patterns':
            [
                # Function name
                {
                    'contentName': 'entity.name.function.python',
                    'begin': r'(?=[a-zA-Z_]\w*)',
                    'patterns':
                    [
                        {'include': '#entity_name_function'}
                    ],
                    'end': r'(?!\w)'
                },
                # Arguments
                {
                    'begin': r'\(',
                    'patterns':
                    [
                        # Keyword arguments
                        {
                            'begin': r'\b([a-zA-Z_]\w*)\s*(=)',
                            'beginCaptures':
                            {
                                1: {'name': 'variable.parameter.function.python'},
                                2: {'name': 'keyword.operator.assignment.python'}
                            },
                            'patterns':
                            [
                                # Keyword assignment
                                {
                                    'begin': r'(?<=(=))\s*',
                                    'beginCaptures':
                                    {
                                        1: {'name': 'keyword.operator.assignment.python'}
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
                                        1: {'name': 'keyword.operator.assignment.python'}
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
                                1: {'name': 'variable.parameter.function.python'}
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
                # Annotation assignment (function)
                {
                    'begin': r'(?<=\))\s*(->)\s*',
                    'beginCaptures':
                    {
                        1: {'name': 'keyword.operator.annotation.assignment.python'}
                    },
                    'patterns':
                    [
                        {'include': '$self'}
                    ],
                    'end': r'(?=\s*:)'
                }
            ],
            # todo: add illegal
            'end': r'(\s*:)',
            'endCaptures':
            {
                2: {'name': 'invalid.illegal.missing_section_begin.python'}
            }
        },


#-- LAMBDA --------------------------------------------------------------------#
        {
            'name' : 'meta.function.anonymous.python',
            'begin': r'\b(lambda)',
            'beginCaptures':
            {
                1: {'name': 'storage.type.function.anonymous.python'}
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
                                1: {'name': 'variable.parameter.function.python'},
                                2: {'name': 'keyword.operator.assignment.python'}
                            },
                            'patterns':
                            [
                                {'include': '$self'}
                            ],
                            'end': r'(?=,|:)'
                        },
                        # Positional arguments
                        {
                            'name' : 'variable.parameter.function.python',
                            'match': r'\b[a-zA-Z_]\w*'
                        }
                    ],
                    'end': r'(?=,|:)'
                }
            ],
            'end': r':'
        },


#-- DECORATOR -----------------------------------------------------------------#
        # Decorator with arguments
        {
            'name' : 'meta.function.decorator.with_arguments.python',
            'begin': r'^\s*(@\s*[a-zA-Z_]\w*(\.[a-zA-Z_]\w*)*)\s*\(',
            'beginCaptures':
            {
                1: {'name': 'support.function.decorator.python'}
            },
            'patterns':
            [
                {'include': '#keyword_arguments'},
                {'include': '$self'}
            ],
            'end': r'\)'
        },
        # Decorator without arguments
        {
            'name' : 'meta.function.decorator.without_arguments.python',
            'begin': r'^\s*(@\s*[a-zA-Z_]\w*(\.[a-zA-Z_]\w*)*)',
            'beginCaptures':
            {
                1: {'name': 'support.function.decorator.python'}
            },
            'end': r'(?=\s|$\n?|#)'
        },

#-- CONSTANTS -----------------------------------------------------------------#
        {
            'name' : 'constant.language.word_like.python',
            'match': r'\b(None|True|False|Ellipsis|NotImplemented)\b'
        },
        {
            'name' : 'constant.language.symbol_like.python',
            'match': r'(?<=\W|^)\.\.\.(?=\W|$)'
        },


#-- STORAGES ------------------------------------------------------------------#
        {
            'name' : 'storage.type.function.python',
            'match': r'\b(def|lambda)\b'
        },
        {
            'name' : 'storage.type.class.python',
            'match': r'\b(class)\b'
        },


#-- BUILTINS ------------------------------------------------------------------#
        {
            'include': '#builtin_types'
        },
        {
            'include': '#builtin_functions'
        },
        {
            'include': '#builtin_exceptions'
        },


#-- MAGIC STUFFS --------------------------------------------------------------#
        {
            'include': '#magic_function_names'
        },
        {
            'include': '#magic_variable_names'
        },


#-- ETC -----------------------------------------------------------------------#
        {
            'include': '#line_continuation'
        },
        {
            'include': '#language_variables'
        },


#-- STRUCTURES ----------------------------------------------------------------#
        # LIST
        {
            'name': 'meta.structure.list.python',
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
        # GROUP
        {
            'begin': r'\(',
            'patterns':
            [
                {'include': '$self'}
            ],
            'end': r'\)'
        },
        # DICTINARY
        {
            'name': 'meta.structure.dictionary.python',
            'begin': r'{',
            'patterns':
            [
                {
                    'begin': r'(?<={|,|^)\s*(?![,}])',
                    'patterns':
                    [
                        {
                            'include': '$self'
                        }
                    ],
                    'end'  : r'\s*(?:(?=}|:))'
                },
                {
                    'begin': r'(?<=:|^)\s*',
                    'patterns':
                    [
                        {
                            'include': '$self'
                        }
                    ],
                    'end'  : r'\s*(?:(?=}|,))'
                }
            ],
            'end'  : r'}'
        },


#-- ACCESS --------------------------------------------------------------------#
        {
            'name' : 'meta.function_call.python',
            'begin': r'(\)|\]|[a-zA-Z_]\w*(?:\.[a-zA-Z_]\w*)*)\s*\(',
            'patterns':
            [
                {'include': '#keyword_arguments'},
                {'include': '$self'}
            ],
            'end': r'\)'
        },


#-- STRING --------------------------------------------------------------------#
        {
            'include': '#string_quoted'
        }
    ],


#-- REPOSITORY ----------------------------------------------------------------#
    'repository':
    {

#-- BUILTINS ------------------------------------------------------------------#
        'builtin_exceptions':
        {
            'name' : 'support.type.exception.python',
            'match':
            (
                r'\b('
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
        'builtin_functions':
        {
            'name' : 'support.function.builtin.python',
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
        # todo: rearrange -> what is builtin function and what is builtin type?
        'builtin_types':
        {
            'name' : 'support.type.python',
            'match':
            (
                r'\b('
                r'basestring|bool|buffer|bytearray|bytes|classmethod|complex|dict|'
                r'enumerate|file|float|frozenset|int|list|memoryview|object|open|'
                r'property|reversed|set|slice|staticmethod|str|super|tuple|type'
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
        'illegal_names':
        {
            'name' : 'invalid.illegal_names.name.python',
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
        'keyword_arguments':
        {
            'begin': r'\b([a-zA-Z_]\w*)\s*(=)',
            'beginCaptures':
            {
                1: {'name': 'variable.parameter.function.python'},
                2: {'name': 'keyword.operator.assignment.python'}
            },
            'patterns':
            [
                {'include': '$self'}
            ],
            'end': r'(?=,|[\n)])'
        },

#-- MAGIC STUFFS --------------------------------------------------------------#
        'magic_function_names':
        {
            'name' : 'support.function.magic.python',
            'match':
            (
                r'\b(__(?:'
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
                r')__)\b'
            )
        },
        # todo: rearrange -> what is magic function and what is magic variable?
        'magic_variable_names':
        {
            'name' : 'support.variable.magic.python',
            'match':
            (
                r'\b__('
                r'all|annotations|bases|class|debug|dict|doc|file|'
                r'members|metaclass|mro|name|qualname|slots|weakref'
                r')__\b'
            )
        },
        'language_variables':
        {
            'name' : 'variable.language.python',
            'match': r'\b(self|cls)\b'
        },
        'line_continuation':
        {
            'match': r'(\\)(.*)$\n?',
            'captures':
            {
                1: {'name': 'punctuation.separator.continuation.line.python'},
                2: {'name': 'invalid.illegal.unexpected_text.python'}
            }
        },

#-- STRING --------------------------------------------------------------------#
        # todo: decide if source.sql and special words, like SELECT and INSERT needed
        'string_quoted':
        {
            # stringprefix:  "r"  | "u"  | "R"  | "U"  |
            # bytesprefix :  "b"  | "B"  | "br" | "Br" | "bR" |
            #                "BR" | "rb" | "rB" | "Rb" | "RB" |
            'patterns':
            [
                # Single BLOCK
                {
                    'name' : 'string.quoted.single.block.python',
                    'begin': r"([bBuU]?)'''",
                    'beginCaptures':
                    {
                        1: {'name': 'storage.type.string.prefix.python'}
                    },
                    'patterns':
                    [
                        {'include': '#string_patterns'}
                    ],
                    'end': r"'''|('|'')",
                    'endCaptures':
                    {
                        1: {'name': 'invalid.illegal.unclosed_string.python'}
                    }
                },
                {
                    'name' : 'string.quoted.single.block.python',
                    'begin': r"([rR][bB]|[bB][rR]|[rR])'''",
                    'beginCaptures':
                    {
                        1: {'name': 'storage.type.string.prefix.python'}
                    },
                    'patterns':
                    [
                        {'include': '#string_patterns'},
                        {'include': '#regular_expressions'}
                    ],
                    'end': r"'''|('|'')",
                    'endCaptures':
                    {
                        1: {'name': 'invalid.illegal.unclosed_string.python'}
                    }
                },

                # Single LINE
                {
                    'name' : 'string.quoted.single.line.python',
                    'begin': r"([bBuU]?)'",
                    'beginCaptures':
                    {
                        1: {'name': 'storage.type.string.prefix.python'}
                    },
                    'patterns':
                    [
                        {'include': '#string_patterns'}
                    ],
                    'end': r"'|(\n)",
                    'endCaptures':
                    {
                        1: {'name': 'invalid.illegal.unclosed_string.python'}
                    }
                },
                {
                    'name' : 'string.quoted.single.line.python',
                    'begin': r"([rR][bB]|[bB][rR]|[rR])'",
                    'beginCaptures':
                    {
                        1: {'name': 'storage.type.string.prefix.python'}
                    },
                    'patterns':
                    [
                        {'include': '#string_patterns'},
                        {'include': '#regular_expressions'}
                    ],
                    'end': r"'|(\n)",
                    'endCaptures':
                    {
                        1: {'name': 'invalid.illegal.unclosed_string.python'}
                    }
                },

                # Double BLOCK
                {
                    'name' : 'string.quoted.double.block.python',
                    'begin': r'([bBuU]?)"""',
                    'beginCaptures':
                    {
                        1: {'name': 'storage.type.string.prefix.python'}
                    },
                    'patterns':
                    [
                        {'include': '#string_patterns'}
                    ],
                    'end': r'"""|("|"")',
                    'endCaptures':
                    {
                        1: {'name': 'invalid.illegal.unclosed_string.python'}
                    }
                },
                {
                    'name' : 'string.quoted.double.block.python',
                    'begin': r'([rR][bB]|[bB][rR]|[rR])"""',
                    'beginCaptures':
                    {
                        1: {'name': 'storage.type.string.prefix.python'}
                    },
                    'patterns':
                    [
                        {'include': '#string_patterns'},
                        {'include': '#regular_expressions'}
                    ],
                    'end': r'"""|("|"")',
                    'endCaptures':
                    {
                        1: {'name': 'invalid.illegal.unclosed_string.python'}
                    }
                },

                # Double LINE
                {
                    'name' : 'string.quoted.double.line.python',
                    'begin': r'([bBuU]?)"',
                    'beginCaptures':
                    {
                        1: {'name': 'storage.type.string.prefix.python'}
                    },
                    'patterns':
                    [
                        {'include': '#string_patterns'}
                    ],
                    'end': r'"|(\n)',
                    'endCaptures':
                    {
                        1: {'name': 'invalid.illegal.unclosed_string.python'}
                    }
                },
                # {
                #     'name' : 'meta.format_attribute.format.python',
                #     'begin': r'(\.format)\s*\(',
                #     'beginCaptures':
                #     {
                #         1: {'name': 'invalid.illegal.none.python'}
                #     },
                #     'patterns':
                #     [
                #         {
                #             'name' : 'string.quoted.double.format.python',
                #             'begin': r'([uUbB]?)"',
                #             'beginCaptures':
                #             {
                #                 1: {'name': 'storage.type.string.prefix.python'}
                #             },
                #             'patterns':
                #             [
                #                 {'include': '#string_patterns'},
                #                 {'include': '#format_mini_language'}
                #             ],
                #             'end': r'"|(\n)',
                #             'endCaptures':
                #             {
                #                 1: {'name': 'invalid.illegal.unclosed_string.python'}
                #             }
                #         }
                #     ],
                #     'end': r'\)'
                # },
                # {
                #     'name' : 'string.quoted.double.format.python',
                #     'begin': r'([uUbB]?)"',
                #     'beginCaptures':
                #     {
                #         1: {'name': 'storage.type.string.prefix.python'}
                #     },
                #     'patterns':
                #     [
                #         {'include': '#string_patterns'},
                #         {'include': '#format_mini_language'}
                #     ],
                #     'end': r'"\.format',  # |(\n)',
                #     'endCaptures':
                #     {
                #         2: {'name': 'invalid.illegal.unclosed_string.python'}
                #     }
                # },
                {
                    'name' : 'string.quoted.double.line.python',
                    'begin': r'([rR][bB]|[bB][rR]|[rR])"',
                    'beginCaptures':
                    {
                        1: {'name': 'storage.type.string.prefix.python'}
                    },
                    'patterns':
                    [
                        {'include': '#string_patterns'},
                        {'include': '#regular_expressions'}
                    ],
                    'end': r'"|(\n)',
                    'endCaptures':
                    {
                        1: {'name': 'invalid.illegal.unclosed_string.python'}
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
            'name' : 'string.interpolated.placeholder.python',
            'match': r'%(\(\w+\))?#?0?-?[ ]?\+?(\d*|\*)(\.(\d*|\*))?[hlL]?[diouxXeEfFgGcrs%]'
        },
        'format_mini_language':
        {
            'patterns':
            [
                {
                    'name' : 'constant.other.placeholder.format.python',
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
            'name' : 'constant.character.escaped.special.python',
            'match': r'\\(x\h{2}|[0-7]{3}|\n|\"|\'|a|b|f|n|r|t|v|\\)'
        },
        'escaped_unicode_characters':
        {
            # 16bit hex | 32bit hex | unicodename
            'name' : 'constant.character.escaped.python',
            'match': r'\\(u\h{4}|U\h{8}|N\{[a-zA-Z\s]+\})'
        },

#-- REGEX ---------------------------------------------------------------------#
        'regular_expressions':
        {
            'patterns':
            [
                {
                    'name' : 'keyword.control.anchor.regex.python',
                    'match': r'\\[bBAZzG]|\^|\$'
                },
                {
                    # \number
                    'name' : 'keyword.other.group_reference_order.regex.python',
                    'match': r'\\[1-9]\d?'
                },
                {
                    # (?P=this_is_a_group)
                    'name' : 'keyword.other.group_reference_name.regex.python',
                    'match': r'\(\?P=[a-zA-Z_]\w*\)'
                },
                {
                    # {2}, {2,}, {,2}, {2,3}, {2,3}?
                    'name' : 'keyword.operator.quantifier.regex.python',
                    'match': r'[?+*][?+]?|\{(\d+,\d+|\d+,|,\d+|\d+)\}\??'
                },
                {
                    'name' : 'keyword.operator.or.regex.python',
                    'match': r'\|'
                },
                {
                    # (?# comment)
                    'name' : 'comment.block.regex.python',
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
                    'name' : 'keyword.other.option_toggle.regex.python',
                    'match': r'\(\?[aiLmsux]+\)'
                },
                {
                    # (?=  positive look-ahead)
                    # (?!  negative look-ahead)
                    # (?<= positive look-behind)
                    # (?<! negative look-behind)
                    # (?:  non-capturing)
                    # (?P<id> group)
                    # (?(id/name)yes-pattern|no-pattern)
                    'name' : 'meta.group.assertion.regex.python',
                    'begin': r'\(\?(=|!|<=|<!|:|P<[a-z]\w*>|\(([1-9]\d?|[a-zA-Z_]\w*\)))?',
                    'patterns':
                    [
                        {'include': '#regular_expressions'}
                    ],
                    'end': r'\)'
                },
                {
                    'include': '#regular_expressions_escaped_characters'
                },
                {
                    'include': '#regular_expressions_character_classes'
                }
            ]
        },
        'regular_expressions_character_classes':
        {
            'patterns':
            [
                {
                    # \w, \W, \s, \S, \d, \D, .
                    'name' : 'constant.character.character_class.regex.python',
                    'match': r'\\[wWsSdD]|\.'
                },
                {
                    # [set of characters]
                    'name' : 'constant.other.character_class.set.regex.python',
                    'begin': r'\[(\^)?',
                    'beginCaptures':
                    {
                        1: {'name': 'keyword.operator.negation.regex.python'}
                    },
                    'patterns':
                    [
                        {'include': '#regular_expressions_character_classes'},
                        {'include': '#regular_expressions_escaped_characters'}
                        # {
                        #    'name' : 'constant.other.character_class.special.regex.python',
                        #    'match': r'\]'
                        # }
                    ],
                    'end': r'\]'
                }
            ]
        },
        'regular_expressions_escaped_characters':
        {
            'name' : 'constant.character.escaped.special.regex.python',
            'match': r'\\(\?|\.|\*|\+|\{|\}|\||\(|\)|\[|\]|\^|\$)'
        }
    },
    'uuid': '851B1429-B8B4-4C1E-8030-399BDA994393'
}

if __name__ == '__main__':
    import convert
    convert.dict_to_lang(
        dictionary = syntax,
        name  = 'Python',
        path  = '~/Library/Application Support/Sublime Text 3/Packages/Python/',
        local = True
    )
