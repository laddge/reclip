import socket
import pickle


def serve(host='127.0.0.1', port=8000, saveto=None):
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
                    content = dic['content']
                    if saveto:
                        try:
                            with open(saveto, 'w') as f:
                                f.write(content)
                        except Exception as e:
                            print(e)
                elif dic['mode'] == 'g':
                    if saveto:
                        try:
                            with open(saveto, 'r') as f:
                                content = f.read()
                        except Exception as e:
                            print(e)
                elif dic['mode'] == 'd':
                    content = ''
                    if saveto:
                        try:
                            with open(saveto, 'w') as f:
                                f.write(content)
                        except Exception as e:
                            print(e)
                conn.send(content.encode('utf-8'))
                print('sent : \'{}\' -> {}'.format(content, addr))


if __name__ == '__main__':
    serve()
