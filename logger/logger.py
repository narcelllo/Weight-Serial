import serial
import os

FILE = r'dados.txt'
CONFIGPORT = r'./config_logger/config_port.txt'
CONFIGDIRECTORY = r'./config_logger/config_directory.txt'
CONFIGBAUNDRATE = r'./config_logger/config_baundrate.txt'

with open(CONFIGDIRECTORY, 'r') as file:
    weightfile = file.read()

complete_file = os.path.join(weightfile, FILE)

def read_serial_data():
    data = ''
    
    with open(CONFIGPORT, 'r') as file:
        port = file.read()

    with open(CONFIGBAUNDRATE, 'r') as file:
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

with open(complete_file,  "w") as file: 
        file.write(str_logger)
