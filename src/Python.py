#!/usr/bin/python3
# -*- coding: utf8 -*-

#-- CHEASHEET -----------------------------------------------------------------#
# HOWTO: http://sublimetext.info/docs/en/reference/syntaxdefs.html
# REGEX: http://manual.macromates.com/en/regular_expressions

# Syntax Definition
syntax = {
    'name': 'Python 3',
    'comment': '\n\t\tWritten by Peter Varo (c)2013-2014\n\t\thttp://github.com/petervaro/python\n\t',
    'scopeName': 'source.python3',
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
            'name' : 'comment.line.hashmark.python3',
            'match': r'#.*$\n?'
        },


#-- NUMBERS -------------------------------------------------------------------#
        {
            'name' : 'constant.numeric.integer.binary.python3',
            'match': r'\b0b[01]+'
        },
        {
            'name' : 'constant.numeric.integer.hexadecimal.python3',
            'match': r'\b0x\h+'
        },
        {
            'name' : 'constant.numeric.integer.octal.python3',
            'match': r'\b0o[0-7]+'
        },
        {
            # .001  .1e6  .1E6  .1e+6  .1E+6  .1e-6  .1E-6
            'name' : 'constant.numeric.float_and_complex.decimal.floatnumber.python3',
            'match': r'(?<=\W|^)\.\d+([eE][+-]?\d+)?[jJ]?'
        },
        {
            # 1.  1.0  1.e10  1.1e6  1.1E6  1.1e+6  1.1E+6  1.1e-6  1.1E-6
            'name' : 'constant.numeric.float_and_complex.decimal.pointfloat.python3',
            'match': r'\d+\.(\d*([eE][+-]?\d+)?)?[jJ]?(?=\W)'
        },
        {
            # 1e6  1E6  1e+6  1E+6  1e-6  1E-6
            'name' : 'constant.numeric.float_and_complex.decimal.exponent.python3',
            'match': r'(?<![\.\d])\d+[eE][+-]?\d+[jJ]?'
        },
        {
            'name' : 'constant.numeric.integer_and_complex.decimal.python3',
            'match': r'\b(?<!\.)([1-9]\d*|0)[jJ]?'
        },


#-- KEYWORDS ------------------------------------------------------------------#
        {
            'name' : 'storage.modifier.declaration.python3',
            'match': r'\b(global|nonlocal)\b'
        },
        {
            'name' : 'keyword.control.import_and_import_from.python3',
            'match': r'\b(import|from)\b'
        },
        {
            'name' : 'keyword.control.flow_block_delimiters.python3',
            'match':
            (
                r'\b(elif|else|except|finally|for|if|try|while|'
                r'with|break|continue|pass|raise|return|yield)\b'
            )
        },
        {
            'name' : 'keyword.operator.bool.logical.python3',
            'match': r'\b(and|in|is|not|or)\b'
        },
        {
            'name' : 'keyword.other.python3',
            'match': r'\b(as|assert|del)\b'
        },


#-- OPERATORS -----------------------------------------------------------------#
        {
            'name' : 'keyword.operator.comparison.python3',
            'match': r'<=|>=|==|<|>|!='
        },
        {
            'name' : 'keyword.operator.assignment.augmented.python3',
            'match': r'\+=|-=|\*=|/=|//=|%=|&=|\|=|\^=|<<=|>>=|\*\*='
        },
        {
            'name' : 'keyword.operator.arithmetic.python3',
            'match': r'\+|-|\*|\*\*|/|//|%|<<|>>|&|\||\^|~'
        },
        {
            'name' : 'keyword.operator.value_and_annotation_assignment.python3',
            'match': r'=|->'
        },


#-- CLASS ---------------------------------------------------------------------#
        {
            'name' : 'meta.class.python3',
            'begin': r'^\s*(class)\s+(?=[a-zA-Z_]\w*(\s*\()?)',
            'beginCaptures':
            {
                1: {'name': 'storage.type.class.python3'}
            },
            'patterns':
            [
                {
                    'contentName': 'entity.name.type.class.python3',
                    'begin': r'(?=[a-zA-Z_]\w*)',
                    'patterns':
                    [
                        {'include': '#entity_name_class'}
                    ],
                    'end': r'(?!\w)'
                },
                {
                    'contentName': 'meta.class.inheritance.python3',
                    'begin': r'\(',
                    'patterns':
                    [
                        {
                            'contentName': 'entity.other.inherited-class.python3',
                            'begin': r'(?<=\(|,)\s*',
                            'patterns':
                            [
                                {'include': '$self'}
                            ],
                            'end': r'\s*(?:,|(?=\)))',
                            'endCaptures':
                            {
                                1: {'name': 'punctuation.separator.inheritance.python3'}
                            }
                        }
                    ],
                    'end': r'\)|:'
                }
            ],
            'end'  : r'(\)?\s*:|\s+([\w#\s:]+))',
            'endCaptures':
            {
                3: {'name': 'invalid.illegal.missing_section_begin.python3'}
            }
        },


