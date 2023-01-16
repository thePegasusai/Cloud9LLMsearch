Use Amazon Cognito to create a user pool and authentication service:

import boto3

cognito = boto3.client('cognito-idp')

# Create a new user pool
response = cognito.create_user_pool(
    PoolName='my-search-pool'
)

# Create a new app client for the user pool
response = cognito.create_user_pool_client(
    UserPoolId=response['UserPool']['Id'],
    ClientName='my-search-client'
)
