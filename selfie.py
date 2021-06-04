import re
import boto3
from botocore.exceptions import NoCredentialsError

ACCESS_KEY = '12345'
SECRET_KEY = '123456789'

def key():
    s = input()
  
    temp = re.findall(r'\d+', s)
    res = list(map(int, temp))
    return(res[0])

def upload_to_aws(local_file='paul-12345.jpg',bucket_name="kwikpic_selfies", s3_file_name=None):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)
    
    if s3_file is None:
        s3_file=str(key())+'.jpg'
    try:
        s3.upload_file(local_file, bucket_name, s3_file_name)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False

uploaded = upload_to_aws('local_file', 'bucket_name', 's3_file_name')