def lambda_handler(event, context):
    print("Sawy")
    return {
        "statusCode": 200,
        "body": "Hello World"
    }
