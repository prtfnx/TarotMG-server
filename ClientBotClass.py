import pickle
import socket
HOST = '127.0.0.3'
PORT = 8888
"""
Class Client describe structure of Client 
to connect to service and communicate
"""


class Client:
    
    def __init__(self, user_name, user_id):
        """Constructor"""
        self.user_name = user_name
        self.user_id = user_id
     
    def connection(self, ask):
        """Maintain connection with master"""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            print('connected')
            request = self.form_request(ask)
            message = pickle.dumps(request)
            s.sendall(message)
            s.sendall(b'\\n')  # write separator
            print('taking reponse from master')
            data = s.recv(4096)  # take response from master
            print('response taken from master')
            response = pickle.loads(data)
            answer = self.form_answer(response)
            return answer

    def form_request(self, message):
        """Form request from message"""
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
            'close_connection': True
        }
        return request

    def form_answer(self, response):
        """Form answer to slave"""
        if response['errors'] == []:
            return {'adress':'from master','results':response['results']}
        else:
            pass # TODO logic to operate with errors
