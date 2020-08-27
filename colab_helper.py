import requests
from secrets import bot_token, bot_chatID

def tg_sendMessage(msg):
    send_url = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + msg

    response = requests.get(send_url)

    return response.json

def notifyTrainFinish(name):
    tg_sendMessage('Training finished for '+name)
