import os
import boto3
from botocore.exceptions import NoCredentialsError, ClientError

class S3Sync:
    def __init__(self, bucket_name, region_name='us-east-1'):
        self.s3 = boto3.client('s3', region_name=region_name)
        self.bucket_name = bucket_name
    
    def upload_to_s3(self, file_name, object_name=None):
        if object_name is None:
            object_name = file_name
        try:
            self.s3.upload_file(file_name, self.bucket_name, object_name)
            print(f"File '{file_name}' uploaded successfully to bucket '{self.bucket_name}' as '{object_name}'.")
        except FileNotFoundError:
            print(f"The file '{file_name}' was not found.")
        except NoCredentialsError:
            print("Credentials not available.")
        except Exception as e:
            print(f"An error occurred: {e}")


    def download_from_s3(self, object_name, file_name=None):
        """Downloads a file from an S3 bucket."""
        if file_name is None:
            file_name = object_name  # Use object name if no file name is provided
        try:
            # Download the file
            self.s3.download_file(self.bucket_name, object_name, file_name)
            print(f"File '{object_name}' downloaded successfully from bucket '{self.bucket_name}' as '{file_name}'.")
        except FileNotFoundError:
            print(f"The file '{file_name}' was not found.")
        except NoCredentialsError:
            print("Credentials not available.")
        except ClientError as e:
            print(f"An error occurred: {e.response['Error']['Message']}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


# obj = S3Sync('emtion-sentiment')
# obj.download_from_s3('text.csv','datapath/newtxt.csv')
# obj.upload_to_s3('datapath/sentiment.csv' ,'sentiment.csv')


