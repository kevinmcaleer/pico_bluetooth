from machine import UART, Pin 
from time import sleep

# uos provides information such as the machine name and build version numbers
import uos

# setup the UART
id = 1
rx = Pin(5)
tx = Pin(4)
baudrate=9600 # default is 9600

# create the UART
uart = UART(id=id, baudrate=baudrate,tx=tx, rx=rx)

while True:
    if uart.any() > 0:
        try:
            print(uart.readline())
        except:
            print("Something weird happened")
    sleep(1)
    uart.write("test from remote")