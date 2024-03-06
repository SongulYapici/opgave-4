from socket import *
import random
import threading

def process_command(command, connectionSocket):
    if command == 'Random':
        connectionSocket.send('Input numbers'.encode())
        numbers = connectionSocket.recv(1024).decode()
        num1, num2 = map(int, numbers.split())
        result = random.randint(min(num1, num2), max(num1, num2))
    elif command == 'Add':
        connectionSocket.send('Input numbers'.encode())
        numbers = connectionSocket.recv(1024).decode()
        num1, num2 = map(int, numbers.split())
        result = num1 + num2
    elif command == 'Subtract':
        connectionSocket.send('Input numbers'.encode())
        numbers = connectionSocket.recv(1024).decode()
        num1, num2 = map(int, numbers.split())
        result = num1 - num2
    else:
        result = 'Invalid command'
    
    return result

def client_thread(connectionSocket, addr):
    try:
        print(f'Connection established with {addr}')
        while True:
            command = connectionSocket.recv(1024).decode()
            if not command:
                break 
            
            result = process_command(command, connectionSocket)
            connectionSocket.send(str(result).encode())
    finally:
        connectionSocket.close()
        print(f'Connection closed with {addr}')

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('Server is ready to listen')

while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target=client_thread, args=(connectionSocket, addr)).start()