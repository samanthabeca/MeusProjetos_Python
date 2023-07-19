void setup()
{
  pinMode(10, OUTPUT);
  Serial.begin(115200);
}

void loop() {
  int intervalo_pisca;
  intervalo_pisca=4000;
  digitalWrite(10, LOW);
  Serial.write('0');
  delay(intervalo_pisca);
  digitalWrite(10, HIGH);
  Serial.write('1');
  delay(intervalo_pisca);
}