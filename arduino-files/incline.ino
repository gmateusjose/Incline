// Variable to configure the sensibility
int sensor_distance = 100;
int uncertainty = 0.01;

// Settings for counting the movements and calculating the mean
int count = 0;
int total_movements = 50;
float sum = 0;

// Dinamically allocate memory to store the time measurements
float *measurements = (float*)malloc(total_movements * sizeof(float));

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
    bool on_top = analogRead(8) < sensor_distance && analogRead(7) > sensor_distance;
    bool on_bottom = analogRead(8) > sensor_distance && analogRead(7) < sensor_distance;
    
    if(on_top){
      top = millis();
    } else if (on_bottom){
      bottom = millis();
    }

    // Checking the stop condition compute the results
    // and then print the results 
    if(top != 0 and bottom != 0 and bottom > top){
      // Calculating the time duration and storing all the values
      float time_duration = (float)(bottom - top)/1000;
      measurements[count] = time_duration;
      sum += time_duration;
      
      Serial.print("Attempt ");
      Serial.print(count + 1);
      Serial.print(": ");
      Serial.print(time_duration);
      Serial.println(" s");
      break;
    }
  }
  if(count < total_movements - 1){
    // increase the movements counting
    count++;
  } else {
    // Calculate the mean and finish the execution
    float mean = sum / (float)total_movements;
    Serial.print("\nMean: ");
    Serial.print(mean);
    Serial.print(" +- ");

    // Calculating the total_uncertainty
    float new_sum = 0;
    for(int i = 0; i < total_movements; i++){
      new_sum += pow(measurements[i] - mean, 2);
    }
    float dp_squared = new_sum / (float)pow(total_movements, 2);
    float total_uncertainty = sqrt(dp_squared + pow(uncertainty, 2));

    // Displaying the total uncertainty
    Serial.print(total_uncertainty);
    Serial.println(" s");

    // Freeing up the memory and exiting
    free(measurements);
    exit;
  }
}
