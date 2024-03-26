from machine import Pin
from utime import sleep
from random import randint
btn_fours = Pin(0, Pin.IN, Pin.PULL_UP); btn_twos = Pin(1, Pin.IN, Pin.PULL_UP); btn_ones = Pin(2, Pin.IN, Pin.PULL_UP); submit = Pin(3, Pin.IN, Pin.PULL_UP); led_fours = Pin(4, Pin.OUT); led_twos = Pin(5, Pin.OUT); led_ones = Pin(6, Pin.OUT); red = Pin(7, Pin.OUT); white = Pin(8, Pin.OUT)
def main(): #Main code
    number = randint(0,7) #Pick a random number from 0 to 7
    print(number) #For debug purposes
    while 1: #Forever
        sleep(0.1) #Clock speed 10 Hertz
        if btn_fours.value() == 0: #If leftmost button pressed
            led_fours.toggle() #Toggle leftmost blue LED
            while btn_fours.value() == 0: pass #Wait until button is released
        elif btn_twos.value() == 0: #If middle blue button is pressed
            led_twos.toggle() #Toggle middle blue LED
            while btn_twos.value() == 0: pass #Wait unitl button is released
        elif btn_ones.value() == 0: #If rightmost blue button pressed
            led_ones.toggle() #Toggle rightmost blue LED
            while btn_ones.value() == 0: pass #Wait unitl button is released
        elif submit.value() == 0: #If green button pressed
            guess = 4*led_fours.value() + 2*led_twos.value() + led_ones.value() #Convert binary to int
            if guess == number: white.value(1); sleep(1); white.value(0); led_fours.value(0); led_twos.value(0); led_ones.value(0); main() #If user's guess is equal to number then flash white LED and reset system
            else: red.value(1); sleep(1); red.value(0) #If not, flash red LED and repeat
main() #Initiate main function
