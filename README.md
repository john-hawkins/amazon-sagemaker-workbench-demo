AWS Sagemaker Workbench Demo
============================

This project is an experiment in designing custom data science workbenches on AWS Sagemaker.

It provides a set of conventions, scripts and notebooks that illustrate how
you can design a customised workbench inside Sagemaker.

You can clone this repository and then change the configuration for loading data training
models to apply it to your own problem.

The goals of project are as follows:

* Illustrate how to train a combination of Sagemaker and bespoke models.
* Perform model selection using a flexible independent model comparison app.
* Investigate/Explain their performance using a set of general purpose tools.
* Deploy the selected model.

The process is designed to permit the above as a temporal process that mimics a standard
model development workflow.


# Approach   

We achieve this with a combination of convention, configuration and prebuilt applications
that depend on these requirements.

* Data is partitioned in an independent job that should be respected by all models
* Models are then built independently according to the data scientists ideas and requirements
* Models are deployed to and endpoint and registered in order to permit comparison
* Comparison is performed using these endpoints on independent data.
* After selection and final deployment, all artefacts are cleaned.


# Key Conventions

* Overall data partitioning is done once to enforce rigorous comparison of methods.
* Datasets should be registered  through the [dataset utility functions](utils/datasets.py)
* All models load their training data through the [dataset utility functions](utils/datasets.py)
* All experiments should be performed inside an [independent directory below experiments](experiments)   
* Completed models need to be deployed and registered using the [models utility functions](utils/models.py)
* The application 



# Usage

Clone this notebook into an instance of Sagemaker Studio.

Follow the Notebook [00_Load_and_prepare_data.pynb](data/00_Load_and_prepare_data.pynb)
to generate a dataset.

Examples of multiple ways to build models on this data is shown in the [experiments directory](experiments)



