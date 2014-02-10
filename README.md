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
      Specification:
<table>
<tr><td>LCD controller</td><td>Philips PFC8833</td></tr>
<tr><td>Interface</td><td>SPI Serial connection</td></tr>
<tr><td>Pixel resolution</td><td>132x132 pixels</td></tr>
<tr><td>Color resolution</td><td>12 bits (4096 colors)</td></tr>
<tr><td>Visible area</td><td>3cm x 3cm</td></tr>
<tr><td>Operating voltage</td><td>3.3V</td></tr>
</table>
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
      table border="1" cellpadding="3" cellspacing="0">
<tr>
<td>1</td>
<td>VDD 3,3V</td>
<td> </td>
</tr>
<tr>
<td>2</td>
<td>/Reset</td>
<td>PB4</td>
</tr>
<tr>
<td>3</td>
<td>SDATA</td>
<td>PB3</td>
</tr>
<tr>
<td>4</td>
<td>SCLK</td>
<td>PB5</td>
</tr>
<tr>
<td>5</td>
<td>/CS</td>
<td>PB2</td>
</tr>
<tr>
<td>6</td>
<td>VLCD 3,3V</td>
<td> </td>
</tr>
<tr>
<td>7</td>
<td>NC</td>
<td> </td>
</tr>
<tr>
<td>8</td>
<td>GND</td>
<td> </td>
</tr>
<tr>
<td>9</td>
<td>LED-</td>
<td> </td>
</tr>
<tr>
<td>10</td>
<td>LED+ (6V)</td>
<td> </td>
</tr>
</table>
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
