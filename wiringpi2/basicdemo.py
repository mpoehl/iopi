# Turns on and off each pin in turn of an mcp23017 on address 0x20 and 0x21  ( AB Electronics IO Pi )
# run using sudo python basicdemo.py

import wiringpi2

pin_base = 65
i2c_addr = 0x20
i2c_addr_2 = 0x21


wiringpi2.wiringPiSetup()
wiringpi2.mcp23017Setup(pin_base,i2c_addr)
wiringpi2.mcp23017Setup(pin_base+16,i2c_addr_2)

#for pin in pins:
while True:
	for pin in range(65,97): 	#65 to 97 excluding 97
		wiringpi2.pinMode(pin,1)
		wiringpi2.digitalWrite(pin,1)
		wiringpi2.delay(100)
		wiringpi2.digitalWrite(pin,0)
