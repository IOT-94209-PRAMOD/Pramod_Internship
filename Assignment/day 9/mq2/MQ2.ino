#define MQ2_PIN 34     
#define LED_PIN 2      

void setup() {
  Serial.begin(9600);
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  int gasValue = analogRead(MQ2_PIN);

  Serial.print("Gas Value: ");
  Serial.println(gasValue);

  // Threshold check
  if (gasValue > 2000) {
    Serial.println("⚠ GAS / SMOKE DETECTED!");
    digitalWrite(LED_PIN, HIGH);
  } else {
    digitalWrite(LED_PIN, LOW);
  }

  delay(1000);
}

