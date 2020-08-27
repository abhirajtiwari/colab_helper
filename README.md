# colab_helper
Simple utilities to make life easy on Google Colab

## colab_butler_bot
Telegram bot with basic functionality to send a message when training is over.
To use this: 
* copy the snippets.ipynb url as your snippet notebook
* make a secrets.py file in your google drive with the variables **bot_token** and **bot_chatID**. Refer this [medium article](https://medium.com/@ManHay_Hong/how-to-create-a-telegram-bot-and-send-messages-with-python-4cf314d9fa3e) to see how to get bot_token and bot_chatID.
* then execute the snippet in any of your colab notebook to get `colab_helper.tg_sendMessage(msg)` and `colab_helper.notifyTrainFinish(identifier)` (msg and identifier are strings).
