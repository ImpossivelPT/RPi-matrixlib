import spidev
import time

dev = spidev.SpiDev(0,0) # open up /dev/spidev0.1

dev.max_speed_hz = 10000
dev.lsbfirst = False
dev.bits_per_word = 16
"""
dev.mode = 1
dev.max_speed_hz = 500000
dev.cshigh = False

dev.threewire = False
dev.loop = False # loop is "loopback"


"""
#dev.xfer([0x0000])
#dev.xfer([0x80,0x20])
#dev.xfer([0x80,0x60])
#dev.xfer([0xA0,0x3C])
dev.writebytes([0x1004])

dev.writebytes([0x100C])

dev.writebytes([0xA03C])

    
#print dev.bits_per_word


dev.close()