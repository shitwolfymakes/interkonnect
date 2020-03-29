""" Interconnect allows control of programs/devices via SMS """


from queue import Queue


class Interkonnect:
    def __init__(self, ik_data):
        self.ik_data = ik_data
        self.creds = (ik_data.get("email"), ik_data.get("pass"))
        self.wait_time = ik_data.get("wait_time")

        self.commands_queue = None
    #end init

    def check_inbox(self):
        self.commands_queue = Queue()
    #end check_inbox
#end Interkonnect
