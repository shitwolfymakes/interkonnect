import os.path
import json
import imapclient
import pyzmail
from bs4 import BeautifulSoup


def main():
    # read in creds
    data = {}
    if os.path.exists("ik_properties.json"):
        with open("ik_properties.json") as ik_props:
            data = json.load(ik_props)
    #end if

    imap_obj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
    imap_obj.login(data.get("email"), data.get("pass"))
    imap_obj.select_folder('INBOX')
    email_ids = imap_obj.search()#'UNSEEN')
    if email_ids:
        for email_id in email_ids:
            print(email_id)
            raw_msg = imap_obj.fetch([email_id], ['BODY[]', 'FLAGS'])
            message = pyzmail.PyzMessage.factory(raw_msg[email_id][b'BODY[]'])
            print(message.get_address('from'))
            tmp = message.html_part.get_payload().decode('utf-8')
            #print(tmp)
            soup = BeautifulSoup(tmp, "html.parser")
            print(soup.text.rstrip().split())


    #end if

#end main


if __name__ == "__main__":
    main()
