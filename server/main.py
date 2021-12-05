import socket
import pickle
import sys
import asyncio
from smtplib import SMTP
import os
from dotenv import load_dotenv
from collector import check
from time import sleep

sys.path.insert(0, 'D:/admin/lab_7/client')
from classes import ProcessData

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
# from server_data import username, password, admin_address

HOST = '127.0.0.1'
PORT = 50007
ID = 100000

username = os.environ['EMAIL_LOGIN']
password = os.environ['EMAIL_PASSWORD']
imap_host = os.environ['IMAP_HOST']
imap_port = os.environ['IMAP_PORT']
smtp_host = os.environ['SMTP_HOST']
smtp_port = os.environ['SMTP_PORT']
check_period = os.environ['PERIOD_CHECK']
admin_address = os.environ['ADMIN_ADDRESS']
admin_password = os.environ['ADMIN_PASSWORD']


# print(username, password, imap_port, imap_host, smtp_port, smtp_host, check_period, admin_address, sep="\n")


def main_func():
    global ID

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                data_variable = pickle.loads(data)
                if "@" and (".com" or ".ru") in data_variable.email:
                    ID += 1
                    answer = "OK!"
                    conn.send(answer.encode())
                    break
                else:
                    answer = "Некорректный адрес. Попробуйте снова"
                    conn.send(answer.encode())

        print(data_variable)
        msg = f"Subject: {ID}\n" \
              f"{data_variable.msg}"
        msg_2 = f"Subject: {ID}\n" \
                f"Ваша заявка принята!"
        with SMTP("smtp.gmail.com:587") as smtp:
            smtp.starttls()
            smtp.login(username, password)
            smtp.sendmail(
                username,
                admin_address,
                msg.encode("utf-8")
            )
            smtp.sendmail(
                username,
                data_variable.email,
                msg_2.encode("utf-8")
            )


if __name__ == "__main__":
    main_func()
    while True:
        check(ID, admin_address, admin_password)
        sleep(float(check_period))

    # loop = asyncio.get_event_loop()
    # loop.create_task(check(check_period, ID, admin_address, admin_password))
    # sleep(15)
    # main_func()
    # while True:
    #     print('')
