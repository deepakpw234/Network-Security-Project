import os
import sys

from src.exception.exception import CustomException
from src.logging.logger import logging

class S3Sync:
    def syn_folder_to_s3(self,folder,aws_bucket_url):
        command = f"aws s3 sync {folder} {aws_bucket_url} "
        os.system(command)

    def syn_s3_to_folder(self,folder,aws_bucket_url):
        command = f"aws s3 sync {aws_bucket_url} {folder} "
        os.system(command)