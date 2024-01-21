import RPi.GPIO as GPIO

# Define pin numbers for motor control
motor_a1 = 12
motor_a2 = 13
motor_b1 = 16
motor_b2 = 18

# Set up GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(motor_a1, GPIO.OUT)
GPIO.setup(motor_a2, GPIO.OUT)
GPIO.setup(motor_b1, GPIO.OUT)
GPIO.setup(motor_b2, GPIO.OUT)

# Forward
def forward():
    GPIO.output(motor_a1, GPIO.HIGH)
    GPIO.output(motor_a2, GPIO.LOW)
    GPIO.output(motor_b1, GPIO.HIGH)
    GPIO.output(motor_b2, GPIO.LOW)

# Backward
def backward():
    GPIO.output(motor_a1, GPIO.LOW)
    GPIO.output(motor_a2, GPIO.HIGH)
    GPIO.output(motor_b1, GPIO.LOW)
    GPIO.output(motor_b2, GPIO.HIGH)

# Stop
def stop():
    GPIO.output(motor_a1, GPIO.LOW)
    GPIO.output(motor_a2, GPIO.LOW)
    GPIO.output(motor_b1, GPIO.LOW)
    GPIO.output(motor_b2, GPIO.LOW)

# Implement control logic based on user input from motion remote/interface

# Example: Move forward on button press
if button_pressed:
    forward()

# Clean up GPIO on exit
GPIO.cleanup()
