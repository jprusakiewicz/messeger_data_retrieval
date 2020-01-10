import json

with open('raw_request_history.txt') as json_file:
    data = json.load(json_file) #data is a list of dits

for dict in data:
    conv_data = dict['data'] #without next //todo foreach
    print(conv_data)
    data_json = {}
    message = []
    person = []
    for i in range(0, len(conv_data)):  #foreach person
        conv_id = conv_data[i]['id']
        person.append(conv_data[i]['participants']['data'][0]['name'])
        message.append((conv_data[i]['messages']['data']))

    new_mes = {}
    all_mes = []
    for i in range(0, len(message)):
        new_mes[person[i]] = message[i]

    for mes in new_mes.values():
        for i in range(len(mes)):
            mes[i] = mes[i]['message'] #ecstract message only, cant do it in line 17

    all_mes += new_mes.values()
    #all_mes += new_mes.keys()
with open('all_participants_data.txt', 'w', encoding='utf-8') as outfile:
     json.dump(all_mes, outfile, ensure_ascii=False)
