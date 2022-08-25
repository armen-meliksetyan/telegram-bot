import telebot

bot = telebot.TeleBot('1129293409:AAH9c1oiqA4oTfc29d4PyKgoWshWfNe8-T4')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Hello, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEFHvJitzZvoW2Svuko6qLWcNDn3eFSxQACKgMAAs-71A4f8rUYf2WfMCkE')

@bot.message_handler(commands=['help'])
def start(message):
    mess = 'The bot now is for testing only. Contact with my admin: https://t.me/armmeliksetyan'
    bot.send_message(message.chat.id, mess, parse_mode='html')
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEFHwhit0nmCXtblYHdtbM64uMeviBUwgACFQMAAs-71A5n0o9RaoG_uikE')

@bot.message_handler()
def get_user_text(message):
    if message.text == "Hello":
        bot.send_message(message.chat.id, f"Hi {message.from_user.first_name}", parse_mode='html')
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEFHvJitzZvoW2Svuko6qLWcNDn3eFSxQACKgMAAs-71A4f8rUYf2WfMCkE')
    elif message.text == "id" or message.text == "Id" or message.text == "iD" or message.text == "ID":
        bot.send_message(message.chat.id, f"Your ID: {message.from_user.id}", parse_mode='html')
    else:
        bot.send_message(message.chat.id, "sorry, I don't understand you. I am not very clever yet.", parse_mode='html')
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEFH35it2bGiYbkWzSYktqZ1k_uyCFPQAACIAMAAs-71A4jijg8wgu1oCkE')

bot.polling(none_stop=True)