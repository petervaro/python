# TODO: Add this functionality src.convert.Theme

# Convert dictionary to css
def dict_to_css(dictionary, name, local):
    # todo: decide if we need `word-wrap: break-word;` or not?
    KEYS = {
        'fontStyle' : 'font-style',
        'foreground': 'color',
        'background': 'background-color'
    }
    output = []
    output.append('/*\n*{auth}\n*{name} syntax highlight theme\n*\n*{comm}\n*/\n'.format(
            auth = dictionary['author'],
            name = dictionary['name'],
            comm = dictionary['comment']
        )
    )
    output.append('body\n{\n\tbackground: #282828;\n}\n')
    pre = dictionary['settings'][0]['settings']
    output.append('pre, code\n{{\n{default}{dynamic}\n}}\n'.format(
            default = (
                '\tmargin: 0px;\n'
                '\tpadding-left: 20px;\n'
                '\tfont-size: 12.5px;\n'
                "\tfont-family: 'Menlo', monospace;\n"
            ),
            dynamic = '\n'.join(
                [
                    '\tbackground: {};'.format(pre['background']),
                    '\tcolor: {};'.format(pre['foreground']),
                ]
            )
        )
    )
    output.append('::selection\n{{\n\tbackground: {};\n}}\n'.format(
        hex_to_rgba(pre['selection']))
    )
    for item in dictionary['settings'][1:]:
        try:
            _name  = item['scope']
            prefs = []
            for key, value in item['settings'].items():
                try:
                    k = KEYS[key]
                except KeyError:
                    k = key
                if value.startswith('#') and len(value) == 9:
                    v = hex_to_rgba(value)
                else:
                    v = value
                prefs.append('\t{}: {};'.format(k, v))
            output.append('pre .{}\n{{\n{}\n}}\n'.format(_name, '\n'.join(prefs)))
        except KeyError:
            pass
    with open(os.path.join(os.pardir, local, '{}.css'.format(name)), 'w') as f:
        f.write('\n'.join(output))
    print(name, 'style dictionary has been converted and placed.')
