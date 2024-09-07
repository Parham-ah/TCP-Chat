import socket

IP = '127.0.0.1'
PORT = 1995

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((IP, PORT))
    s.sendall(b'Hello Server')
    data = s.recv(1024)


print('Recived message from Server: ', data.decode('utf-8'))