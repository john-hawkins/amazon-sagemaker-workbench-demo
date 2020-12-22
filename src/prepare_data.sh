#!/bin/bash

if [ $# -eq 0 ]
then
        echo "This script requires a path to the data directory"
        exit 0
fi

cd $1
mkdir raw
wget -P raw/ -N https://archive.ics.uci.edu/ml/machine-learning-databases/00296/dataset_diabetes.zip

cd raw
unzip dataset_diabetes.zip

