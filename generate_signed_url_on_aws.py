import boto3
from botocore.exceptions import ClientError

def generate_presigned_url(bucket_name, object_name, access_key, secret_key, region="us-east-1", expiration=3600):
    s3_client = boto3.client(
        's3',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name=region
    )
    
    try:
        response = s3_client.generate_presigned_url(
            'get_object',
            Params={'Bucket': bucket_name, 'Key': object_name},
            ExpiresIn=expiration
        )
    except ClientError as e:
        print(f"Failed to generate URL: {e}")
        return None

    return response

# アカウントとオブジェクトの設定
bucket_name = 'your_bucket_name'
object_name = 'your_object_name'
access_key = 'your_access_key'
secret_key = 'your_secret_key'
region = 'your_region'

# 署名付きURLを生成
signed_url = generate_presigned_url(bucket_name, object_name, access_key, secret_key, region)
if signed_url:
    print("Generated signed URL:", signed_url)
