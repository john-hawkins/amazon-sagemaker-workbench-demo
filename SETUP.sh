#!/bin/bash

# THIS SCRIPT WILL INITIALISE A TERMINAL TO USE THE RUN SCRIPT

ln -s /opt/conda/bin/python /usr/local/bin/python3

# Sagemaker Kernel Images do not come with an editor by default
# INSTALL VIM

apt-get update
apt-get install vim

