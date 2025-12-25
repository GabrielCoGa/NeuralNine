import socket
import threading

nickname = input("Choose your nickname: ")
if nickname == 'admin':
    password = input("Enter admin password: ")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_server = '127.0.0.1'
port_server = 55555

client_socket.connect((ip_server, port_server))

stop_thread = False

def receiveMessages():
    while True:
        global stop_thread
        if stop_thread:
            break
        try:
            message = client_socket.recv(1024).decode('ascii')
            if message == 'NICK':
                client_socket.send(nickname.encode('ascii'))
                next_message = client_socket.recv(1024).decode('ascii')
                if next_message == 'PASS':
                    client_socket.send(password.encode('ascii'))
                    if client_socket.recv(1024).decode('ascii') == 'REFUSE':
                        print("Connection was refuesed! Wrong password!")
                        stop_thread = True

            else:
                print(message)
        except:
            print("An error occurred!")
            client_socket.close()
            break

def sendMessages():
    while True:
        if stop_thread:
            break
        message = f'{nickname}: {input("")}'
        if message[len(nickname) + 2:].startswith('/'):
            if nickname == 'admin':
                if message[len(nickname) + 2:].startswith('/kick'):
                    kick_nickname = message[len(nickname) + 2 + 6:]
                    client_socket.send(f'KICK {kick_nickname}'.encode('ascii'))
                elif message[len(nickname) + 2:].startswith('/ban'):
                    ban_nickname = message[len(nickname) + 2 + 5:]
                    client_socket.send(f'BAN {ban_nickname}'.encode('ascii'))
            else:
                print("Commands can only be used by the admin!")
        else:
            client_socket.send(message.encode('ascii'))


recieve_thread = threading.Thread(target=receiveMessages)
recieve_thread.start()

send_thread = threading.Thread(target=sendMessages)
send_thread.start()


