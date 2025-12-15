def lambda_handler(event, context):
    print("Aish")
    return {
        "statusCode": 200,
        "body": "Hello World"
    }
