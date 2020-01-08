import requests
import json

single_conv = 'https://graph.facebook.com/v3.3/108525050657214/'

acc_token = '&access_token=EAAjc4szTP2ABANzI5tV6QLZBaicCLTbrf7adKtQYW5YQwq1hG88rgwPbeo6udhMRlyhxV7Q5pmLuyYl6ZBgX8PM9lFqkAZCfozDNyp66fj3ZBZCxmdEaNtViaz1PNXWlM5zBXooAZCvJqYpueuW24RGbrYk3xZCUCfDmdNd7AZCAdOuBezUTBEiqFjZC7dlGc9ZBVxS5kcEZBgCIQZDZD'

conversation = 'https://graph.facebook.com/v3.3/108525050657214/conversations?fields=participants,link&limit=400{0}'.format(acc_token)
r = requests.get(conversation)



print(r.json()['data'][0])
conv_data = r.json()['data']
for i in range(0, len(conv_data)):
    conv_id = conv_data[i]['id']
    print(conv_data[i]['id'])
    r_conv = requests.get('https://graph.facebook.com/v3.3/108525050657214/{0}'.format(acc_token))
    print(r_conv)
