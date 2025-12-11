def lambda_handler(event, context):
    print("Working?")
    return {
        "statusCode": 200,
        "body": "Hello World"
    }
