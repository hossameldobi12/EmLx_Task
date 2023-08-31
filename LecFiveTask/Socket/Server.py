'''
info : this file for socket server 
Name : Hossam Adel Mostafa

'''


import socket
import threading

Ip = socket.gethostbyname(socket.gethostname())
Port = 5050
Adder = (Ip,Port)
size = 1024
FORMAT = "utf-8"


def handle_client(conn,addr) :
    print(f"[NEW CONNETION] {addr} connected to server :")
    connection = True
    while connection:
        client_msg = conn.recv(size).decode(FORMAT)
        if client_msg == "D":
            connection = False
        else:
            print(f"{addr} send a message :{client_msg}")
            server_msg = input("enter server message : ")
            conn.send(server_msg.encode(FORMAT))
            
    conn.close()

            



def main() :
    print("[STARTING] Server Is Starting....")
    Server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    Server.bind(Adder)
    Server.listen()
    print(f"[LISTENING] Server Is Listening {Adder}")
    while True:
        conn , addr = Server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
        


if __name__== "__main__" :
    main()