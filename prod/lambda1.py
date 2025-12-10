def lambda_handler(event, context):
    print("sawy")
    return {
        "statusCode": 200,
        "body": "Hello World"
    }
