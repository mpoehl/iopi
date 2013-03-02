#!/usr/bin/env python
# abelectronics IO Pi Expander board read inputs on each bus as decimal and binary
# # Requries Python 2 and smbus
# I2C API depends on I2C support in the kernel

# Version 1.0  - 02/03/2013
# Version History:
# 1.0 - Initial Release
# 
from smbus import SMBus
import sys
import getopt
import time
import re

# set io pi chip i2c addresses
expander_address1 = 0x20
expander_address2 = 0x21


for line in open('/proc/cpuinfo').readlines():
    m = re.match('(.*?)\s*:\s*(.*)', line)
    if m:
        (name, value) = (m.group(1), m.group(2))
        if name == "Revision":
            if value [-4:] in ('0002', '0003'):
                i2c_bus = 0
            else:
                i2c_bus = 1
            break

            
bus = SMBus(i2c_bus)

#set both chips and buses as inputs
bus.write_byte_data(expander_address1,0x00,0xff)
bus.write_byte_data(expander_address1,0x01,0xff)
bus.write_byte_data(expander_address2,0x00,0xff)
bus.write_byte_data(expander_address2,0x01,0xff)


while 1: 
	# read inputs on address 1
	a = bus.read_byte_data(expander_address1,0x12)
	print a
	print (bin(a))
	time.sleep(0.5)
	b = bus.read_byte_data(expander_address1,0x13)
	print b
	print (bin(b))
	time.sleep(0.5)
	
	# read inputs on address 2
	a = bus.read_byte_data(expander_address2,0x12)
	print a
	print (bin(a))
	time.sleep(0.5)
	b = bus.read_byte_data(expander_address2,0x13)
	print b
	print (bin(b))