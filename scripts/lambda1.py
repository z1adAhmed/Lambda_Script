def lambda_handler(event, context):
    print("Test1")
    return {
        "statusCode": 200,
        "body": "Hello World"
    }
