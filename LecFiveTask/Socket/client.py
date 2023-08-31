'''
info : this file for socket client
Name : Hossam Adel Mostafa

'''
import socket

Ip = socket.gethostbyname(socket.gethostname())
Port = 5050
Adder = (Ip,Port)
size = 1024
FORMAT = "utf-8"


def main():
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(Adder)
    print(f"[CONNECTED] client connected to server at {Adder}")
    connected = True
    while True:
        client_msg = input(">> ")
        client.send(client_msg.encode(FORMAT))
        if client_msg == "D" :
            connected == False
        else :
           server_msg = client.recv(size).decode(FORMAT)  
           print(f"server message is : {server_msg}")         
        


if __name__ == "__main__":
    main()