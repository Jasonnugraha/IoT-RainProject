//Alarm System
const int trig = 9;     //trigger
const int echo = 10;    //sensor
const int light = 13;   //LED

// Variables
long duration;
int distance;
char serialListener;

void setup() {
  // Sets the trigger to be the output
    pinMode(trig, OUTPUT);
    //Sets the echo as source of input
    pinMode(echo, INPUT);

    // Sets light as an output
    pinMode(light, OUTPUT);

    Serial.begin(9600);
}

void loop() {
  Serial.flush();
  serialListener = Serial.read();
  // Clearing trigger, make sure that it is cleared and restarted always
    digitalWrite(trig, LOW);
    delayMicroseconds(5);

    // Setting the trigger
    digitalWrite(trig, HIGH);
    delayMicroseconds(10);
    digitalWrite(trig, LOW);

    // To read the echo (sensor) which is the sound detected (This is the time which is detected in microseconds)
    duration = pulseIn(echo, HIGH);

    // Calculating the distance
    distance = (duration*0.034)* 0.5;

        
     if(serialListener == 'H'){
      digitalWrite(light, HIGH);
     }
     if (serialListener == 'L'){
       digitalWrite(light, LOW);
     }

    //Show the distance
    Serial.println(distance);
    delay(1000);
}
