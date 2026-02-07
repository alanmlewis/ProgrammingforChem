int pin = A0;

void setup() {
  pinMode(pin, INPUT);
  Serial.begin(9600);
}

void loop() {
  Serial.print(analogRead(pin));
  Serial.print('\n');
}