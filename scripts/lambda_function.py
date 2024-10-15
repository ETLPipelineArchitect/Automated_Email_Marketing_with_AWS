import json
import boto3
import pandas as pd

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        # Load raw CSV data from S3
        obj = s3.get_object(Bucket=bucket, Key=key)
        df = pd.read_csv(obj['Body'])
        # Transform data (example transforms)
        df['open_rate'] = df['opens'] / df['emails_sent'] * 100
        # Save processed data back to S3
        processed_key = key.replace('raw-data', 'processed-data').replace('.csv', '_processed.csv')
        csv_buffer = df.to_csv(index=False)
        s3.put_object(Bucket=bucket, Key=processed_key, Body=csv_buffer)
    return {'statusCode': 200, 'body': json.dumps('Data transformation complete.')}
