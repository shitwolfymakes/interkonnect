"""
This demo is a proof of concept of how interkonnect works. Once this works, everything
can be pulled out and moved into interkonnect.py, and the only stuff that will remain
here is what the user does with the data that is returned
"""

import os.path
import json
from queue import Queue

import imapclient
import pyzmail
from bs4 import BeautifulSoup


def main():
    # read in creds
    data = {}
    if os.path.exists("../ik_properties.json"):
        with open("../ik_properties.json") as ik_props:
            data = json.load(ik_props)
    #end if

    commands_queue = Queue()
    imap_obj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
    imap_obj.login(data.get("email"), data.get("pass"))
    imap_obj.select_folder('INBOX')
    email_ids = imap_obj.search()#'UNSEEN')
    if email_ids:
        for email_id in email_ids:
            # get data from the email
            tokens = []
            print("email id: %s" % email_id)
            raw_msg = imap_obj.fetch([email_id], ['BODY[]', 'FLAGS'])
            message = pyzmail.PyzMessage.factory(raw_msg[email_id][b'BODY[]'])
            print(message.get_address('from'))
            if message.text_part is not None:
                payload = message.text_part.get_payload().decode('utf-8')
                tokens = payload.split()[0:6]
                #print("plain text:", tokens)
            elif message.html_part is not None:
                payload = message.html_part.get_payload().decode('utf-8')
                soup = BeautifulSoup(payload, "html.parser")
                tokens = soup.text.rstrip().split()[0:6]
                #print("html:", tokens)
            elif message.mailparts[0].type.startswith('text/'):
                mailpart = message.mailparts[0]
                payload, used_charset = pyzmail.decode_text(mailpart.get_payload(), mailpart.charset, None)
                tokens = payload.split()[0:6]
                #print("plain text:", tokens)
            else:
                #TODO: return error
                pass
            #end if/elif/else

            # handling carrier extra shit
            if 'T-Mobile' in tokens:
                # tmomail.net
                tokens.remove('T-Mobile')
            elif 'Multimedia' in tokens[0] and 'Message' in tokens[1]:
                # mms.att.net
                tokens.remove(tokens[0])
                tokens.remove(tokens[0])
            #end if/elif

            print(tokens)
            print()
            commands_queue.put(tokens)
        #end for
    #end if
    print(list(commands_queue.queue))

#end main


if __name__ == "__main__":
    main()
