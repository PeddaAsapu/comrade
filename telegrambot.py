import django
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'comrade.settings'
django.setup()

from telegram.ext import *
from bot.models import *
from trip.models import *
import json


API_KEY = '5969605735:AAHRetW-aJBlO05QyhcXgHjpFNuDc57z_zY'

print("Bot started")

def get_trip_details(update) :
    update.message.reply_text('Select your means of transportation: \n\n' +'/Air \n \n' +'/Rail')


def existing_user(id):
    user = TelegramUsers.objects.filter(pk=id).first()
    if user:
        return True
    return False 

def create_user(update) :
    print("Update details")
    print("="*100)
    print(update)
    print("="*100)
    first_name = str(update.message.chat.first_name)
    last_name = str(update.message.chat.last_name)
    user_id = str(update.message.chat.id)
    is_bot = False
    try:
        is_bot = update.message['from']['is_bot']
    except Exception as e:
        print(e)
        pass
    telegram_users = TelegramUsers(user_id=user_id,first_name=first_name, last_name=last_name, is_bot=is_bot)
    telegram_users.save()

def handle_message(update, context):
    text = str(update.message.text).lower()
    print("update : ", update)
    print("text Entered : ", text)
    first_name = str(update.message.chat.first_name).capitalize()
    user_id = update.message.chat.id
    if not existing_user(user_id):
        create_user(update)
    print(f"User {first_name} Already exists ")
    update.message.reply_text(f'Hi {first_name}. Hearty Welcome from team Comrade.')
    update.message.reply_text('Are you ready to enter your trip details ? \n\n' +'/Yes \n \n' +'/No')
    if text == '/yes' :
        get_trip_details(update)
    else :
        update.message.reply_text('Choose \n\n' +'/Ready  \n When you are ready ')
    
    
if __name__ == '__main__' :
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_handler(CommandHandler("Yes", get_trip_details))
    updater.start_polling(1.0)
    updater.idle()