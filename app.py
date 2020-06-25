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

# Generate new bucketname
bucketname =  create_bucket_name("wise_")
print(f'> new bucketname = {bucketname}')










print("stopping S3 basics .................................................................")