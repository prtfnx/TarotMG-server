import pickle
import asyncio
"""
Class Client describe structure of Client 
to connect to service and communicate
"""


class Client:
    dict_of_clients = {}

    def __init__(self, user_name, user_id):
        """Constructor"""
        self.user_name = user_name
        self.user_id = user_id
        self.data_stream_in = asyncio.Queue()  # data stream to connection
        self.data_stream_out = asyncio.Queue() 
        self.close_connection = False  # signal to disconnect from master
        self.keep_connection = True  # signal to stop client
        Client.dict_of_clients[user_id] = self

    @staticmethod
    def get_instance(user_name, user_id):
        """Get instance of client if exist, if not, create new"""
        if user_id in Client.dict_of_clients:
            return Client.dict_of_clients[user_id]
        else:
            return Client(user_name, user_id)

    async def connection(self):
        """Maintain connection with master"""
        reader, writer = await asyncio.open_connection(
         '127.0.0.1', 8888)
        print('connected')
        while self.keep_connection:
            print('start waiting for request')
            request = await self.form_request()
            print('take request')
           
            message = pickle.dumps(request)
            writer.write(message)
            writer.write(b'\\n') # write separator
            self.data_stream_in.task_done()
            print('taking reponse from master')
            data = await reader.readuntil(b'\\n') # take response from master
            print('response taken from master')
            response = pickle.loads(data)
            answer = self.form_answer(response)
            print('puting answer to stream')
            await self.data_stream_out.put(answer)

    async def form_request(self):
        """Form request from message"""
        print('start form_request')
        print(self.data_stream_out)
        await self.data_stream_out.join()
        message = await asyncio.wait_for(self.data_stream_in.get(), 5)
        print('get data from stream')
        # message must be dict with  2 list:
        # {operations: ['op1','op2'..],
        # arguments [[arg11, arg12, ..],[arg21, arg22, ..], ..]}
        request = {
            'context': {
                'user_id': self.user_id,
                'user_name': self.user_name,
                'number_of_operations': len(message['operations']),
                'from_app': 'bot'
            },
            'operations': message['operations'],
            'arguments': message['arguments'],
            'close_connection': self.close_connection
        }
        return request

    def form_answer(self, response):
        """Form answer to slave"""
        if response['errors'] == []:
            return {'adress':'from master','results':response['results']}
        else:
            pass # TODO logic to operate with errors

            
async def test():
    print('1')
    test = Client.get_instance('testname', 232)
    
    message = {
      'adress': 'to master',
      'operations': ['create_new_deck', 'get_cards'],
      'arguments': [['thoth'], [[2, 3, 4]]]}
    await test.data_stream_in.put(message)
    print('start connect from main')
    task_connection = asyncio.create_task(test.connection())
    task_put = asyncio.create_task(test.data_stream_in.put(message))
    #await asyncio.gather(task_connection, task_put)
    print('taken')
    print(test.data_stream_out)
    print('taking data from stream from main')
    await asyncio.sleep(10)
    answer = await test.data_stream_out.get()
    print(answer)
asyncio.run(test())
