import RPi.GPIO as GPIO
import time

#set GPIO port mode to BCM
GPIO.setmode(GPIO.BCM)

#escape warnings
GPIO.setwarnings(False)


#define pins
#Motor
IN1 = 20
IN2 = 21
IN3 = 19
IN4 = 26
ENA = 16
ENB = 13
#start button
key = 8
#ultrasonic module
EchoPin = 0
TrigPin = 1
#infrared module
IRSensorLeft = 12
IRSensorRight = 17
#servo for Ultrasonic Sensor
ServoPin = 23
#Global Vars
orientation = 1 # 1 y+, 2 x-, 3 y-, 4 x+
#initialize servo
GPIO.setup(ServoPin, GPIO.OUT)
pwm_servo = GPIO.PWM(ServoPin, 50)
pwm_servo.start(0)
#TrackSensorLeftPin1 TrackSensorLeftPin2 TrackSensorRightPin1 TrackSensorRightPin2
TrackSensorLeftPin1  =  3  
TrackSensorLeftPin2  =  5   
TrackSensorRightPin1 =  4   
TrackSensorRightPin2 =  18
#Set PWM
GPIO.setup(ENA,GPIO.OUT,initial=GPIO.HIGH)
GPIO.setup(ENB,GPIO.OUT,initial=GPIO.HIGH)
pwm_ENA = GPIO.PWM(ENA, 2000)
pwm_ENB = GPIO.PWM(ENB, 2000)


def init():
    GPIO.setup(IN1,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(IN2,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(IN3,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(IN4,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(key,GPIO.IN)
    GPIO.setup(EchoPin,GPIO.IN)
    GPIO.setup(TrigPin,GPIO.OUT)
    GPIO.setup(IRSensorLeft, GPIO.IN)
    GPIO.setup(IRSensorRight, GPIO.IN)
    GPIO.setup(TrackSensorLeftPin1,GPIO.IN)
    GPIO.setup(TrackSensorLeftPin2,GPIO.IN)
    GPIO.setup(TrackSensorRightPin1,GPIO.IN)
    GPIO.setup(TrackSensorRightPin2,GPIO.IN)
    #Set the PWM pin and frequency to 2000hz
    pwm_ENA.start(0)
    pwm_ENB.start(0)
    