import os
import plistlib

def int_to_str(obj):
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

def dict_to_plist(dictionary, file_name, file_path=None, local_copy=False):
    d = int_to_str(dictionary)
    if file_path:
        with open('{}.tmLanguage'.format(os.path.join(os.path.expanduser(file_path), file_name)), 'w+b') as f:
            plistlib.writePlist(d, f)
    if local_copy:
        with open('{}.tmLanguage'.format(file_name), 'w+b') as f:
            plistlib.writePlist(d, f)
    print(file_name, 'has been converted and placed.')
