# iBeacon find example
# University of Idaho
# Edited by Doug Barnes May 2021

from __future__ import print_function
import blescan
import sys

import bluetooth._bluetooth as bluez

dev_id = 0
try:
	sock = bluez.hci_open_dev(dev_id)
	print ("ble thread started")

except:
	print ("error accessing bluethooth device...")
	sys.exit(1)

blescan.hci_le_set_scan_parameters(sock)
blescan.hci_enable_le_scan(sock)

def beacon_scan():#scan 50 nearest bluetooth devices and find iBeacons via MAC address
	returnedList = blescan.parse_events(sock, 50)
	print ("----------")
	for beacon in returnedList:
		if beacon[0] == 'd':
			beaconSplit = beacon.split(",")
			if beaconSplit[0] == "dd:33:0a:11:17:f7": #Bluecharm 1
				print("BLUECHARM #1")
				print(beacon)
			elif beaconSplit[0] == "dd:33:0a:11:1d:6b": #Bluecharm 2
				print("BLUECHARM #2")
				print(beacon)
			elif beaconSplit[0] == "dd:33:0a:11:1a:fb": #Bluecharm 3
				print("BLUECHARM #3")
				print(beacon)

while True:
	beacon_scan()
