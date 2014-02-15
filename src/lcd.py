"""@package pcf8833
This package contains the binding for the LCD woth the controller pcf8833 

More details and examples at:
https://github.com/engpedrorafael/pcf8833
"""

import time
import math
import wiringPy
from PIL import Image,ImageDraw,ImageFont,ImageFile,ImageChops

# useful constants
ON,   OFF = [1, 0]
HIGH, LOW = [1, 0]

RED   = (255,0,0)
GREEN = (0,255,0)
BLUE  = (0,0,255)
WHITE = (255,255,255)
BLACK = (0,0,0)


class Driver:
    """Class for interfacing the pcf8833 LCD driver
    """
   
    def __init__(self, SDATA=2, SCLK=3, RST=4, CS=14):
        """The constructor"""
        self._memVar = 0
        self._vRes = 132
        self._hRes = 132

        #Set GPIO pins
        self._SDATA = SDATA
        self._SCLK = SCLK
        self._RST = RST
        self._CS  = CS

        #create a SPI instance
        self.__spiInterface = SPI(SDATA, SCLK, RST, CS)        

        #Var used for data sequencial data write
        self.__storedColor = None

        #Initialize the device
        self.initDevice()
   
    def colouredBars(self):
        """Test the LCD by writing 4 Horizontal lines
           Top down:  White, Blue, Green, Red"""
        self.setRegion((1,1),(self._vRes, self._hRes))
        pixelsPerLine = self._hRes * (self._vRes/4)

        #red bar
        for i in range(pixelsPerLine):
          self.setPixel(RED)

        #green bar
        for i in range(pixelsPerLine):
          self.setPixel(GREEN)

        #blue bar
        for i in range(pixelsPerLine):
          self.setPixel(BLUE)

        #white bar
        for i in range(pixelsPerLine):
          self.setPixel(WHITE)

    def test(self):
        """Test method for testing all the functionalities"""

        print "======== Testing LCD ========"

        #Draw Coloured Horizontal bars
        print "Drawing 4 horizontal bars..."
        self.colouredBars()
        time.sleep(1)

        #Test LCD ON/OFF
        print "Flicking LCD..."
        self.OFF()
        time.sleep(1)
        self.ON()

        #Test Clear method
        print "Filling LCD with RED..."
        self.clear(RED)
        time.sleep(2)

        #Test Backgroud draw
        print "Filling LCD with GREEND in background while LCD is OFF..."
        self.OFF()
        self.clear(GREEN)
        self.ON()
        time.sleep(3)

        print "Clearing LCD with WHITE..."
        #Test Axes orientation with a graph
        self.clear(WHITE)

        print "Drawing some graphics..."
        xA = range(132)
        for x in xA:
            y = int(math.sin((x*6*math.pi)/132.0)*(132.0/2.0-20)+(132.0/2))
            self.setSinglePixel((x, y), BLACK)

        for x in xA:
            y = int(math.sin((x*3*math.pi)/132.0)*(132.0/2.0-50)+(132.0/2))
            self.setSinglePixel((x, y), RED)

        for x in xA:
            y = int(math.cos((x*6*math.pi)/132.0)*(132.0/2.0-30)+(132.0/2))
            self.setSinglePixel((x, y), GREEN)

        for x in xA:
            self.setSinglePixel((x, x), BLUE)

        print "All tests done."

    def setPixel(self, color):
        """Set a pixel to a specific color
           This method will store each odd pixel collor and will write in every other bit
               Data format: 2-pixes-per-3-bytes
                     BBBB GGGG | RRRR BBBB | GGGG RRRR
        """
        r = (color[0]>>4) ^ 0xFF
        g = (color[1]>>4) ^ 0xFF
        b = (color[2]>>4) ^ 0xFF
        if self.__storedColor is None:
            self.__storedColor = (r, g, b)
        else:
            byte1=((self.__storedColor[2]<<4) | (self.__storedColor[1] & 0x0F)) & 0xFF
            byte2=((self.__storedColor[0]<<4) | (b & 0x0F)) & 0xFF
            byte3=((g<<4) | (r & 0x0F)) & 0xFF
            self.__spiInterface.sData(byte1)
            self.__spiInterface.sData(byte2)
            self.__spiInterface.sData(byte3)
            self.__storedColor = None

    def setSinglePixel(self, point, color):
        """Set a pixel to a specific color
           This method will write teh color data into the pixel position directly
               Data format: 1-pixel-per-2-bytes
                     BBBB GGGG | RRRR XXXX
        """
        self.setRegion(point, point)
        r=(color[0]>>4) ^ 0xFF
        g=(color[1]>>4) ^ 0xFF
        b=(color[2]>>4) ^ 0xFF
        byte1=(b<<4) | (g & 0x0F)
        byte2=(r<<4) 
        self.__spiInterface.sData(byte1)
        self.__spiInterface.sData(byte2)


    def setRegion(self, startPoint, endPoint):
        """Set a region for sequential data writing bottom up
        """
        self.__spiInterface.command(0x2B)         #Page Address Set
        self.__spiInterface.sData(startPoint[1])   # Start Y
        self.__spiInterface.sData(endPoint[1])    # end Y

        self.__spiInterface.command(0x2A)         #Column Address Set
        self.__spiInterface.sData(startPoint[0])  # start X
        self.__spiInterface.sData(endPoint[0])    # end X

        self.__spiInterface.command(0x2C)         # Start sending pixel data 
        self.__storedColor = None

    def clear(self, color):
        """Fills the screen with a specific color
        """
        self.setRegion((0,0),(self._vRes, self._hRes))

	for i in range(self._vRes * self._hRes):
           self.setPixel(color)

    def loadImage(self,path):
        self.setRegion((1,1),(self._vRes, self._hRes))
        bitmap = Image.open(path)
        pixels = list(bitmap.getdata())
        pixels.reverse()
        for p in pixels:
            self.setPixel(p)

    def initDevice(self):
        """Initialise the screen"""
        wiringPy.debug(0)

        if wiringPy.setup_gpio() != 0:
            raise IOError("Failed to initialize wiringPy properly")

        fd = wiringPy.setup_bitbang(self._CS, self._SDATA, self._SCLK, 0)
        if fd == -1:
            raise IOError("Failed to initialize bitbang properly")

        pins = [self._SDATA, self._SCLK, self._RST, self._CS]
        map(lambda p: wiringPy.pin_mode(p, ON), pins)

        # Reset the device
        self.reset()

        #Exit LCD sleep mode
        self.__spiInterface.command(0x11)

        #Turns on Booster voltage
        self.__spiInterface.command(0x03)
       
        #Display inversion ON 
        self.__spiInterface.command(0x21)
        
        #Set LCD params: 
        self.__spiInterface.command(0x36)
        self.__spiInterface.sData(0xC8)
        
        #Set pixel format
        self.__spiInterface.command(0x3A)

        #Set Contrast
        self.setContrast()	

        #Clear All pixels
        #self.__spiInterface.command(0x22) 

        #Display on
        self.ON()

        #Set to no operation
        self.__spiInterface.command(0x00)

    def reset(self):
        """Resets the device"""
        wiringPy.digital_write(self._RST, OFF)
        time.sleep(0.5)
        wiringPy.digital_write(self._RST, ON)

    def OFF(self):
        """Display OFF"""
        self.__spiInterface.command(0x28)

    def ON(self):
        """Display ON"""
        self.__spiInterface.command(0x29)

    def setContrast(self, contrast = 59):
        """Set the LCD contrast"""
        self.__spiInterface.command(0x25)
        self.__spiInterface.sData(contrast)


