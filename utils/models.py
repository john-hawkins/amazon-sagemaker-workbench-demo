# -*- coding: utf-8 -*-
"""
   Model API Interface

   These functions allow models built in independent jobs to register their existance and
   permit global, indepedendent comparison in other parts of the workbench.
"""
import os
import json
import sys
from os.path import abspath

path = os.path.split(__file__)[0]

config_file = abspath(os.path.join(path, "../config/models.json"))


def list_models():
    """
      Get all models built in this project
    """
    config = get_config()
    return list(config['models'].keys())


def register(name, description, artefact, endpoint):
    """
      Register a model for comparison
    """
    temp = {"name": name, "description":description, "artefact":artefact, "endpoint":endpoint}
    config = get_config()
    config['models'][name] = temp
    write_config(config)
    return "Done"


def get_config():
    with open(config_file) as json_file:
        data = json.load(json_file)
    return data

def write_config(data):
    with open(config_file, 'w') as outfile:
        json.dump(data, outfile, indent=2)



