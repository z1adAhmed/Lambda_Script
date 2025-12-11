def lambda_handler(event, context):
    print("Test")
    return {
        "statusCode": 200,
        "body": "Hello World"
    }
