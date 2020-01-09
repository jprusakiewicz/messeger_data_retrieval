import requests
import json

#request for only one person 'https://graph.facebook.com/v5.0/t_2705948632785028/messages?access_token=EAAjc4szTP2ABANM2ZAX7BR65Uo8EHSkmQF54GEcSVEhZAx6tXpZCRvVckHnDv7eb8ul2ObnLzGrpUu5CL4zURVCX7wxSYlt20GZAf9Ca7rROH5Ir2wecEV2iXVFbxS4KmdqwtZBKcKlYpJP9lgUb1JLZC2Yo8e39iAcl467VeTIcHlAyNGZAJBK&fields=message&limit=25&after=QVFIUmpSQWN3VGZAJZAm9kaFZATbGFhY3FNNUU4X0U4NTZAGSldvRFBrUVplZAm9qZAHBkTVRnTzRtZA1lQM2xPR3ZAaeWxZAbFpYNjRJaERRRkphRDU2b0ZAJOGxTZAU11WDJOWkd3T2JOMmhsNjJ3SWczNDFDUmF4ZAFQ5SGlCR29rOFgydWZArU2xq'
#single_conv = 'https://graph.facebook.com/v3.3/108525050657214/'
acc_token = open("token.txt", "r").read()
conversation = 'https://graph.facebook.com/v3.3/114322838608649/conversations?fields=participants%2Clink%2cmessages{{message}}{0}'.format(acc_token)
r = requests.get(conversation)

conv_data = r.json()['data']
data_json = {}
message = []
person = []
for i in range(0, len(conv_data)):  #foreach person
    conv_id = conv_data[i]['id']
    person.append(conv_data[i]['participants']['data'][0]['name'])
    message.append((conv_data[i]['messages']['data']))
print(r.json())
new_mes = {}
for i in range(0, len(message)):
    new_mes[person[i]] = message[i]

for mes in new_mes.values():
    for i in range(len(mes)):
        mes[i] = mes[i]['message'] #ecstract message only, cant do it in line 17

with open('data.txt', 'w', encoding='utf-8') as outfile:
     json.dump(new_mes, outfile, ensure_ascii=False)



