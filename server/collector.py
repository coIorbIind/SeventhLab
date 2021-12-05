import asyncio
from imaplib import IMAP4_SSL
import email
from email import policy
import json


# async def check(period, id, user, password):
#     try:
#         with open("success_request.json") as file:  # чтение файла
#             success_request_dict = json.load(file)
#         with open("error_request.json") as file:  # чтение файла
#             error_request_dict = json.load(file)
#     except json.decoder.JSONDecodeError:
#         success_request_dict = dict()
#         error_request_dict = dict()
#
#     with IMAP4_SSL("imap.gmail.com", 993) as M:
#         M.login(user, password)
#         M.select()
#         typ, data = M.search(None, 'ALL')
#         for num in data[0].split():
#             typ, data = M.fetch(num, '(RFC822)')
#             for response_part in data:
#                 if isinstance(response_part, tuple):
#                     msg = email.message_from_bytes(response_part[1], policy=policy.default)
#                     new_dict = dict()
#                     new_dict["subj"] = msg['subject']
#                     new_dict["from"] = msg['from']
#                     text = ''
#                     for part in msg.walk():
#                         if part.get_content_type() == 'text/plain':
#                             text += part.get_payload(decode=True).decode('utf-8')
#                     new_dict["body"] = text
#                     if str(id) not in success_request_dict.keys() and str(id) in msg['subject']:
#                         success_request_dict[str(id)] = new_dict
#                     elif msg['subject'] not in error_request_dict.keys():
#                         error_request_dict[msg['subject']] = new_dict
#     with open("success_request.json", "w") as file:
#         json.dump(success_request_dict, file, indent=4, ensure_ascii=False)
#     with open("error_request.json", "w") as file:
#         json.dump(error_request_dict, file, indent=4, ensure_ascii=False)
#
#     await asyncio.sleep(float(period))

def check(id, user, password):
    try:
        with open("success_request.json") as file:  # чтение файла
            success_request_dict = json.load(file)
        with open("error_request.json") as file:  # чтение файла
            error_request_dict = json.load(file)
    except json.decoder.JSONDecodeError:
        success_request_dict = dict()
        error_request_dict = dict()

    with IMAP4_SSL("imap.gmail.com", 993) as M:
        M.login(user, password)
        M.select()
        typ, data = M.search(None, 'ALL')
        for num in data[0].split():
            typ, data = M.fetch(num, '(RFC822)')
            for response_part in data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1], policy=policy.default)
                    new_dict = dict()
                    new_dict["subj"] = msg['subject']
                    new_dict["from"] = msg['from']
                    text = ''
                    for part in msg.walk():
                        if part.get_content_type() == 'text/plain':
                            text += part.get_payload(decode=True).decode('utf-8')
                    new_dict["body"] = text
                    if str(id) not in success_request_dict.keys() and str(id) in msg['subject']:
                        success_request_dict[str(id)] = new_dict
                    elif msg['subject'] not in error_request_dict.keys():
                        error_request_dict[msg['subject']] = new_dict
    with open("success_request.json", "w") as file:
        json.dump(success_request_dict, file, indent=4, ensure_ascii=False)
    with open("error_request.json", "w") as file:
        json.dump(error_request_dict, file, indent=4, ensure_ascii=False)

