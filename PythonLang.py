lang = {
	'comment': '\n\t\tWritten by Peter Varo (c)2013\n\t\thttp://github.com/petervaro/python3\n\t',
	'name': 'PythonLang 3',
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
		{
			'name' : 'comment.line.hashmark.python',
			'match': r'#.*$\n?'
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
			# new: function annotation assignment
			'name' : 'keyword.operator.assignment.python',
			'match': r'=|->'
		},
		# {
		# 	'name' : 'meta.class.python',
		# 	'begin': r'^\s*(class)\s+(?=[a-zA-Z_]\w*\s*(\((metaclass\s*=\s*)?\)\s)?*:)',
		# 	'end'  : r''
		# }
		{
			# new: function annotation assignment
			'name' : 'constant.language.python',
			'match': r'\b(None|True|False|Ellipsis|NotImplemented)\b'
		}
	],
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
		}
	},
	'uuid': '851b1429-b8b4-4c1e-8030-399bda994393'
}

if __name__ == '__main__':
	# Import python modules
	import os
	import json

	# Constants
	FILE = 'PythonLang'
	PATH = '~/Library/Application\ Support/Sublime\ Text\ 3/Packages/User/{0}.tmLanguage'

	# Create json file
	with open('{}.json'.format(FILE), 'w') as f:
		f.write(json.dumps(lang))
	# Convert JSON file to PropertyList XML
	os.system(('plutil -convert xml1 {0}.json -o ' + PATH).format(FILE))
	os.system(('plutil -convert xml1 {0}.json -o {0}.tmLanguage').format(FILE))
