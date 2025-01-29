import requests
import json
import boto3

response = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd")


if response.status_code == 200:
    data = response.json()

    json_data = json.dumps(data,indent=4)

    s3_client = boto3.client("s3")

    s3_client.put_object(Bucket="project-api-s3-load", Key="crypto_data.json", Body=json_data)

    print("Data successfully saved to S3 bucket")
else:
    print("Failed to fetch data:", response.status_code)
