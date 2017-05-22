DOCUMENTATION = '''
---
module: json_file_replacer
short_description: Replace the value of a specific key inside a json
description:
    - Replace recursively, inside a json file, the value of a specific key.
version_added: "0.1"
options:
  path:
    description:
      - The path of json file.
    required: true
    default: null
    aliases: []
  keyToFind:
    description:
      - The key that you want to find to replace its value.
    required: true
    default: null
    aliases: []
  valueToReplace:
    description:
      - The newer value
    required: true
    default: null
    aliases: []
  backup:
    description:
      - If you want to save the json file in order to have a backup file
    required: false
    default: False
    aliases: []
'''

EXAMPLES = '''
# Basic example of json file replacer
tasks:
- name: "Replace the value of specific key inside a json file"
  cloudfront_invalidate:
    path: "ABSOLUTE_PATH"
    keyToFind: "KEY_TO_FIND"
    valueToReplace: "VALUE_TO_REPLACE"
    backup: True
'''

import os
import json

try:
    from shutil import copyfile
except ImportError:
    shutil_installed = False
else:
    shutil_installed = True


def deep_replace(dictionary, keyToFind, valueToReplace):
    if isinstance(dictionary, dict):
        for key, val in dictionary.items():
            if key == keyToFind:
                dictionary[key] = valueToReplace
            deep_replace(val, keyToFind, valueToReplace)


def main():
    arg_spec = dict(
        path=dict(required=True),
        keyToFind=dict(required=True),
        valueToReplace=dict(required=True),
        backup=dict(required=False, default=False, type='bool')
    )
    module = AnsibleModule(argument_spec=arg_spec,
                           add_file_common_args=True,
                           supports_check_mode=True)

    path = module.params['path']
    keyToFind = module.params['keyToFind']
    valueToReplace = module.params['valueToReplace']
    backup = module.params['backup']

    if not shutil_installed:
        module.fail_json(msg="This module requires the shutil Python Library")

    if not os.path.exists(path):
        module.fail_json(msg="The file doesn't exist")

    try:
        if backup:
            print backup
            copyfile(path, path + ".bkp")

        json_data = json.loads(open(path).read())

        original_data = json.dumps(json_data)
        deep_replace(json_data, keyToFind, valueToReplace)

        f = open(path, "w")
        try:
            f.write(json.dumps(json_data, indent=4))
        finally:
            f.close()

        isFound = (original_data == json_data) and False or True

        module.exit_json(msg="Deep replacer finished", changed=isFound)

    except Exception:
        e = get_exception()
        module.fail_json(msg=str(e))


# import module snippets
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.pycompat24 import get_exception

if __name__ == '__main__':
    main()
