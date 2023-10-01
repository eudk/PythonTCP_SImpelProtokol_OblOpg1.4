from socket import *
import threading
import random

def handleClient(clientSocket): #envejs kommunikation mellem client og server (client sender request, server sender response)
    while True:
        try:
            data = clientSocket.recv(1024).decode()
            if not data: 
                break

            command, number1, number2 = data.split(';')
            number1, number2 = int(number1), int(number2)

            if command == "Random":
                result = random.randint(number1, number2) #random tal mellem number1 og number2
            elif command == "Add":
                result = number1 + number2
            elif command == "Subtract":
                result = number1 - number2
            else:
                result = "Unknown command"

            response = str(result)
            clientSocket.send(response.encode())
        except ValueError:
            response = "Invalid request format. Use 'Command;Number1;Number2'"
            clientSocket.send(response.encode())

    clientSocket.close()

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The Server is ready...!')

while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target=handleClient, args=(connectionSocket,)).start()
