from __future__ import division
import time
import RPi.GPIO as GPIO


# Import the PCA9685 module.
import Adafruit_PCA9685
#from ultrasonic import distance
#mport sensor module



# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
servo_min = 500  # Min pulse length out of 4096
servo_max = 900  # Max pulse length out of 4096

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 101      # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(101)

print('Moving servo on channel 0, press Ctrl-C to quit...')

def initializer(ini):
    pwm.set_pwm(0, 0, 700)
    time.sleep(tf)

def foward():
	#foward above 700 
	#backward below 650
    # Move servo on channel O between extremes.
    pwm.set_pwm(0, 0, 755)
    time.sleep(.45)
    pwm.set_pwm(0, 0, 700)
    time.sleep(.45)
    
  
  
        
def backward():
    pwm.set_pwm(0, 0, 700)
    time.sleep(1)
    pwm.set_pwm(0, 0, 644)
    time.sleep(.45)
    pwm.set_pwm(0, 0, 700)
    time.sleep(.45)
    
def stop():
    pwm.set_pwm(0, 0, 700)
    time.sleep(.2)
##    time.sleep(.00002)
##    pwm.set_pwm(0, 0, 700)
##    time.sleep(.00002)    
         
def turnRight(tf):
    
    pwm.set_pwm(3, 0, 900)
    time.sleep(2)
    #pwm.set_pwm(3, 0, 700)
    #time.sleep(2)
    

def turnLeft(tf):
    pwm.set_pwm(3, 0, 500)
    time.sleep(2) 
    #pwm.set_pwm(3, 0, 700)
    #time.sleep(2)

def demo():
    pwm.set_pwm(0, 0, 700)
    time.sleep(1)
    pwm.set_pwm(0, 0, 500)
    time.sleep(1)
    pwm.set_pwm(0, 0, 700)
    time.sleep(1)
    pwm.set_pwm(0, 0, 650)
    time.sleep(3)
    pwm.set_pwm(0, 0, 700)
    time.sleep(1)
    pwm.set_pwm(0, 0, 650)
    time.sleep(3)
    pwm.set_pwm(0, 0, 700)
    time.sleep(1)
    pwm.set_pwm(0, 0, 750)
    time.sleep(3)
    pwm.set_pwm(0, 0, 700)
    time.sleep(1)
    

def disint():
    GPIO.setmode(GPIO.BCM)

    TRIG = 18
    ECHO = 17
    TRIG1 = 23
    ECHO1 = 22
    TRIG2 = 25
    ECHO2 = 24

    print "Distance measurement in progress"

    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    GPIO.setup(TRIG1,GPIO.OUT)
    GPIO.setup(ECHO1,GPIO.IN)
    GPIO.setup(TRIG2,GPIO.OUT)
    GPIO.setup(ECHO2,GPIO.IN)


    
    GPIO.output(TRIG,False)
    print "Waiting for sensor to settle"
    time.sleep(0.2)

    GPIO.output(TRIG1,False)
    print "Waiting for sensor to settle"
    time.sleep(0.2)

    GPIO.output(TRIG2,False)
    print "Waiting for sensor to settle"
    time.sleep(0.2)

def distance():
    GPIO.setmode(GPIO.BCM)

    TRIG = 18
    ECHO = 17

##    print "Distance measurement in progress"
##
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
##
##
##    
##    GPIO.output(TRIG,False)
##    print "Waiting for sensor to settle"
##    time.sleep(.00000002)

    while True:
            
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)


        while GPIO.input(ECHO) == 0:
            pulse_start = time.time()

        while GPIO.input(ECHO) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance.dis = pulse_duration * 17150

        distance.dis = round(distance.dis, 2)
        


        #print "Distance:", distance, "cm"
        return distance.dis
        GPIO.cleanup()

def distance1():
    GPIO.setmode(GPIO.BCM)

    TRIG1 = 23
    ECHO1 = 22

##    print "Distance measurement in progress"
##
    GPIO.setup(TRIG1,GPIO.OUT)
    GPIO.setup(ECHO1,GPIO.IN)
##
##
##    
##    GPIO.output(TRIG,False)
##    print "Waiting for sensor to settle"
##    time.sleep(.00000002)

    while True:
            
        GPIO.output(TRIG1, True)
        time.sleep(0.00001)
        GPIO.output(TRIG1, False)


        while GPIO.input(ECHO1) == 0:
            pulse_start = time.time()

        while GPIO.input(ECHO1) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance.dis1 = pulse_duration * 17150

        distance.dis1 = round(distance.dis1, 2)
        


        #print "Distance:", distance, "cm"
        return distance.dis1
        GPIO.cleanup()


def distance2():
    GPIO.setmode(GPIO.BCM)

    TRIG2 = 25
    ECHO2 = 24

##    print "Distance measurement in progress"
##
    GPIO.setup(TRIG2,GPIO.OUT)
    GPIO.setup(ECHO2,GPIO.IN)
##
##
##    
##    GPIO.output(TRIG,False)
##    print "Waiting for sensor to settle"
##    time.sleep(.00000002)

    while True:
            
        GPIO.output(TRIG2, True)
        time.sleep(0.00001)
        GPIO.output(TRIG2, False)


        while GPIO.input(ECHO2) == 0:
            pulse_start = time.time()

        while GPIO.input(ECHO2) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance.dis2 = pulse_duration * 17150

        distance.dis2 = round(distance.dis2, 2)
        


        #print "Distance:", distance, "cm"
        return distance.dis2
        GPIO.cleanup()



def autonomy():
    pwm.set_pwm(3, 0, 900)   #turning right of front wheels
    time.sleep(1)
    pwm.set_pwm(0, 0, 670)   #initializer
    time.sleep(1)
    pwm.set_pwm(0, 0, 700)   #initializers
    time.sleep(1)
    pwm.set_pwm(0, 0, 648)   #moving backward
    time.sleep(1.7)
    pwm.set_pwm(0, 0, 700)   
    time.sleep(1)
    pwm.set_pwm(3, 0, 500)    #turning front wheels left
    time.sleep(1)
    
    for x in range(0,13):
        distance()
        distance1()
        distance2()
        dist = distance.dis
        dist1 = distance.dis1
        dist2 = distance.dis2
        #choosing smallest distance
        if (dist < dist1):
            small = dist
        else:
            small = dist1
           
        print "curdis is", dist
        print "curdis1 is", dist1
        print "front distance is",dist2

        
        
        if(small > 11):
            backward()
          
        else:
            pwm.set_pwm(0, 0, 700)  #stop
            time.sleep(1)
            pwm.set_pwm(3, 0, 900)  #turning right of front wheels
            time.sleep(1)
            foward()
            pwm.set_pwm(3, 0, 675)  #initializes/centers front wheels
            time.sleep(1)
            if(dist2 > 10):
                foward()
                if(dist2 <= 10):
                    pwm.set_pwm(0, 0, 700)
                    time.sleep(1)

        
        
        
##        if dist2 > 10: #back sensors
##            foward(0.5)
##            
##        else:
##            stop()
                

       

        #else:
##            stop()
##            pwm.set_pwm(3, 0, 675)
##            time.sleep(1)
##            foward(1)
##            pwm.set_pwm(3, 0, 900)
##            time.sleep(1)
##            foward(1)
            

    


        
#distance()
disint()
autonomy()


