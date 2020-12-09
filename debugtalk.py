import hashlib
import time

import requests


def sleep(n_secs):
    time.sleep(n_secs)


def get_params(n=1):
    '''
    获取列表套字典的数据结构
    :return:
    '''
    return [
        ['正常登录', 'admin', '1234', 'success'],
        ['密码为空', 'admin', '', '用户名或密码不能为空'],
        ['用户名为空', '', '1234', '用户名或密码不能为空'],
        ['用户名和密码为空','','','用户名或密码不能为空']
    ]

def sign():
    optCode = 'testfan'
    phoneNum = 1111
    timestamp = int(time.time()*1000)
    sign = str(phoneNum)+optCode+str(timestamp)
    md5_sign = hashlib.md5(sign.encode()).hexdigest()
    return {"phoneNum": phoneNum,"optCode":optCode,"timestamp":timestamp,"sign":md5_sign}

def get_token():
    '''
    成功登陆之后，获取token值,供依赖token做请求的接口去应用
    构造请求
    :return:
    '''
    url = 'http://localhost:8080/pinter/bank/api/login2'
    data = {
        'userName': 'admin',
        'password': 1234
    }

    resp = requests.post(url, data=data)
    try:
        token = resp.json().get('data')
    except:
        token = ''
    return token


def hook_up():
    print('前置执行setup_hook')


def hook_down():
    print('后置执行teardown_hook')


def hook_log(value):
    print(value)


# 整数转成字符串
def int_to_str(arg):
    return str(arg)

# 字符串转成int
def str_to_int(arg):
    return int(arg)



if __name__ == '__main__':
    # print(get_params())
    # print(sign())
    print(get_token())
    hook_log('测试用例')