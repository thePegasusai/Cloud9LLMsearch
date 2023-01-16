# Create an Elasticsearch Service (ESS) cluster:

import boto3

es = boto3.client('es')

# Create a new Elasticsearch Service cluster
response = es.create_elasticsearch_domain(
    DomainName='my-search-cluster',
    ElasticsearchVersion='7.6',
    ElasticsearchClusterConfig={
        'InstanceType': 'r5.large.elasticsearch',
        'InstanceCount': 1,
        'DedicatedMasterEnabled': False
    },
    EBSOptions={
        'EBSEnabled': True,
        'VolumeType': 'gp2',
        'VolumeSize': 10
    }
)
