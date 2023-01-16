# create CloudFront distribution

import boto3

cf = boto3.client('cloudfront')

# Create a new CloudFront distribution
response = cf.create_distribution(
    DistributionConfig={
        'CallerReference': 'my-search-distribution',
        'Origins': {
            'Quantity': 1,
            'Items': [
                {
                    'Id': 'my-search-origin',
                    'DomainName': 'my-search-origin.s3.amazonaws.com',
                    'S3OriginConfig': {
                        'OriginAccessIdentity': 'origin-access-identity/cloudfront/my-search-origin'
                    }
                }
            ]
        },
        'DefaultCacheBehavior': {
            'TargetOriginId': 'my-search-origin',
            'ViewerProtocolPolicy': 'redirect-to-https',
            'AllowedMethods': ['GET', 'HEAD', 'OPTIONS'],
            'CachedMethods': ['GET', 'HEAD'],
            'ForwardedValues': {
                'QueryString': True,
                'Cookies': {'Forward': 'all'},
                'Headers': {'Quantity': 0}
            }
        },
        'Enabled': True
    }
)
