#!/usr/bin/env python

from distutils.core import setup
setup(
    name = "pcf8833",
    version = "0.0.1",
    author = "Pedro Almeida",
    author_email = "engpedrorafael@gmail.com",
    description = ("Library to drive the PCF8833 LCD using WiringPi software bit-banding"),
    license = "GLPv2",
    keywords = "raspberry pi rpi lcd nokia 6100 pcf8833",
    url = "https://github.com/rm-hull/pcd8544",
    packages=['pcf8833'],
    package_dir={'pcf8833': 'src'}
)
