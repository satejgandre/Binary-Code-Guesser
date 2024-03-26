from machine import Pin
from utime import sleep
from random import randint
btn_fours = Pin(0, Pin.IN, Pin.PULL_UP); btn_twos = Pin(1, Pin.IN, Pin.PULL_UP); btn_ones = Pin(2, Pin.IN, Pin.PULL_UP); submit = Pin(3, Pin.IN, Pin.PULL_UP); led_fours = Pin(4, Pin.OUT); led_twos = Pin(5, Pin.OUT); led_ones = Pin(6, Pin.OUT); red = Pin(7, Pin.OUT); white = Pin(8, Pin.OUT); number = randint(0,7)
while 1:
    sleep(0.1)
    if btn_fours.value() == 0:
        led_fours.toggle()
        while btn_fours.value() == 0: pass
    elif btn_twos.value() == 0:
        led_twos.toggle()
        while btn_twos.value() == 0: pass
    elif btn_ones.value() == 0:
        led_ones.toggle()
        while btn_ones.value() == 0: pass
    elif submit.value() == 0:
        guess = 4*led_fours.value() + 2*led_twos.value() + led_ones.value()
        if guess == number: white.value(1); sleep(1); machine.reset()
        else: red.value(1); sleep(1); red.value(0)