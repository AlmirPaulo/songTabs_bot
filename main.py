# Software: songTabs_bot
# Description: A Telegram bot that give guitar tabs to songs.
# Info Page: https://github.com/AlmirPaulo/songTabs_bot

# Author: Almir Paulo
# Github: https://github.com/AlmirPaulo/
# Website: https://almirpaulo.github.io/
# Email: ap.freelas@gmail.com


from telegram.ext import (CallbackContext,
 Updater, 
 Filters, 
 CommandHandler,
  MessageHandler, 
  CallbackQueryHandler 
  )
from telegram import (Update, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode)
import side, os 

#Variables
token = os.getenv('TOKEN')

def start(update: Update, context: CallbackContext) -> None:
  update.message.reply_text('''
    Welcome! \n Type the name of your favorite artist or song to get your tabs. ''')

def help(update: Update, context: CallbackContext) -> None:
  update.message.reply_text('''Just type the name of your favorite artist or song. If something goes wrong, try in another way (just the first name of the artist, for instance). \n I will give you all the available tab options, you click, get the link and enjoy.''')

def get_tabs(update: Update, context: CallbackContext) -> None:
  user_input = update.message.text
  keyboard = []
  for i in side.api_req(user_input):
    keyboard.append([InlineKeyboardButton(f"{i['artist']['name']} - {i['title']}", callback_data=i['id'])])

  reply = InlineKeyboardMarkup(keyboard)
  update.message.reply_text('Choose your tab: ', reply_markup=reply)

def button(update: Update, context: CallbackContext) -> None:
  query = update.callback_query
  query.answer()
  query.edit_message_text(text=f"<a href= 'http://www.songsterr.com/a/wa/song?id={query.data}'>Click here</a> to get your tabs.\n Enjoy!", parse_mode=ParseMode.HTML)

def main():

    #Token
  updater = Updater(token.strip())

    #Commands
  updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, get_tabs))
  updater.dispatcher.add_handler(CallbackQueryHandler(button))
  updater.dispatcher.add_handler(CommandHandler('start', start))
  updater.dispatcher.add_handler(CommandHandler('help', help))
    
   #Server
  side.keep_alive()
    #Main Loop
  updater.start_polling()
  updater.idle()

main()