import os
import yaml
import boto3
import sagemaker
import sys
from os.path import abspath

path = os.path.split(__file__)[0]
 
config_file = abspath(os.path.join(path, "../config/project.yaml"))

boto_session = boto3.Session()
region = boto_session.region_name


if region is None:
    bucket_name = "" 
    bucket_prefix = "project_"
    sgmk_session = ""
    sgmk_client = ""
    sgmk_role = ""
else:
    bucket_name = sagemaker.Session().default_bucket()
    bucket_prefix = "project_"  
    sgmk_session = sagemaker.Session()
    sgmk_client = boto_session.client("sagemaker")
    sgmk_role = sagemaker.get_execution_role()

####################################################################
def print_failure(message, end = '\n'):
    sys.stderr.write('\x1b[1;31m' + message.strip() + '\x1b[0m' + end)

def print_success(message, end = '\n'):
    sys.stdout.write('\x1b[1;32m' + message.strip() + '\x1b[0m' + end)

def get_config():
    with open(config_file) as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
    config['region'] = region
    config['bucket_name'] = bucket_name
    config['bucket_prefix'] = bucket_prefix
    config['sgmk_session'] = sgmk_session
    config['sgmk_client'] = sgmk_client
    config['sgmk_role'] = sgmk_role
    return config


def get(param):
    config = get_config()
    return config.get(param, None)

def write_config(config):
    with open(config_file, 'w') as file:
        documents = yaml.dump(config, file)

def get_path(root_filepath):
    """
        Given a path to a file from the root of the project.
        We convert it to be an absolute path.
        This function depends on this utility being one directory deeper than root.
    """
    return abspath(os.path.join(path, "../", root_filepath))


def get_path_to_raw_data():
    """
        Retrieve the path to the raw data. 
        Returns a valid path regardless of where the API is being used.
    """
    return abspath(os.path.join(path, "../data/raw/raw.csv"))


def get_path_to_processed_data():
    """
        Retrieve the path to the processed data.
        Returns a valid path regardless of where the API is being used.    
    """
    return os.path.join(path, "../data/processed/processed.csv")
    

def get_path_to_partitioned_data():
    """
        Retrieve the path to the partitioned data.
        Returns a valid path regardless of where the API is being used.
    """
    return abspath(os.path.join(path, "../data/partitioned/"))


def validate_project():
    """
        Ensure that the project configuration is self-consistent
    """
    conf = get_config() 
    # TODO: Run checks on partitioning paramters

def validate_data(df):
    """
        Ensure that the dataset meets the project definittion
    """
    conf = get_config() 
    target = conf.get("target","")
    if target not in df.columns:
        print_failure("ERROR: Target variable not found in dataframe")
        exit(1)



