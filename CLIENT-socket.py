import socket

HOST = '127.0.0.1'
PORT = 61324

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print('connected to server.')



    while True:
        message = input("Enter your message: ")
        s.sendall(message.encode())
        data = s.recv(1024)
        print(f'Recived message from server is : {data.decode("utf-8")}')
