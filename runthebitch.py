import time
import pigpio

PW_SPEED = 1200
PW_TIMEOUT = 10

print("Starting pigpio connection")
pi = pigpio.pi()

if not pi.connected:
	print("pigpio not connected...")
	exit()

print("Setting servo pw to 1000")
pi.set_servo_pulsewidth(4, 1000)
pi.set_servo_pulsewidth(18,1000)

time.sleep(1)

print("Setting servo pw to SPEED")
pi.set_servo_pulsewidth(4, PW_SPEED)
pi.set_servo_pulsewidth(18,PW_SPEED)

time.sleep(PW_TIMEOUT)

pi.set_servo_pulsewidth(4, 1000)
pi.set_servo_pulsewidth(18,1000)

print("Stopping pigpio connection")
pi.stop()
