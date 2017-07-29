import requests

url = 'https://api.telegram.org/bot409693072:AAGTDWRyKgvhI2MdX5Oe-YsOXWQ5KdaqrEw/'

def get_updates_json(request):  
    params = {'timeout': 100, 'offset': None}
    response = requests.get(request + 'getUpdates')
    return response.json()

def last_update(data):  
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]

def get_chat_id(update):  
    chat_id = update['message']['chat']['id']
    return chat_id

def send_mess(chat, text):  
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    print "sending text: "+ text
    return response


def get_chat_input(chatdata):
    return chatdata['message']['text']