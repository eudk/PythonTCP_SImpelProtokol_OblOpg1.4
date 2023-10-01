from socket import *

serverIp = '127.0.0.1'  # localhost
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverIp, serverPort))

print("Connected to the server: " + serverIp)

while True:
    command = input("Command (Generate 'Random' Number, 'Add' func or 'Subtract' func): ")
    number1 = input("Number 1: ")
    number2 = input("Number 2: ")

    request = f"{command};{number1};{number2}"
    clientSocket.send(request.encode())

    response = clientSocket.recv(1024).decode()
    print("Server", serverIp,": " ,response)

    another = input("Do you want to keep going? (yes/no): ")
    if another.lower() != 'yes':
        break

clientSocket.close()
