import boto3

import os

from datetime import datetime

from config import * 

s3 = boto3.client("s3")

backup_folder = datetime.now().strftime("Backup_%Y-%m-%d_%H-%M-%S")

datetime.now()

for file in os.listdir(LOCAL_FOLDER):

    path= os.path.join(LOCAL_FOLDER, file)

    if os.path.isfile(path):

        s3.upload_file(
            path,
            BUCKET_NAME,
            backup_folder + "/" + file
        )


        print(file, "Uploaded")
print("Backup Completed")