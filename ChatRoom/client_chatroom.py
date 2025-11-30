import socket
import threading

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_server = '127.0.0.1'
port_server = 55555

client_socket.connect((ip_server, port_server))

nickname = input("Choose your nickname: ")

def receiveMessages():
    while True:
        try:
            message = client_socket.recv(1024).decode('ascii')
            if message == 'NICK':
                client_socket.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("An error occurred!")
            client_socket.close()
            break

def sendMessages():
    while True:
        message = f'{nickname}: {input("")}'
        client_socket.send(message.encode('ascii'))


recieve_thread = threading.Thread(target=receiveMessages)
recieve_thread.start()

send_thread = threading.Thread(target=sendMessages)
send_thread.start()


