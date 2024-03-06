from socket import *

def get_server_response(client_socket):
    return client_socket.recv(1024).decode()

serverName = "localhost"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))


command = input("Enter the command (Random, Add, Subtract): ")
clientSocket.send(command.encode())


serverResponse = get_server_response(clientSocket)
print('From server:', serverResponse)


if serverResponse == "Input numbers":
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    numbers = f"{num1} {num2}"
    clientSocket.send(numbers.encode())

    result = get_server_response(clientSocket)
    print('Result from server:', result)

clientSocket.close()