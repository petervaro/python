#!/usr/bin/python3
# -*- coding: utf8 -*-

import os
import plistlib

# Generate and print separator comments
def str_to_separator(string: str) -> None:
    print('#{:-<78}#'.format('-- {} '.format(string.upper())))


# Convert integer dictionary keys into string literals
def int_to_str(obj: object) -> object:
        try:
            for key, value in obj.items():
                obj[key] = int_to_str(value)
                if isinstance(key, int):
                    obj[str(key)] = obj.pop(key)
        except AttributeError:
            if isinstance(obj, list):
                for i, item in enumerate(obj):
                    obj[i] = int_to_str(item)
        return obj


# Convert dictionary into property list file
def dict_to_plist(dictionary, name, extension, path, local) -> None:
        d = int_to_str(dictionary)
        n = '{}.{}'.format(name, extension)
        p = os.path.join(os.path.expanduser(path), n)
        if path:
            with open(p, 'w+b') as f:
                plistlib.writePlist(d, f)
        if local:
            with open(os.path.join('compiled', n), 'w+b') as f:
                plistlib.writePlist(d, f)


# Convert dictionary to TextMate Theme file
def dict_to_theme(dictionary: dict, name: str, path: str = None, local: bool = False) -> None:
    dict_to_plist(dictionary, name, 'tmTheme', path, local)
    print(name, 'style dictionary has been converted and placed.')


# Convert dictionary to TextMate Language file
def dict_to_lang(dictionary: dict, name: str, path: str = None, local: bool = False) -> None:
    dict_to_plist(dictionary, name, 'tmLanguage', path, local)
    print(name, 'syntax dictionary has been converted and placed.')


# Convert hexadecimal values to rgba
def hex_to_rgba(hexa: str) -> str:
    return 'rgba({}, {}, {}, {:.2f})'.format(
        int(hexa[1:3], 16),
        int(hexa[3:5], 16),
        int(hexa[5:7], 16),
        int(hexa[7:], 16)/255
    )

# Convert dictionary to css
def dict_to_css(d, fname):
    # todo: decide if we need `word-wrap: break-word;` or not?
    KEYS = {
        'fontStyle' : 'font-style',
        'foreground': 'color',
        'background': 'background-color'
    }
    output = []
    output.append('/*\n*{auth}\n*{name} syntax highlight theme\n*\n*{comm}\n*/\n'.format(
            auth = d['author'],
            name = d['name'],
            comm = d['comment']
        )
    )
    output.append('body\n{\n\tbackground: #282828;\n}\n')
    pre = d['settings'][0]['settings']
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
    for item in d['settings'][1:]:
        try:
            name  = item['scope']
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
            output.append('pre .{}\n{{\n{}\n}}\n'.format(name, '\n'.join(prefs)))
        except KeyError:
            pass
    print(fname, 'style dictionary has been converted and placed.')
    return '\n'.join(output)
