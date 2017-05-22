# ansible-json-file-replacer
This is a simple Ansible module used to replace recursively, inside a json file, the value of a specific key

### Requirements
* First and foremost, you need Ansible installed and configured for your environment
* shutil python library

### Installation & Configuration
* Clone/download this repo
* Place the cloudfront_invalidate.py file in your Ansible module path

### Usage
* See the example.yml playbook for a working example (after replacing your details of course)
* Basic usage clearing a single path:
```
- name: "Replace the value of specific key inside a json file"
  json_file_replacer:
    path: "ABSOLUTE_PATH"
    keyToFind: "KEY_TO_FIND"
    valueToReplace: "VALUE_TO_REPLACE"
    backup: True
```

## License

Copyright 2017 Tierra SpA

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

[http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.