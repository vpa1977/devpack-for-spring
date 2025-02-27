#!/usr/bin/python3

import yaml
import toml

with open("supported.yaml", "r") as yaml_file:
    yaml_data = yaml.safe_load(yaml_file)

with open("supported.versions.toml", "r") as toml_file:
    toml_data = toml.load(toml_file)

def set_versions(yaml_data, toml_data):
    libraries = toml_data['libraries']
    snaps = yaml_data['content-snaps']
    for _, description in snaps.items():
        description['version'] = libraries[description['version']]['version']

set_versions(yaml_data, toml_data)

with open("transformed.yaml", "w") as yaml_file:
    yaml.safe_dump(yaml_data, yaml_file)
