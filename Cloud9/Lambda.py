# Use an AWS Lambda function to handle incoming search requests and query the ESS cluster for the relevant data:

import boto3

def lambda_handler(event, context):
    # Get the search query from the event
    query = event['query']
    
    # Connect to the Elasticsearch Service
    es = boto3.client('es')
    
    # Run the search query
    response = es.search(
        index='my-search-index',
        body={
            'query': {
                'match': {
                    '_all': query
                }
            }
        }
    )
    
    # Format the search results
    results = []
    for hit in response['hits']['hits']:
        results.append(hit['_source'])
    
    # Return the search results to the user
    return {'results': results}
