import requests
import numpy as np
from time import sleep

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
    return response


data = get_updates_json(url)
update= last_update(data)
chat =  get_chat_id(update)

print update
print chat
#print send_mess(chat, 'bla')

text = ['Marvin, you are great', 'Marvin, I love you', 'Marvin, lets have...', 'Marvin, who is the girl in our bed?!?!']
def main():  
    update_id = last_update(get_updates_json(url))['update_id']
    t = 0
    while t<30:
        data = last_update(get_updates_json(url))
        if update_id == data['update_id']:
            send_text = ''
            send_text += 'How do you feel about '
            send_text += data['message']['text'].replace('me','you')
            send_mess(get_chat_id(data), send_text)
            update_id += 1
        sleep(1)
        t+=1

if __name__ == '__main__':  
    main()