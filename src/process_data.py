import numpy as np
import pandas as pd
import sys
sys.path.append("../")
import utils.config as cfg

path_to_lookup = cfg.get_path("data/raw/dataset_diabetes/IDs_mapping.csv")

path_to_raw = cfg.get_path_to_raw_data()
path_to_processed = cfg.get_path_to_processed_data()

def process_raw_data(rawdata_path, output_path):
    df = pd.read_csv(rawdata_path, sep=",")
    processed = process_dataframe(df)
    processed.to_csv(output_path, index=False, header=True)    

def process_dataframe(df):
    # Only shape the target if it is present
    if "readmitted" in df:
        df["readmitted"] = np.where( df["readmitted"]=="NO",0,1)
    
    lookup = pd.read_csv(path_to_lookup, sep=",")
    d = lookup.set_index('admission_type_id')['description'].to_dict()
    df['admission_type_id'] = np.vectorize(d.get)(df['admission_type_id'])
    
    return df
 

if __name__ == "__main__":
    process_raw_data(path_to_raw, path_to_processed)

