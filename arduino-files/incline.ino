/* Board's Configuration */
#define minimalDistance 100
#define firstSensor 8
#define secondSensor 7

/* Launching settings and uncertainty configuration */
#define LAUNCHES 5
#define UNCERTAINTY 0.01

/* Defining LauncherCounter and dinamically allocate memory to record all launchers */
int launcherCounter = 0;
float *measurements = (float*) malloc(LAUNCHES * sizeof(float));

/* Pin and serial configuration */
void setup() {
  pinMode(firstSensor, INPUT);
  pinMode(secondSensor, INPUT);
  Serial.begin(9600);
}

/* Main function */
void loop() {
  // set the variables to save the time when the sphere is at the top
  // and when the shpere is at the bottom.
  long top = 0;
  long bottom = 0;
  
  // Capture all the movements
  while(true){
    // Look to see if sphere is on the top or at the bottom
    bool on_top = analogRead(firstSensor) < minimalDistance && analogRead(secondSensor) > minimalDistance;
    bool on_bottom = analogRead(firstSensor) > minimalDistance && analogRead(secondSensor) < minimalDistance;
    
    if(on_top){
      top = millis();
    } else if (on_bottom){
      bottom = millis();
    }

    // Checking the measurement condition and save the result.
    if(top != 0 and bottom != 0 and bottom > top){
      float measurement = (float)(bottom - top)/1000;
      measurements[launcherCounter] = measurement;
      print_attempts(measurement);
      break;
    }
  }

  // Computing the stop condition.
  if(launcherCounter < LAUNCHES - 1){
    launcherCounter++;
  } else {
    calculate_mean();
    free(measurements);
    exit;
  }
}

/* Function to calculate mean and the total uncertainty */
void calculate_mean(){
  // Defining the variable to store the mean
  // and the square of the standart deviation 
  float mean = 0;
  float squaredSD = 0; 
  
  // Loop over all the measurements made to calculate the mean 
  for (int i = 0; i < LAUNCHES; i++){
    mean += measurements[i] / (float) LAUNCHES;
  }

  // Loop over all values again to calculate the total uncertainty
  for (int i = 0; i < LAUNCHES; i++){
    squaredSD += pow(measurements[i] - mean, 2) / (float) pow(LAUNCHES, 2);
  }
  float totalUncertainty = sqrt(squaredSD + pow(UNCERTAINTY, 2));

  // Print out the mean and the total uncertainty
  Serial.print("\nMean: ");
  Serial.print(mean);
  Serial.print(" +- ");
  Serial.print(totalUncertainty);
  Serial.print(" s.");
}

/* Function to print the measurements made */ 
void print_attempts(float measurement){
  Serial.print("Attempt ");
  Serial.print(launcherCounter + 1);
  Serial.print(": ");
  Serial.print(measurement);
  Serial.println(" s");
}
