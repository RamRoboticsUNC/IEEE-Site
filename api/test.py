def handler(event, context):
    """Simple test handler to see if the issue is with FastAPI"""
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/html',
            'Access-Control-Allow-Origin': '*'
        },
        'body': '''<!DOCTYPE html>
<html>
<head>
    <title>IEEE Site Test</title>
</head>
<body>
    <h1>Hello from Vercel!</h1>
    <p>This is a simple test to see if the basic handler works.</p>
</body>
</html>'''
    }
