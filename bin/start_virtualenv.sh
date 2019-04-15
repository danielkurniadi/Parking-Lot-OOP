#!/bin/bash

INVENV=$(python -c 'import sys; print ("1" if hasattr(sys, "real_prefix") else "0")')

if [ $INVENV -eq 0 ]
then
	echo "Starting virtualenv"
	virtualenv .virtualenv
	. .virtualenv/bin/activate
	pip3 install -r Parking-engine/requirements.txt --upgrade
else
	echo "virtualenv already running"
fi

export DBUS_SESSION_BUS_ADDRESS=/dev/null