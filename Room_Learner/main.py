import time

import init
from drive import run, back, brake
from distance import objectAlongPath, IR_detect
from coordinate_writer import write_room_data
from coordinate_reader import create_model, predict_model
from hit_protocol import hit_protocol

# global coordinate vars
x_cord = 0
y_cord = 0

# create model
model, hit_data = create_model()

#DRIVER
time.sleep(2)

try:
    init.init()
    init.TrackSensorLeftValue1 = init.GPIO.input(init.TrackSensorLeftPin1)
    init.TrackSensorLeftValue2 = init.GPIO.input(init.TrackSensorLeftPin2)
    init.TrackSensorRightValue1 = init.GPIO.input(init.TrackSensorRightPin1)
    init.TrackSensorRightValue2 = init.GPIO.input(init.TrackSensorRightPin2)
    
    if init.TrackSensorLeftValue1 == True and init.TrackSensorLeftValue2 == True and init.TrackSensorRightValue1 == True and init.TrackSensorRightValue2 == True:
        print("Starting line detected")

    while True:
        run(15,15)
        time.sleep(1)
        y_cord = y_cord + 1
        if(predict_model(model,[x_cord,y_cord+1],hit_data) == ['yes']):
            brake()
            time.sleep(1)
            x_cord, y_cord = hit_protocol(x_cord, y_cord)
        elif(IR_detect(init.GPIO,init.IRSensorLeft,init.IRSensorRight) == True):
            write_room_data([[x_cord, y_cord,"yes"]])
            back(10,10)
            time.sleep(1)
            x_cord, y_cord = hit_protocol(x_cord, y_cord)
        else:
            write_room_data([[x_cord, y_cord,"no"]])

    brake()
    time.sleep(1)
    print("Done")  
except KeyboardInterrupt:
    pass

init.pwm_ENA.stop()
init.pwm_ENB.stop()
init.GPIO.cleanup()