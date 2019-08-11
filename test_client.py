import asyncio
import pickle

async def tcp_echo_client():
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888)

    print('Send ')
 
    request = {
        'context': {
            'user_id': 323,
            'user_name': 'user_name',
            'number_of_operations': 2,
            'from_app': 'test'
            },
        'operations': ['create_new_deck', 'get_cards'],
        'arguments': [['thoth',], [[1],]],
        'close_connection': True
        }
 
    message = pickle.dumps(request)
    writer.write(message)

    data = await reader.read()
    response = pickle.loads(data)
    print(response)
    print(response['results'][1][0].name)

    print('Close the connection')
    writer.close()

asyncio.run(tcp_echo_client())
