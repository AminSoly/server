import socket
import threading

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip = "192.168.1.110"
port = 5555
s.bind((ip, port))


def handle(conn, addr):
    print(f"[NEW CONNECTION] {addr} is connected to the server ")

    while True:
        msg = conn.recv(1024).decode()
        if msg:
            print(f"[MESSAGE] : {msg}")
            conn.send("message recieved !".encode())
        else:
            break
            conn.close()    
            
        
            

def start():
    print(f"[LISTENING] listening on {ip}:{port} ...")
    s.listen(5)
    while True:
        conn, addr = s.accept()
        t = threading.Thread(target = handle, daemon = True, args = (conn, addr))
        t.start()


start()        