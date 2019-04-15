import os
import sys

from parkings.client.session import Session
from parkings.models.spaces import CarSlots as ParkingLot
from parkings.models.vehicle import Car

INTERACTIVE_MODE = True

def parsecmd():
    if len(sys.argv)>1:
        INTERACTIVE_MODE = False
        print("File argument detected\n")
        return str(sys.argv[1])
    else:
        print("Interactive mode detected\n")
        return ""

def main():
    client = None
    filepath = parsecmd()
    
    # Route the program to the client based on interactivity. 
    # if input file is used, session run on non-interactive mode.
    # If terminal is used to key in the inputs by user, program is in non interactive mode. 
    if INTERACTIVE_MODE:
        # if interactive mode
        session = Session(is_inter=True)
    else:
        session = Session(filepath=filepath)
    session.run()

if __name__ == '__main__':
    main()
