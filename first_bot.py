from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
import logging
import  settings

#Логгирование
logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s",
                    level = logging.INFO,
                    filename = "bot.log"
                    )

#Функция на ответ:
def greet_user(update, bot):
    text = 'Вызван/startt'
    logging.info(text)
    update.message.reply_text(text)

#Зеркальный ответ (Эхо бот)
def talk_to_me(update, bot):
    user_text = "Привет {}! Ты написал(а) {}".format(update.message.chat.first_name, update.message.text)
    logging.info("User: %s, Chat_id: %s, Messsage: %s", update.message.chat.username,
                update.message.chat.id, update.message.text)
    update.message.reply_text(user_text)

#Такая дает ответ на имя пользователя
#def greet_user(update: Updater, context: CallbackContext) -> None:
    #update.message.reply_text(f'Hello {update.effective_user.first_name}')

# Основная фунция
def main():
    mybot = Updater(settings.API_KEY)

    logging.info('Loading, bot is starting')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("Start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()

main()
