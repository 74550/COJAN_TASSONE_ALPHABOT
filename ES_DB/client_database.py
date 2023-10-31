# CORREZIONE PROF
from email.mime import message
import socket as sck
import time
from threading import Thread

s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)

SEPARATOR = ';'
SERVER_ALPHABOT = ('192.168.1.139',5000)

class ThreadLed(Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        print(s.recv(4096).decode())

class ThreadMess(Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            message_robot=s.recv(4096).decode().split(";")
            if(len(message_robot)==2):
                if(message_robot[0]=="0" and message_robot[0]=="0"):
                    print("davanti")
                #print(message_robot)

            

def main():
    s.connect(SERVER_ALPHABOT)
    t = ThreadLed()
    t.start()
    t2= ThreadMess()
    t2.start()

    while True:
        command = input('inserire un comando: ')
        if ((command.lower()=='w') or (command.lower()=='q') or (command.lower()=='a') or (command.lower()=='s')):
            mex = f'{command}{SEPARATOR}{0}'.encode()
        else:
            duration = input('inserire durata in secondi')
            mex = f'{command}{SEPARATOR}{duration}'.encode()

        #invio mex
        s.sendall(mex)

        if command.lower() == 'e':
            break

        
    s.close()




if __name__ == '__main__':
    main()