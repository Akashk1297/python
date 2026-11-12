import boto3
s=boto3.client("s3")
s.list_objects_v2(Bucket='abcd')
s.create_bucket(Bucket='abcd',CreateBucketConfiguration={"LocationConstraint": "ap-south-1"})
s.upload_object(Bucket='abcd',FileName='abc.txt',Key='xyz.txt')
s.delete_object(Bucket='abcd',Key='xyz.txt')
