import time
from init import *

#get distance with ultrasonic module
def Distance():
    GPIO.output(TrigPin,GPIO.LOW)
    time.sleep(0.000002)
    GPIO.output(TrigPin,GPIO.HIGH)
    time.sleep(0.000015)
    GPIO.output(TrigPin,GPIO.LOW)

    t3 = time.time()

    while not GPIO.input(EchoPin):
        t4 = time.time()
        if (t4 - t3) > 0.03 :
            return -1


    t1 = time.time()
    while GPIO.input(EchoPin):
        t5 = time.time()
        if(t5 - t1) > 0.03 :
            return -1

    t2 = time.time()
    time.sleep(0.01)
    return ((t2 - t1)* 340 / 2) * 100

#get averages of distance based on ultrasonic execution
def get_distance():
    num = 0
    ultrasonic = []
    while num < 5:
            distance = Distance()
            while int(distance) == -1 :
                distance = Distance()
            while (int(distance) >= 500 or int(distance) == 0) :
                distance = Distance()
            ultrasonic.append(distance)
            num = num + 1
            time.sleep(0.01)
    
    distance = (ultrasonic[1] + ultrasonic[2] + ultrasonic[3])/3
    print("distance is %f"%(distance) ) 
    return distance

#detect object in path
def objectAlongPath():
    distance = get_distance()
    if distance < 20:
        return True
    else:
        return False

#detect object collision via IR sensor
def IR_detect(GPIO, IRSensorLeft, IRSensorRight):
    leftIR = GPIO.input(IRSensorLeft)
    rightIR = GPIO.input(IRSensorRight)
    if(leftIR == False or rightIR == False):
        return True
    else:
        return False