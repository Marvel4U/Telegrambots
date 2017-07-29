import requests
import numpy as np
from time import sleep
from telegram_bot_lib import *

from dummy_cooking_api_lib import *



class botlist:
    def __init__(self, API_connector):
        self.TG = API_connector
        self.bot_dict = {}
    def add(self, ID):
        self.bot_dict[ID] = cooking_bot(TG)
    def get_message(self):
        ID = TG.get_chat_id()
        if not(ID) in self.bot_dict.keys():
            self.add(ID)
        self.bot_dict[ID].get_message()


class cooking_bot:
    def __init__(self, API_connector):
        self.state = 'greeting'
        # other states:
        # 'search', 'cook'
        self.cookstate = False
        self.TG = API_connector
        self.recipe = ''
        #self.requsting = False

    def get_message(self):
        self.raw_message = self.TG.get_chat_input()
        self.message_interpret()
        self.respond()
        
    def send(self, text):
        self.TG.send_mess(text)
    
    def message_interpret(self):
        self.message = self.raw_message
    
    def respond(self):
        if self.state == 'greeting':
            self.greet()
        elif self.state == 'search':
            self.search()
            self.recipe = 'lasagna'
            if self.state=='cook': 
                self.cookstate = False
                self.TG.update_id -= 1
        elif self.state == 'cook':
            self.cook(self.recipe)

    def greet(self):
        self.send('Hello, what do we want to cook together today?')
        sleep(1)
        self.search_init()

    def search_init(self):
        self.send('Are you hungry for anything particular?')
        self.state = 'search'

    def search(self):
        item = 'lasagna'
        if item in self.message:
            self.send("That's a great idea, I have a great recipe for "+item+"!")
            self.state = 'cook'
        else:
            self.send("Sorry I don't have a recipe for this, but how about some lasagna?")
            requesting = 'lasagna'
            self.state = 'search'

    def cook(self,recipe):
        if self.cookstate == False:
            self.send("These are the ingredients you need: ")
            
            ingredients = get_ingredients(recipe)
            send_str = ''
            for ing in ingredients:
                send_str += str(ing[0]) + ' '+ ing[1] + '\n'
            self.send(send_str)
            self.cookstate = 1
            
            self.send("Tell me when you are ready to start.")
        elif self.cookstate != False:
            instructions = get_instructions(recipe).split('\n')
            #print instructions
            self.send(instructions[self.cookstate])
            self.cookstate += 1
            
        self.state = "cook"
            
    
    



#data = get_updates_json(url)
#update= last_update(data)
#chat =  get_chat_id(update)

#def main():
if True:
    TIMEOUT = 30
    TG = Telegram_API()
    #BL = botlist(TG)
    bot = cooking_bot(TG)
    
    t = 0
    while t<TIMEOUT:
        TG.update_chat()
        if TG.new_message():
            print 'new message coming'
            bot.get_message()
        sleep(1)
        t+=1
    print "Time is up..."

#if __name__ == '__main__':  
    #main()










