# Create an Amazon Glue Data Catalog:

import boto3

glue = boto3.client('glue')

# Create a new Glue Data Catalog
response = glue.create_database(
    DatabaseInput={
        'Name': 'my-search-catalog',
        'Description': 'Data catalog for my search data'
    }
)
