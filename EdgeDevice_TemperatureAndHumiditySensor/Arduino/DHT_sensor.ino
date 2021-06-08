#include "DHT.h"         
const int DHTPIN = 4;      
const int DHTTYPE = DHT11;  

DHT dht(DHTPIN, DHTTYPE);
void setup() {
  Serial.begin(9600);
  dht.begin();       
}

void loop() {
  float h = dht.readHumidity();    
  float t = dht.readTemperature(); 
  Serial.println(String(t)+"space"+String(h));            
  delay(1000);                     
}
