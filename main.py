# HackOverFlow - Team QUINN
import Rpi.GPIO as GPIO
import time

#Raspberry pi gpio numbers
SPICLK=11
SPIMISO=9
SPICS=8
SPIMOSI=10
#sensor pin numbers
mq135_dpin=37
mq135_apin=0
def init():
    GPIO.setwarnings(False)
    GPIO.cleanup()		
    GPIO.setmode(GPIO.BCM)
#set up the SPI interface pins
    GPIO.setup(SPIMOSI, GPIO.OUT)
    GPIO.setup(SPIMISO, GPIO.IN)
    GPIO.setup(SPICLK, GPIO.OUT)
    GPIO.setup(SPICS, GPIO.OUT)
    GPIO.setup(mq135_dpin,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
#Read SPI data from MCP3008
def readadc(adcnum, clockpin, mosipin, misopin, cspin:
	if ((adcnum > 7) or (adcnum < 0)):
		return -1
		GPIO.output(cspin, True)	

		GPIO.output(clockpin, False) 
		GPIO.output(cspin, False) 
		commandout = adcnum
		commandout |= 0x18  
		commandout <<= 3    
		for i in range(5):
			if (commandout & 0x80):
				GPIO.output(mosipin, True)
			else:
				GPIO.output(mosipin, False)
				commandout <<= 1
				GPIO.output(clockpin, True)
				GPIO.output(clockpin, False)

		adcout = 0
# read in one empty bit, one null bit and 10 ADC bits
		for i in range(12):
			GPIO.output(clockpin, True)
			GPIO.output(clockpin, False)
			adcout <<= 1
			if (GPIO.input(misopin)):
				adcout |= 0x1
				GPIO.output(cspin, True)
				adcout >>= 1      
	    	return adcout
#main ioop
def main():
	init()
	print("please wait...")
	time.sleep(20)
	while True:
		CO2level=readadc(mq135_apin, SPICLK, SPIMOSI, SPIMISO, SPICS)
		if GPIO.input(mq135_dpin
			print("Gas not leak")
			time.sleep(0.5)
		else:
			print("The PPM Level \n",CO2level)
			time.sleep(0.5)
if __name__ =='__main__':
	try:
		main()
		pass
		except KeyboardInterrupt:
			pass

GPIO.cleanup()


