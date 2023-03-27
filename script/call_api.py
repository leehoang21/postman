import requests
import json
import params

def handelResponse(r):
        try:
            j = json.loads(r.text)
            
            pretty = json.dumps(j, indent=2, sort_keys=True)
        except:
            pretty = r.text
            
        try :
            headerPretty = json.dumps(r.headers, indent=2, sort_keys=True)
        except:
            headerPretty = r.headers
      
        
        response = {
            "status_code": r.status_code,
            "reason": r.reason,
            "headers":headerPretty,
            "body": pretty,
           
        }
        return response['body']
        

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
        body  = handelBody(params)
        r = requests.get(url, json=body, params=body,
                        headers=params.headers, data=params.data)
        j = handelResponse(r)
        return j


    def post(self,params):
        url = handelUrl(params)
        body  = handelBody(params)
        r = requests.post(url, json=body, params=body,
                        headers=params.headers, data=params.data)
        j = handelResponse(r)
        return j


    def put(self,params):
        url = handelUrl(params)
        body  = handelBody(params)
        r = requests.put(url, json=body, params=body,
                        headers=params.headers, data=params.data)
        j = handelResponse(r)
        return j


    def delete(self,params):
        url = handelUrl(params)
        body  = handelBody(params)
        r = requests.delete(url, json=body, params=body,
                        headers=params.headers, data=params.data)
        j = handelResponse(r)
        return j


    def patch(self,params):
        url = handelUrl(params)
        body  = handelBody(params)
        r = requests.patch(url, json=body, params=body,
                        headers=params.headers, data=params.data)
        j = handelResponse(r)
        return j

    def head(self,params):
        url = handelUrl(params)
        body  = handelBody(params)
        r = requests.head(url, json=body, params=body,
                        headers=params.headers, data=params.data)
        j = handelResponse(r)
        return j

    def options(self,params):
        url = handelUrl(params)
        body  = handelBody(params)
        r = requests.options(url, json=body, params=body,
                        headers=params.headers, data=params.data)
        j = handelResponse(r)
        return j



# apiHost = 'http:hoanglee/'
# hosttest = 'https://www.python.org/'
# token = 'yJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC8xMzQuMjA5LjEwNi4yMjM6MjA0NVwvYXBpXC9hdXRoXC9sb2dpbiIsImlhdCI6MTY3OTQxMTkwMywiZXhwIjoxNjc5NDU1MTAzLCJuYmYiOjE2Nzk0MTE5MDMsImp0aSI6IjF6dm9ZZzM1OWtjc1N5SmsiLCJzdWIiOjIsInBydiI6IjIzYmQ1Yzg5NDlmNjAwYWRiMzllNzAxYzQwMDg3MmRiN2E1OTc2ZjcifQ.tAIInZ8S7cz_3rSk8mVOVtCdZ_pkCOcBqGaBcINQfxI'
# # test get
# # print(get(apiHost+'asks?page=1&limit=10'))
# # test post
# reponse = post(params=params.Params(
#    url =  hosttest + "testGet200",
# ),)
# # test put
# # print(put(hosttest))
# # test delete
# # print(delete(hosttest))
