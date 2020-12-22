import os
import yaml
import boto3
import sagemaker

path = os.path.split(__file__)[0]
 
config_file = os.path.join(path, "../config/project.yaml")

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
    return os.path.join(path, "../", root_filepath)


def get_path_to_raw_data():
    """
        Retrieve the path to the raw data. 
        Returns a valid path regardless of where the API is being used.
    """
    return os.path.join(path, "../data/raw/raw.csv")


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
    return os.path.join(path, "../data/partitioned/")


