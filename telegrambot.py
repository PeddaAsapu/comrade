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
    text = str(update.message.text).lower()
    user_id = update.message.chat.id
    user_trips = Trip.objects.filter(user=user_id)
    
    for trip in user_trips:
        message = "Your Trip details are below: \n"
        message += "="*19
        message += f"\nMode of Transport : {trip.mode_of_transport} \n"
        if trip.mode_of_transport.name == 'Flight':
            message += f"Airlines: {trip.vehicle.provider} \n"
            message += f"Flight Number: {trip.vehicle} \n"
        message += f"Date: {trip.travel_date_time.date()} \n"
        message += f"Time of Flight: {trip.travel_date_time.time().strftime('%H:%M')} \n"
        message += f"From: {trip.source_location} \n"
        message += f"To: {trip.destination_location} \n"
    return message
    #update.message.reply_text('Select your means of transportation: \n\n' +'/Air \n \n' +'/Rail')


def existing_user(id):
    user = TelegramUsers.objects.filter(pk=id).first()
    if user:
        return True
    return False 

def create_user(update) :
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

def exit_command(update):
    update.message.reply_text("Thank You. See you again :) ")   

def handle_message(update, context):
    text = str(update.message.text).lower()
    first_name = str(update.message.chat.first_name).capitalize()
    user_id = update.message.chat.id
    if not existing_user(user_id):    
        create_user(update)
    print("text ", text )
    if text not in ['/yes','/no','/explore','/exit'] :
        update.message.reply_text(f'Hi {first_name}. Welcome from team Comrade.')
        update.message.reply_text('Glad that we have you in our System Already!!')
        update.message.reply_text('Would you like to see your existing Trip Details ? \n' +'/Yes \n' +'/No')
    elif text == '/yes' :
        message = get_trip_details(update)
        update.message.reply_text(message)
        update.message.reply_text('Explore other options ? \n' +'/Explore \n' +'/Exit')
    elif text == '/no' or  text == '/explore':
        update.message.reply_text("Choose the Other Options from below: \n")
        update.message.reply_text('/Edit  - Edit Trip Details \n' +'/Find - Finds your travel mate \n' + '/Help \n' + '/Exit')
    
    elif text == '/exit' :
        exit_command(update)
    
    #update.message.reply_text('Are you ready to enter your trip details ? \n\n' +'/Yes \n \n' +'/No')
    #if text == '/yes' :
    #    get_trip_details(update)
    #else :
    #    update.message.reply_text('Choose \n\n' +'/Ready  \n When you are ready ')
    
    
if __name__ == '__main__' :
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_handler(CommandHandler("My_Trip_Details", handle_message))
    dp.add_handler(CommandHandler("Yes", get_trip_details))
    updater.start_polling()
    updater.idle()