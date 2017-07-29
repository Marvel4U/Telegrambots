import requests


class Telegram_API:
    def __init__(self):
        self.url = 'https://api.telegram.org/bot409693072:AAGTDWRyKgvhI2MdX5Oe-YsOXWQ5KdaqrEw/'
        self.update_id = self.last_update(self.get_updates_json(self.url))['update_id'] +1
        
    def update_chat(self):
        self.newdata = self.last_update(self.get_updates_json(self.url))
        self.chat_id = self.get_chat_id(self.newdata)
        
    def new_message(self):
        new_msg = self.update_id == self.newdata['update_id']
        if new_msg:
            self.update_id += 1
        return new_msg


    def get_updates_json(self,request):  
        params = {'timeout': 100, 'offset': None}
        response = requests.get(request + 'getUpdates')
        return response.json()

    def last_update(self,data):  
        results = data['result']
        total_updates = len(results) - 1
        return results[total_updates]

    def get_chat_id(self,update):  
        chat_id = update['message']['chat']['id']
        return chat_id

    def send_mess(self, text):  
        params = {'chat_id': self.chat_id, 'text': text}
        response = requests.post(self.url + 'sendMessage', data=params)
        print "sending text: "+ text
        return response

    def get_chat_input(self):
        return self.newdata['message']['text']