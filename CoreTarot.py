import asyncio
import pickle
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
        self.selected_deck = None
        self.hand = []  # hand with cards

    def register_user(self, user_name, user_id):
        pass

    # TODO maybe need to full login authetication process

    def sign_user(self, user_name):
        pass

    def create_new_deck(self, deck_name):
        user_id = self.user_id
        new_deck = Deck(deck_name, user_id)
        new_deck.create()
        self.selected_deck = new_deck

    def load_deck(self, deck_name, user_id):
        sqlite = SQLite()
        new_deck = sqlite.select_deck(deck_name, user_id)
        self.selected_deck = new_deck

    def save_deck(self):
        deck = self.selected_deck
        sqlite = SQLite()
        return sqlite.save_deck(deck)
    
    def delete_deck(self):
        deck = self.selected_deck
        sqlite = SQLite()
        sqlite.delete_deck(deck.name, deck.user_id)
    
    def shuffle_deck(self):
        self.selected_deck.shuffle
    
    def put_from_hand_to_deck(self):
        for _ in range(len(self.hand)):
            self.selected_deck.card_list.append(hand.pop())

    def get_cards(self, positions=[1]):
        """Take cards from deck to hand."""
        deck = self.selected_deck
        hand = self.hand
        for position in positions:
            length_of_deck = len(deck.card_list)
            if position > length_of_deck:
                position = length_of_deck
            hand.append(deck.get_card(position))
        return hand

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


async def handle_connection(reader, writer):
    """Callback function on connection. Protocol:
    Request:{
        context:{
            user_id: string 'user_id'
            user_name: string 'user_name'
            number_of_operations: int number_of_operations
            from_app: string 'app_name'
                }
        operations: list string ['oper1', 'oper2'...[]
        arguments: list list any [ [args1.1, arg1.2], [args2.1, args2.2],... ]
        close_connection: bool True/False
            }

     Response:{
        errors: list string [err1, err2, err3..] # one error to every operation from request
        results: list any [res1, res2, res3..]   #
              }
    """
    print('start recieving')
    data = await reader.read(10000)
    message = pickle.loads(data)
    print(message)
    user_id = message['context'].get('user_id')
    user_name = message['context'].get('user_name')
    core = Tarot(user_name, user_id)
    results = []
    errors = []
    print('start manage operations')
    for operation, arguments in zip(message['operations'], message['arguments']):
        print(f'manage {operation}')
        func = {
            'create_new_deck': core.create_new_deck,
            'load_deck': core.load_deck,
            'save_deck': core.save_deck,
            'delete_deck': core.delete_deck,
            'shuffle_deck': core.shuffle_deck,
            'get_cards': core.get_cards,
            'get_decks': core.get_decks,
            'put_from_hand_to_deck': core.put_from_hand_to_deck
            }[operation]
        print(f'managed {func}')  
        results.append(func(*arguments))
    response ={'errors': errors, 'results': results}
    print(f'response:{response}')
    message = pickle.dumps(response)
    from pympler import asizeof # test
    print(asizeof.asizeof(message) )# test
    writer.write(message)
    await writer.drain()
    print("Close the connection")
    writer.close()


async def server():
    server = await asyncio.start_server(
        handle_connection, '127.0.0.1', 8888)
    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')
    async with server:
        await server.serve_forever()


def main():
    asyncio.run(server())

if __name__ == '__main__':
    main()
