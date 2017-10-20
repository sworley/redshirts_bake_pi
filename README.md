Purchase:

- --Raspberry Pi 3 - Model B - ARMv8 with 1G RAM
  - -- [https://www.adafruit.com/product/3055](https://www.adafruit.com/product/3055)
- --PN532 NFC/RFID controller breakout board - v1.6
  - -- [https://www.adafruit.com/product/364](https://www.adafruit.com/product/364)
- --Adafruit Assembled Pi Cobbler Breakout + Cable for Raspberry Pi - Model B
  - -- [https://www.adafruit.com/product/914](https://www.adafruit.com/product/914)
- --Full sized breadboard
  - -- [https://www.adafruit.com/product/239](https://www.adafruit.com/product/239)
- --Premium Male/Male Jumper Wires - 40 x 3&quot; (75mm)
  - -- [https://www.adafruit.com/product/759](https://www.adafruit.com/product/759)
- --Premium Female/Male &#39;Extension&#39; Jumper Wires - 20 x 6&quot;
  - -- [https://www.adafruit.com/product/1954](https://www.adafruit.com/product/1954)
- --A
  - --

Modifications I have made to the default &quot;setup&quot;

- --Upgraded to 16Gb MicroSD card(s) as I am running the full install (not the Lite version).
  - -- [https://goo.gl/5bH6Dj](https://goo.gl/5bH6Dj)
- --

Steps I have taken.

1.  Open up the mbed Microcontroller and plug into USB.
  1. Remove packaging
  2. Plug USB cable into the MAC
  3. Plug USB cable into the mbed Microcontroller
  4. Navigate to the shared drive called &quot;mbed&quot;
  5. Open the file called mbed.htm
2. Create a new mbed user account.
  1. Once the webpage mbed.htm loads
  2. Create a new user
  3. You will see an auto-register for your Microcontroller
    1. If you don&#39;t, browse back to the MBED/mbed.htm page and open it again.  It should autoregister.
  4. Confirm your email address from the newly created account.
3. Download Raspbian Stretch Light
  1. [https://www.raspberrypi.org/downloads/raspbian/](https://www.raspberrypi.org/downloads/raspbian/)
  2. Unzip to 2017-09-07-raspbian-stretch-lite.img
4. Download Etcher (Or something similar)
  1. [https://etcher.io/](https://etcher.io/)
5. Before you eject/remove the MicroSD, add a single empty file called &quot;ssh&quot; on the boot partition, this enables remote logins.
6. Insert the microSD into your PC/MAC
7. Write the image to the MicroSD via Etcher
8. Open/Unbox the Raspberry Pi3
  1. Connect HDMI
  2. Connect keyboard &amp; mouse
  3. Insert the MicroSD that has Raspbian Lite
  4. Connect the USB from the mbed Microcontroller
  5. Connect a power source
9. Once the desktop is up, you can login there or ssh directly to the device.
  1. Login &amp; change the password from the defaults.
  2. Enabled VNC
  3. Change the memory split between the GPU (graphics) and the system to 16 Mb.
    1. It will be necessary to reboot for this change to take effect.
10. Perform updates to get things to the latest version
  1. sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get dist-upgrade -y
sudo rpi-update

      **REBOOT Required**

1. Login to the Pi and change the password.
  1. Connect to the Pi3;  ssh pi@raspberrypi.local.
    1. The default pwd is raspberry, change this first.
    2. passwd, enter raspberry, enter a new pwd &lt;somethingnew&gt;, and enter it a second time to confirm &lt;somethingnew&gt;.
2. Fixing the serial port based off of Pi 3 changes (disabeling BlueTooth, not sure it&#39;s necessary, however I understand the need to get back to the default UART … ToDo: Look into the core\_freq option/discussion, is this better???)
  1.
    1. [https://www.raspberrypi.org/forums/viewtopic.php?t=138223&amp;p=918859](https://www.raspberrypi.org/forums/viewtopic.php?t=138223&amp;p=918859)
  2. Update the config to account for the pi3 port change.
    1. sudo vi /boot/config.txt
    2. Make the following change, add the line …
      1. dtoverlay=pi3-miniuart-bt
  3. Stop BT from trying to utilize the UART
    1. sudo systemctl disable hciuart
  4. Enter into the configuration screen, sudo raspi-config.
    1. Disable the serial console ption 5, P6 serial
      1. Allow a login shell over Serial: No
      2. Would you like the Serial port hardware to be enabled: Yes

**REBOOT Required**

1. Building libnfc
  1. [https://learn.adafruit.com/adafruit-nfc-rfid-on-raspberry-pi/building-libnfc](https://learn.adafruit.com/adafruit-nfc-rfid-on-raspberry-pi/building-libnfc)
  2. At /home/pi, create a repos directory.
  3. mkdir repos &amp;&amp; cd $\_.
  4. I have cloned libnfc for convenience, it&#39;s ok to utilize the original code for this.
    1. git clone https://github.com/sworley/libnfc.
  5. Configure to build to the target system.
    1. cd libnfc.
    2. sudo mkdir -p /etc/nfc/devices.d.
    3. sudo cp contrib/libnfc/pn532\_uart\_on\_rpi.conf.sample /etc/nfc/devices.d/pn532\_uart\_on\_rpi.conf.
  6. Update the config file
    1. echo &quot;allow\_intrusive\_scan = true&quot; | sudo tee --append /etc/nfc/devices.d/pn532\_uart\_on\_rpi.conf
  7. Pull the necessary tools to compile libnfc
    1. sudo apt-get install autoconf -y
    2. sudo apt-get install libtool -y
    3. sudo apt-get install libpcsclite-dev libusb-dev -y
    4. autoreconf -vis
    5. ./configure --with-drivers=pn532\_uart --sysconfdir=/etc --prefix=/usr.
  8. Compile the code
    1. sudo make clean.
    2. sudo make install all.

Some Notes:

[https://www.hackster.io/secured-pi/facial-recognition-rfid-lock-with-raspberry-pi-e81f98](https://www.hackster.io/secured-pi/facial-recognition-rfid-lock-with-raspberry-pi-e81f98)

[https://learn.adafruit.com/adafruit-nfc-rfid-on-raspberry-pi](https://learn.adafruit.com/adafruit-nfc-rfid-on-raspberry-pi)

[https://learn.adafruit.com/adafruit-nfc-rfid-on-raspberry-pi/freeing-uart-on-the-pi](https://learn.adafruit.com/adafruit-nfc-rfid-on-raspberry-pi/freeing-uart-on-the-pi)

[https://learn.adafruit.com/adafruit-nfc-rfid-on-raspberry-pi/testing-it-out](https://learn.adafruit.com/adafruit-nfc-rfid-on-raspberry-pi/testing-it-out)
