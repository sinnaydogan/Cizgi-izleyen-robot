import RPi.GPIO as IO
import time
IO.setwarnings(False)
IO.setmode(IO.BCM)

IO.setup(14,IO.IN) #GPIO 14 -> Sol sensor
IO.setup(15,IO.IN) #GPIO 15 -> Sag sensor

IO.setup(4,IO.OUT) #GPIO 4 -> Motor 1 
IO.setup(3,IO.OUT) #GPIO 3 -> Motor 2

while 1:

 

    if(IO.input(14)==0 and IO.input(15)==0): #forward- duz gidiyor     
        IO.output(4,True) #1+
        IO.output(3,True) #2+
	    
        print ("duz gidiyor...")
    
    elif(IO.input(14)==0 and IO.input(15)==1): #turn right-saga gidiyor  
        IO.output(4,True) #1+
        IO.output(3,False) #2-
	   
        print ("saga gidiyor...")

    elif(IO.input(14)==1 and IO.input(15)==0): #turn left - sola gidiyor
        IO.output(4,False) #1-
        IO.output(3,True) #2+
	   
        print ("sola donuyor...")

    else:  #durma islemi
        IO.output(4,False) #1A+
        IO.output(3,False) #1B-
        
        print ("duruyor...")
