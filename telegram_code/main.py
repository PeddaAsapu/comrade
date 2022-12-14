from urllib import response
from config import API_KEY 
from telegram.ext import *
import Responses as R


print("BOT Started !!")

def start_command(update, context):
    first_name = str(update.message.chat.first_name).capitalize()
    update.message.reply_text(f'Hello {first_name} !! Welcome to Comrade. We will help you to find a comrade for your ride.')
    update.message.reply_text('Select your means of transportation: \n\n' +'/Air \n \n' +'/Rail')
    
def help_command(update, context):
    update.message.reply_text('Please send the issue you are facing, to support@comrade.com')
    
def air_command(update, context):
    update.message.reply_text('''Enter the following info and please provide a line spacing after each response
                              Start Date:
                              Start place:
                              Destination:
                              Flight number:
                              Your e-mail: ''')
    update.message.reply_text("Click /exit once you are done. Thanks!!")
def rail_command(update, context):
    update.message.reply_text('''Enter the following info and please provide a line spacing after each response
                              Start Date:
                              Start place:
                              Destination:
                              Train number:
                              Your e-mail: ''')
    update.message.reply_text("Click /exit once you are done. Thanks!!")
    
def exit_command(update, context):
    update.message.reply_text("Thanks for reaching us. We send you an e-mail shortly, if we have your comrade.")
    
def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.user_responses(text)
    update.message.reply_text(response)

def welcome_message(update, context):
    update.message.reply_text('Welcome to Comrade. We will help you to find a comrade for your ride.')

def error(update, context):
    print("Something went wrong!!")
    
if __name__ == '__main__' :
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher
    #dp.add_handler(MessageHandler(Filters.text, welcome_message))
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("Air", air_command))
    dp.add_handler(CommandHandler("Rail", rail_command))
    dp.add_handler(CommandHandler("exit", exit_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()