import json
from urllib.parse import parse_qs
import requests

def hello(event, context):
    urlSlack = 'https://slack.com/api/chat.postMessage'
    body = parse_qs(event['body'])
    print(body)
    if not body['token'][0] == 'SEU_TOKEN':
        return {"statusCode": 401, "body": "User not allowed"}
    messageBody = body['text'][0]
    userNameSent = body['user_name'][0]
    try:    
        userName = messageBody.split(" ")[0]        
        if not (messageBody):
            return {"statusCode": 500, "body": "Must preovide all values"}
        message = {'text': messageBody, 'channel': 'SEU_CHANNEL','username': 'elogio', 'link_names':userName}
        message = json.dumps(message)
        response = requests.post(urlSlack, data=message,headers={'content-type': 'application/json' , 'Authorization':'Bearer SEU_OAUTH_TOKEN'})
        
        print(response)
        return {'statusCode': 200, 'body': 'Elogio registrado com sucesso!'}
    except Exception as exc:
        print(exc)
