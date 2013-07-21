import os
import plistlib

# Generate and print separator comments
def str_to_separator(string: str) -> None:
    print('#{:-<78}#'.format('-- {} '.format(string.upper())))


# Convert integer dictionary keys into string literals
def int_to_str(obj) -> object:
        try:
            for key, value in obj.items():
                obj[key] = int_to_str(obj[key])
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
            with open(n, 'w+b') as f:
                plistlib.writePlist(d, f)


# Convert dictionary to TextMate Theme file
def dict_to_theme(dictionary: dict, name: str, path: str = None, local: bool = False) -> None:
    dict_to_plist(dictionary, name, 'tmTheme', path, local)
    print(name, 'style dictionary has been converted and placed.')


# Convert dictionary to TextMate Language file
def dict_to_lang(dictionary: dict, name: str, path: str = None, local: bool = False) -> None:
    dict_to_plist(dictionary, name, 'tmLanguage', path, local)
    print(name, 'syntax dictionary has been converted and placed.')
