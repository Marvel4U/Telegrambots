import requests
import numpy as np
from time import sleep
from telegram_bot_lib import *

from dummy_cooking_api_lib import *





state = 'greeting'
requsting = False
cookstate = False
# other states:
# 'search', 'cook'

def greet():
    send_text = 'Hello, what do we want to cook together today?'
    send_mess(chat_id, send_text)

def search_init():
    send_text = 'Are you hungry for anything particular?'
    send_mess(chat_id, send_text)
    return 'search'

def search(message):
    item = 'lasagna'
    if item in message:
        send_text = "That's a great idea, I have a great recipe for "+item+"!"
        state = 'cook'
    else:
        send_text = "Sorry I don't have a recipe for this, but how about some lasagna?"
        requesting = 'lasagna'
        state = 'search'

    send_mess(chat_id, send_text)
    return state

def cook(recipe, cookstate):
    if cookstate == False:
        send_text = "These are the ingredients you need: "
        send_mess(chat_id, send_text)
        
        ingredients = get_ingredients(recipe)
        for ing in ingredients:
            send_text = str(ing[0]) + ' '+ ing[1]
            send_mess(chat_id, send_text)
        cookstate = 1
        
        send_text = "Tell me when you are ready to start."
        send_mess(chat_id, send_text)
    elif cookstate != False:
        instructions = get_instructions(recipe).split('\n')
        print instructions
        send_text = instructions[cookstate]
        send_mess(chat_id, send_text)
        cookstate += 1
        
    return "cook", cookstate
        


def read_cook():
    pass





#data = get_updates_json(url)
#update= last_update(data)
#chat =  get_chat_id(update)

#def main():
if True:
    update_id = last_update(get_updates_json(url))['update_id'] +1
    t = 0
    while t<30:
        chatdata = last_update(get_updates_json(url))
        chat_id = get_chat_id(chatdata)
        if update_id == chatdata['update_id']:
            message = get_chat_input(chatdata)
            print state
            if state == 'greeting':
                greet()
                sleep(1)
                state = search_init()
            elif state == 'search':
                state = search(message)
                recipe = 'lasagna'
                if state=='cook': 
                    cookstate = False
                    update_id -= 1
            elif state == 'cook':
                state, cookstate = cook(recipe, cookstate)
            
            update_id += 1
        sleep(1)
        t+=1
    print "Time is up..."

#if __name__ == '__main__':  
    #main()










