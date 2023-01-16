# Use IAM roles to control access to your resources:

import boto3

iam = boto3.client('iam')

# Create a new IAM role for the Lambda function
response = iam.create_role(
    RoleName='my-search-lambda-role',
    AssumeRolePolicyDocument='{
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "Service": "lambda.amazonaws.com"
                },
                "Action": "sts:AssumeRole"
            }
        ]
    }',
    Description='Role for the my-search Lambda function'
)

# Attach the necessary policies to the role
iam.attach_role_policy(
    RoleName='my-search-lambda-role',
    PolicyArn='arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess'
)

iam.attach_role_policy(
    RoleName='my-search-lambda-role',
    PolicyArn='arn:aws:iam::aws:policy/AmazonESReadOnlyAccess'
)

iam.attach_role_policy(
    RoleName='my-search-lambda-role',
    PolicyArn='arn:aws:iam::aws:policy/CloudWatchLogsFullAccess'
)

iam.attach_role_policy(
    RoleName='my-search-lambda-role',
    PolicyArn='arn:aws:iam::aws:policy/AWSLambdaExecute'
)


