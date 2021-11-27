import socket
import pickle
import os
import json


def comm(host, port, dic):
    if not host or not port:
        try:
            conf = json.load(open(os.path.expanduser('~/.reclip.json'), 'r'))
            if not host:
                host = conf['host']
            if not port:
                port = int(conf['port'])
        except Exception as e:
            print(e)
            print('Can\'t read config!')
            exit(1)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        data = pickle.dumps(dic)
        s.send(data)
        res = b''
        while True:
            recv = s.recv(1024)
            if not recv:
                break
            res += recv
        print(res.decode('utf-8'))


def set(host=None, port=None, value=''):
    dic = {
        'mode': 's',
        'value': value,
    }
    comm(host, port, dic)


def get(host=None, port=None):
    dic = {
        'mode': 'g',
    }
    comm(host, port, dic)


def delete(host=None, port=None):
    dic = {
        'mode': 's',
        'value': '',
    }
    comm(host, port, dic)
