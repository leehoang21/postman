from flask import Flask
from pyngrok import ngrok
from flask import Response

app = Flask(__name__)


class MockServerModel:
    response: str = None
    status: int = None
    path: str = None
    methods: list = None

    def __init__(self, response, status, path, methods):
        self.response = response
        self.status = status
        self.path = path
        self.methods = methods
    
    def toString(self):
        return f'''
        response: {self.response} 
        status: {self.status}
        path: {self.path}
        methods: {self.methods}
            
        '''

def mockServer():
        _data = MockServer.data
        return Response(
            response=_data.response,
            status=_data.status,
            headers={
                'Content-Type': 'text/html',
                'Server': 'Apache/2.4.18 (Ubuntu)',
                'X-Powered-By': 'PHP/7.0.22-0ubuntu0.16.04.1',
                'X-Frame-Options': 'SAMEORIGIN',
                'X-Content-Type-Options': 'nosniff',
                'X-XSS-Protection': '1; mode=block',
            },

        )
class MockServer:
    def __init__(self, listData):
        for data in listData:
            self.data = data
            app.add_url_rule('/'+data.path, data.path, mockServer)

# url = ngrok.connect(5000).public_url
# print('Henzy Tunnel URL:', url)

def run():
    app.run()
