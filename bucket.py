import boto3
import os

aws_access_key_id = 'DO00G4VJUPZTWQ82Y2UQ'
aws_secret_access_key = 'ZVFAAJOLnqZN3PlMK/c00PCqIykkxmU+qIn6wGfK9H0'
endpoint_url = 'https://first-project1-staging.sgp1.digitaloceanspaces.com'
space_name = 'first-project1-staging'
object_key = 'image/courses_standard/Lkg.png'
local_file_path = 'C:/Users/raham/Downloads/Lkg.png'

s3 = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    endpoint_url=endpoint_url
)

os.makedirs(os.path.dirname(local_file_path), exist_ok=True)

s3.download_file(space_name, object_key, local_file_path)