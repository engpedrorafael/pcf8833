PCF8833 LCD python bindings for the Raspberry Pi
=======

Schematics &amp; python module to drive a PCF8833 LCD [as used on Nokia 6100] <br/>
This project is intended to help who wants to create a cheap prototype setup to interface an LCD controlled by the Philips PCF8833 chip.

<table>
  <tr>
    <td>
      <img src="https://raw.github.com/engpedrorafael/pcf8833/master/doc/images/LCD6100.jpg"/>
    </td>
    <td>
      specifications:<br/>
    </td>
  </tr>
</table>

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
<table>
  <tr>
    <td>
      <img src="https://raw.github.com/engpedrorafael/pcf8833/master/doc/images/lcdpinout.jpg"/>
    </td>
    <td>
      Here more
    </td>
  </tr>
</table>
Something more
<table>
  <tr>
    <td>
      <img src="https://raw.github.com/engpedrorafael/pcf8833/master/doc/images/GPIOs.png"/>
    </td>
    <td>
      <img src="https://raw.github.com/engpedrorafael/pcf8833/master/doc/images/shematics.png"/>
    </td>
  </tr>
</table>
Describe pinouts and components here

Cheap Prototype
-----------------
This can be tested with an old or broken NOKIA 6100 with a working LCD. Because it's hard to connect to the LCD directly because of the very small LCD connector, one can use the phone's PCB to easily connect wires to the LCD as the LCD pins are mapped in the cooper connection under the LCD as shown in the image:

![Phone PCB connections](https://raw.github.com/engpedrorafael/pcf8833/master/doc/images/phonePCB.jpg)

And here it is working!

![Tesing](https://raw.github.com/engpedrorafael/pcf8833/master/doc/images/prototype.jpg)

![Test image](https://raw.github.com/engpedrorafael/pcf8833/master/doc/images/testImage.jpg)



References
----------
* https://projects.drogon.net/raspberry-pi/wiringpi/pins/

* https://github.com/rm-hull/pcd8544

* https://github.com/rm-hull/wiringPi
