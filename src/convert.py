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
def dict_to_plist(dictionary, name, path):
        d = int_to_str(dictionary)
        d['name'] = name
        with open(path, 'w+b') as f:
            plistlib.writePlist(d, f)


# Convert dictionary to TextMate Theme file
def dict_to_theme(dictionary: dict, name: str, path: str = None, local: bool = False) -> None:
    dict_to_plist(dictionary, name, 'tmTheme', path, local)
    print(name, 'style dictionary has been converted and placed.')


# Convert dictionary to TextMate Language file
def dict_to_lang(dictionary,
                 repo_fname='',
                 repo_dname='',
                 test_fname='',
                 test_dname='',
                 test_fpath=''):
    """
    dictionary: a dict object, contains the syntax definition

    repo_fname: if provided:
                name of the file that will be placed insed CWD

    repo_dname: if repo_fname provided:
                definition name of syntax (appears in Sublime Text)

    test_fname: if provided:
                name of the file that will be placed into test_fpath

    test_dname: if test_fname provided:
                definition name of syntax (appears in Sublime Text)

    test_fpath: if test_fname provided:
                location where the test file will be placed
    """
    # Place local copy
    if repo_fname:
        repo_dname = repo_dname if repo_dname else repo_fname
        dict_to_plist(dictionary,
                      repo_dname,
                      os.path.join(os.pardir,
                                   '{}.{}'.format(repo_fname, 'tmLanguage')))
        print(repo_dname, 'syntax dictionary has been converted and placed.')

    # Place Sublime User copy
    if test_fname:
        test_dname = test_dname if test_dname else test_fname
        dict_to_plist(dictionary,
                      test_dname,
                      os.path.join(os.path.expanduser(test_fpath),
                                   '{}.{}'.format(test_fname, 'tmLanguage')))
        print(test_dname, 'syntax dictionary has been converted and placed.')


# Convert hexadecimal values to rgba
def hex_to_rgba(hexa: str) -> str:
    return 'rgba({}, {}, {}, {:.2f})'.format(
        int(hexa[1:3], 16),
        int(hexa[3:5], 16),
        int(hexa[5:7], 16),
        int(hexa[7:], 16)/255
    )

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
