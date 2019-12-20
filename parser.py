import uuid
import boto3
from botocore.exceptions import ClientError
from fastapi import UploadFile
from typing import (List, Union, Dict)

BUCKET_NAME: str = 'testbucketimgloftly'
s3_client = boto3.client('s3')


def handle_file_upload(file: UploadFile):
    ''' Uploads unvalidated files to S3 (use validation beforehand!)'''
    try:
        file_name: str = file.filename
        unique_id = str(uuid.uuid4().int)[:5]
        extension: str = file.filename.split('.')[1]
        s3_client.upload_file(file_name + extension, BUCKET_NAME,
                              'loftly_image' + unique_id + extension)
        print('Image Saved to S3')
    except Exception as e:
        print(e)
