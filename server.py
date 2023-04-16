import socket
import threading

class User:
    def __init__(self, conn,addr):
        self.conn, self.addr = conn,addr
        
    def session(self):
        while True:
            try:
                self.GetStream()
                if not self.data:
                    break
                self.PrintData()
            except socket.error as e:
                print(f"Error receiving/sending data from {self.addr}: {e}")
                self.conn.close()
                break
    def GetStream(self):
        self.data = self.conn.recv(1024).decode('utf-8')
        
    def PrintData(self):
        file_name = self.addr
        file_name = "".join(map(str, file_name))
        file_name = file_name.replace('\\',"")
        file_name = file_name.replace('\'',"")
        file_name = file_name.replace('(',"")
        file_name = file_name.replace(')',"")
        with open(f"./log/{self.addr}",'a+') as f:
            f.write(self.data+'\n')
        # print(f"{self.addr} send: {self.data}")      
        

class App:
    def __init__(self, host,port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((host,port))
        self.socket.listen()
        print(f"server is on {host}:{port}")
        
    def listen(self):
        while True:
            conn, addr = self.socket.accept()
            new_user = User(conn, addr)
            thread = threading.Thread(target=new_user.session)
            thread.start()
            print(f"{addr} connected")
            

if __name__ == "__main__":
    server = App('0.0.0.0',7777)
    server.listen()