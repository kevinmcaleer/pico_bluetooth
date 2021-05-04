from machine import UART, Pin 
from time import sleep

# uos provides information such as the machine name and build version numbers
import uos

# setup the UART
id = 0
rx = Pin(1)
tx = Pin(0)
baudrate=9600

# create the UART
uart = UART(id=id, baudrate=baudrate,tx=tx, rx=rx)

def help():
    print("AT commands")
    print("-"*50)
    print("AT               - Attention, should return 'OK'")
    print("AT+ORGL          - restore default settings")
    print("AT+VERSION       - returns the verison number")
    print("AT+UART?         ")
    print("AT+PSWD?         ")
    print("AT+NAME?         - print out the current bluetooth device name")
    print("AT+NAME<name>    - set the name of the device, e.g. AT+NAMERobot will set it to 'Robot'")
    print("AT+PIN<pin>      - will set the pin e.g. 'AT+PIN4321' will set the pin to '4321'")



# Print a pretty command line
print("-"*50)
print("PicoTerm")
print(uos.uname())
print("type 'quit' to exit, or help for commands")
# Loop
command = ""
while True and command !='quit':
    # Write our command prompt
    command = input("PicoTerm>")
    if command == 'help':
        help()
    elif command != 'quit':
        uart.write(command)
        print(command)
        sleep(0.1)
        response = bytes()
        
        if uart.any() > 0:
            response = uart.readline()
            print("reading data")
        output = "".join(["'",str(command),"'","response:",str(response.decode('utf-8'))])
        print(output)
    elif command == 'quit':
        print("-"*50)
        print('Bye.')