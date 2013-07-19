from PythonLang import lang

lang['name'] = 'Cython'
lang['scopeName'] = 'source.cython'
lang['fileTypes'] = ['pyx', 'pxi', 'pxd']
lang['foldingStartMarker'] = (
	r'^\s*((cp?)?def|class|property|struct|enum|union)'
	r'\s+([.\w>]+)\s*(\((.*)\))?\s*:|\{\s*$|\(\s*$|\[\s*$|^\s*"""(?=.)(?!.*""")'
)
lang['uuid'] = 'D085155B-E40A-40B3-8FEC-6865318CDEEA'

if __name__ == '__main__':
	import convert
	convert.dict_to_plist(
		dictionary = lang,
		file_name  = 'Cython',
		file_path  = '~/Library/Application Support/Sublime Text 3/Packages/User/',
		local_copy = True
	)
