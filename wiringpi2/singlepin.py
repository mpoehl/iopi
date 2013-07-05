# Single Pin control of IO Pi board mcp23017 on address 0x20 and 0x21  ( AB Electronics IO Pi )
# run using sudo python singlepin.py
import wiringpi2

pin_base = 65
i2c_addr = 0x20
i2c_addr_2 = 0x21

wiringpi2.wiringPiSetup()
wiringpi2.mcp23017Setup(pin_base,i2c_addr)
wiringpi2.mcp23017Setup(pin_base+16,i2c_addr_2)

# reset all pins as outputs and turn off
for pin in range(65,97):
	wiringpi2.pinMode(pin,1)
	wiringpi2.digitalWrite(pin,0)
	
# turn on pin 96 - IC 2 pin 16 on IO Pi
wiringpi2.pinMode(96,1)
wiringpi2.digitalWrite(96,1)

