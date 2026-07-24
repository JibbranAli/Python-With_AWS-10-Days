import boto3
from config import *

def delete_backup_folder():
    s3 = boto3.client("s3")
    
    backup = input("BACKUP FOlder : ")
    
    response = s3.list_objects_v2(
        Bucket=BUCKET_NAME,
        Prefix=backup
    )
    print(response)
    
    
    for item in response.get("Contents", []):
        s3.delete_object(
            Bucket=BUCKET_NAME,
            Key=item["Key"]
        )
    
        print (item["Key"], "DELETED")
    
    print("BACKUP REMOVED")
