import call_api
import mock_server

def header(header):
    if header == None:
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }
    return headers
class Params:
    def __init__(self, url=None, params=None, headers=None, data=None, json=None):
        self.url = ''
        self.params = {}
        self.headers = header(headers)
        self.data = ''
        self.json = {}
        self.method = 'get'
        self.typeBody = 'json'
        self.environments = {}
        self.listMockServer = []

    def printList(self,l):
        s = ''
        for i in l:
            s = '\t'+ i.toString() + '\n'
        return s

    def toString(self):
        return f'''
        url: {self.url} 
        params: {self.params}
        headers: {self.headers}
        data: {self.data}
        json: {self.json}
        method: {self.method}
        typeBody: {self.typeBody}
        environments: {self.environments}
        list mock server : {self.printList(self.listMockServer)}
        
        '''
   


    def addMockServer(self, value: dict):
        self.listMockServer.append(mock_server.MockServerModel(
            value['response'], value['status'], value['path'], value['methods'],),)
        listMock = self.listMockServer
        mock_server.mockServers(listMock)

    def removeMockServer(self, path: str):
        for e in self.listMockServer:
            if e.path == path:
                self.listMockServer.remove(e)
                
    def addHeader(self, value: dict):
        for key in value:
            self.headers[key] = value[key]

    def removeHeader(self, value: list):
        for key in value:
            self.headers.pop(key)

    def addJson(self,  value: dict):
        for key in value:
            self.json[key] = value[key]

    def removeJson(self, value: list):
        for key in value:
            self.json.pop(key)

    def addParams(self, value: dict):
        for key in value:
            self.params[key] = value[key]

    def removeParams(self, value: list):
        for key in value:
            self.params.pop(key)

    def changeData(self, value):
        self.data = value

    def changeMethod(self, value: str):
        self.method = value.strip().lower()

    def addEnvironment(self, value: dict):
        for key in value:
            self.environments[key] = value[key]

    def removeEnvironment(self, value: list):
        for key in value:
            self.environments.pop(key)

    def send(self):
        callApi: call_api.CallApi = call_api.CallApi()
        if self.method == 'get':
            return callApi.get(self)
        elif self.method == 'post':
            return callApi.post(self)
        elif self.method == 'put':
            return callApi.put(self)
        elif self.method == 'delete':
            return callApi.delete(self)
        elif self.method == 'patch':
            return callApi.patch(self)
        elif self.method == 'head':
            return callApi.head(self)
        elif self.method == 'options':
            return callApi.options(self)
        else:
            print('Method not found')
            return None
