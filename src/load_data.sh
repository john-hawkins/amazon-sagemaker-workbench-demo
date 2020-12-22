#!/bin/bash

if [ $# -eq 0 ]
then
        echo "This script requires a path to the data directory"
        exit 0
fi

# GET THE DATA
cd $1
mkdir raw
wget -P raw/ -N https://archive.ics.uci.edu/ml/machine-learning-databases/00296/dataset_diabetes.zip

# EXTRACT IT
cd raw
unzip dataset_diabetes.zip
mv dataset_diabetes/diabetic_data.csv ./raw.csv
mv dataset_diabetes/IDs_mapping.csv ./IDs_mapping.csv

# CLEAN UP
rm dataset_diabetes.zip
rm dataset_diabetes/*
rm -d dataset_diabetes
