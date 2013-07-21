from Python import syntax

syntax['name'] = 'Cython'
syntax['scopeName'] = 'source.cython'
syntax['fileTypes'] = ['pyx', 'pxi', 'pxd']
syntax['keyEquivalent'] = '^~C'
syntax['foldingStartMarker'] = (
	r'^\s*((cp?)?def|class|property|struct|enum|union)'
	r'\s+([.\w>]+)\s*(\((.*)\))?\s*:|\{\s*$|\(\s*$|\[\s*$|^\s*"""(?=.)(?!.*""")'
)
syntax['uuid'] = 'D085155B-E40A-40B3-8FEC-6865318CDEEA'

if __name__ == '__main__':
	import convert
	convert.dict_to_plist(
		dictionary = syntax,
		name  = 'Cython',
		path  = '~/Library/Application Support/Sublime Text 3/Packages/Cython',
		local = True
	)
