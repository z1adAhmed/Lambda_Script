def lambda_handler(event, context):
    print("Hello World2")
    return {
        "statusCode": 200,
        "body": "Hello World"
    }
