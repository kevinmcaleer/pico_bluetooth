from machine import UART, Pin 
from time import sleep, ticks_ms
import uos

id = 0
rx = Pin(1)
tx = Pin(0)
baudrate=9600
bits=8
parity=None
stop=1

uart = UART(id=id, baudrate=baudrate, bits=bits, parity=parity, stop=stop,tx=tx, rx=rx)

print(uos.uname())

def send_command_wait_response(cmd, uart=uart, timeout=1000):
    print("CMD:" + cmd)
    uart.write(cmd)
    wait_response(uart, timeout)

def wait_response(uart, timeout=1000):
    previous_millis = ticks_ms()
    response = b""
    while (ticks_ms() - previous_millis) < timeout:
        if uart.any():
            response = b"".join([response, uart.read(1)])
    print(response)


led_onboard = Pin(25, Pin.OUT)
led_onboard.value(0)
sleep(0.5)
led_onboard.value(1)
sleep(1)
led_onboard.value(0)

while True:
    print("waiting for data")
    print("-"*50)
    while uart.any():
        data_input = uart.read()
        data_output = uart.write("Got: ", data_input)
        print(data_input)