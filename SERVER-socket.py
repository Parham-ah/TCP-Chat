import socket

IP='127.0.0.1'
PORT=1995

#server code

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((IP, PORT))
    s.listen()
    print(f'server is ready to listen {IP}:{PORT}...')
    conn, addr = s.accept()

    with conn:
        print(f'connected by {addr}')
        data = conn.recv(1024)
        print('recived message from client: ', data.decode('utf-8'))
        conn.sendall(b'Hello, Client')
    












