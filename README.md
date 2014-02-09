PCF8833 LCD python bindings for the Raspberry Pi
=======

Schematics &amp; python module to drive a PCF8833 LCD [as used on Nokia 6100] <br/>
This project is intended to help who wants to create a cheap prototype setup to interface an LCD controlled by the Philips PCF8833 chip.

![PCF8833](https://raw.github.com/engpedrorafael/pcf8833/master/doc/images/LCD6100.jpg)


Further technical details for the LCD screen can be found in the 
[datasheet](https://raw.github.com/engpedrorafael/pcf8833/master/doc/PCF8833.pdf) [PDF].

Pre-requisites
--------------
Compile and install the wiringPi python bindings from https://github.com/rm-hull/wiringPi. 

Next, install PIL (Python Imaging Library) as follows:

    $ sudo apt-get install zlibc libjpeg-dev libpng3 libfreetype6 libfreetype6-dev python-pip
    $ find /usr/lib -name libjpeg.so
    $ sudo ln -s /usr/lib/arm-linux-gnueabihf/libjpeg.so /usr/lib/
    $ sudo pip install PIL

Building and installing the software
------------------------------------
After having cloned from github:

    $ python setup.py clean build
    $ sudo python setup.py install

This should install the files in your local dist-files area (somewhere
like `/usr/local/lib/python2.7/distfiles/pcf8833`).

Next, test at the hardware and software is working:

    $ cd examples
    $ sudo ./loadImage.py

Wiring schematic
----------------

![Wiring Schematic](link here)

Describe pinouts and components here

Cheap Prototype  
-----------------
![Wiring Schematic](link here)

![Wiring Schematic](link here)


References
----------
* https://projects.drogon.net/raspberry-pi/wiringpi/pins/

* https://github.com/rm-hull/pcd8544

* https://github.com/rm-hull/wiringPi
