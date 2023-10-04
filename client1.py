import socket as sck

SEPARATOR = ";"
SERVER_ALPHABOT = ("192.168.1.139", 5000)

def main():
    soc = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    soc.connect(SERVER_ALPHABOT)
    
    while True:
        command = input("Inserire il comando:")
        duration = input("Inserire la durata in sec:")
        message = f"{command}{SEPARATOR}{duration}".encode()
        soc.sendall(message)
        
        if command.lower() == "e":
            break
        
    soc.close()
    
    
if __name__ == "__main__":
    main()

