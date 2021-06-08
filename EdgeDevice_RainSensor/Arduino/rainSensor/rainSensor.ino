int rainSensorPin = A0;
//int buttonPin = 10;
//int LEDPin = 11;
int rainSensorValue;
String raining = "not raining";
//int buttonDown;
//int buttonUp;

unsigned long previousMillis = 0;        // will store last time millis() was called

// constants won't change:
const long interval = 1000;           // interval at which to run the loop (milliseconds)

void setup() {
  
  Serial.begin(9600);
//  pinMode(buzzerPin, OUTPUT);
//  pinMode(buttonPin, INPUT_PULLUP);
//  pinMode(LEDPin, OUTPUT);
}

void loop() {
  
  unsigned long currentMillis = millis();
//
//  //detect the button press
//  if (digitalRead(buttonPin) == false) {
//    //change current clothes state
//    changeClothesState();
//    //pause the program until button released
//    while (digitalRead(buttonPin) == false){}
//  }

  if (currentMillis - previousMillis >= interval) {
    // save the last milisecond
    previousMillis = currentMillis;
  
    //detect rain
    rainSensorValue = analogRead(rainSensorPin);
  
    //print weather state, also send msg to raspberry pi
    Serial.println(String(rainSensorValue));

//    //if Raspberry Pi is talking to Arduino
//    if (Serial.available() > 0)
//    {
//      //read the message
//      String data = Serial.readStringUntil('\n');
//      //turn on buzzer for rain alert
//      if (data == "1")
//        break;
//      //turn on buzzer for humidity alert
//      if (data == "2") 
//        break;
//    }
  }
}
