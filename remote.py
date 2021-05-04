from time import sleep

from machine import Pin, UART

# setup the UART
id = 0
rx = Pin(1)
tx = Pin(0)
baudrate=9600

# create the UART
uart = UART(id=id, baudrate=baudrate,tx=tx, rx=rx)

up = Pin(13, Pin.IN, Pin.PULL_UP)
down = Pin(10, Pin.IN, Pin.PULL_UP)
left = Pin(12, Pin.IN, Pin.PULL_UP)
right = Pin(11, Pin.IN, Pin.PULL_UP)
button_a = Pin(15, Pin.IN, Pin.PULL_UP)
button_b = Pin(14, Pin.IN, Pin.PULL_UP)
print("Remote Control active")
print("-"*50)

# Loop
command = ""
   


while True:
    response = bytes()
    if uart.any() > 0:
        while uart.any() > 0:
            # response += uart.read(1)
            response = uart.readline()
            print(response)
        output = "".join(["'",str(command),"'","response:",str(response.decode('utf-8'))])
        print(output)
    if up.value()==0:
        print("up")
        uart.write("up\n\r")
        sleep(0.01)
    if down.value()==0:
        print("down")
        uart.write("down\n\r")
        sleep(0.01)
    if left.value()==0:
        print('left')
        uart.write("left\n\r")
        sleep(0.01)
    if right.value()==0:
        print("right")
        uart.write("right\n\r")
        sleep(0.01)
    if button_a.value()==0:
        print("button_a")
        uart.write("button_a\n\r")
        sleep(0.01)
    if button_b.value()==0:
        print("button b")
        uart.write("button_b\n\r")
        sleep(0.01)
    sleep(0.1)
