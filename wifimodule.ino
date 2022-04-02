## For Wifi Module
			      		
#include <MQ135.h>

#define PIN_MQ135 A0

MQ135 mq135_sensor(PIN_MQ135);

float temperature = 21.0; 
float humidity = 25.0; 
void setup() {
  Serial.begin(9600);
}

