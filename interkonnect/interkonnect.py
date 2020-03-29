""" Interconnect allows control of programs/devices via SMS """

from queue import Queue

import imapclient
import pyzmail
from bs4 import BeautifulSoup


class Interkonnect:
    def __init__(self, ik_data):
        self.ik_data = ik_data
        self.wait_time = ik_data.get("wait_time")

        # login to the
        self.imap_obj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
        self.imap_obj.login(ik_data.get("email"), ik_data.get("pass"))
    #end init

    def check_inbox(self):
        commands_queue = Queue()
        self.imap_obj.select_folder('INBOX')
        email_ids = self.imap_obj.search('UNSEEN')
        if email_ids:
            print(email_ids)
            for email_id in email_ids:
                # get data from the email
                tokens = []
                print("email id: %s" % email_id)
                raw_msg = self.imap_obj.fetch([email_id], ['BODY[]', 'FLAGS'])
                message = pyzmail.PyzMessage.factory(raw_msg[email_id][b'BODY[]'])
                print(message.get_address('from'))
                if message.text_part is not None:
                    payload = message.text_part.get_payload().decode('utf-8')
                    tokens = payload.split()[0:6]
                    # print("plain text:", tokens)
                elif message.html_part is not None:
                    payload = message.html_part.get_payload().decode('utf-8')
                    soup = BeautifulSoup(payload, "html.parser")
                    tokens = soup.text.rstrip().split()[0:6]
                    # print("html:", tokens)
                elif message.mailparts[0].type.startswith('text/'):
                    mailpart = message.mailparts[0]
                    payload, used_charset = pyzmail.decode_text(mailpart.get_payload(), mailpart.charset, None)
                    tokens = payload.split()[0:6]
                    # print("plain text:", tokens)
                else:
                    # TODO: return error
                    pass
                # end if/elif/else

                # handling carrier extra shit
                if 'T-Mobile' in tokens:
                    # tmomail.net
                    tokens.remove('T-Mobile')
                elif 'Multimedia' in tokens[0] and 'Message' in tokens[1]:
                    # mms.att.net
                    tokens.remove(tokens[0])
                    tokens.remove(tokens[0])
                # end if/elif

                print(tokens)
                print()
                commands_queue.put(tokens)
            # end for
        # end if
        print(list(commands_queue.queue))
        return commands_queue
    #end check_inbox
#end Interkonnect
