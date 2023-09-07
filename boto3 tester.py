import boto3


s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
    print(bucket.name)

print("done")
client = boto3.client('lexv2-models')
client2 = boto3.client('lexv2-runtime')
botid = 'S71ZZ3C4MI'
botaliasid = 'TSTALIASID'
localeid = 'en_US'
"""
message = 'I need access'
"""
sessionid = "new_session"
"""botid = str(id)
'dialogAction':{'type': 'ElicitIntent', 'subSlotToElicit':{'name':'FlowerType'}},
"""
describe = client.describe_bot(botId = botid)
"""print(describe)"""
putsession = client2.put_session(botId = botid, botAliasId = botaliasid, localeId = localeid, sessionId = sessionid, 
messages = [{'contentType': 'PlainText', 'imageResponseCard': {'title':'titlee', 'buttons': [{'text': 'buttontext', 'value': 'buttonvalue'},]}},],
sessionState = {'intent':{'name': 'OrderFlowers', 'slots': {'FlowerType':{'value':{'interpretedValue':'roses'},}}, 'state': 'Fulfilled'}})
print("session created: ", putsession)
getsession = client2.get_session(botId = botid, botAliasId = botaliasid, localeId = localeid, sessionId = sessionid)
print("session information: ", getsession)
"""

response = client2.recognize_utterance(
    botId= botid,
    botAliasId= botaliasid,
    localeId= localeid,
    sessionId= sessionid,
    requestContentType= 'PCM',
    inputStream= text

)
"""
"""
response2 = client2.recognize_text(botId = botid, botAliasId = botaliasid, localeId = localeid, sessionId = sessionid, text = text)

input1 = input('How may I help you?')
"""
response = client2.recognize_text(
    botId= botid,
    botAliasId= botaliasid,
    localeId= 'en_US',
    sessionId= "new_session",
    text= 'I need access')
"""print("bot response: ", response)
"""
response_content = response['messages'][0]['content']

response_content1 = response['messages'][1]['content']




"""
print("bot response: ", response_content)
"""


next = input(response_content  + response_content1 + '\n')
"""
print(next)

"""
response2 = client2.recognize_text(
    botId= botid,
    botAliasId= botaliasid,
    localeId= 'en_US',
    sessionId= "new_session",
    text= next)

response_content2 = response2['messages'][0]['content']
next2 = input(response_content2 + '\n')

response3 = client2.recognize_text(
    botId= botid,
    botAliasId= botaliasid,
    localeId= 'en_US',
    sessionId= "new_session",
    text= next2)

response_content3 = response3['messages'][0]['content']
next3 = input(response_content3 + '\n')

response4 = client2.recognize_text(
    botId= botid,
    botAliasId= botaliasid,
    localeId= 'en_US',
    sessionId= "new_session",
    text= next3)

response_content4 = response4['messages'][0]['content']
next4 = input(response_content4 + '\n')

response5 = client2.recognize_text( 
    botId= botid,
    botAliasId= botaliasid,
    localeId= 'en_US',
    sessionId= "new_session",
    text= next4)

response_content5 = response5['messages'][0]['content']
print(response_content5)


"""response = client2.recognize_text(botId = botid)"""

"""print(client.list_bots())"""

"""
for bot in client.list_bots():
    print(bot.botName)
"""

"""sessionState={
        'dialogAction': {
            'type': 'ElicitIntent'
        },
        'intent': {
            'name': 'OrderFlowers',
            'slots': {
                'FlowerType': {
                    'value': {
                        'originalValue': message,
                        'interpretedValue': message,
                    },
                    'shape': 'Scalar'
                }
            },
            'state': 'InProgress',
            'confirmationState': 'None'

        }
        
    }
"""

"""
lex = boto3.resource('lex')

for bot in lex.bots.all():
    print(bot.name)

"""


    

"""
bot response:  {'ResponseMetadata': {'RequestId': '3bbe2550-9664-4888-930b-a1ce1df8bf27', 
'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '3bbe2550-9664-4888-930b-a1ce1df8bf27',
 'strict-transport-security': 'max-age=31536000; includeSubDomains', 'x-content-type-options': 
 'nosniff', 'date': 'Fri, 21 Jul 2023 18:07:13 GMT', 'content-type': 'application/json', 
 'content-length': '769', 'connection': 'keep-alive'}, 'RetryAttempts': 2}, 'messages':
   [{'content': 'Okay, I can help you with that.', 'contentType': 'PlainText'}, 
    {'content': 'Do you need Contractor access or Emp general access', 'contentType': 'PlainText'}], 
    'sessionState': {'dialogAction': {'type': 'ElicitSlot', 'slotToElicit': 'AccessType'}, 'intent': 
{'name': 'AccessRequest', 'slots': {'AccessType': None, 'DatesNeeded': None, 'ReasonNeeded': None}, 
 'state': 'InProgress', 'confirmationState': 'None'}, 'sessionAttributes': {}, 'originatingRequestId': 
 '5b97fcfb-e14d-4c24-b9c6-6114d95ae0ed'}, 'interpretations': [{'nluConfidence': {'score': 1.0}, 
'intent': {'name': 'AccessRequest', 'slots': {'AccessType': None, 'DatesNeeded': None,
 'ReasonNeeded': None}, 'state': 'InProgress', 'confirmationState': 'None'}}, {'intent': 
{'name': 'FallbackIntent', 'slots': {}}}], 'sessionId': 'new_session'}
"""

    