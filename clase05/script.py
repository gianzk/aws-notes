import boto3
import pandas as pd
import io
import json

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Obtener el nombre del archivo Parquet desde el evento S3
    bucket = 'bucketdemov2' #
    key = 'outputv1/run-1680363939227-part-block-0-r-00000-snappy.parquet' #

    # Leer el archivo Parquet en un dataframe de pandas
    s3_object = s3.get_object(Bucket=bucket, Key=key)
    
    buffer = io.BytesIO(s3_object['Body'].read())

    df = pd.read_parquet(buffer)

    # Convertir el dataframe en un diccionario y luego en JSON
    data_dict = df.to_dict(orient='records')
    json_data = json.dumps(data_dict)

    return {
        'statusCode': 200,
        'body': json_data
    }