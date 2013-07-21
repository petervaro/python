import os
import plistlib

# Generate and print separator comments
def str_to_separator(string) -> None:
    print('#{:-<78}#'.format('-- {} '.format(string.upper())))


# Convert integer dictionary keys into string literals
def int_to_str(obj) -> None:
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
def dict_to_plist(dictionary: dict, name: str, path: str = None, local: bool = False) -> None:
    d = int_to_str(dictionary)
    p = os.path.join(os.path.expanduser(path))
    if p:
        with open('{}.tmLanguage'.format(p, name), 'w+b') as f:
            plistlib.writePlist(d, f)
    if local:
        with open('{}.tmLanguage'.format(name), 'w+b') as f:
            plistlib.writePlist(d, f)
    print(name, 'syntax dictionary has been converted and placed.')
