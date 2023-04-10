import json
from datetime import datetime


class History:
    def __init__(self, time=None, config=None, response=None):
        self.time = time
        self.config = config
        self.response = response

    def toJson(self):
        model = {
            'time': self.time,
            'config': self.config,
            'response': self.response,
        }
        return json.dumps(model)

    def toString(self):
        return f'''
        time: {self.time} 
        config: {self.config}
        response: {self.response}
        '''


def createHistory():
    with open('history.json', 'w') as f:
        json.dump('[]', f)


def addHistory(param, response):
    data = loadData() 
    with open('history.json', 'w') as f:
        
        # create history
        dateNow = datetime.now()
        format_code = '%d/%m/%Y %H:%M:%S'
        strDate = dateNow.strftime(format_code)
        history = History(
            time=strDate, config=param.toJson(), response=response)
        # add history
        data.append(history.toJson())
        json.dump(data, f)


def loadData():
    try:
        f = open('history.json', 'r')
        data = json.load(f)
        if data == '':
            return []
        j = []
        for item in data:
          j.append(json.loads(item))
        return data
    except Exception as e:
      print(e)
      return []


def displayHistory():
    data = loadData()
    for item in data:
        history = json.loads(item)
        print('\ntime :' +history['time'])
        print('\nconfig :'+history['config'])
        print('\nresponse :'+history['response'])
        print('------------------------------------------------------------------')
