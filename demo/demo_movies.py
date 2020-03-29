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

interk = None
def main():
    # read in creds
    data = {}
    if os.path.exists("../ik_properties.json"):
        with open("../ik_properties.json") as ik_props:
            data = json.load(ik_props)
    #end if
    global interk
    interk = interkonnect.Interkonnect(data)

    # main listener loop
    while True:
        queue_status = True
        # loop over the commands in the queue
        command_queue = interk.check_inbox()
        while queue_status:
            try:
                parse_command(command_queue.get_nowait())
            except queue.Empty:
                queue_status = False
        #end while
        time.sleep(interk.wait_time)
    #end while
#end main


def parse_command(command):
    address = command[0]
    command = command[1]
    print("From %s:\n\tcommand: %s" % (address, command))
    if 'help' in command[0].lower():
        _handle_help(address)
    elif 'register' in command[0].lower():
        _handle_register(address, command[1])
    elif 'list' in command[0].lower():
        _handle_list(address, command[1])
    elif 'find' in command[0].lower():
        pass
    else:
        #TODO: return error
        pass
#end parse_command


def _handle_help(address):
    msg = 'For a list of dvds, text "list dvd"\n'
    msg += 'For a list of blurays, text "list bluray"\n'
    global interk
    interk.reply(address, msg)
#end _handle_help


def _handle_register(address, key):
    pass
#end _handle_register


def _handle_list(address, list_type):
    if 'dvd' in list_type.lower():
        print("LISTING DVDS\n\n")
        _send_dvd_list(address)
    elif 'bluray' in list_type.lower():
        print("LISTING BLURAYS\n\n")
    else:
        #TODO: return error
        pass
    #end if/elif/else
#end _handle_list


def _send_dvd_list(address):
    msg = ""
#end _send_dvd_list


def _send_bluray_list(address):
    msg = ""
#end _send_bluray_list


def _handle_find(address, title):
    pass
#end _handle_find


if __name__ == "__main__":
    main()
