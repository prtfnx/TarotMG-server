import asyncio
import pickle

async def tcp_echo_client():
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888)
    while 1:
        print('Send ')
 
        request = {
            'context': {
                'user_id': 323,
                'user_name': 'user_name',
                'number_of_operations': 2,
                'from_app': 'test'
                },
            'operations': ['create_new_deck', 'get_cards'],
            'arguments': [['thoth',], [[2,3,4]]],
            'close_connection': False
            }
    
        message = pickle.dumps(request)
        writer.write(message)
        writer.write(b'\\n')
        print('receive')
        data = await reader.readuntil(b'\\n')
        response = pickle.loads(data)
        print(response)
        results_cards=response['results'][1]
        print(results_cards)
        for result in results_cards:
            print(result.name)
            
        await asyncio.sleep(1)
    writer.close()

asyncio.run(tcp_echo_client())
