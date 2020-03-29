"""
This demo is a proof of concept of how interkonnect works. Once this works, everything
can be pulled out and moved into interkonnect.py, and the only stuff that will remain
here is what the user does with the data that is returned
"""

import os.path
import json
from queue import SimpleQueue

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

    commands_queue = SimpleQueue()
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
                tmp = message.text_part.get_payload().decode('utf-8')
                tokens = tmp.split()
                print("plain text:", tokens)
            elif message.html_part is not None:
                tmp = message.html_part.get_payload().decode('utf-8')
                #print(tmp)
                soup = BeautifulSoup(tmp, "html.parser")
                tokens = soup.text.rstrip().split()
                print("html:", tokens)
            elif message.mailparts[0].type.startswith('text/'):
                mailpart = message.mailparts[0]
                payload, used_charset = pyzmail.decode_text(mailpart.get_payload(), mailpart.charset, None)
                print("plain text:", payload.split())
            else:
                #TODO: return error
                pass
            #end if/elif/else

            print()
        #end for
    #end if

#end main


if __name__ == "__main__":
    main()
