// Variable to configure the sensibility
int sensor_distance = 100; 

// Settings for counting the movements and calculating the mean
int count = 1;
int total_movements = 50;
float sum = 0;

void setup() {
  // pin configuration and serial configuration
  pinMode(8, INPUT);
  pinMode(7, INPUT);
  Serial.begin(9600);
}

void loop() {
  // set the variables to save the time when the sphere is at the top
  // and when the shpere is at the bottom.
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

    // Checking the stop condition compute the results
    // and then print the results 
    if(top != 0 and bottom != 0 and bottom > top){
      float time_duration = (float)(bottom - top)/1000;
      sum += time_duration;
      Serial.print("Attempt ");
      Serial.print(count);
      Serial.print(": ");
      Serial.print(time_duration);
      Serial.println(" s");
      break;
    }
  }
  if(count < total_movements){
    // increase the movements counting
    count++;
  } else {
    // Calculate the mean and finish the execution
    float mean = sum / (float)count;
    Serial.print("Mean: ");
    Serial.print(mean);
    Serial.println(" s");
    exit;
  }
}
