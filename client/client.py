import sys
from socket import *
HOST = '127.0.0.1'
conn = True

while(conn):
    PORT = input("OPEN#: ")

    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((HOST, int(PORT)))

    while (True):
        s = input("Command: ")

        if s.startswith("GET"):
            
            sock.send(s.encode("utf-8"))

            name = sock.recv(1024).decode("utf-8")
            data = sock.recv(1024).decode("utf-8")
            print("The file name is:")
            print(name)
            print("The file content is:")
            print(data)
            print("GET COMMAND SUCCESSFUL\n")
            f = open(name, "w")
            f.writelines(data)
            f.close()

        elif s.startswith("PUT"):

            fileName = s[4:]
            try:
                # open the file
                with open(fileName, "r") as fileObj:
                    
                    sock.send("PUT".encode("utf-8"))
                    
                    fileData = fileObj.read(65536)
                    sock.send(fileName.encode())
                    print(fileData)
                    sock.send(fileData[0:].encode())

            except FileNotFoundError:
                print("File doesn't exist!\n")

        elif s.startswith("CLOSE"):
                break
                
        elif s.startswith("QUIT"):
                print("Goodbye!")
                conn = False;
                break
        else:
            print("Invalid command")

   
    sock.close()