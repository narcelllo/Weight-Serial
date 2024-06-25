import serial
import os

FILE = r'dados.txt'
CONFIGPORT = r'./config_logger/config_port.txt'
CONFIGDIRECTORY = r'./config_logger/config_directory.txt'
CONFIGBAUNDRATE = r'./config_logger/config_baundrate.txt'

with open(CONFIGDIRECTORY, 'r') as file:
    weightfile= file.read()

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

with open(complete_file,  "w") as file: 
        file.write(normalized_data)

# normalize_data = str("".join(map(str, normalize_data))) transforma arrai em inteiro e converte em STR
