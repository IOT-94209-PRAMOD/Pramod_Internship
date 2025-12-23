void setup() {
  // put your setup code here, to run once:
    Serial.begin(115200);
    serial.println("UART SETUP is done")
    
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println("Hello ESP32");
  delay(1000);
}
