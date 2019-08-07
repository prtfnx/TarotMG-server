from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, InlineQueryHandler, BaseFilter
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
import random
import CoreTarot
import logging
import datetime
import settings

# For log
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def start_command(update, context):
    text = 'Я люблю телему 93! Люблю печеньки! Люблю посвящения в 11 градус! Для создания колодны введите "/create_deck name" где name - "thoth"'
    context.bot.send_message(chat_id=update.message.chat_id, text=text)


def create_deck(update, context):
    user_id = update.message.from_user.id
    user_name = update.message.from_user.name
    deck_name = context.args[0]
    tarot = CoreTarot.Tarot(user_name, user_id)
    deck = tarot.create_new_deck(deck_name, user_id)
    save_deck(tarot, deck)
    update.message.reply_text(
        'Создание колодны успешно! Спасибо лично алистеру кравли и его ЖЕЗЛУ. Для того чтобы достать одну карту введите "/one_card name_of_deck" для 4 карт "/set_of_cards name_of_deck')


def save_deck(tarot, deck):
    tarot.save_deck(deck)


def load_deck(update, context):
    pass


def user_decks(update):
    user_id = update.message.from_user.id
    user_name = update.message.from_user.name
    tarot = CoreTarot.Tarot(user_name, user_id)
    decks = tarot.get_decks(user_id)
    decks_string = ', '.join([str(deck) for deck in decks])
    update.message.reply_text('Твои колоды, сучка: ' + decks_string)


def one_card(update, context):
    user_id = update.message.from_user.id
    user_name = update.message.from_user.name
    deck_name = context.args[0]
    if len(context.args) > 1:
        position = int(context.args[1])
    else:
        position = random.randint(0, 77)
    tarot = CoreTarot.Tarot(user_name, user_id)
    deck = tarot.load_deck(deck_name, user_id)
    card = deck.get_card(position)
    update.message.reply_text(card.name)
    context.bot.send_photo(chat_id=update.message.chat_id, photo=open(card.path_to_image, 'rb'))


def set_of_cards(update, context):
    user_id = update.message.from_user.id
    user_name = update.message.from_user.name
    deck_name = context.args[0]
    position = random.sample(range(0, 77), 4)
    tarot = CoreTarot.Tarot(user_name, user_id)
    deck = tarot.load_deck(deck_name, user_id)
    for i in range(4):
        card = deck.get_card(position[i])
        update.message.reply_text(card.name)
        context.bot.send_photo(chat_id=update.message.chat_id, photo=open(card.path_to_image, 'rb'))


def main():
    updater = Updater(settings.token, use_context=True)  # Token API to Telegram
    dp = updater.dispatcher
    # Handlers
    start_command_handler = CommandHandler('start', start_command)
    create_deck_command_handler = CommandHandler('create_deck', create_deck)
    user_decks_command_handler = CommandHandler('user_decks', user_decks)
    one_card_command_handler = CommandHandler('one_card', one_card)
    set_of_cards_command_handler = CommandHandler('set_of_cards', set_of_cards)
    # Add handlers to dispatcher
    dp.add_handler(start_command_handler)
    dp.add_handler(create_deck_command_handler)
    dp.add_handler(user_decks_command_handler)
    dp.add_handler(one_card_command_handler)
    dp.add_handler(set_of_cards_command_handler)
    # Start seek for update
    updater.start_polling(clean=True)
    # Stop bot for  Ctrl + C
    updater.idle()


if __name__ == '__main__':
    main()
