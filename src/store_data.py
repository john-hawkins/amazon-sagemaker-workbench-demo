import sys
sys.path.append("./")
sys.path.append("../")
import utils.config as cfg

path_to_partitioned = cfg.get_path_to_partitioned_data()
config = cfg.get_config()
bucket_name = config['bucket_name']
bucket_prefix = config['bucket_prefix']
sgmk_session = config['sgmk_session']

def store_data(input_path):
    """
        Store the datasets into the required S3 Location
    """
    # Upload CSV files to S3 for SageMaker training
    train_uri = sgmk_session.upload_data(
        path=input_path +"/train.csv",
        bucket=bucket_name,
        key_prefix=bucket_prefix,
    )
    val_uri = sgmk_session.upload_data(
        path=input_path +"/validation.csv",
        bucket=bucket_name,
        key_prefix=bucket_prefix,
    )
    test_uri = sgmk_session.upload_data(
        path=input_path +"/test.csv",
        bucket=bucket_name,
        key_prefix=bucket_prefix,
    )
    return train_uri, val_uri, test_uri

if __name__ == "__main__":
    train, val, test = store_data( path_to_partitioned )
    cfg.add_s3_path("train", train)
    cfg.add_s3_path("validation", val)
    cfg.add_s3_path("test", test)



