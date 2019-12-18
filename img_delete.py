import boto3

BUCKET_NAME = 'testbucketimgloftly'
KEY = # get file name

s3 = boto3.resource('s3')
s3.Object(BUCKET_NAME, KEY).delete()