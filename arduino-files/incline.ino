/* Board's Configuration */
#define firstSensor 53
#define secondSensor 52

/* Launching settings and uncertainty configuration */
#define LAUNCHES 50
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
    /*  Look to see if the sphere is at the top or at the bottom. Important:
     *   
     *  If the digitalRead() returns 1 -> there's nothing
     *  If the digitalRead() returns 0 -> there's something
     */
    bool on_top = digitalRead(firstSensor) == 0 && digitalRead(secondSensor) == 1;
    bool on_bottom = digitalRead(firstSensor) == 1 && digitalRead(secondSensor) == 0;
    
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
