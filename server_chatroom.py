# Simple Chatroom Server in Python
#Lista de reproducción de YouTube con tutorial paso a paso:
#https://youtube.com/playlist?list=PL7yh-TELLS1FwBSNR_tH7qVbNpYHL4IQs&si=cbfE8-E8hmcl3V1C
#Video específico de este archivo:
#https://youtu.be/3UOyky9sEQY?si=MhxZaznDBdrA58sq

import threading
import socket


ip_server = '127.0.0.1'
port_server = 5555

host_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_server.bind((ip_server, port_server))
host_server.listen()
print(f"Server started on {ip_server}:{port_server}")

clients = []
nicknames = []

def sendBroadcast(message);
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


           

