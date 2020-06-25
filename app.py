print("starting S3 basics .................................................................")
# Import AWS Lib for Python
import boto3
import uuid


# Define high level interface for S3
s3_resource = boto3.resource('s3')


# Define procedure to generate a unique bucketname
def create_bucket_name(bucket_prefix):
    # The generated bucket name must be between 3 and 63 chars long
    return ''.join([bucket_prefix, str(uuid.uuid4())])


# Show current session settings
print (f'> region name       :{boto3.session.Session().region_name}')
print (f'> active profile    :{boto3.session.Session().profile_name}')


# define function  for bucket creation
def create_bucket(bucket_prefix, s3_connection):
    session = boto3.session.Session()
    current_region = session.region_name
    bucket_name = create_bucket_name(bucket_prefix)
    bucket_response = s3_connection.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
        'LocationConstraint': current_region})
    print(bucket_name, current_region)
    return bucket_name, bucket_response


# Create an actual bucket
first_bucket_name, first_response = create_bucket(bucket_prefix='wisefinger',
                                                  s3_connection=s3_resource.meta.client)






print("stopping S3 basics .................................................................")