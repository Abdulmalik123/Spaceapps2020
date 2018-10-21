
//convert into lig3ht intensity

int lightSensor =  A0;
  int * Array = new int();
 volatile int  Change1 = 0;
 volatile int  Change2= 0;
  bool Change1Read =   true; // we want to compare two different changes
void setup() {
  // put your setup code here, to run once:
  pinMode(A0,INPUT);
  Serial.begin(9600);
}
// 
void loop() {

  // put your main code here, to run repeatedly:
    for(int i = 0;  i < 25; i++){
       Array[i] =  analogRead(lightSensor); // get the values       
        delay(1000);//we do this to 5 seconds 
       if( i != 0){
       if( Change1Read == true){
        
        Change1 =    Array[i] - Array[i-1];//  The change 
        if(Change1 <0){ Change1 =  Change1 *-1;}
        Change1Read = false;
       }
       else{
           Change2  =    Array[i] - Array[i-1];
           Change1Read = true; //
            if(Change2   < 0){  Change2  = Change2 *-1;}
            else{};//Absolute value
         if((Change2 *.4)> Change1){ // so if the change by point 4 is 
         
              Array[i] = map(Array[i], 0,1023 , 0 ,5000) ; // get  raw dat wich will be millivolts
             Serial.println(Array[i]);
           }
           else{
            Serial.print("");
            };
        }
      }
   }
     
   delay(100);
}
