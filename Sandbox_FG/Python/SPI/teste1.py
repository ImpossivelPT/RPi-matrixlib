import spidev
import time

dev = spidev.SpiDev(0,0) # open up /dev/spidev0.1
"""
dev.max_speed_hz = 10000
dev.mode = 1
dev.max_speed_hz = 500000
dev.cshigh = False
dev.lsbfirst = False
dev.threewire = False
dev.loop = False # loop is "loopback"

dev.bits_per_word = 8
"""
#dev.xfer([0x0000])
#dev.xfer([0x80,0x20])
#dev.xfer([0x80,0x60])
#dev.xfer([0xA0,0x3C])
"""
dev.cshigh = True
dev.cshigh = False
dev.writebytes([1025])

dev.cshigh = True
dev.cshigh = False
dev.writebytes([1027])

dev.cshigh = True
dev.cshigh = False
dev.writebytes([10255])
"""

    
#print dev.bits_per_word


dev.close()