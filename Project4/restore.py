import boto3

import os

from config import *

def restore():
    s3 = boto3.client("s3")
    
    backup_name = input("ENTER BACKUP Folder : ")
    
    response = s3.list_objects_v2(
        Bucket=BUCKET_NAME,
        Prefix=backup_name
    )
    
    
    os.makedirs(RESTORE_FOLDER, exist_ok=True)
    
    for item in response.get("Contents", []):
        filename = item["Key"].split("/")[-1]
        print(filename)
        if filename:
            destination = os.path.join(
                RESTORE_FOLDER,
                filename
            )
            s3.download_file(
                BUCKET_NAME,
                item["Key"],
                destination
            )
    
            print(filename, "Restored")
    print("Restore Completed ")