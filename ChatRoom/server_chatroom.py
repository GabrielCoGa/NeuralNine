# Simple Chatroom Server in Python
#Video específico de este archivo:
#https://youtu.be/3UOyky9sEQY?si=MhxZaznDBdrA58sq

import threading
import socket


ip_server = '127.0.0.1'
port_server = 55555

host_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_server.bind((ip_server, port_server))
host_server.listen()

print(f"Server started on {ip_server}:{port_server}")

clients = []
nicknames = []

def sendBroadcast(message):
    for client in clients:
        client.send(message)

def handleClient(client):
    while True:
        try:
            message = client.recv(1024)
            sendBroadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
            sendBroadcast(f"{nickname} left the chat!".encode('utf-8'))
            break

def receiveConnections():
    while True:
        client, address = host_server.accept()
        print(f"Connected with {str(address)}")
        
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print(f'Nickname of the client is {nickname}')
        sendBroadcast(f'{nickname} joined the chat!'.encode('ascii'))
        client.send('Connected to the server!'.encode('ascii'))

        thread = threading.Thread(target=handleClient, args=(client,))
        thread.start()

print("Server is running and listening for connections...")
receiveConnections()










           

