import boto3

from config import * 
def list_backup():
    s3 = boto3.client("s3")
    
    response = s3.list_objects_v2(Bucket=BUCKET_NAME)
    
    folders = set()
    
    for item in response.get ("Contents", []):
    
        folder = item["Key"].split("/")[0]
    
        folders.add(folder)
    print("Backup HISTORY ")
    
    for folder in sorted(folders):
        print(folder)