import os
import sys

from parkings.client.session import Session
from parkings.models.spaces import CarSlots as ParkingLot
from parkings.models.vehicle import Car

def parsecmd():
    if len(sys.argv)>1:
        IMode = False
        return IMode, str(sys.argv[1])
    else:
        IMode = True
        return IMode, ""

def main():
    client = None
    IMode, filepath = parsecmd()
    
    # Route the program to the client based on interactivity. 
    # if input file is used, session run on non-interactive mode.
    # If terminal is used to key in the inputs by user, program is in non interactive mode. 
    if IMode:
        # if interactive mode
        session = Session(is_inter=True)
    else:
        session = Session(filepath=filepath)
    session.run()

if __name__ == '__main__':
    main()
