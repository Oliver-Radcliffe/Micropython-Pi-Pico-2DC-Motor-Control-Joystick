import machine
import utime

# The following code has been used to interface a Raspberry Pi Pico with and L298N DC Motor Driver Module and an anlogue joystick.
# On the L298N leave the enable jumper pins in place. The motors are controlled via PWM to IN pins on the L298N.

frequency = 1500 # Global motor PWM frequency. Change this and see how it effects the motor operation.

# Motor 1 setup

joystick1 = machine.ADC(26) # Connect pin 26 on the Pi Pico to VRX on a Dual-Axis Joystick Module
pwm1 = machine.PWM(machine.Pin(14)) # Setup pin 14 to output PWM, connect to IN1 on L298N
pwm1.freq(frequency)
pwm2 = machine.PWM(machine.Pin(15)) # Setup pin 15 to output PWM, connect to IN2 on L298N
pwm2.freq(frequency)

# Motor 2 setup

joystick2 = machine.ADC(27) # Connect pin 27 on the Pi Pico to VRY on a Dual-Axis Joystick Module
pwm3 = machine.PWM(machine.Pin(16)) # Setup pin 16 to output PWM, connect to IN3 on L298N
pwm3.freq(frequency)
pwm4 = machine.PWM(machine.Pin(17)) # Setup pin 17 to output PWM, connect to IN4 on L298N
pwm4.freq(frequency)


# Loop to read in joystick value and change motor direction based on joystick position

while True:
    motor_control = joystick1.read_u16()
    
    if motor_control > 32900:
        pwm1.duty_u16(0)
        pwm2.duty_u16((motor_control - 32768) * 2)
        print("Motor 1 Forwards - ADC Value =", (motor_control - 32768) * 2)

    elif (motor_control < 32100):
        pwm1.duty_u16((32768 - motor_control) * 2)
        pwm2.duty_u16(0)
        print("Motor 1 Backwards - ADC Value =", 32768 - motor_control)
        
    else:
        pwm1.duty_u16(0)
        pwm2.duty_u16(0)
        print("Motor 1 stopped")
    
    motor_control = joystick2.read_u16()
    
    if motor_control > 33000:
        pwm3.duty_u16(0)
        pwm4.duty_u16((motor_control - 32768) * 2)
        print("Motor 2 Forwards - ADC Value =", (motor_control - 32768) * 2)

    elif (motor_control < 32000):
        pwm3.duty_u16((32768 - motor_control) * 2)
        pwm4.duty_u16(0)
        print("Motor 2 Backwards - ADC Value =", 32768 - motor_control)
        
    else:
        pwm3.duty_u16(0)
        pwm4.duty_u16(0)
        print("Motor 2 stopped")
        
    utime.sleep(0.1)
    


