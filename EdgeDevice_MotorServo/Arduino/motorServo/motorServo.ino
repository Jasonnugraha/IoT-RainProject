#include <Servo.h>
#define servoPin 7
#define LED_PIN 8

int i = 0;
int j = 0;
int k = 0;
Servo servo_3;

unsigned long previousMs = 0;
const long servoInterval = 50;
const long interval = 1000;

char serialListener;
bool shadeOut = true;

void setup()
{
    Serial.begin(9600);
    servo_3.attach(servoPin);
    servo_3.write(0);
    pinMode(LED_PIN, OUTPUT);
}

void loop()
{
    unsigned long currentMs = millis();

    if (currentMs - previousMs >= interval)
    {

        Serial.flush();
        serialListener = Serial.read();
        // serial listener to send the command to the arudino
        if (serialListener == 'L')
        {
            // NOT RAIN
            if (shadeOut == true)
            {
                for (k = 120; k >= 0; k -= 1)
                {
                    if (currentMs - previousMs >= servoInterval)
                    {
                        servo_3.write(k);
                        //delay(50); // Wait for 50 millisecond(s)
                    }
                    else
                    {
                        k++;
                    }
                }
                shadeOut = false;
            }
            digitalWrite(LED_PIN, LOW);
        }
        if (serialListener == 'H')
        {
            // RAIN
            if (shadeOut == false)
            {
                for (i = 0; i <= 120; i += 1)
                {
                    if (currentMs - previousMs >= servoInterval)
                    {
                        servo_3.write(i);
                    }
                    else
                    {
                        i--;
                    }

                    //delay(50); // Wait for 50 millisecond(s)
                }
                shadeOut = true;
            }
        }
        if (serialListener == 'X')
        {
            // RAIN
            if (shadeOut == false)
            {
                for (i = 0; i <= 120; i += 1)
                {
                    if (currentMs - previousMs >= servoInterval)
                    {
                        servo_3.write(i);
                    }
                    else
                    {
                        i--;
                    }

                    //delay(50); // Wait for 50 millisecond(s)
                }
                shadeOut = true;
            }
        }

        if (serialListener == 'B')
        {
            digitalWrite(LED_PIN, HIGH);
            if (shadeOut == true)
            {
                for (k = 120; k >= 0; k -= 1)
                {
                    if (currentMs - previousMs >= servoInterval)
                    {
                        servo_3.write(k);
                        //delay(50); // Wait for 50 millisecond(s)
                    }
                    else
                    {
                        k++;
                    }
                }
                shadeOut = false;
            }
        }
        else if (serialListener == 'X')
        {
            digitalWrite(LED_PIN, HIGH);
        }
        else
        {
            digitalWrite(LED_PIN, LOW);
        }
        //delay(1000);
        previousMs = currentMs;
    }
}
