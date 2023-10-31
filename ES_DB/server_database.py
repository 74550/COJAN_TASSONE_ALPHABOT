# CORREZIONE PROF
import socket
import sqlite3
import socket as sck
import AlphaBot
import time
from threading import Thread

SEPARATOR = ';'

# creazione socket tcp server
s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
# creazione istanza AlphaBot
r = AlphaBot.AlphaBot()

def shortcut_list(command):
    con=sqlite3.connect("dataBase_shortcuts.db")
    cur=con.cursor()
    res=cur.execute(f"SELECT Mov_Sequence FROM Movements WHERE Shortcut='{command.upper()}'")
    lista=res.fetchall()
    stringa= f"{lista[0][0]}"
    comandi=stringa.split(",")
    con.close()
    return comandi


class ThreadLed(Thread):
    def __init__(self, connesione):
        super().__init__()
        self.connessione = connesione

    def run(self):
        while True:
            self.connessione.sendall(f'{r.getSensoLeft()}{SEPARATOR}{r.getSensoRight()}'.encode())
            print(f'{r.getSensoLeft()}{SEPARATOR}{r.getSensoRight()}'.encode())
            time.sleep(1)

class ThreadMess(Thread):
    def __init__(self, conn):
        super().__init__()
        self.conn = conn

    def run(self):
        while True:
            message_robot=f"{r.getDataSensors()}".encode()
            conn.sendall(message_robot)
            time.sleep(2)

def main():
    # bind
    address = ('0.0.0.0', 5000)
    s.bind(address)
    s.listen()

    connesione, clientAddress = s.accept()
    
    

    thread = ThreadLed(connesione)
    thread.start()
    tmess =ThreadMess(connesione)
    tmess.start()

    while True:
        mex = connesione.recv(4096).decode() # mex decodificato in ascii
        

        # mex command example: f;10
        splitMex = mex.split(SEPARATOR)

        if len(splitMex) != 2:
            print('error')
            continue # continua il ciclo senza eseguire l'istruzione rimanente

        command = splitMex[0]
        duration = int(splitMex[1])



        if ((command.lower()=='w') or (command.lower()=='q') or (command.lower()=='a') or (command.lower()=='s')):
            comandi=shortcut_list(command)
            for element in comandi:
                istruzione=element.split(SEPARATOR)
                if istruzione[0].lower() == 'b':
                    r.backward()
                    time.sleep(int(istruzione[1]))
                    r.stop()
                elif istruzione[0].lower() == 'f':
                    r.forward()
                    time.sleep(int(istruzione[1]))
                    r.stop()
                elif istruzione[0].lower() == 'r':
                    r.right()
                    time.sleep(int(istruzione[1]))
                    r.stop()
                elif istruzione[0].lower() == 'l':
                    r.left()
                    time.sleep(int(istruzione[1]))
                    r.stop()
                elif istruzione[0].lower() == 'e':
                    break
                else:
                    print('error')
        else:
        # duration in second
            if command.lower() == 'b':
                r.backward()
                time.sleep(duration)
                r.stop()
            elif command.lower() == 'f':
                r.forward()
                time.sleep(duration)
                r.stop()
            elif command.lower() == 'r':
                r.right()
                time.sleep(duration)
                r.stop()
            elif command.lower() == 'l':
                r.left()
                time.sleep(duration)
                r.stop()
            elif command.lower() == 'e':
                break
            else:
                print('error')
            
    message_robot=f"{r.getDataSensors()}".encode()
    connessione.sendall(message_robot)

    connesione.close()
    s.close()


if __name__ == '__main__':
    main()



