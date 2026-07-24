import boto3
from config import *

def delete_3_backup():
    s3 = boto3.client("s3")
    response= s3.list_objects_v2(
        Bucket=BUCKET_NAME
    )   
    folders = set()
    
    for item in response.get("Contents", []):
        folders.add(item["Key"].split("/")[0])
    
    folders = sorted(folders)
    
    if len(folders) > 3:
        old = folders[:-3]
    
        for folder in old:
    
            response = s3.list_objects_v2(
                Bucket=BUCKET_NAME,
                Prefix=folder
            )
            for file in response.get("Contents", []):
                s3.delete_object(
                    Bucket=BUCKET_NAME,
                    Key = file["Key"]
                )
            print(folder , "DELETED")
    else:
        print("No Old Backup Found")

