#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import pigpio

flywheelMotorA = 4
flywheelMotorB = 18

actionLedPin = 27
triggerServo = 23

servoSleepTime = 0.65

GPIO.setmode(GPIO.BCM)
GPIO.setup(actionLedPin, GPIO.OUT)

def servoAction(count, triggerServo):
	triggerCount = 1

	# Light the LED to indicate the program is ready

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

def flywheelAction(shots):
	flywheelPi = pigpio.pi()
	if not flywheelPi.connected:
		print("flywheelPi not connected...")
		exit()

	PW_SPEED = 1200

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

def init():
	print("Init the servo!")

def fire():
	# Fire away, captain!
	print("Firing the cannon!")
	flywheelAction(3);


# flywheelAction()
# servoAction(3, triggerServo)