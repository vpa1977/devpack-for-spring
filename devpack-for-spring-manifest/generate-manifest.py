#!/usr/bin/python3

import yaml
import toml
import sys

with open(sys.argv[1], "r") as yaml_file:
    yaml_data = yaml.safe_load(yaml_file)

with open(sys.argv[2], "r") as toml_file:
    toml_data = toml.load(toml_file)

def set_versions(yaml_data, toml_data):
    libraries = toml_data['libraries']
    snaps = yaml_data['content-snaps']
    for _, description in snaps.items():
        description['version'] = libraries[description['version']]['version']

set_versions(yaml_data, toml_data)

with open(sys.argv[3], "w") as yaml_file:
    yaml.safe_dump(yaml_data, yaml_file)
