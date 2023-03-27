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
        try :
            cookiesPretty = json.dumps(r.cookies, indent=2, sort_keys=True)
        except:
            cookiesPretty = r.cookies
        
        response = {
            'status_code': r.status_code,
            'reason': r.reason,
            'headers':headerPretty,
            'body': pretty,
            'cookies':cookiesPretty,
        }
            
        return response['body']
        

def handelBody(params):
    if params.typeBody == 'json':
        return params.json
    else:
        return params.data

def handelUrl(params):
    url = params.url
    if params.url.__contains__('{{'):
        listUrl = url.split('{{')
        for i in range(len(listUrl)):
            if listUrl[i].__contains__('}}'):
                lists = listUrl[i].split('}}')
                listUrl[i] = lists[0]
                listUrl[i].insert(i, lists[1])
        url = listUrl.join('')
    return url
        


class CallApi:
    def get(self, params):
        url = handelUrl(params)
        body  = handelBody(params)
        r = requests.get(params.url, json=body, params=body,
                        headers=params.headers, data=params.data)
        j = handelResponse(r)
        return j


    def post(self,params):
        body  = handelBody(params)
        r = requests.post(params.url, json=body, params=body,
                        headers=params.headers, data=params.data)
        j = handelResponse(r)
        return j


    def put(self,params):
        body  = handelBody(params)
        r = requests.put(params.url, json=body, params=body,
                        headers=params.headers, data=params.data)
        j = handelResponse(r)
        return j


    def delete(self,params):
        body  = handelBody(params)
        r = requests.delete(params.url, json=body, params=body,
                        headers=params.headers, data=params.data)
        j = handelResponse(r)
        return j


    def patch(self,params):
        body  = handelBody(params)
        r = requests.patch(params.url, json=body, params=body,
                        headers=params.headers, data=params.data)
        j = handelResponse(r)
        return j

    def head(self,params):
        body  = handelBody(params)
        r = requests.head(params.url, json=body, params=body,
                        headers=params.headers, data=params.data)
        j = handelResponse(r)
        return j

    def options(self,params):
        body  = handelBody(params)
        r = requests.options(params.url, json=body, params=body,
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
