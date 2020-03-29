""" Interconnect allows control of programs/devices via SMS """


from queue import Queue

import imapclient


class Interkonnect:
    def __init__(self, ik_data):
        self.ik_data = ik_data
        self.wait_time = ik_data.get("wait_time")

        self.commands_queue = None

        # login to the
        self.imap_obj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
        self.imap_obj.login(ik_data.get("email"), ik_data.get("pass"))
        self.imap_obj.select_folder('INBOX')
    #end init

    def check_inbox(self):
        self.commands_queue = Queue()
    #end check_inbox
#end Interkonnect
