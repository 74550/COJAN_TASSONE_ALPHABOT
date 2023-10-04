import socket as sck
import Alphabot
import time

SEPARATOR = ";"

def main():
    robot = Alphabot.AlphaBot()
    soc = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    address = ("0.0.0.0", 5000)
    soc.bind(address)
    soc.listen()
    conn, client_address = soc.accept()
    
    while True:
        '''
        F;int
        '''
        message = conn.recv(4096).decode()
        spliitted_message = message.split(SEPARATOR)
        
        if len(spliitted_message) != 2:
            print("ERROR")
            continue #passa all'iterazione successiva
        
        command = spliitted_message[0]
        duration = int(spliitted_message[1])
        
        #durata in secondi
        if (command.lower() == "f"):
            robot.backward()
            time.sleep(duration)
            robot.stop()
        elif(command.lower() == "b"):
            robot.backward()
            time.sleep(duration)
            robot.stop()
        elif(command.lower() == "l"):
            robot.backward()
            time.sleep(duration)
            robot.stop()
        elif(command.lower() == "r"):
            robot.backward()
            time.sleep(duration)
            robot.stop()
        elif(command.lower() == "e"):
            break
        else:
            print("ERROR")
            
        message_robot = f"{robot.getDataSensors()}".encode()
        conn.sendall(message_robot)
            
    conn.close()
    soc.close()
            
        
        

if __name__ == "__main__":
    main()


