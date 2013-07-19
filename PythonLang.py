lang = {
	'name': 'PythonLang 3',
	'comment': '\n\t\tWritten by Peter Varo (c)2013\n\t\thttp://github.com/petervaro/Python3\n\t',
	'scopeName': 'source.python',
	'fileTypes': ['py'],
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
			'match': r'=|->'  # todo: use `:` as assignment ?
		},


#-- CLASS ---------------------------------------------------------------------#
		{
			'name' : 'meta.class.python',
			'begin': r'^\s*(class)\s+(?=[a-zA-Z_]\w*(\s*\()?)',
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
					'end': r'\)|:',
					'beginCaptures':
					{
						1: {'name': 'punctuation.definition.inheritance.begin.python'}
					}
				}
			],
			'end'  : r'(\)?\s*(:)|\s+([\w#\s:]+))',
			'beginCaptures':
			{
				1: {'name': 'storage.type.class.python'}
			},
			'endCaptures':
			{
				1: {'name': 'punctuation.inheritance.class.python'},
				2: {'name': 'punctuation.section.class.python'},
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
				1: {'name': 'punctuation.section.function.python'},
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
		{
			'begin': r'\(',
			'patterns':
			[
				{'include': '$self'}
			],
			'end': r'\)'
		},
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
		}


#-- STRING --------------------------------------------------------------------#

#-- REGEX ---------------------------------------------------------------------#

	],


#-- REPOSITORY ----------------------------------------------------------------#
	'repository':
	{
		'builtin_exceptions':
		{
			'name' : 'support.type.exception.python',
			'match':
			(
				r'(?x)\b('
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
				r'(?x)\b('
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
			'name' : 'support.type.python',
			'match':
			(
				r'(?x)\b('
				r'basestring|bool|buffer|bytearray|bytes|classmethod|complex|dict|'
				r'enumerate|file|float|frozenset|int|list|memoryview|object|open|'
				r'property|reversed|set|slice|staticmethod|str|super|tuple|type'
				r')\b'
			)
		},
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
		'magic_function_names':
		{
			'name' : 'support.function.magic.python',
			'match':
			(
				r'(?x)\b(__(?:'
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
		# todo: what is magic function and what is magic variable?
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
		}
		# todo: Tuple parameter unpacking removed.
		#		You can no longer write def foo(a, (b, c)): ....
		#		Use def foo(a, b_c): b, c = b_c instead.

		# todo: [uU][bB][rR]
		# todo: (r'string' r'string' r'string')
	},
	'uuid': '851B1429-B8B4-4C1E-8030-399BDA994393'
}


if __name__ == '__main__':
	import convert
	convert.dict_to_plist(
		dictionary = lang,
		file_name  = 'PythonLang',
		file_path  = '~/Library/Application Support/Sublime Text 3/Packages/User/',
		local_copy = True
	)
