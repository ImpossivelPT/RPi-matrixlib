import spidev

dev = spidev.SpiDev(0,0) # open up /dev/spidev0.1

dev.max_speed_hz = 10000
dev.mode = 1
dev.max_speed_hz = 500000
dev.cshigh = False
dev.lsbfirst = False
dev.threewire = False
dev.loop = False # loop is "loopback"
dev.bits_per_word = 16

#dev.xfer([0x0000])
dev.xfer([0x8020])
dev.xfer([0x8060])
dev.xfer([0xA03C])

#print dev.bits_per_word


dev.close()