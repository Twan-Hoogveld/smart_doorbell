from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

def echo(update : Update, context: CallbackContext) -> None:
    print(context.args)
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def caps(update : Update, context : CallbackContext) -> None:
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

updater = Updater(token='YOUR_TOKEN',use_context=True)

updater.dispatcher.add_handler(CommandHandler('caps', caps))
updater.dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), echo))
updater.dispatcher.add_handler(CommandHandler('hello',hello))

updater.start_polling()
updater.idle()
