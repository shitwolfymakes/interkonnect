"""
This demo is a proof of concept of how interkonnect works. Once this works, everything
can be pulled out and moved into interkonnect.py, and the only stuff that will remain
here is what the user does with the data that is returned
"""

import os.path
import json
import queue
import time

import interkonnect


def main():
    # read in creds
    data = {}
    if os.path.exists("../ik_properties.json"):
        with open("../ik_properties.json") as ik_props:
            data = json.load(ik_props)
    #end if
    interk = interkonnect.Interkonnect(data)

    # main listener loop
    while True:
        print("in listener")
        queue_status = True
        # loop over the commands in the queue
        while queue_status:
            print("in queue")
            command_queue = interk.check_inbox()
            try:
                parse_command(command_queue.get_nowait())
            except queue.Empty:
                queue_status = False
        #end while
        time.sleep(interk.wait_time)
    #end while
#end main


def parse_command(command):
    print("command:", command)
    pass
#end parse_command


if __name__ == "__main__":
    main()
