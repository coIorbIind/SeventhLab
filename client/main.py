import pickle
import socket
from classes import ProcessData

HOST = '127.0.0.1'
PORT = 50007

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        email_address = input("Введите email: ")
        msg = input("Напишите сообщение: ")
        variable = ProcessData(email_address, msg)
        data_variable = pickle.dumps(variable)
        s.send(data_variable)
        data = s.recv(1024)
        print('Received', data.decode())
        if data.decode() == "OK!":
            break
