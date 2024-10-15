import boto3
import pandas as pd

def upload_data_to_s3(csv_file_path, bucket_name, s3_key):
    s3 = boto3.client('s3')
    s3.upload_file(csv_file_path, bucket_name, s3_key)

if __name__ == '__main__':
    upload_data_to_s3('path/to/your/email_campaign_data.csv', 'your-bucket', 'email-campaigns/raw-data/email_campaign_data.csv')
