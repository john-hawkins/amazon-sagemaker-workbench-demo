import numpy as np
import pandas as pd
import sys
sys.path.append("../")
import utils.config as cfg

path_to_lookup = cfg.get_path("data/raw/dataset_diabetes/IDs_mapping.csv")

def process_raw_data(rawdata):
    df_data = pd.read_csv(rawdata, sep=",")
    # Only shape the target if it is present
    if "readmitted" in df_data:
        df_data["readmitted"] = np.where( df_data["readmitted"]=="NO",0,1)
    lookup = pd.read_csv(path_to_lookup, sep=",")
    d = lookup.set_index('admission_type_id')['description'].to_dict()
    df_data['admission_type_id'] = np.vectorize(d.get)(df['admission_type_id'])
    return df_data


 

