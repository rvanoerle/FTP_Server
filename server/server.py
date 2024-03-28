from socket import *
HOST = '127.0.0.1'
PORT = 12000
# set up the tcp socket
sock = socket(AF_INET, SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen()
# listen for a connection
conn, addr = sock.accept()
print("Connected to " , addr)
while (True):
    data = conn.recv(1024).decode("utf-8")

    if data.startswith("GET"):

        fileName = data[4:]
    
        try:
            # open the file
            with open(fileName, "r") as fileObj:
                 
                 fileData = fileObj.read(65536)
                 conn.send(fileName.encode())
                 print(fileData)
                 conn.send(fileData[0:].encode())

        except FileNotFoundError:
            print("File doesn't exist\n")

    elif data.startswith("PUT"):

        name = conn.recv(1024).decode("utf-8")
        data = conn.recv(1024).decode("utf-8")
        print("The file name is:")
        print(name)
        print("The file content is:")
        print(data)
        print("PUT COMMAND SUCCESSFUL\n")
        f = open(name, "w")
        f.writelines(data)
        f.close()

    else:
        print("Client disconnected")
        break

conn.close()
sock.close()