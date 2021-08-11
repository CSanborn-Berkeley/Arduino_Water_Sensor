void setup() {
  // put your setup code here, to run once:
  pinMode(LED_BUILTIN,OUTPUT);
  pinMode(2,INPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:

  if(digitalRead(2) == LOW){
    Serial.write("Water");
  }
  else{
    Serial.write("Dry");
  }
  delay(1000);
}
