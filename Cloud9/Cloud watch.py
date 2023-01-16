# Use Amazon CloudWatch to monitor the performance and usage of your resources:

import boto3

cloudwatch = boto3.client('cloudwatch')

# Put a custom metric for the number of search requests
cloudwatch.put_metric_data(
    Namespace='MySearch',
    MetricData=[
        {
            'MetricName': 'SearchRequests',
            'Dimensions': [
                {
                    'Name': 'DomainName',
                    'Value': 'my-search-cluster'
                }
            ],
            'Value': 1,
            'Unit': 'Count'
        }
    ]
)

# Put an alarm for when the number of search requests exceeds a threshold
cloudwatch.put_metric_alarm(
    AlarmName='SearchRequestThreshold',
    ComparisonOperator='GreaterThanThreshold',
    EvaluationPeriods=1,
    MetricName='SearchRequests',
    Namespace='MySearch',
    Period=60,
    Threshold=1000,
    AlarmActions=[
        'arn:aws:sns:us-east-1:1234567890:my-search-alerts'
    ],
    Dimensions=[
        {
            'Name': 'DomainName',
            'Value': 'my-search-cluster'
        }
    ],
    Statistic='SampleCount'
)
