import boto3
client = boto3.client('ecr')

repository_name = "my_native_repo"

response = client.create_repository(repositoryName=repository_name)

repository_url = response['repository']['repositoryUri']
print(repository_url)