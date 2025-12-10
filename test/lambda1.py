def lambda_handler(event, context):
    print("Awsome")
    return {
        "statusCode": 200,
        "body": "Hello World"
    }
