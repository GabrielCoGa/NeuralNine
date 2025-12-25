# Advanced Chatroom Server in Python
#Video específico de este archivo:
#https://www.youtube.com/watch?v=F_JDA96AdEI&t=378s

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
            msg = message = client.recv(1024)
            if msg.decode('ascii').startswith('KICK'):
                name_to_kick = msg.decode('ascii')[5:]
                kick_user(name_to_kick)
            elif msg.decode('ascii').startswith('BAN'):
                name_to_ban = msg.decode('ascii')[4:]
                kick_user(name_to_ban)
                with open('bans.txt', 'a') as f:
                    f.write(f'{name_to_ban}\n')
                print(f'{name_to_ban} was banned!')
            else:
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

        if nickname == 'admin':
            client.send('PASS'.encode('ascii'))
            password = client.recv(1024).decode('ascii')
            if password != 'adminpass':
                client.send('REFUSE'.encode('ascii'))
                client.close()
                continue

        nicknames.append(nickname)
        clients.append(client)

        print(f'Nickname of the client is {nickname}')
        sendBroadcast(f'{nickname} joined the chat!'.encode('ascii'))
        client.send('Connected to the server!'.encode('ascii'))

        thread = threading.Thread(target=handleClient, args=(client,))
        thread.start()

print("Server is running and listening for connections...")
receiveConnections()










           

