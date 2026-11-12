import boto3
s=boto3.client("s3")
s.list_api_v2(Bucket='abcd')
s.create_bucket(Bucket='abcd')
s.upload_object(Bucket='abcd',FileName='abc.txt',key='xyz.txt')
s.delete_object(Bucket='abcd',Key='xyz.txt')
