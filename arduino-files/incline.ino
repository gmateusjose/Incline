// Variables for measurement of distance
int sensor_distance = 100;
int count = 1;

void setup() {
  pinMode(8, INPUT);
  pinMode(7, INPUT);
  Serial.begin(9600);
}

void loop() {
  long top = 0;
  long bottom = 0;
  
  // Capture all the movements
  while(true){
    // Look to see if sphere is on the top or at the bottom
    bool on_top = analogRead(7) < sensor_distance && analogRead(8) > sensor_distance;
    bool on_bottom = analogRead(7) > sensor_distance && analogRead(8) < sensor_distance;
    
    if(on_top){
      top = millis();
    } else if (on_bottom){
      bottom = millis();
    }

    // Checking the stop condition and print the results 
    if(top != 0 and bottom != 0 and bottom > top){
      Serial.print("Attempt ");
      Serial.print(count);
      Serial.print(": ");
      Serial.print(1.0*(bottom - top)/1000);
      Serial.println(" s");
      break;
    }
  }
  count++;
}
