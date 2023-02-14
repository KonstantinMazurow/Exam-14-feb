# Создать бота, можно использовать существующего, который на команду /привет
# отвечает "привет" + username (его взять из getupdates)

import requests

TOKEN ='6103018803:AAHKXloqXkVsc90ml4lGJzoQPHtvY4ZG6Vw'

BASE_URL = 'http://api.telegram.org/bot' + TOKEN + '/'

def updates():
    current_updates_link = BASE_URL + 'getupdates'
    request = requests.get(current_updates_link)
    return request.json()

def message():
    data = updates()
    chat_id = data['result'][-1]['message']['chat']['id']
    last_message = data['result'][-1]['message']['text']
    message_list = {'chat_id' : chat_id, 'text' : last_message}
    return message_list

def send_message(chat_id, text='...'):
    url = BASE_URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)


def bot_answer():
    answer = message()
    text = answer['text']
    id = answer['chat_id']
    data = updates()
    if text == '/привет':
        first_name = data['result'][-1]['message']['chat']['first_name']
        last_name = data['result'][-1]['message']['chat']['last_name']
        send_message(id, 'Привет ' + first_name + ' ' + last_name)

 

bot_answer()