from flask import Flask
from flask.views import MethodView
from pyngrok import ngrok
from flask import Response
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
class MockServer(MethodView):  
    def init(self, data):
        self.response = Response(
                response= data.response,
                status= data.status,
                headers={
                    'Content-Type': 'text/html',
                    'Server': 'Apache/2.4.18 (Ubuntu)',
                    'X-Powered-By': 'PHP/7.0.22-0ubuntu0.16.04.1',
                    'X-Frame-Options': 'SAMEORIGIN',
                    'X-Content-Type-Options': 'nosniff',
                    'X-XSS-Protection': '1; mode=block',
                },
            )
    def get(self):  
            file = open("plc.txt", "wb")
            file.write(bytes())
            s= file.readline()
            file.close()
            return s
    def post(self):
            return self.response
    def put(self):
            return self.response
    def delete(self):
            return self.response
    def patch(self):
            return self.response
    def head(self):
            return self.response
    def options(self):        
            return self.response

    
# url = ngrok.connect(5000).public_url
# print('Henzy Tunnel URL:', url)

def run(listData):
    app = Flask(__name__)
    for data in listData:
        view =  MockServer()
        v = view.as_view(data.path)
        app.add_url_rule(
            '/'+data.path, view_func=v, methods=['GET', 'POST']
        )
    app.run()

run([MockServerModel('{"name":"henzy"}', 200, '/', ['GET', 'POST'])])
