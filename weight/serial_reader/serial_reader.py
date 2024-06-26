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
    weightfile= file.read()

weightfile += FILE

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

    return data

def normalize_data(data):
    normalize_data = []

    limits = data.split('    ')

    for limit in limits:
        if limit:
            data_limit = limit.strip()
            if len(data_limit) >= 7:
                collect_data = data_limit[:7]
                try:
                    int_data = int(collect_data)
                    normalize_data.append(int(int_data))
                except ValueError:
                    continue

    return normalize_data [3]

# apenas para teste
#fdata = '    0058560018/06/202415:043F    0058560018/06/202415:043F    0058560018/06/202415:043F    0058560018/06/202415:043F    0058560018/06/202415:043F    '
#print(normalize_data(fdata))

data = read_serial_data()

normalized_data = str(normalize_data(data))

with open(weightfile,  "w") as file: 
        file.write(normalized_data)

# normalize_data = str("".join(map(str, normalize_data))) transforma arrai em inteiro e converte em STR
