import socket
import pickle


def delete(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        dic = {
                'mode': 's',
                'content': '',
            }
        data = pickle.dumps(dic)
        s.send(data)
        res = b''
        while True:
            recv = s.recv(1024)
            if not recv:
                break
            res += recv
        print(res.decode('utf-8'))


if __name__ == '__main__':
    delete('127.0.0.1', 8000)
