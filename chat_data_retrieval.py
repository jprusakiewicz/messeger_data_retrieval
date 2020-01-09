import requests
import json

#request for only one person 'https://graph.facebook.com/v5.0/t_2705948632785028/messages?access_token=EAAjc4szTP2ABANM2ZAX7BR65Uo8EHSkmQF54GEcSVEhZAx6tXpZCRvVckHnDv7eb8ul2ObnLzGrpUu5CL4zURVCX7wxSYlt20GZAf9Ca7rROH5Ir2wecEV2iXVFbxS4KmdqwtZBKcKlYpJP9lgUb1JLZC2Yo8e39iAcl467VeTIcHlAyNGZAJBK&fields=message&limit=25&after=QVFIUmpSQWN3VGZAJZAm9kaFZATbGFhY3FNNUU4X0U4NTZAGSldvRFBrUVplZAm9qZAHBkTVRnTzRtZA1lQM2xPR3ZAaeWxZAbFpYNjRJaERRRkphRDU2b0ZAJOGxTZAU11WDJOWkd3T2JOMmhsNjJ3SWczNDFDUmF4ZAFQ5SGlCR29rOFgydWZArU2xq'
single_conv = 'https://graph.facebook.com/v3.3/108525050657214/'
acc_token = '&access_token=EAAjc4szTP2ABANM2ZAX7BR65Uo8EHSkmQF54GEcSVEhZAx6tXpZCRvVckHnDv7eb8ul2ObnLzGrpUu5CL4zURVCX7wxSYlt20GZAf9Ca7rROH5Ir2wecEV2iXVFbxS4KmdqwtZBKcKlYpJP9lgUb1JLZC2Yo8e39iAcl467VeTIcHlAyNGZAJBK'
conversation = 'https://graph.facebook.com/v3.3/108525050657214/conversations?fields=participants%2Clink%2cmessages{{message}}{0}'.format(acc_token)
r = requests.get(conversation)

print(r.json()['data'][0])
print(r.json()['data'][1]) #not all data ->care for next
conv_data = r.json()['data']
data_json = {}
mes = []
person = []
for i in range(0, len(conv_data)):  #dla każdego rozmówcy
    conv_id = conv_data[i]['id']
    print(conv_data[i]['id'])
    print(conv_data[i]['messages']['data'])
    print(conv_data[i]['participants']['data'])
    #print(conv_data[i]['id'])
    #r_conv = requests.get('https://graph.facebook.com/v3.3/108525050657214/{0}'.format(acc_token))
    person.append(conv_data[i]['participants']['data'][0]['name'])
    mes.append((conv_data[i]['messages']['data']))



messages = conv_data[1]['messages']['data'] #wiadomości tylko z klara
for i in range(0, len(messages)):
    # print(messages[i])
    print(messages[i]['message'])

print(type(messages))
for i in range(0, len(mes)):
    print("person: {}".format(person[i]))
    print(mes[i][0]['message']) #print only first question from everyone


print("nowy")
j = 0 #person index
for i in range(0, len(mes[j])):
    print(mes[j][i]['message']) #print all from person index

new_mes = {}
print("all")
for i in range(0, len(mes)):
    print("person: {}".format(person[i]))
    # new_mes[person[i]] = mes[i][0]['message'] #dont touch
    new_mes[person[i]] = mes[i]
    #for j in range(0, len(mes[i])):
       #print(mes[i][j]['message']) #print all for all
        #new_mes[i] += mes[i][j]['message']


for key in new_mes.values():
    #print(new_mes.iteritems())
    for i in range(len(key)):
        key[i] = key[i]['message']


#j_per = json.dumps(new_mes, ensure_ascii=False)
#print(j_per)
with open('data.txt', 'w', encoding='utf-8') as outfile:
     json.dump(new_mes, outfile, ensure_ascii=False)



