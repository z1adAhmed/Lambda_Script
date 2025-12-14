def lambda_handler(event, context):
    print("Mr Hammad")
    return {
        "statusCode": 200,
        "body": "Hello World"
    }
