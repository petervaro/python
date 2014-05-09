#!/usr/bin/python3
# -*- coding: utf8 -*-

#-- CHEASHEET -----------------------------------------------------------------#
# HOWTO: http://sublimetext.info/docs/en/reference/syntaxdefs.html
# REGEX: http://manual.macromates.com/en/regular_expressions

# Syntax Definition
syntax = {
    'name': 'Cython',
    'comment': '\n\t\tWritten by Peter Varo (c)2013-2014\n\t\thttp://github.com/petervaro/python\n\t',
    'scopeName': 'source.cython',
    'fileTypes': ['pyx', 'pxi', 'pxd'],
    'keyEquivalent': '^~C',
    # hashbang
    'firstLineMatch': r'^#!/.*\bpython[\d.-]*\b',
    # Folding marks for the TextEditor
    'foldingStartMarker':
        r'^\s*((cp?)?def|class)\s+([.\w>]+)\s*(\((.*)\))?\s*:|\{\s*$|\(\s*$|\[\s*$|^\s*"""(?=.)(?!.*""")',
    'foldingStopMarker':
        r'^\s*$|^\s*\}|^\s*\]|^\s*\)|^\s*"""\s*$',
    # Patterns
    'patterns':
    [
#-- COMMENT -------------------------------------------------------------------#
        {
            'name' : 'comment.line.hashmark.cython',
            'match': r'#.*$\n?'
        },


#-- NUMBERS -------------------------------------------------------------------#
        {
            'name' : 'constant.numeric.integer.binary.cython',
            'match': r'\b0b[01]+'
        },
        {
            'name' : 'constant.numeric.integer.hexadecimal.cython',
            'match': r'\b0x\h+'
        },
        {
            'name' : 'constant.numeric.integer.octal.cython',
            'match': r'\b0o[0-7]+'
        },
        {
            # .001  .1e6  .1E6  .1e+6  .1E+6  .1e-6  .1E-6
            'name' : 'constant.numeric.float_and_complex.decimal.floatnumber.cython',
            'match': r'(?<=\W|^)\.\d+([eE][+-]?\d+)?[jJ]?'
        },
        {
            # 1.  1.0  1.1e6  1.1E6  1.1e+6  1.1E+6  1.1e-6  1.1E-6
            'name' : 'constant.numeric.float_and_complex.decimal.pointfloat.cython',
            'match': r'\d+\.(\d*([eE][+-]?\d+)?)?[jJ]?(?=\W)'
        },
        {
            # 1e6  1E6  1e+6  1E+6  1e-6  1E-6
            'name' : 'constant.numeric.float_and_complex.decimal.exponent.cython',
            'match': r'(?<![\.\d])\d+[eE][+-]?\d+[jJ]?'
        },
        {
            'name' : 'constant.numeric.integer_and_complex.decimal.cython',
            'match': r'\b(?<!\.)([1-9]\d*|0)[jJ]?'
        },


#-- KEYWORDS ------------------------------------------------------------------#
        {
            'name' : 'storage.modifier.declaration.cython',
            'match':
            (
                r'\b(global|nonlocal|gil|nogil|extern|api|public|readonly|'
                r'const(\svolatile)?|inline)\b'
            )
        },
        {
            'name' : 'keyword.control.import_and_import_from.cython',
            'match': r'\b(cimport|include|extern|import|from)\b'
        },
        {
            'name' : 'keyword.control.flow_block_delimiters.cython',
            'match':
            (
                r'\b(elif|else|except|finally|for|if|try|while|with|break|'
                r'continue|pass|raise|return|yield|IF|ELIF|ELSE|DEF)\b'
            )
        },
        {
            'name' : 'keyword.operator.bool.logical.cython',
            'match': r'\b(and|in|is|not|or)\b'
        },
        {
            'name' : 'keyword.other.cython',
            'match': r'\b(as|assert|by|del)\b'
        },


#-- OPERATORS -----------------------------------------------------------------#
        {
            'name' : 'keyword.operator.comparison.cython',
            'match': r'<=|>=|==|<|>|!='
        },
        {
            'name' : 'keyword.operator.assignment.augmented.cython',
            'match': r'\+=|-=|\*=|/=|//=|%=|&=|\|=|\^=|<<=|>>=|\*\*='
        },
        {
            'name' : 'keyword.operator.arithmetic.cython',
            'match': r'\+|-|\*|\*\*|/|//|%|<<|>>|&|\||\^|~'
        },
        {
            'name' : 'keyword.operator.value_and_annotation_assignment.cython',
            'match': r'=|->'
        },
        {
            'name' : 'keyword.operator.type_test.cython',
            'match': r'\?'
        },


#-- CLASS ---------------------------------------------------------------------#
        {
            'name' : 'meta.class.cython',
            'begin': r'^\s*(cdef\s+)?(class)\s+(?=[a-zA-Z_]\w*(\s*\()?)',
            'beginCaptures':
            {
                1: {'name': 'storage.type.class.definition.cython'},
                2: {'name': 'storage.type.class.cython'}
            },
            'patterns':
            [
                {
                    'contentName': 'entity.name.type.class.cython',
                    'begin': r'(?=[a-zA-Z_]\w*)',
                    'patterns':
                    [
                        {'include': '#entity_name_class'}
                    ],
                    'end': r'(?!\w)'
                },
                {
                    'contentName': 'meta.class.inheritance.cython',
                    'begin': r'\(',
                    'patterns':
                    [
                        {
                            'contentName': 'entity.other.inherited-class.cython',
                            'begin': r'(?<=\(|,)\s*',
                            'patterns':
                            [
                                {'include': '$self'}
                            ],
                            'end': r'\s*(?:,|(?=\)))',
                            'endCaptures':
                            {
                                1: {'name': 'punctuation.separator.inheritance.cython'}
                            }
                        }
                    ],
                    'end': r'\)|:'
                }
            ],
            'end'  : r'(\)?\s*:|\s+([\w#\s:]+))',
            'endCaptures':
            {
                3: {'name': 'invalid.illegal.missing_section_begin.cython'}
            }
        },


#-- FUNCTION ------------------------------------------------------------------#
        {
            'name' : 'meta.function.cython',
            'begin': r'^\s*((cp?)?def)\s+(?=[a-zA-Z_]\w*\s*\()',
            'beginCaptures':
            {
                1: {'name': 'storage.type.function.cython'}
            },
            'patterns':
            [
                # Type declaration
                # Function name
                {
                    'contentName': 'entity.name.function.cython',
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
                                1: {'name': 'variable.parameter.function.cython'},
                                2: {'name': 'keyword.operator.assignment.cython'}
                            },
                            'patterns':
                            [
                                # Keyword assignment
                                {
                                    'begin': r'(?<=(=))\s*',
                                    'beginCaptures':
                                    {
                                        1: {'name': 'keyword.operator.assignment.cython'}
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
                                        1: {'name': 'keyword.operator.assignment.cython'}
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
                                1: {'name': 'variable.parameter.function.cython'}
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
                # Global Interpreter Lock
                {
                    'begin': r'\)\s*(nogil)\s*',
                    'beginCaptures':
                    {
                        1: {'name': 'storage.modifier.declaration.cython'}
                    },
                    'end': r'\s*((->)|:|\n+)'
                },
                # Annotation assignment (function)
                {
                    'begin': r'(?<=\))\s*(->)\s*',
                    'beginCaptures':
                    {
                        1: {'name': 'keyword.operator.annotation.assignment.cython'}
                    },
                    'patterns':
                    [
                        {'include': '$self'}
                    ],
                    'end': r'(?=\s*:)'
                }
            ],
            # todo: add illegal
            'end': r'(\s*:|\n+)',
            'endCaptures':
            {
                2: {'name': 'invalid.illegal.missing_section_begin.cython'}
            }
        },

#-- LAMBDA --------------------------------------------------------------------#
        {
            'name' : 'meta.function.anonymous.cython',
            'begin': r'\b(lambda)',
            'beginCaptures':
            {
                1: {'name': 'storage.type.function.anonymous.cython'}
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
                                1: {'name': 'variable.parameter.function.cython'},
                                2: {'name': 'keyword.operator.assignment.cython'}
                            },
                            'patterns':
                            [
                                {'include': '$self'}
                            ],
                            'end': r'(?=,|:)'
                        },
                        # Positional arguments
                        {
                            'name' : 'variable.parameter.function.cython',
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
            'name' : 'meta.function.decorator.with_arguments.cython',
            'begin': r'^\s*(@\s*[a-zA-Z_]\w*(\.[a-zA-Z_]\w*)*)\s*\(',
            'beginCaptures':
            {
                1: {'name': 'support.function.decorator.cython'}
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
            'name' : 'meta.function.decorator.without_arguments.cython',
            'begin': r'^\s*(@\s*[a-zA-Z_]\w*(\.[a-zA-Z_]\w*)*)',
            'beginCaptures':
            {
                1: {'name': 'support.function.decorator.cython'}
            },
            'end': r'(?=\s|$\n?|#)'
        },

#-- CONSTANTS -----------------------------------------------------------------#
        {
            'name' : 'constant.language.word_like.cython',
            'match':
            (
                r'\b(NULL|None|True|False|Ellipsis|NotImplemented|'
                r'UNAME_SYSNAME|UNAME_NODENAME|UNAME_RELEASE|UNAME_VERSION|'
                r'UNAME_MACHINE|EXIT_FAILURE|EXIT_SUCCESS|RAND_MAX)\b'
            )
        },
        {
            'name' : 'constant.language.symbol_like.cython',
            'match': r'(?<=\W|^)\.\.\.(?=\W|$)'
        },


#-- STORAGES ------------------------------------------------------------------#
        {
            'name' : 'storage.type.function.cython',
            'match': r'\b((c(p|type)?)?def|lambda)\b'
        },
        {
            'name' : 'storage.type.class.cython',
            'match': r'\b(class)\b'
        },


#-- BUILTINS ------------------------------------------------------------------#
        {
            'include': '#builtin_types'
        },
        {
            'include': '#c_types'
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
            'name': 'meta.structure.list.cython',
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
            'name' : 'meta.structure.group.python',
            'begin': r'(?<=,|=|\+|-|\*|/|\||:|<|>|~|%|\^|\\)\s*\(',
            'patterns':
            [
                {'include': '$self'}
            ],
            'end': r'\)'
        },

#-- ACCESS --------------------------------------------------------------------#
        {
            'name' : 'meta.function_call.python',
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
            'name' : 'support.type.exception.cython',
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
            'name' : 'support.function.builtin.cython',
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
        # todo: rearrange -> what is builtin function and what is builtin type?
        'builtin_types':
        {
            'name' : 'support.type.cython',
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
            'name' : 'support.type.c_types.cython',
            'match':
            (
                r'(?<!\.)\b('
                r'bint|(long\s)?double|enum|float|struct|union|void|const|fused|'
                r'((un)?signed\s)?(char|((short|long(\slong)?)\s)?int|short|long(\slong)?)'
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
            'name' : 'invalid.illegal_names.name.cython',
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
        'keyword_arguments':
        {
            'begin': r'\b([a-zA-Z_]\w*)\s*(=)(?!=)',
            'beginCaptures':
            {
                1: {'name': 'variable.parameter.function.cython'},
                2: {'name': 'keyword.operator.assignment.cython'}
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
            'name' : 'support.function.magic.cython',
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
        # todo: rearrange -> what is magic function and what is magic variable?
        'magic_variable_names':
        {
            'name' : 'support.variable.magic.cython',
            'match':
            (
                r'\b__('
                r'all|annotations|bases|builtins|class|debug|dict|doc|file|'
                r'members|metaclass|mro|name|qualname|slots|weakref'
                r')__\b'
            )
        },
        'language_variables':
        {
            'name' : 'variable.language.cython',
            'match': r'(?<!\.)\b(self|cls)\b'
        },
        'line_continuation':
        {
            'match': r'(\\)(.*)$\n?',
            'captures':
            {
                1: {'name': 'punctuation.separator.continuation.line.cython'},
                2: {'name': 'invalid.illegal.unexpected_text.cython'}
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
                    'name' : 'string.quoted.single.block.cython',
                    'begin': r"([bBuU]?)'''",
                    'beginCaptures':
                    {
                        1: {'name': 'storage.type.string.prefix.cython'}
                    },
                    'patterns':
                    [
                        {'include': '#string_patterns'}
                    ],
                    'end': r"'''"
                },
                {
                    'name' : 'string.quoted.single.block.cython',
                    'begin': r"([rR][bB]|[bB][rR]|[rR])'''",
                    'beginCaptures':
                    {
                        1: {'name': 'storage.type.string.prefix.cython'}
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
                    'name' : 'string.quoted.single.line.cython',
                    'begin': r"([bBuU]?)'",
                    'beginCaptures':
                    {
                        1: {'name': 'storage.type.string.prefix.cython'}
                    },
                    'patterns':
                    [
                        {'include': '#string_patterns'}
                    ],
                    'end': r"'|(\n)",
                    'endCaptures':
                    {
                        1: {'name': 'invalid.illegal.unclosed_string.cython'}
                    }
                },
                {
                    'name' : 'string.quoted.single.line.cython',
                    'begin': r"([rR][bB]|[bB][rR]|[rR])'",
                    'beginCaptures':
                    {
                        1: {'name': 'storage.type.string.prefix.cython'}
                    },
                    'patterns':
                    [
                        {'include': '#string_patterns'},
                        {'include': '#regular_expressions'}
                    ],
                    'end': r"'|(\n)",
                    'endCaptures':
                    {
                        1: {'name': 'invalid.illegal.unclosed_string.cython'}
                    }
                },

                # Double BLOCK
                {
                    'name' : 'string.quoted.double.block.cython',
                    'begin': r'([bBuU]?)"""',
                    'beginCaptures':
                    {
                        1: {'name': 'storage.type.string.prefix.cython'}
                    },
                    'patterns':
                    [
                        {'include': '#string_patterns'}
                    ],
                    'end': r'"""'
                },
                {
                    'name' : 'string.quoted.double.block.cython',
                    'begin': r'([rR][bB]|[bB][rR]|[rR])"""',
                    'beginCaptures':
                    {
                        1: {'name': 'storage.type.string.prefix.cython'}
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
                    'name' : 'string.quoted.double.line.cython',
                    'begin': r'([bBuU]?)"',
                    'beginCaptures':
                    {
                        1: {'name': 'storage.type.string.prefix.cython'}
                    },
                    'patterns':
                    [
                        {'include': '#string_patterns'}
                    ],
                    'end': r'"|(\n)',
                    'endCaptures':
                    {
                        1: {'name': 'invalid.illegal.unclosed_string.cython'}
                    }
                },
                # {
                #     'name' : 'meta.format_attribute.format.cython',
                #     'begin': r'(\.format)\s*\(',
                #     'beginCaptures':
                #     {
                #         1: {'name': 'invalid.illegal.none.cython'}
                #     },
                #     'patterns':
                #     [
                #         {
                #             'name' : 'string.quoted.double.format.cython',
                #             'begin': r'([uUbB]?)"',
                #             'beginCaptures':
                #             {
                #                 1: {'name': 'storage.type.string.prefix.cython'}
                #             },
                #             'patterns':
                #             [
                #                 {'include': '#string_patterns'},
                #                 {'include': '#format_mini_language'}
                #             ],
                #             'end': r'"|(\n)',
                #             'endCaptures':
                #             {
                #                 1: {'name': 'invalid.illegal.unclosed_string.cython'}
                #             }
                #         }
                #     ],
                #     'end': r'\)'
                # },
                # {
                #     'name' : 'string.quoted.double.format.cython',
                #     'begin': r'([uUbB]?)"',
                #     'beginCaptures':
                #     {
                #         1: {'name': 'storage.type.string.prefix.cython'}
                #     },
                #     'patterns':
                #     [
                #         {'include': '#string_patterns'},
                #         {'include': '#format_mini_language'}
                #     ],
                #     'end': r'"\.format',  # |(\n)',
                #     'endCaptures':
                #     {
                #         2: {'name': 'invalid.illegal.unclosed_string.cython'}
                #     }
                # },
                {
                    'name' : 'string.quoted.double.line.cython',
                    'begin': r'([rR][bB]|[bB][rR]|[rR])"',
                    'beginCaptures':
                    {
                        1: {'name': 'storage.type.string.prefix.cython'}
                    },
                    'patterns':
                    [
                        {'include': '#string_patterns'},
                        {'include': '#regular_expressions'}
                    ],
                    'end': r'"|(\n)',
                    'endCaptures':
                    {
                        1: {'name': 'invalid.illegal.unclosed_string.cython'}
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
            'name' : 'string.interpolated.placeholder.cython',
            'match': r'%(\(\w+\))?#?0?-?[ ]?\+?(\d*|\*)(\.(\d*|\*))?[hlL]?[diouxXeEfFgGcrs%]'
        },
        'format_mini_language':
        {
            'patterns':
            [
                {
                    'name' : 'constant.other.placeholder.format.cython',
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
            'name' : 'constant.character.escaped.special.cython',
            'match': r'\\(x\h{2}|[0-7]{3}|\n|\"|\'|a|b|f|n|r|t|v|\\)'
        },
        'escaped_unicode_characters':
        {
            # 16bit hex | 32bit hex | unicodename
            'name' : 'constant.character.escaped.cython',
            'match': r'\\(u\h{4}|U\h{8}|N\{[a-zA-Z\s]+\})'
        },

#-- REGEX ---------------------------------------------------------------------#
        'regular_expressions':
        {
            'patterns':
            [
                {
                    'name' : 'keyword.control.anchor.regex.cython',
                    'match': r'\\[bBAZzG]|\^|\$'
                },
                {
                    # \number
                    'name' : 'keyword.other.group_reference_order.regex.cython',
                    'match': r'\\[1-9]\d?'
                },
                {
                    # (?P=this_is_a_group)
                    'name' : 'keyword.other.group_reference_name.regex.cython',
                    'match': r'\(\?P=[a-zA-Z_]\w*\)'
                },
                {
                    # {2}, {2,}, {,2}, {2,3}, {2,3}?
                    'name' : 'keyword.operator.quantifier.regex.cython',
                    'match': r'[?+*][?+]?|\{(\d+,\d+|\d+,|,\d+|\d+)\}\??'
                },
                {
                    'name' : 'keyword.operator.or.regex.cython',
                    'match': r'\|'
                },
                {
                    # (?# comment)
                    'name' : 'comment.block.regex.cython',
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
                    'name' : 'keyword.other.option_toggle.regex.cython',
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
                    'name' : 'meta.group.assertion.regex.cython',
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
                    'begin': r'\[(\^)?(\](?=.*\]))?',
                    'beginCaptures':
                    {
                        1: {'name': 'keyword.operator.negation.regex.python'}
                    },
                    'patterns':
                    [
                        {
                            'name': 'constant.character.escaped.special.open.regex.python',
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
            'name' : 'constant.character.escaped.special.regex.python',
            'match': r'\\(\\|\?|\.|\*|\+|\{|\}|\||\(|\)|\[|\]|\^|\$)'
        }
    },
    'uuid': 'D085155B-E40A-40B3-8FEC-6865318CDEEA'
}

if __name__ == '__main__':
    import convert
    _name = 'Cython'
    convert.dict_to_lang(dictionary=syntax,
                         repo_fname=_name,
                         repo_dname=_name,
                         test_fname=_name,
                         test_dname='Cython_TEST',
                         test_fpath='~/Library/Application Support/'
                                    'Sublime Text 3/Packages/User/')
