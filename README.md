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

Steps I have taken.

1. On a PC\MAC\Linux host … download Raspbian Stretch Light
  1. [https://www.raspberrypi.org/downloads/raspbian/](https://www.raspberrypi.org/downloads/raspbian/)
  2. Unzip to 2017-09-07-raspbian-stretch-lite.img
2. Download Etcher (Or something similar)
  1. [https://etcher.io/](https://etcher.io/)
3. Before you eject/remove the MicroSD, add a single empty file called &quot;ssh&quot; on the boot partition, this enables remote logins.
4. Insert the microSD into your system
5. Write the image to the MicroSD via Etcher
6. Open/Unbox the Raspberry Pi3
  1. Connect HDMI
  2. Connect keyboard &amp; mouse
  3. Insert the MicroSD that has Raspbian Lite
  4. Connect a power source
7. Once the desktop is up, you can login there or ssh directly to the device.
  1. Login &amp; change the password from the defaults.
  2. Enabled VNC
  3. Change the memory split between the GPU (graphics) and the system to 16 Mb.
    1. It will be necessary to reboot for this change to take effect.
8. Perform updates to get things to the latest version
  1. sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get dist-upgrade -y
sudo rpi-update

      **REBOOT Required**

1. Login to the Pi and change the password.
  1. Connect to the Pi3;  ssh pi@raspberrypi.local.
    1. The default pwd is raspberry, change this first.
    2. passwd, enter raspberry, enter a new pwd &lt;somethingnew&gt;, and enter it a second time to confirm &lt;somethingnew&gt;.
2.  Create a repo directory
  1. Change to the repo directory and check out the AdaFruit Python PN532 Repo
    1. Git clone [https://github.com/sworley/Adafruit\_Python\_PN532.git](https://github.com/sworley/Adafruit_Python_PN532.git)
  2. Following the instructions …
    1. [https://learn.adafruit.com/raspberry-pi-nfc-minecraft-blocks/hardware-wiring](https://learn.adafruit.com/raspberry-pi-nfc-minecraft-blocks/hardware-wiring)
    2. [https://learn.adafruit.com/raspberry-pi-nfc-minecraft-blocks/library-installation](https://learn.adafruit.com/raspberry-pi-nfc-minecraft-blocks/library-installation)
  3. Now you are ready to start working on the project that we are here for.  Clone the teams repository …
    1. Git clone [https://github.com/sworley/redshirts\_bake\_pi.git](https://github.com/sworley/redshirts_bake_pi.git)

Now we should be ready to start programming for the project!!

This does not account for the added camera (as I do not have that hardware yet)

This does not account for any of the S3/Image lookup pieces yet.

Feel free to contribute what you can when you can!

Some Notes:

[https://www.hackster.io/secured-pi/facial-recognition-rfid-lock-with-raspberry-pi-e81f98](https://www.hackster.io/secured-pi/facial-recognition-rfid-lock-with-raspberry-pi-e81f98)

[https://learn.adafruit.com/adafruit-nfc-rfid-on-raspberry-pi](https://learn.adafruit.com/adafruit-nfc-rfid-on-raspberry-pi)

[https://learn.adafruit.com/adafruit-nfc-rfid-on-raspberry-pi/freeing-uart-on-the-pi](https://learn.adafruit.com/adafruit-nfc-rfid-on-raspberry-pi/freeing-uart-on-the-pi)

[https://learn.adafruit.com/adafruit-nfc-rfid-on-raspberry-pi/testing-it-out](https://learn.adafruit.com/adafruit-nfc-rfid-on-raspberry-pi/testing-it-out)
