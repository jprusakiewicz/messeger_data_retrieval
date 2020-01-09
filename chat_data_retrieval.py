import requests
import json

#request for only one person 'https://graph.facebook.com/v5.0/t_2705948632785028/messages?access_token=EAAjc4szTP2ABANM2ZAX7BR65Uo8EHSkmQF54GEcSVEhZAx6tXpZCRvVckHnDv7eb8ul2ObnLzGrpUu5CL4zURVCX7wxSYlt20GZAf9Ca7rROH5Ir2wecEV2iXVFbxS4KmdqwtZBKcKlYpJP9lgUb1JLZC2Yo8e39iAcl467VeTIcHlAyNGZAJBK&fields=message&limit=25&after=QVFIUmpSQWN3VGZAJZAm9kaFZATbGFhY3FNNUU4X0U4NTZAGSldvRFBrUVplZAm9qZAHBkTVRnTzRtZA1lQM2xPR3ZAaeWxZAbFpYNjRJaERRRkphRDU2b0ZAJOGxTZAU11WDJOWkd3T2JOMmhsNjJ3SWczNDFDUmF4ZAFQ5SGlCR29rOFgydWZArU2xq'
single_conv = 'https://graph.facebook.com/v3.3/108525050657214/'
acc_token = '&access_token=EAAjc4szTP2ABANM2ZAX7BR65Uo8EHSkmQF54GEcSVEhZAx6tXpZCRvVckHnDv7eb8ul2ObnLzGrpUu5CL4zURVCX7wxSYlt20GZAf9Ca7rROH5Ir2wecEV2iXVFbxS4KmdqwtZBKcKlYpJP9lgUb1JLZC2Yo8e39iAcl467VeTIcHlAyNGZAJBK'
conversation = 'https://graph.facebook.com/v3.3/108525050657214/conversations?fields=participants%2Clink%2cmessages{{message}}{0}'.format(acc_token)
r = requests.get(conversation)

#print(r.json()['data'][0])
#print(r.json()['data'][1]) #not all data ->care for next
conv_data = r.json()['data']
data_json = {}
mes = []
person = []
for i in range(0, len(conv_data)):  #foreach person
    conv_id = conv_data[i]['id']
    #print(conv_data[i]['id'])
    #print(conv_data[i]['messages']['data'])
    #print(conv_data[i]['participants']['data'])
    #r_conv = requests.get('https://graph.facebook.com/v3.3/108525050657214/{0}'.format(acc_token))
    person.append(conv_data[i]['participants']['data'][0]['name'])
    mes.append((conv_data[i]['messages']['data']))

new_mes = {}
for i in range(0, len(mes)):
    new_mes[person[i]] = mes[i]

for key in new_mes.values():
    #print(new_mes.iteritems())
    for i in range(len(key)):
        key[i] = key[i]['message'] #ecstract message only

with open('data.txt', 'w', encoding='utf-8') as outfile:
     json.dump(new_mes, outfile, ensure_ascii=False)



