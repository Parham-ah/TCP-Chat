from encodings import utf_8
import socket
import threading

HOST = '127.0.0.1'
PORT = 61324

def handle_client(conn, addr):
    print(f"new client connected : {addr}")
    with conn:
        while True:
            data = conn.recv(1024)
            print(f'Recived message from {addr}: {data.decode("utf-8")}')
            message = input('Enter your message : ')
            conn.sendall(message.encode())

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f'server is listening on {HOST}:{PORT}')  
        while True:
            conn, addr = s.accept()
            threading.Thread(target = handle_client, args= (conn, addr)).start() 

start_server()                 











