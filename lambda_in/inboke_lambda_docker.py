import json
import boto3
import os 
import json

ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

client = boto3.client(
    service_name='lambda', 
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=SECRET_ACCESS_KEY,
    )
 
def inboke_lambda_1(inputParams):
 
    response = client.invoke(
        FunctionName = 'arn:aws:lambda:us-east-2:781211160608:function:inference-lambda-docker-function',
        InvocationType = 'RequestResponse',
        Payload = json.dumps(inputParams)
    )
 
    responseFromInferenceLambdaDockerFunction = json.load(response['Payload'])

    return responseFromInferenceLambdaDockerFunction