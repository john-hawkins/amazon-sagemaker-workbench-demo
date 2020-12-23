#!/bin/bash

# ######################################################################
# Add refernces to any modelling jobs to execute
# All jobs should obtain access to the training data via the config API
# ######################################################################

python ./01_prebuilt_xgboost_container.py

python ./02_custom_scikit_learn_model.py

python ./03_sagemaker_autopilot.py


