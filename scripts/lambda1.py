def lambda_handler(event, context):
    print("Test2")
    return {
        "statusCode": 200,
        "body": "Hello World"
    }