class SPI:
    """Class for communication vis SPI serial Connection
    """

    def __init__(self, SDATA, SCLK, RST, CS):
        """The constructor"""
        #Set GPIO pins
        self._SDATA = SDATA
        self._SCLK = SCLK
        self._RST = RST
        self._CS  = CS

    def command(self, data):
        """Send a hex self.__spiInterface.command through the serial port (SDATA 0 first)"""
        wiringPy.digital_write(self._CS,0)        # disable CS
        wiringPy.digital_write(self._SDATA,0)     # Disable Serial Data line, This means we are sending a self.__spiInterface.command
        wiringPy.digital_write(self._SCLK,0)      # Disable Serial Clock
        wiringPy.digital_write(self._SCLK,1)      # Enable Serial Clock
        for j in range(8):
            if ((data & 0x80) == 0x80):
                wiringPy.digital_write(self._SDATA,1)
            else:
                wiringPy.digital_write(self._SDATA,0)
            wiringPy.digital_write(self._SCLK,0)        # Disable Clock
            wiringPy.digital_write(self._SCLK,1)        # Enable Clock
            data <<= 1
        wiringPy.digital_write(self._SCLK,0)            # Disable Clock
        wiringPy.digital_write(self._SDATA,0)           # Disable Serial Data     

        wiringPy.digital_write(self._CS,1)              # Enable CS

    def sData(self, data):
        """Send hex data through the serial port (SDATA 1 first)"""
        wiringPy.digital_write(self._CS,0)        # disable CS
        wiringPy.digital_write(self._SDATA,1)     # Enable Serial Data line, This means we are sending data
        wiringPy.digital_write(self._SCLK,0)      # Disable Serial Clock
        wiringPy.digital_write(self._SCLK,1)      # Enable Serial Clock

        for j in range(8):
            if ((data & 0x80) == 0x80):
                wiringPy.digital_write(self._SDATA,1)  # Enable Serial Data
            else:
                wiringPy.digital_write(self._SDATA,0)  # Disable Serial Data line

            wiringPy.digital_write(self._SCLK,0)       # Disable Clock
            wiringPy.digital_write(self._SCLK,1)       # Enable Clock
            data <<= 1
        wiringPy.digital_write(self._SCLK,0)      # Disable Clock
        wiringPy.digital_write(self._SDATA,0)     # Disable Serial Data

        wiringPy.digital_write(self._CS,1)        # Enable CS
            
        

if __name__ == "__main__":
    myLcd = Driver()
    myLcd.test()
    print "Done. You should see now Graphics in the LCD."

