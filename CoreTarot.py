from DeckClass import Deck
from SQLiteClass import SQLite
"""
Main governing class with API
For every session make one Tarot object
"""
# Need full refactoring
# TODO Russian: Необходимо переделать весь проект в мультисервис
# Далее следует список как необходимо сделать на мое мнение
# Пользователь через бота или веб сервис подает запрос на работу с колодой
# Сервер или сервис или демон обрабатывает этот запрос
# Создается обьект Tarot, который в себе хранит: данные юзера, выбранную колоду
# Состояние сессии хранится в этом обьекте в сервисе в течении всего использования
# Далее пользователь через бота или вебсервис выбирает производить какието действия
# Приходит сообщение на сервис или демон и необходимые действия передаются на обьект Tarot
# Который производит необходимые операции принимая через АПИ ниже информацию
# И срет информацию обратно к сервису а тот к пользователю
# Сервис этот это по сути должен быть в этом классе в main() или около
# Тоесть не полноценный сервер навороченный, а просто прием и отправка информации
# для АПИ CoreTarot
# Как-то так, мне так это видится
# В текущем состоянии он просто дергает функции из классов 
  
class Tarot:
    """Governor of app"""
    def __init__(self, user_name, user_id):
        """Constructer"""
        self.user_name = user_name
        self.user_id = user_id

    def register_user(self, user_name, user_id):
        pass

    # TODO maybe need to full login authetication process

    def sign_user(self, user_name):
        pass

    def create_new_deck(self, deck_name, user_id):
        new_deck = Deck(deck_name, user_id)
        new_deck.create()
        return new_deck

    def load_deck(self, deck_name, user_id):
        sqlite = SQLite()
        new_deck = sqlite.select_deck(deck_name, user_id)
        return new_deck

    def save_deck(self, deck):
        sqlite = SQLite()
        return sqlite.save_deck(deck)
    
    def delete_deck(self, deck):
        pass
    
    def shuffle_deck(self, deck):
        pass

    def get_decks(self, user_id):
        decks = []
        counter = 0
        sqlite = SQLite()
        if (sqlite.is_deck_exist("thoth")):
            decks.append('THOTH')
            counter += 1
        if (sqlite.is_deck_exist("rw")):
            decks.append('Rider Waite')
            counter += 1
        if (sqlite.is_deck_exist("mr")):
            decks.append('Marseilles')
            counter += 1

        if (counter == 0):
            decks.append('нихуя нету')

        return decks

