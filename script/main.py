#listkey là list các key cần xóa
#vd ['key1','key2']
#lệnh chọn http method : 'http_method : <method>'
    #method có 12 loại là get, post, put, delete, patch, copy, head, options, link, unlink, purge, lock, unlock, propfind, view
    #nhập dạng str
#lệnh đổi url : 'url : <url>'
    #url là str
#lệnh thêm params : 'add_params : <params>'
    #params là dict
#lệnh xóa params : 'remove_params : <listkey>' 
#lệnh thêm header : 'add_header : <header>' 
# header là dict
#lệnh xóa header : 'remove_header : <listkey>'
#lệnh loại body : 'type_body : <body>' 
    # body có 2 loại là json và khác(nhập bắt cứ thứ gì khác json là được)
    # đổi loại không xoá dữ liệu loại cũ
#lệnh thêm body : 'add_body : <body>'
#lệnh xóa body : 'remove_body : <listkey>'
    # loại json thì nhập dict
    # loại khác thì nhập bất kỳ
    # nếu 2 lệnh này được gọi thì type_body sẽ được đổi thành json
#lệnh chageBody : 'change_body : <body>'
    # nếu 2 lệnh này được gọi thì type_body sẽ được đổi thành khác
#lệnh thêm biến môi trường : 'add_environment : <environment>'
#lệnh xóa biến môi trường : 'remove_environment : <environment>'
    # environment là str
    # cách nhập biến môi trường vào url thì biến môi trường để trong dấu {{}}
    # vd : 'url : http://{{environment}}.com'
#lệnh in config : 'config'
#nhập json vd : '{"name":"thanh"}'
#nhập lệnh add mock server : 
# vd : 
#   'add_mock_server' : {
#       'methods' : ['post','get'],
#       'path' : '/api/v1/users',
#       'response' : {}
#       'status' : 200
# }
#lệnh xóa mock server :remove_mock_server : <path>
#lệnh thoát : 'quit'


import params
import json

param = params.Params()

def handelDataJson(data:str):
    try :
        data= data.strip()
        body = json.loads(data)
        if type(body) is dict:
            return body
        else:
            print('cần nhập dữ liệu dạng dict')
            return None

    except Exception as e:
        print('định dạng json không hợp lệ')
        print(e)
        return None

while True:
    try :
        command = input("Nhập lệnh :")
        
        if command == 'quit':
            break
        elif command[:11].strip() == 'http_method':
            param.changeMethod(command[13:].strip())
        elif command[:3].strip() == 'url':
            param.url = command[5:].strip()
        elif command[:6].strip() == 'add_header':
            header = handelDataJson(command[8:].strip())
            if header is not None:
                param.addHeader(header)
        elif command[:11].strip() == 'remove_header':
            header = handelDataJson(command[13:].strip())
            if header is not None:
                param.removeHeader(header)
        elif command[:10].strip() == 'add_params':
            body = handelDataJson(command[12:].strip())
            if param is not None:
                param.addParams(body)
        elif command[:15].strip() == 'remove_params':
            body = handelDataJson(command[17:].strip())
            if param is not None:
                param.removeParams(body)
        elif command[:10].strip() == 'type_body':
            param.typeBody = command[12:].strip()
        elif    command[:8].strip() == 'add_body':
            param.typeBody = 'json'
            body = handelDataJson(command[10:].strip())
            if body is not None:
                param.addJson(body)
        elif command[:9].strip() == 'remove_body':
            param.typeBody = 'json'
            body = handelDataJson(command[11:].strip())
            if body is not None:
                param.removeJson(body)
        elif command[:8].strip() == 'change_body':
            param.typeBody = ''
            param.changeData(command[10:].strip())
        elif command[:4].strip() == 'send':
            print(param.send())
        elif command[:6].strip() == 'config':
            print(param.toString())
        elif command[:15].strip() == 'add_environment':
            environment = handelDataJson(command[17:].strip())
            if param is not None:
                param.addEnvironment(environment)
        elif command[:19].strip() == 'remove_environment':
            param.removeEnvironment(command[21:].strip())
        elif command[:15].strip() == 'add_mock_server':
            data = handelDataJson(command[17:].strip())
            if body is not None:
                param.addMockServer(data)
        elif command[:16].strip() == 'remove_mock_server':
            param.removeMockServer(command[18:].strip())
        else:
            print(command[:16])
            print('lệnh không hợp lệ')
    except Exception as e:
        print(e)