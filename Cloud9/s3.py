

#Create an S3 bucket to store your data inputs: 

import boto3

s3 = boto3.client('s3')

# Create a new S3 bucket
s3.create_bucket(Bucket='my-search-data')
