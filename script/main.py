#lệnh chọn http method : 'http_method : <method>'
    #method có 12 loại là get, post, put, delete, patch, copy, head, options, link, unlink, purge, lock, unlock, propfind, view
    #nhập dạng str
#lệnh đổi url : 'url : <url>'
    #url là str
#lệnh thêm params : 'add_params : <params>'
    #params là dict
#lệnh xóa params : 'remove_params : <params>'
#lệnh thêm header : 'add_header : <header>' 
#lệnh xóa header : 'remove_header : <header>'
    # header là dict
#lệnh loại body : 'type_body : <body>' 
    # body có 2 loại là json và khác(nhập bắt cứ thứ gì khác json là được)
    # đổi loại không xoá dữ liệu loại cũ
#lệnh thêm body : 'add_body : <body>'
#lệnh xóa body : 'remove_body : <body>'
    # loại json thì nhập dict
    # loại khác thì nhập bất kỳ
    # nếu 2 lệnh này được gọi thì type_body sẽ được đổi thành json
#lệnh chageBody : 'change_body : <body>'
    # nếu 2 lệnh này được gọi thì type_body sẽ được đổi thành khác
#lệnh in config : 'config'
#nhập json vd : '{"name":"thanh"}'

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
        command = input("Enter a command: ")
        command = command.strip()
        if command == 'quit':
            break
        elif command[:11] == 'http_method':
            param.changeMethod(command[13:])
        elif command[:3] == 'url':
            param.url = command[5:]
        elif command[:6] == 'add_header':
            header = handelDataJson(command[8:])
            if header is not None:
                param.addHeader(header)
        elif command[:11] == 'remove_header':
            header = handelDataJson(command[13:])
            if header is not None:
                param.removeHeader(header)
        elif command[:10] == 'add_params':
            body = handelDataJson(command[12:])
            if param is not None:
                param.addParams(body)
        elif command[:15] == 'remove_params':
            body = handelDataJson(command[17:])
            if param is not None:
                param.removeParams(body)
        elif command[:10] == 'type_body':
            param.typeBody = command[12:]
        elif    command[:8] == 'add_body':
            param.typeBody = 'json'
            body = handelDataJson(command[10:])
            if body is not None:
                param.addJson(body)
        elif command[:9] == 'remove_body':
            param.typeBody = 'json'
            body = handelDataJson(command[11:])
            if body is not None:
                param.removeJson(body)
        elif command[:8] == 'change_body':
            param.typeBody = ''
            param.changeData(command[10:])
        elif command[:4] == 'send':
            print(param.send())
        elif command[:6] == 'config':
            print(param.toString())
        else:
            print('lệnh không hợp lệ')
    except Exception as e:
        print(e)