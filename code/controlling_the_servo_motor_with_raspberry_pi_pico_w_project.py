import machine
from time import sleep as s
servopin = 15
potpin = 26
pot = machine.ADC(machine.Pin(potpin))
servo = machine.PWM(machine.Pin(servopin))
servo.freq(50)
 
while True:
    potval = pot.read_u16()
    print(potval)
    s(.5)
    angle = (180/65535)*potval
    writeval = 6553/180 * angle + 1638
    servo.duty_u16(int(writeval))
