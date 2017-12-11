int potPin = 2;

int mid1 = 0;

int durchlaufe = 100;

double maxVal = 600;

double minVal = 300;



void setup() {

  Serial.begin(9600);

  Serial.println("Hi");

}



void loop() {

                                             //0%   300

 /* mid1 = 0;                                 25%   520

  for(int i = 0; i < durchlaufe; i++) {       50%   550

    mid1 += getVal();                         75%   560

    delay(1);                                 100%  570

  }

  mid1 = mid1 / durchlaufe;*/

  Serial.println(getVal());

  delay(10);

  //mid1 = mid1 * 0.95 + (double) val * 0.05;

}



int getVal() {

  int val = analogRead(potPin);

  int orig = val;

  if(val > maxVal) {

    val = maxVal;

  } else if(val < minVal) {

    val = minVal;

  }



  val = (val - minVal) / ((maxVal - minVal) / 100);

  return orig;

}
