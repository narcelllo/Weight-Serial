import os
import sys
import serial

FILE = r'/dados.txt'

current_directory = os.path.dirname(os.path.abspath(sys.executable if hasattr(sys, 'frozen') else __file__))

parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
config_port = os.path.join(parent_directory, "config_port.txt")
config_baudrate = os.path.join(parent_directory, "config_baudrate.txt")
config_directory = os.path.join(parent_directory, "config_directory.txt")

with open(config_directory, 'r') as file:
    weightfile = file.read()

weightfile += FILE
str_logger = 'Deu certo!'
with open(weightfile,  "w") as file: 
        file.write(str_logger)

def read_serial_data():
    data = ''
    
    with open(config_port, 'r') as file:
        port = file.read()

    with open(config_baudrate, 'r') as file:
        baundrate = int(file.read())

    serialPort = serial.Serial(port, baundrate)
    serialPort.flushInput()

    byte = serialPort.read(254)
    if byte:
        data += byte.decode('utf-8')
        
    serialPort.flushInput()          
    serialPort.close()
    
    return data, serialPort

logger = read_serial_data()

str_logger = str(logger)

with open(weightfile,  "w") as file: 
        file.write(str_logger)
