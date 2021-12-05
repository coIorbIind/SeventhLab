from smtplib import SMTP
from server_data import username, password, admin_address

msg = 'Hello!'
with SMTP("smtp.gmail.com:587") as smtp:
    smtp.starttls()
    smtp.login(username, password)
    smtp.sendmail(
        username,
        admin_address,
        msg
    )
