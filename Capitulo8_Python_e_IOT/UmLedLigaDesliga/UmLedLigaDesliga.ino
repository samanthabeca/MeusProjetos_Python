void setup() {
  // put your setup code here, to run once:
  pinMode(10, OUTPUT);
  Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
  int valor_recebido;
  if (Serial.available()){
    valor_recebido = Serial.read();
    if (valor_recebido == '0'){
      digitalWrite(10, LOW);
    } else {
      digitalWrite(10, HIGH);
    }
  }
}
