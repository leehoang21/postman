import requests
import json
import params
from history import addHistory

def handelResponse(r,param):
    try:
        j = json.loads(r.text)
        pretty = json.dumps(j, indent=2, sort_keys=True)
    except:
        pretty = r.text
    try:
        headerPretty = json.dumps(r.headers, indent=2, sort_keys=True)
    except:
        headerPretty = r.headers
    response = '\t\t\t\t'+str(r.status_code)+' ' + r.reason + '\n' + pretty
    #save to history
    addHistory(param,response)
    return response

def handelBody(params):
    if params.typeBody == 'json':
        return params.json
    else:
        return params.data

def handelUrl(params):
    url = str(params.url)
    for key in params.environments:
        url = url.replace('{{'+key+'}}', params.environments[key])
    return url


class CallApi:

    def get(self, params):
        url = handelUrl(params)
        body = handelBody(params)
        r = requests.get(url, json=body, params=body,
                         headers=params.headers, data=params.data)
        j = handelResponse(r,param=params)
        return j

    def post(self, params):
        url = handelUrl(params)
        body = handelBody(params)
        r = requests.post(url, json=body, params=body,
                          headers=params.headers, data=params.data)
        j = handelResponse(r,param=params)
        return j

    def put(self, params):
        url = handelUrl(params)
        body = handelBody(params)
        r = requests.put(url, json=body, params=body,
                         headers=params.headers, data=params.data)
        j = handelResponse(r,param=params)
        return j

    def delete(self, params):
        url = handelUrl(params)
        body = handelBody(params)
        r = requests.delete(url, json=body, params=body,
                            headers=params.headers, data=params.data)
        j = handelResponse(r,param=params)
        return j

    def patch(self, params):
        url = handelUrl(params)
        body = handelBody(params)
        r = requests.patch(url, json=body, params=body,
                           headers=params.headers, data=params.data)
        j = handelResponse(r,param=params)
        return j

    def head(self, params):
        url = handelUrl(params)
        body = handelBody(params)
        r = requests.head(url, json=body, params=body,
                          headers=params.headers, data=params.data)
        j = handelResponse(r,param=params)
        return j

    def options(self, params):
        url = handelUrl(params)
        body = handelBody(params)
        r = requests.options(url, json=body, params=body,
                             headers=params.headers, data=params.data)
        j = handelResponse(r,param=params)
        return j
