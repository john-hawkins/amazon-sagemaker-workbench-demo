# -*- coding: utf-8 -*-
"""
These functions determine the interface between data preparation and modelling.
"""
import pandas as pd

def get_training_data_path():
    """
      Get the path to training data on S3
    """
    return ""


def get_validation_data_path():
    """
      Get the path to validation data on S3
    """
    return ""


def get_testing_data_path():
    """
      Get the path to testing data on S3
    """
    return ""


def push_data_to_s3(local_path, purpose="training"):
    """
       Place a prepared dataset into the project S3 bucket in the right location
    """
    return "done"


def get_path_to_data_on_s3(purpose="training"):
    """
       Return the S3 path to the required dataset
    """
    return ""

