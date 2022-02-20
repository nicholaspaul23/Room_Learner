import time
from init import *
from drive import *
from distance import *
from coordinate_writer import write_room_data
from coordinate_reader import create_model, predict_model

'''
    The hit protocol will rotate the robot left and drive it along side the object to see how long it is
    once it has reached the end of the object it will record the data then turn to go around object back to original path
    if it meets an object in its path along the way it will run this protocol recursively unitl it is back on its path
'''

def hit_protocol(x_cord, y_cord):
    # create model
    model, hit_data = create_model()
    spin_left(15,15)
    time.sleep(2.2)
    brake()
    time.sleep(1)
    GPIO.output(ServoPin, True)
    pwm_servo.ChangeDutyCycle(10 / 18 + 2)
    time.sleep(1)
    GPIO.output(ServoPin, False)
    pwm_servo.ChangeDutyCycle(0)
    global orientation
    orientation = 1 if orientation == 4 else orientation + 1
    run(15,15)
    time.sleep(1)
    while objectAlongPath():
        if (orientation % 2 == 0):
            x_cord = x_cord - 1 if orientation == 2 else x_cord + 1
            write_room_data([[x_cord, y_cord,"yes"]])
        else:
            if(orientation == 3):
                y_cord = y_cord - 1
                write_room_data([[x_cord-1, y_cord,"yes"]]) #x_cord decr to account for the object bein on its side
            else:
                y_cord = y_cord + 1
                write_room_data([[x_cord+1, y_cord,"yes"]])
        #check for objects in path
        if(predict_model(model,[x_cord,y_cord+1],hit_data) == ['yes']):
            brake()
            time.sleep(1)
            x_cord, y_cord = hit_protocol(x_cord, y_cord)
        elif(IR_detect(GPIO,IRSensorLeft,IRSensorRight) == True):
            write_room_data([[x_cord, y_cord,"yes"]])
            back(10,10)
            time.sleep(1)
            x_cord, y_cord = hit_protocol(x_cord, y_cord)
        run(15,15)
        time.sleep(1)
       
    x_cord, y_cord = back_on_path(x_cord, y_cord)
    return x_cord, y_cord

def back_on_path(x_cord, y_cord):
    global orientation
    if (orientation % 2 == 0):
        x_cord = x_cord - 1 if orientation == 2 else x_cord + 1
    else:
        y_cord = y_cord - 1 if orientation == 3 else y_cord + 1
    write_room_data([[x_cord, y_cord,"no"]])
    spin_right(15,15)
    time.sleep(1.7)
    brake()
    time.sleep(1)
    GPIO.output(ServoPin, True)
    pwm_servo.ChangeDutyCycle(95 / 18 + 2)
    time.sleep(1)
    GPIO.output(ServoPin, False)
    pwm_servo.ChangeDutyCycle(0)
    orientation = orientation - 1
    return x_cord, y_cord