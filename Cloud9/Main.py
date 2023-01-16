# This main.py file will import all the functions from the different files, and call them in the main() function. Once you run this main.py file it will run all the functions in the order they have been defined in the main function and it will create all the resources that you have defined in the different files.
It's important to make sure that the functions are defined and working correctly in each file and the dependencies are satisfied in order for the main.py file to work correctly.

from s3_bucket import create_s3_bucket
from elasticsearch_cluster import create_elasticsearch_cluster
from glue_catalog import create_glue_catalog
from cloudfront_distribution import create_cloudfront_distribution
from cognito_pool import create_cognito_pool
from cloudwatch_metrics import create_cloudwatch_metrics

def main():
    create_s3_bucket()
    create_elasticsearch_cluster()
    create_glue_catalog()
    create_cloudfront_distribution()
    create_cognito_pool()
    create_cloudwatch_metrics()

if __name__ == "__main__":
    main()
