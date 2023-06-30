from os import name
from time import sleep

if name == 'nt':
    import RPi_test.GPIO as GPIO
else:
    import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

pins=[i for i in range(1,41) if i not in [1,2,4,6,9,14,17,20,25,27,28,30,34,39]]
for i in pins:
        GPIO.setup(i, GPIO.OUT,initial=GPIO.HIGH)

while True:
    print('on')
    for i in pins:
        GPIO.output(i,1)
    sleep(1.5)
    print('off')
    for i in pins:
        GPIO.output(i,0)
    sleep(1.5)