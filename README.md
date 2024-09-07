# TCP-Chat
Chat between Server and Client with TCP Protocol 

## TCP Client-Server Communication Project

## Overview
This project demonstrates a simple TCP communication between a server and multiple clients using Python. The server listens for incoming connections and can handle multiple clients simultaneously using threads, while each client can send messages to the server and receive responses.

## Files
- **server.py**: Implements the server-side application that accepts connections from clients, receives messages, and sends responses.
- **client.py**: Implements the client-side application that connects to the server, sends messages, and receives responses.

## Requirements
- Python 3.x
- Visual Studio Code (VS Code)

## How to Run

### Step 1: Set Up the Server in VS Code
1. Open **Visual Studio Code (VS Code)**.
2. Go to `File` > `Open Folder...` and select the folder containing `server.py`.
3. Open the file `server.py` in VS Code.
4. In the terminal section at the bottom of VS Code, make sure the Python environment is selected, then run the server file.
The server will start listening on 127.0.0.1:61324.

### Step 2: Set Up the Client in Another Instance of VS Code
Open a new instance of Visual Studio Code (VS Code).
Go to File > Open Folder... and select the folder containing client.py.
Open the file client.py in the second instance of VS Code.
run client.py file.
The client will connect to the server at 127.0.0.1:61324.

#### Enter a message in the terminal where the client is running, and press Enter. The message will be sent to the server, and the server's response will be displayed in the terminal.

