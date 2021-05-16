#!/usr/bash/python3

#Importing the socket module
import socket

#Creating the client function
def client():
    host = socket.gethostname()
    port = 55010 #Choose socket between 1024 and 65535

    ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ClientSocket.connect((host,port))

    print("Please choose any one number "+"\n 1: Chat" + "\n 2:Send File")

    message = input(":-")

    choice = int(message)
    
    #Option to chat 
    if (choice == 1):
        while message.lower().strip() != 'bye':
         ClientSocket.send(message.encode())
         data = ClientSocket.recv(1024).decode()

         print("Server: " + data)
         message = input(":-")
    #Option to send file 
    elif (choice == 2):

         ClientSocket.send(message.encode())
         filename = input("Enter the name of the file to be sent: ")
         ClientSocket.send(bytes(filename,"utf8"))
         file = open(filename, 'rb')
         while True:
            data = file.read(1024)
            ClientSocket.send(data)
            if not data:
              ClientSocket.close()
              file.close()
              print("Done sending!")
              break
    #Default Option
    else:
        print("Incorrect option! Bye !")
        ClientSocket.close()


if __name__ == "__main__":
    client()
