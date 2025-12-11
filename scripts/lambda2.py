def lambda_handler(event, context):
    print("Zoz")
    return {
        "statusCode": 200,
        "body": "Hello World"
    }
