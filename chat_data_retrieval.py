import requests
import json
import pprint

next_url = ''
long_dict=[]
#request for only one person 'https://graph.facebook.com/v5.0/t_2705948632785028/messages?access_token=EAAjc4szTP2ABANM2ZAX7BR65Uo8EHSkmQF54GEcSVEhZAx6tXpZCRvVckHnDv7eb8ul2ObnLzGrpUu5CL4zURVCX7wxSYlt20GZAf9Ca7rROH5Ir2wecEV2iXVFbxS4KmdqwtZBKcKlYpJP9lgUb1JLZC2Yo8e39iAcl467VeTIcHlAyNGZAJBK&fields=message&limit=25&after=QVFIUmpSQWN3VGZAJZAm9kaFZATbGFhY3FNNUU4X0U4NTZAGSldvRFBrUVplZAm9qZAHBkTVRnTzRtZA1lQM2xPR3ZAaeWxZAbFpYNjRJaERRRkphRDU2b0ZAJOGxTZAU11WDJOWkd3T2JOMmhsNjJ3SWczNDFDUmF4ZAFQ5SGlCR29rOFgydWZArU2xq'
#single_conv = 'https://graph.facebook.com/v3.3/108525050657214/'
acc_token = open("token.txt", "r").read()
conversation = 'https://graph.facebook.com/v3.3/114322838608649/conversations?fields=participants%2Clink%2cmessages{{message}}{0}'.format(acc_token)
r = requests.get(conversation)
conv_data = r.json()
url = conv_data['paging']['next']

while True:
    try:
         #to delete
        conv_data = r.json()
        url = conv_data['paging']['next']
        next_url = url
        print(next_url)
        long_dict.append(conv_data)
        r = requests.get(next_url)
    except:
        long_dict.append(conv_data)
        break
    pass

#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(long_dict)
with open('raw_request_history.txt', 'w', encoding='utf-8') as outfile:
     json.dump(long_dict, outfile, ensure_ascii=False)

