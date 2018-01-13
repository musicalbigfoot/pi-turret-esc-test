#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import pigpio

flywheelMotorA = 4
flywheelMotorB = 18

actionLedPin = 27
triggerServo = 23

servoSleepTime = 0.65

firing = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(actionLedPin, GPIO.OUT)

def isFiring():
	print('Checking for fireAction')
	return firing

def servoAction(count, triggerServo):
	triggerCount = 1

	# Light the LED to indicate the program is ready
	print("Trigger: " + str(count))

	triggerPi = pigpio.pi()
	if not triggerPi.connected:
		print("triggerPi not connected...")
		exit()

	while triggerCount <= count:
		triggerPi.set_servo_pulsewidth(triggerServo, 2500);
		time.sleep(servoSleepTime)
		triggerPi.set_servo_pulsewidth(triggerServo, 500);
		time.sleep(servoSleepTime)

		triggerCount = triggerCount + 1

	triggerPi.stop()

def flywheelAction(speed, shots):
	print("flywheelAction :: start function")
	firing = True

	flywheelPi = pigpio.pi()
	if not flywheelPi.connected:
		print("flywheelPi not connected...")
		exit()

	PW_SPEED = 1200
	if speed == 'mild':
		PW_SPEED = 1200
	elif speed == 'medium':
		PW_SPEED = 1300
	elif speed == 'hot':
		PW_SPEED = 1380

	shots = int(shots)
	if shots < 1:
		shots = 1
	elif shots > 18:
		shots = 1

	GPIO.output(actionLedPin, True)

	flywheelPi.set_servo_pulsewidth(flywheelMotorA, 1000)
	flywheelPi.set_servo_pulsewidth(flywheelMotorB, 1000)
	time.sleep(1);

	# print("Starting the motors...")
	flywheelPi.set_servo_pulsewidth(flywheelMotorA, PW_SPEED)
	flywheelPi.set_servo_pulsewidth(flywheelMotorB, PW_SPEED)

	time.sleep(1)
	# print("Triggering the trigger X times")
	servoAction(shots, triggerServo)

	time.sleep(1);

	# print("killing the motors, flywheelAction done")
	flywheelPi.set_servo_pulsewidth(flywheelMotorA, 1000)
	flywheelPi.set_servo_pulsewidth(flywheelMotorB, 1000)

	GPIO.output(actionLedPin, False)

	firing = False

def fireTest():
	print("fireTest trigger...")
	flywheelAction(3);