#-- FUNCTION ------------------------------------------------------------------#
        {
            'name' : 'meta.function.python3',
            'begin': r'^\s*(def)\s+(?=[a-zA-Z_]\w*\s*\()',
            'beginCaptures':
            {
                1: {'name': 'storage.type.function.python3'}
            },
            'patterns':
            [
                # Function name
                {
                    'contentName': 'entity.name.function.python3',
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
                                1: {'name': 'variable.parameter.function.python3'},
                                2: {'name': 'keyword.operator.assignment.python3'}
                            },
                            'patterns':
                            [
                                # Keyword assignment
                                {
                                    'begin': r'(?<=(=))\s*',
                                    'beginCaptures':
                                    {
                                        1: {'name': 'keyword.operator.assignment.python3'}
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
                                        1: {'name': 'keyword.operator.assignment.python3'}
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
                                1: {'name': 'variable.parameter.function.python3'}
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
                        1: {'name': 'keyword.operator.annotation.assignment.python3'}
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
                2: {'name': 'invalid.illegal.missing_section_begin.python3'}
            }
        },


#-- LAMBDA --------------------------------------------------------------------#
        {
            'name' : 'meta.function.anonymous.python3',
            'begin': r'\b(lambda)',
            'beginCaptures':
            {
                1: {'name': 'storage.type.function.anonymous.python3'}
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
                                1: {'name': 'variable.parameter.function.python3'},
                                2: {'name': 'keyword.operator.assignment.python3'}
                            },
                            'patterns':
                            [
                                {'include': '$self'}
                            ],
                            'end': r'(?=,|:)'
                        },
                        # Positional arguments
                        {
                            'name' : 'variable.parameter.function.python3',
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
        {
            'name' : 'meta.function.decorator.with_arguments.python3',
            'begin': r'^\s*(@\s*[a-zA-Z_]\w*(\.[a-zA-Z_]\w*)*)\s*\(',
            'beginCaptures':
            {
                1: {'name': 'support.function.decorator.python3'}
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
            'name' : 'meta.function.decorator.without_arguments.python3',
            'begin': r'^\s*(@\s*[a-zA-Z_]\w*(\.[a-zA-Z_]\w*)*)',
            'beginCaptures':
            {
                1: {'name': 'support.function.decorator.python3'}
            },
            'end': r'(?=\s|$\n?|#)'
        },

#-- CONSTANTS -----------------------------------------------------------------#
        {
            'name' : 'constant.language.word_like.python3',
            'match': r'\b(None|True|False|Ellipsis|NotImplemented)\b'
        },
        {
            'name' : 'constant.language.symbol_like.python3',
            'match': r'(?<=\W|^)\.\.\.(?=\W|$)'
        },


#-- STORAGES ------------------------------------------------------------------#
        {
            'name' : 'storage.type.function.python3',
            'match': r'\b(def|lambda)\b'
        },
        {
            'name' : 'storage.type.class.python3',
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
            'name': 'meta.structure.list.python3',
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
        {
            'name': 'meta.structure.dictionary.python3',
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
                    'end'  : r'\s*(?:(?=\})|(\:))'
                },
                {
                    'begin': r'(?<=:|^)\s*',
                    'patterns':
                    [
                        {
                            'include': '$self'
                        }
                    ],
                    'end'  : r'\s*(?:(?=\}|,))'
                }
            ],
            'end'  : r'}'
        },
        # GROUPS, TUPLES
        {
            'name' : 'meta.structure.group.python3',
            'begin': r'(?<=,|;|=|\+|-|\*|/|\||:|<|>|~|%|\^|\\)\s*\(',
            'patterns':
            [
                {'include': '$self'}
            ],
            'end': r'\)'
        },

#-- ACCESS --------------------------------------------------------------------#
        {
            'name' : 'meta.function_call.python3',
            'begin': r'(?<!:|,|;|\[|\{|\}|=|\+|-|\*|/|\||<|>|~|%|\^|\\|\n)\s*\(',
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
            'name' : 'support.type.exception.python3',
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
        'builtin_functions':
        {
            'name' : 'support.function.builtin.python3',
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
            'name' : 'support.type.python3',
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
            'name' : 'invalid.illegal_names.name.python3',
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
            'begin': r'\b([a-zA-Z_]\w*)\s*(=)(?!=)',
            'beginCaptures':
            {
                1: {'name': 'variable.parameter.function.python3'},
                2: {'name': 'keyword.operator.assignment.python3'}
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
            'name' : 'support.function.magic.python3',
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
        # todo: rearrange -> what is magic function and what is magic variable?
        'magic_variable_names':
        {
            'name' : 'support.variable.magic.python3',
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
            'name' : 'variable.language.python3',
            'match': r'(?<!\.)\b(self|cls)\b'
        },
        'line_continuation':
        {
            'match': r'(\\)(.*)$\n?',
            'captures':
            {
                1: {'name': 'punctuation.separator.continuation.line.python3'},
                2: {'name': 'invalid.illegal.unexpected_text.python3'}
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
                    'name' : 'string.quoted.single.block.python3',
                    'begin': r"([bBuU]?)'''",
                    'beginCaptures':
                    {
                        1: {'name': 'storage.type.string.prefix.python3'}
                    },
                    'patterns':
                    [
                        {'include': '#string_patterns'}
                    ],
                    'end': r"'''"
                },
                {
                    'name' : 'string.quoted.single.block.python3',
                    'begin': r"([rR][bB]|[bB][rR]|[rR])'''",
                    'beginCaptures':
                    {
                        1: {'name': 'storage.type.string.prefix.python3'}
                    },
                    'patterns':
                    [
                        {'include': '#string_patterns'},
                        {'include': '#regular_expressions'}
                    ],
                    'end': r"'''"
                },

                # Single LINE
                {
                    'name' : 'string.quoted.single.line.python3',
                    'begin': r"([bBuU]?)'",
                    'beginCaptures':
                    {
                        1: {'name': 'storage.type.string.prefix.python3'}
                    },
                    'patterns':
                    [
                        {'include': '#string_patterns'}
                    ],
                    'end': r"'|(\n)",
                    'endCaptures':
                    {
                        1: {'name': 'invalid.illegal.unclosed_string.python3'}
                    }
                },
                {
                    'name' : 'string.quoted.single.line.python3',
                    'begin': r"([rR][bB]|[bB][rR]|[rR])'",
                    'beginCaptures':
                    {
                        1: {'name': 'storage.type.string.prefix.python3'}
                    },
                    'patterns':
                    [
                        {'include': '#string_patterns'},
                        {'include': '#regular_expressions'}
                    ],
                    'end': r"'|(\n)",
                    'endCaptures':
                    {
                        1: {'name': 'invalid.illegal.unclosed_string.python3'}
                    }
                },

                # Double BLOCK
                {
                    'name' : 'string.quoted.double.block.python3',
                    'begin': r'([bBuU]?)"""',
                    'beginCaptures':
                    {
                        1: {'name': 'storage.type.string.prefix.python3'}
                    },
                    'patterns':
                    [
                        {'include': '#string_patterns'}
                    ],
                    'end': r'"""'
                },
                {
                    'name' : 'string.quoted.double.block.python3',
                    'begin': r'([rR][bB]|[bB][rR]|[rR])"""',
                    'beginCaptures':
                    {
                        1: {'name': 'storage.type.string.prefix.python3'}
                    },
                    'patterns':
                    [
                        {'include': '#string_patterns'},
                        {'include': '#regular_expressions'}
                    ],
                    'end': r'"""'
                },

                # Double LINE
                {
                    'name' : 'string.quoted.double.line.python3',
                    'begin': r'([bBuU]?)"',
                    'beginCaptures':
                    {
                        1: {'name': 'storage.type.string.prefix.python3'}
                    },
                    'patterns':
                    [
                        {'include': '#string_patterns'}
                    ],
                    'end': r'"|(\n)',
                    'endCaptures':
                    {
                        1: {'name': 'invalid.illegal.unclosed_string.python3'}
                    }
                },
                # {
                #     'name' : 'meta.format_attribute.format.python3',
                #     'begin': r'(\.format)\s*\(',
                #     'beginCaptures':
                #     {
                #         1: {'name': 'invalid.illegal.none.python3'}
                #     },
                #     'patterns':
                #     [
                #         {
                #             'name' : 'string.quoted.double.format.python3',
                #             'begin': r'([uUbB]?)"',
                #             'beginCaptures':
                #             {
                #                 1: {'name': 'storage.type.string.prefix.python3'}
                #             },
                #             'patterns':
                #             [
                #                 {'include': '#string_patterns'},
                #                 {'include': '#format_mini_language'}
                #             ],
                #             'end': r'"|(\n)',
                #             'endCaptures':
                #             {
                #                 1: {'name': 'invalid.illegal.unclosed_string.python3'}
                #             }
                #         }
                #     ],
                #     'end': r'\)'
                # },
                # {
                #     'name' : 'string.quoted.double.format.python3',
                #     'begin': r'([uUbB]?)"',
                #     'beginCaptures':
                #     {
                #         1: {'name': 'storage.type.string.prefix.python3'}
                #     },
                #     'patterns':
                #     [
                #         {'include': '#string_patterns'},
                #         {'include': '#format_mini_language'}
                #     ],
                #     'end': r'"\.format',  # |(\n)',
                #     'endCaptures':
                #     {
                #         2: {'name': 'invalid.illegal.unclosed_string.python3'}
                #     }
                # },
                {
                    'name' : 'string.quoted.double.line.python3',
                    'begin': r'([rR][bB]|[bB][rR]|[rR])"',
                    'beginCaptures':
                    {
                        1: {'name': 'storage.type.string.prefix.python3'}
                    },
                    'patterns':
                    [
                        {'include': '#string_patterns'},
                        {'include': '#regular_expressions'}
                    ],
                    'end': r'"|(\n)',
                    'endCaptures':
                    {
                        1: {'name': 'invalid.illegal.unclosed_string.python3'}
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
            'name' : 'string.interpolated.placeholder.python3',
            'match': r'%(\(\w+\))?#?0?-?[ ]?\+?(\d*|\*)(\.(\d*|\*))?[hlL]?[diouxXeEfFgGcrs%]'
        },
        'format_mini_language':
        {
            'patterns':
            [
                {
                    'name' : 'constant.other.placeholder.format.python3',
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
            'name' : 'constant.character.escaped.special.python3',
            'match': r'\\(x\h{2}|[0-7]{3}|\n|\"|\'|a|b|f|n|r|t|v|\\)'
        },
        'escaped_unicode_characters':
        {
            # 16bit hex | 32bit hex | unicodename
            'name' : 'constant.character.escaped.python3',
            'match': r'\\(u\h{4}|U\h{8}|N\{[a-zA-Z\s]+\})'
        },

#-- REGEX ---------------------------------------------------------------------#
        'regular_expressions':
        {
            'patterns':
            [
                {
                    'name' : 'keyword.control.anchor.regex.python3',
                    'match': r'\\[bBAZzG]|\^|\$'
                },
                {
                    # \number
                    'name' : 'keyword.other.group_reference_order.regex.python3',
                    'match': r'\\[1-9]\d?'
                },
                {
                    # (?P=this_is_a_group)
                    'name' : 'keyword.other.group_reference_name.regex.python3',
                    'match': r'\(\?P=[a-zA-Z_]\w*\)'
                },
                {
                    # {2}, {2,}, {,2}, {2,3}, {2,3}?
                    'name' : 'keyword.operator.quantifier.regex.python3',
                    'match': r'[?+*][?+]?|\{(\d+,\d+|\d+,|,\d+|\d+)\}\??'
                },
                {
                    'name' : 'keyword.operator.or.regex.python3',
                    'match': r'\|'
                },
                {
                    # (?# comment)
                    'name' : 'comment.block.regex.python3',
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
                    'name' : 'keyword.other.option_toggle.regex.python3',
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
                    'name' : 'meta.group.assertion.regex.python3',
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
                    'name' : 'constant.character.character_class.regex.python3',
                    'match': r'\\[wWsSdD]|\.'
                },
                {
                    # [set of characters]
                    'name' : 'constant.other.character_class.set.regex.python3',
                    'begin': r'\[(\^)?(\](?=.*\]))?',
                    'beginCaptures':
                    {
                        1: {'name': 'keyword.operator.negation.regex.python3'}
                    },
                    'patterns':
                    [
                        {
                            'name': 'constant.character.escaped.special.open.regex.python3',
                            'match': r'\['
                        },
                        {'include': '#regular_expressions_character_classes'},
                        {'include': '#regular_expressions_escaped_characters'}

                    ],
                    'end': r'(?<!\\)\]'
                }
            ]
        },
        'regular_expressions_escaped_characters':
        {
            'name' : 'constant.character.escaped.special.regex.python3',
            'match': r'\\(\\|\?|\.|\*|\+|\{|\}|\||\(|\)|\[|\]|\^|\$)'
        }
    },
    'uuid': '851B1429-B8B4-4C1E-8030-399BDA994393'
}

if __name__ == '__main__':
    import convert
    rname = 'Python3'
    tname = 'Python3_TEST'
    convert.dict_to_lang(dictionary=syntax,
                         repo_fname=rname,
                         repo_dname=rname,
                         test_fname=tname,
                         test_dname=tname,
                         test_fpath='~/Library/Application Support/'
                                    'Sublime Text 3/Packages/User/{}/'.format(tname))
