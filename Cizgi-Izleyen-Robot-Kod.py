import RPi.GPIO as IO
import time
IO.setwarnings(False)
IO.setmode(IO.BCM)

IO.setup(14,IO.IN) #GPIO 2 -> Left IR out
IO.setup(15,IO.IN) #GPIO 3 -> Right IR out

IO.setup(4,IO.OUT) #GPIO 4 -> Motor 1 terminal A
IO.setup(3,IO.OUT) #GPIO 14 -> Motor 1 terminal B

while 1:

 

    if(IO.input(14)==0 and IO.input(15)==0): #both while move forward- duz gidiyor     
        IO.output(4,True) #1A+
        IO.output(3,True) #1B-
	    
        print ("duz gidiyor...")
    
    elif(IO.input(14)==0 and IO.input(15)==1): #turn right-saga gidiyor  
        IO.output(4,True) #1A+
        IO.output(3,False) #1B-
	   
        print ("saga gidiyor...")

    elif(IO.input(14)==1 and IO.input(15)==0): #turn left
        IO.output(4,False) #1A+
        IO.output(3,True) #1B-
	   
        print ("sola donuyor...")

    else:  #stay still
        IO.output(4,False) #1A+
        IO.output(3,False) #1B-
        
        print ("duruyor...")