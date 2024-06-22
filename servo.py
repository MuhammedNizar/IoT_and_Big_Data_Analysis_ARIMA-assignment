import RPi.GPIO as GPIO
import time

SERVO_PIN = 18

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

# Create a PWM instance
pwm = GPIO.PWM(SERVO_PIN, 50)  # 50 Hz frequency
pwm.start(0)  # Initial duty cycle

def set_angle(angle):
    if not 0 <= angle <= 180:
        raise ValueError("Angle must be between 0 and 180 degrees")
    
    # Convert the angle to duty cycle
    duty_cycle = 2 + (angle / 18)
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.5)
    pwm.ChangeDutyCycle(0)  # Turn off the pulse to prevent jitter

try:
    while True:
        # Example usage
        angle = int(input("Enter the angle (0 to 180): "))
        set_angle(angle)

except KeyboardInterrupt:
    print("Exiting program.")

finally:
    # Cleanup
    pwm.stop()
    GPIO.cleanup()

