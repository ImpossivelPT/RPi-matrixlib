#include <wiringPi.h>

// HT1632C PINs

int DISPLAY_CS    = 17;
int DISPLAY_WR    = 27;
int DISPLAY_DATA  = 22;

// All PINs are output
  pinMode(DISPLAY_CS, OUTPUT);
  pinMode(DISPLAY_WR, OUTPUT);
  pinMode(DISPLAY_DATA, OUTPUT);
  

  
  // FG SY SEN 100 0000 0001 -------------------------------------------------------------
  digitalWrite(DISPLAY_CS, LOW);
  
  digitalWrite(DISPLAY_WR, LOW);    //abre
  digitalWrite(DISPLAY_DATA, HIGH);  // 1
  digitalWrite(DISPLAY_WR, HIGH);   //fecha
  
  digitalWrite(DISPLAY_WR, LOW);    //abre
  digitalWrite(DISPLAY_DATA, LOW);  // 0
  digitalWrite(DISPLAY_WR, HIGH);   //fecha
  
  digitalWrite(DISPLAY_WR, LOW);    //abre
  digitalWrite(DISPLAY_DATA, LOW);  // 0
  digitalWrite(DISPLAY_WR, HIGH);   //fecha
  
  // --
  
  digitalWrite(DISPLAY_WR, LOW);    //abre
  digitalWrite(DISPLAY_DATA, LOW);  // 0
  digitalWrite(DISPLAY_WR, HIGH);   //fecha
  
  digitalWrite(DISPLAY_WR, LOW);    //abre
  digitalWrite(DISPLAY_DATA, LOW);  // 0
  digitalWrite(DISPLAY_WR, HIGH);   //fecha
  
  digitalWrite(DISPLAY_WR, LOW);    //abre
  digitalWrite(DISPLAY_DATA, LOW);  // 0
  digitalWrite(DISPLAY_WR, HIGH);   //fecha
  
  digitalWrite(DISPLAY_WR, LOW);    //abre
  digitalWrite(DISPLAY_DATA, LOW);  // 0
  digitalWrite(DISPLAY_WR, HIGH);   //fecha
  
  digitalWrite(DISPLAY_WR, LOW);    //abre
  digitalWrite(DISPLAY_DATA, LOW);  // 0
  digitalWrite(DISPLAY_WR, HIGH);   //fecha
  
  digitalWrite(DISPLAY_WR, LOW);    //abre
  digitalWrite(DISPLAY_DATA, LOW);  // 0
  digitalWrite(DISPLAY_WR, HIGH);   //fecha
  
  digitalWrite(DISPLAY_WR, LOW);    //abre
  digitalWrite(DISPLAY_DATA, LOW);  // 0
  digitalWrite(DISPLAY_WR, HIGH);   //fecha
  
  digitalWrite(DISPLAY_WR, LOW);    //abre
  digitalWrite(DISPLAY_DATA, HIGH);  // 1
  digitalWrite(DISPLAY_WR, HIGH);   //fecha
  
  digitalWrite(DISPLAY_WR, LOW);    //abre
  digitalWrite(DISPLAY_DATA, LOW);  // 0
  digitalWrite(DISPLAY_WR, HIGH);   //fecha
  
  digitalWrite(DISPLAY_WR, LOW);    //abre
  digitalWrite(DISPLAY_DATA, LOW);  // 0
  digitalWrite(DISPLAY_WR, HIGH);   //fecha
  
  digitalWrite(DISPLAY_CS, HIGH);
  
  
  //FG LED ON 100 0000 0011 ------------------------------------------------------------
  
  digitalWrite(DISPLAY_CS, LOW);
  
  digitalWrite(DISPLAY_WR, LOW);    //abre
  digitalWrite(DISPLAY_DATA, HIGH);  // 1
  digitalWrite(DISPLAY_WR, HIGH);   //fecha
  
  digitalWrite(DISPLAY_WR, LOW);    //abre
  digitalWrite(DISPLAY_DATA, LOW);  // 0
  digitalWrite(DISPLAY_WR, HIGH);   //fecha
  
  digitalWrite(DISPLAY_WR, LOW);    //abre
  digitalWrite(DISPLAY_DATA, LOW);  // 0
  digitalWrite(DISPLAY_WR, HIGH);   //fecha
  
  // --
  
  digitalWrite(DISPLAY_WR, LOW);    //abre
  digitalWrite(DISPLAY_DATA, LOW);  // 0
  digitalWrite(DISPLAY_WR, HIGH);   //fecha
  
  digitalWrite(DISPLAY_WR, LOW);    //abre
  digitalWrite(DISPLAY_DATA, LOW);  // 0
  digitalWrite(DISPLAY_WR, HIGH);   //fecha
  
  digitalWrite(DISPLAY_WR, LOW);    //abre
  digitalWrite(DISPLAY_DATA, LOW);  // 0
  digitalWrite(DISPLAY_WR, HIGH);   //fecha
  
  digitalWrite(DISPLAY_WR, LOW);    //abre
  digitalWrite(DISPLAY_DATA, LOW);  // 0
  digitalWrite(DISPLAY_WR, HIGH);   //fecha
  
  digitalWrite(DISPLAY_WR, LOW);    //abre
  digitalWrite(DISPLAY_DATA, LOW);  // 0
  digitalWrite(DISPLAY_WR, HIGH);   //fecha
  
  digitalWrite(DISPLAY_WR, LOW);    //abre
  digitalWrite(DISPLAY_DATA, LOW);  // 0
  digitalWrite(DISPLAY_WR, HIGH);   //fecha
  
  digitalWrite(DISPLAY_WR, LOW);    //abre
  digitalWrite(DISPLAY_DATA, HIGH);  // 1
  digitalWrite(DISPLAY_WR, HIGH);   //fecha
  
  digitalWrite(DISPLAY_WR, LOW);    //abre
  digitalWrite(DISPLAY_DATA, HIGH);  // 1
  digitalWrite(DISPLAY_WR, HIGH);   //fecha
  
  digitalWrite(DISPLAY_WR, LOW);    //abre
  digitalWrite(DISPLAY_DATA, LOW);  // 0
  digitalWrite(DISPLAY_WR, HIGH);   //fecha
  
  digitalWrite(DISPLAY_WR, LOW);    //abre
  digitalWrite(DISPLAY_DATA, LOW);  // 0
  digitalWrite(DISPLAY_WR, HIGH);   //fecha
  
  digitalWrite(DISPLAY_CS, HIGH);
  
}

