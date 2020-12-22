AWS Sagemaker Workbench Demo
============================
```
Status - Work in progress -- Non-Functional
```

This project is an experiment in designing custom data science workbenches on AWS Sagemaker.

It provides a set of conventions, scripts and notebooks that illustrate how
you can design a customised workbench inside Sagemaker.

You can clone this repository and then change the configuration for loading data training
models to apply it to your own problem.

The goals of project are as follows:

* Illustrate how to train a combination of Sagemaker and bespoke models.
* Perform model selection using a flexible independent model comparison app.
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

Clone this repository into an instance of Sagemaker Studio.

There are then two usage pathways you can follow: **GUI/Notebook Workflow** and **Script Workflow**
They both rely on the same underlying scripts and configuration. 

## GUI/Notebook Workflow

### Data Prep

Follow the Notebook [data/prepare_data.ipynb](data/prepare_data.ipynb) 
to understand how we get the data and prepare it for modelling.

### Experiments

Examples of modelling approaches are shown in the [experiments directory](experiments). 

The proposed flow is as follows:

1. Build a [Simple Baseline](experiments/01_Baseline.ipynb) - Using a sci-kit learn script
2. Build an [XGBoost Model](experiments/02_XGBoost.ipynb) - Using a pre-built training job container.
3. Run an [Autopilot Job](experiments/03_Autopilot.ipynb)

With these models built we can then explore their performance.

### Analysis

The [Model Comparisons Notebook](analysis/model_comparison.ipynb) will allow you to compare any model that has been built following the conventions show in the experients sections

This notebook makes extensive use of configuration and GUI widgets so that you can always return and perform additional comparisons after additional models have been run.

### Deployment

The [Deployment Notebook] demonstrates how to select any of the models built and create an endpoint. In some instances there will be additional configuration required to add pre-processing into the endpoint.


## Script Workflow

The same steps as above can be executed using the [RUN](RUN.sh) script in the root of the repository.
This script is parameterised such that you can run individual steps seperately, or the entire process in sequence.

The goal of this workflow is demonstrate how you might automate certains elements of your data science workflow
and develop a code base that is easier to deploy.



