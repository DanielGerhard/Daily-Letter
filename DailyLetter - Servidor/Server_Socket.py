import socket
import DB_Connect
import time

DB_Connect.connect_DB()

print('Inicializando')
time.sleep(0.5)
print('-')
time.sleep(0.5)
print('-')
time.sleep(0.5)
print('-')
time.sleep(0.5)
print('''
______         _  _         _            _    _               
|  _  \       (_)| |       | |          | |  | |              
| | | |  __ _  _ | | _   _ | |      ___ | |_ | |_   ___  _ __ 
| | | | / _` || || || | | || |     / _ \| __|| __| / _ \| '__|
| |/ / | (_| || || || |_| || |____|  __/| |_ | |_ |  __/| |   
|___/   \__,_||_||_| \__, |\_____/ \___| \__| \__| \___||_|   
                      __/ |                                   
                     |___/                                    
está online''')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 12345))
s.listen(5)


def boot_serv():
    while True:
        con, adr = s.accept()
        while True:
            msg = con.recv(1024)
            msg = msg.decode()
            if not msg:
                break
            if msg:
                DB_Connect.registrar_mensagens(msg)
                print('Nova mensagem registrada: ' + msg)


boot_serv()
