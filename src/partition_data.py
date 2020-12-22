from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import sys
sys.path.append("./")
sys.path.append("../")
import utils.config as cfg

path_to_processed = cfg.get_path_to_processed_data()
path_to_partitioned = cfg.get_path_to_processed_data()
target = cfg.get("target")


def partition_data(input_path, output_path, target):
    """
        The partition function will split the data according to the parameters
        in the project configuration.
    """
    df = pd.read_csv(input_path, sep=",")
    train_prop = cfg.get("train_prop")
    valid_prop = cfg.get("valid_prop")
    valid_remainder = valid_prop/(1-train_prop)
    train, rest = train_test_split(df, train_size=train_prop, stratify=target)
    valid, test = train_test_split(rest, train_size=valid_remainder, stratify=target)

    # Create CSV files for Train / Validation / Test
    train.to_csv(output_path + "train.csv", index=False, header=True)
    valid.to_csv(output_path + "validation.csv", index=False, header=True)
    test.to_csv(output_path + "test.csv", index=False, header=True)


if __name__ == "__main__":
    partition_data(path_to_processed, path_to_partitioned, target) 


