
# Upload CSV files to S3 for SageMaker training
train_uri = sgmk_session.upload_data(
    path="data/train.csv",
    bucket=bucket_name,
    key_prefix=bucket_prefix,
)
val_uri = sgmk_session.upload_data(
    path="data/validation.csv",
    bucket=bucket_name,
    key_prefix=bucket_prefix,
)


# Define the data input channels for the training job:
s3_input_train = sagemaker.inputs.TrainingInput(train_uri, content_type="csv")
s3_input_validation = sagemaker.inputs.TrainingInput(val_uri, content_type="csv")

print(f"{s3_input_train.config}\n\n{s3_input_validation.config}")



