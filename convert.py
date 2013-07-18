# Import python modules
import os
import json

def dict_to_plist(dictionary, file_name, file_path):
    # Create JSON file
    with open('{}.json'.format(file_name), 'w') as f:
        f.write(
            json.dumps(
                obj = dictionary,
                indent = 4,
                separators = (',', ': ')
            )
        )
    # Convert JSON file to PropertyList XML
    os.system(('plutil -convert xml1 {0}.json -o ' + file_path).format(file_name))
    os.system(('plutil -convert xml1 {0}.json -o {0}.tmLanguage').format(file_name))
    print(file_name, 'has been converted.')
