#!/usr/bin/python
#
# rsbp.py - Red Shirts Bake Pi <dot> Py
# ----
# This was created for the team building actiity we have found ourselves 
# involved in ... "I'm Givin' Her All She's Got, Captain!"
# ----
# 1.2 - 10.19.17 - sworley - Finally functionality !!! Reading From a RFID
# 1.1 - 10.18.17 - sworley - Imported files into a real repository
# 1.0 - 10.17.17 - sworley - Initially created the file based off of the 
#                            Adafruit_Python_PN532 examples.
# ----
# import-ant stuff ...
import binascii                # Convert card H3XX details
import time                    # Time access/conversions
import Adafruit_PN532 as PN532 # Main lib for PN532 coms over SPI
import RPi.GPIO as GPIO        # Enable access to GPIO

# PN532 SPI configuration
CS   = 18
MOSI = 23
MISO = 24
SCLK = 25

# Card key configuration, defaults are fine
CARD_KEY = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]

# Create and initialize an instance of the PN532 class.
pn532 = PN532.PN532(cs=CS, sclk=SCLK, mosi=MOSI, miso=MISO)
pn532.begin()
pn532.SAM_configuration()

print 'NFC Listener'
print ''
print 'Waiting for RFID card...'
while True:
    # Stand by for a card ...
    uid = pn532.read_passive_target()
    # Try again if no card found.
    if uid is None:
        continue
    # Detect the block type
    print 'Found card with UID 0x{0}'.format(binascii.hexlify(uid))
    # Authenticate and read block 4.
    if not pn532.mifare_classic_authenticate_block(uid, 4, PN532.MIFARE_CMD_AUTH_B,
    CARD_KEY):
        print 'Failed to authenticate with card!'
        continue
    data = pn532.mifare_classic_read_block(4)
    if data is None:
        print 'Failed to read data from card!'
        continue
