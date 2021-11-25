import socket
import pickle


def comm(host, port, dic):
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


def set(host, port, content):
    dic = {
            'mode': 's',
            'content': content,
        }
    comm(host, port, dic)


def get(host, port):
    dic = {
            'mode': 'g',
        }
    comm(host, port, dic)


def delete(host, port):
    dic = {
            'mode': 's',
            'content': '',
        }
    comm(host, port, dic)
