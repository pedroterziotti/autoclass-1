import socket
from threading import Thread, Timer
from Manager.aula_manager import *
import time

HOST = 'localhost'                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port


def main_loop():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        data =''
        while data != 'end':
            conn, addr = s.accept()
            with conn:
                while True:
                    data = conn.recv(1024).decode('utf8')
                    print(data)
                    t=Thread(target=signal_handler,args=(data,),daemon=True)
                    t.run()
                    break


        if t.is_alive():
            t.join()

if __name__ == "__main__":
    start_timers()
    main_loop()
                                    


            