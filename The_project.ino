


int lightSensor =  A0;
volatile int value =0;
void setup() {
  // put your setup code here, to run once:
  pinMode(A0,INPUT);
  Serial.begin(9600);
}
// 
void loop() {

  // put your main code here, to run repeatedly:
 
   value =  analogRead(lightSensor);
   value = map(value,0,1023,0,5000);
  Serial.println(value);
   delay(10000);
}
