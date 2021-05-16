#! /usr/bin/python3

#importing the socket module

import socket

#Creating a function for the server operations

def server():
    
    

        

        data = connection.recv(1024).decode() #Variable to get the option from the user

        option = int(data)

    
        #Option to chat
        if(option == 1):

            #A simple welcome message
            a = 'Welcome to the chatbox :)' + "\n" +"How may I help you .? \n"
            connection.send(a.encode())

            while option==1:

                  
                  indata = connection.recv(1024).decode()
                  if not indata:
                      break
                  print("from connected user: " + str(indata))
                  indata = input(' -> ')
                  connection.send(indata.encode())
                  

        #Option to send file to the server
        elif(option == 2):
                  print("Welcome to File transfer"+"\n")
                  filename = connection.recv(1024).decode("utf8")
                  file = open("sent_"+filename, "ab")
                  while True:
                     data = connection.recv(1024)
                     file.write(data)
                     if not data:
                        print("Done, file saved as {}".format("sent_"+filename) )
                        connection.close()
                        file.close()
                        print("Bye :)"+"\n")
                        break
        
        #Default option
        else:
                  print("Please choose a correct option :(")
                  connection.close() #Closing the connection


if __name__ == "__main__":

    #variable to get the host name and port
    host = socket.gethostname() #Get the host 
    port = 55010 # 

    #Bind host and port
    ServerSocket = socket.socket()
    ServerSocket.bind((host,port))
    print("Server is listening for a connection...")


    ServerSocket.listen(4) #Number 4 means the server can listen to only 4 clients at a given time
    connection, address = ServerSocket.accept() #Accept the connection
    print("A connection has been made.The Connection is from the client: " + str(address) + "\n")
    server() #Calling the server function

