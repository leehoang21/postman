    #url là str
#lệnh thêm params : 'add_params : <params>'
    #params là dict

#lệnh thêm header : 'add_header : <header>' 
# header là dict

#lệnh thêm body : 'add_body : <body>'
    # nếu lệnh này được gọi thì type_body sẽ được đổi thành json
#lệnh thêm biến môi trường : 'add_environment : <environment>'
    # vd add_environment : {"ss":"trubute"}
    # environment là str
    # cách nhập biến môi trường vào url thì biến môi trường để trong dấu {{}}
    # vd : 'url : http://{{environment}}.com'
#nhập json vd : '{"name":"thanh"}' ["ss"] 
########## tất cả các lệnh phía trên phần value đằng sau nhập theo dạng json

#lệnh chageBody : 'change_body : <body>'
    # nếu 2 lệnh này được gọi thì type_body sẽ được đổi thành khác
    # value đằng sau nhập dạng khác json
#lệnh loại body : 'type_body : <body>' 
    # body có 2 loại là json và khác(nhập bắt cứ thứ gì khác json là được)
    # đổi loại không xoá dữ liệu loại cũ

#listkey là list các key cần xóa
#vd ['key1','key2']
#lệnh xóa biến môi trường : 'remove_environment :  <listkey>'
#lệnh xóa params : 'remove_params : <listkey>' 
#lệnh xóa header : 'remove_header : <listkey>'
#lệnh xóa body : 'remove_body : <listkey>'
#lệnh in config : 'config'
#lệnh chọn http method : 'http_method : <method>'
    #method các loại là get, post, put, delete, patch, copy, head, options
    #nhập dạng str
#lệnh đổi url : 'url : <url>'
#lệnh thoát : 'quit'
#lệnh in lịch sử request : history

import params
import json
import history

param = params.Params()

try :
    param.loadData()
except Exception as e:
    param.saveData()

def handelDataJson(data:str):
    try :
        data= data.strip()
        body = json.loads(data)
        if type(body) is dict:
            return body
        else:
            print('cần nhập dữ liệu dạng json')
            return None

    except Exception as e:
        print('định dạng không hợp lệ')
        print(e)
        return None

def handelDataList(data:str):
    try :
        data= data.strip()
        body = json.loads(data)
        if type(body) is list:
            return body
        else:
            print('cần nhập dữ liệu dạng danh sách')
            return None

    except Exception as e:
        print('định dạng không hợp lệ')
        print(e)
        return None

while True:
    try :
        command = input("Nhập lệnh :")
        command = command.lower()
        if command == 'quit':
            break
        elif command == 'history':
            history.displayHistory()
        elif command[:11].strip() == 'http_method':
            param.changeMethod(command[13:].strip())
        elif command[:3].strip() == 'url':
            param.url = command[5:].strip()
        elif command[:10].strip() == 'add_header':
            header = handelDataJson(command[12:].strip())
            if header is not None:
                param.addHeader(header)
        elif command[:13].strip() == 'remove_header':
            listKey = handelDataList(command[15:].strip())
            if listKey is not None:
                param.removeHeader(listKey)
                    
        elif command[:10].strip() == 'add_params':
            body = handelDataJson(command[12:].strip())
            if param is not None:
                param.addParams(body)
        elif command[:13].strip() == 'remove_params':
            listKey = handelDataList(command[15:].strip())
            if listKey is not None:
                param.removeParams(listKey)
        elif command[:9].strip() == 'type_body':
            param.typeBody = command[11:].strip()
        elif    command[:8].strip() == 'add_body':
            param.typeBody = 'json'
            body = handelDataJson(command[10:].strip())
            if body is not None:
                param.addJson(body)
        elif command[:11].strip() == 'remove_body':
            listKey = handelDataList(command[13:].strip())
            if listKey is not None:
                param.removeJson(listKey)
        elif command[:11].strip() == 'change_body':
            param.typeBody = ''
            param.changeData(command[13:].strip())
        elif command[:4].strip() == 'send':
            print(param.send())
        elif command[:6].strip() == 'config':
            print(param.toJson())
        elif command[:15].strip() == 'add_environment':
            environment = handelDataJson(command[17:].strip())
            if param is not None:
                param.addEnvironment(environment)
        elif command[:18].strip() == 'remove_environment':
            listKey = handelDataList(command[20:].strip())
            param.removeEnvironment(listKey)
        else:
            print(command[:16])
            print('lệnh không hợp lệ')
    except Exception as e:
        print(e)
    finally:
        param.saveData()