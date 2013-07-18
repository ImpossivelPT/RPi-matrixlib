import spidev

dev = spidev.SpiDev(0,0) # open up /dev/spidev0.1

dev.max_speed_hz = 10000
dev.mode = 1
dev.max_speed_hz = 500000
dev.cshigh = False
dev.lsbfirst = False
dev.threewire = False
dev.loop = False # loop is "loopback"

dev.bits_per_word = 8

#dev.xfer([0x0000])
#dev.xfer([0x80,0x20])
#dev.xfer([0x80,0x60])
#dev.xfer([0xA0,0x3C])

while True:
    dev.cshigh = False
    dev.writebytes([0xff])
    dev.cshigh = False
    
#print dev.bits_per_word


dev.close()