void loop() {

  // select display
  digitalWrite(DISPLAY_CS, LOW);  
  
  //FG WRITE MODE 101 -----------------------------------------------------------------
  digitalWrite(DISPLAY_WR, LOW);    //abre
  digitalWrite(DISPLAY_DATA, HIGH);  //escreve
  digitalWrite(DISPLAY_WR, HIGH);   //fecha
  
  digitalWrite(DISPLAY_WR, LOW);    //abre
  digitalWrite(DISPLAY_DATA, LOW);  //escreve
  digitalWrite(DISPLAY_WR, HIGH);   //fecha
  
  digitalWrite(DISPLAY_WR, LOW);    //abre
  digitalWrite(DISPLAY_DATA, HIGH);  //escreve
  digitalWrite(DISPLAY_WR, HIGH);   //fecha
  
  //FG ADDRESS 0000000
  digitalWrite(DISPLAY_WR, LOW);    //abre
  digitalWrite(DISPLAY_DATA, LOW);  //escreve
  digitalWrite(DISPLAY_WR, HIGH);   //fecha
  
  digitalWrite(DISPLAY_WR, LOW);    //abre
  digitalWrite(DISPLAY_DATA, LOW);  //escreve
  digitalWrite(DISPLAY_WR, HIGH);   //fecha
  
  digitalWrite(DISPLAY_WR, LOW);    //abre
  digitalWrite(DISPLAY_DATA, LOW);  //escreve
  digitalWrite(DISPLAY_WR, HIGH);   //fecha
  
  digitalWrite(DISPLAY_WR, LOW);    //abre
  digitalWrite(DISPLAY_DATA, LOW);  //escreve
  digitalWrite(DISPLAY_WR, HIGH);   //fecha
  
  digitalWrite(DISPLAY_WR, LOW);    //abre
  digitalWrite(DISPLAY_DATA, LOW);  //escreve
  digitalWrite(DISPLAY_WR, HIGH);   //fecha
  
  digitalWrite(DISPLAY_WR, LOW);    //abre
  digitalWrite(DISPLAY_DATA, LOW);  //escreve
  digitalWrite(DISPLAY_WR, HIGH);   //fecha
  
  digitalWrite(DISPLAY_WR, LOW);    //abre
  digitalWrite(DISPLAY_DATA, LOW);  //escreve
  digitalWrite(DISPLAY_WR, HIGH);   //fecha
  
  
  
  //FG LED 0001
  digitalWrite(DISPLAY_WR, LOW);    //abre
  digitalWrite(DISPLAY_DATA, HIGH);  //escreve
  digitalWrite(DISPLAY_WR, HIGH);   //fecha
  
  digitalWrite(DISPLAY_WR, LOW);    //abre
  digitalWrite(DISPLAY_DATA, HIGH);  //escreve
  digitalWrite(DISPLAY_WR, HIGH);   //fecha
  
  digitalWrite(DISPLAY_WR, LOW);    //abre
  digitalWrite(DISPLAY_DATA, HIGH);  //escreve
  digitalWrite(DISPLAY_WR, HIGH);   //fecha
  
  digitalWrite(DISPLAY_WR, LOW);    //abre
  digitalWrite(DISPLAY_DATA, HIGH);  //escreve
  digitalWrite(DISPLAY_WR, HIGH);   //fecha
  
  
  
  // unselect display
  digitalWrite(DISPLAY_CS, HIGH);  
  
  delay(100);
}