#define trigPin 10  // Trig pin sensörün trig pinine bağlı
#define echoPin 9  // Echo pin sensörün echo pinine bağlı

void setup() {
  Serial.begin(9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop() {
  long duration, distance;
  
  // Trig pinini düşük yapın ve 2 mikrosaniye bekleyin
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  
  // Trig pini yüksek yapın ve 10 mikrosaniye bekleyin
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  // Echo pininden gelen süreyi ölçün
  duration = pulseIn(echoPin, HIGH);
  
  // Mesafeyi hesaplayın (ses hızı yaklaşık 343 m/s veya 0.0343 cm/mikrosaniye)
  distance = (duration / 2) * 0.0343;
  
  // Mesafeyi seri monitöre yazdırın

  Serial.println(distance);

  
  delay(200);  // 1 saniye bekle
}
