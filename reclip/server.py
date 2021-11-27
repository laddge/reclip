import socket
import pickle
import os


def serve(host='127.0.0.1', port=8000):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(5)
        print('Serving reclip on {} port {} ...'.format(host, port))
        while True:
            conn, addr = s.accept()
            with conn:
                data = b''
                while True:
                    recv = conn.recv(1024)
                    data += recv
                    if recv[-1] == 46:
                        break
                dic = pickle.loads(data)
                if dic['mode'] == 's':
                    os.environ['RECLIP_CONTENT'] = dic['content']
                    res = os.environ['RECLIP_CONTENT']
                elif dic['mode'] == 'g':
                    try:
                        content = os.environ['RECLIP_CONTENT']
                    except Exception:
                        content = ''
                    res = content
                elif dic['mode'] == 'd':
                    os.environ['RECLIP_CONTENT'] = ''
                    res = ''
                conn.send(res.encode('utf-8'))
                print('sent : \'{}\' -> {}'.format(res, addr))


if __name__ == '__main__':
    serve()
