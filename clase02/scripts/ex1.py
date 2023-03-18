## crear un usuario con las politicas de tener una clave de acceso
## pre requisitos configurar el aws  ,ejecutamos en cmd aws configure y llenamos data

import boto3

s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
        print(bucket.name)