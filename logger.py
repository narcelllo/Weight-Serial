import serial

WEIGHTFILE = '.\dados.txt'

def read_serial_data():
    data = ''

    with open('.\config_port.txt', 'r') as file:
        port = file.read()

    with open('.\config_baundrate.txt', 'r') as file:
        baundrate = int(file.read())

    serialPort = serial.Serial(port, baundrate)
    serialPort.flushInput()

    byte = serialPort.read(11)
    if byte:
        data += byte.decode('utf-8',errors='ignore')

    serialPort.flushInput()          
    serialPort.close()
    return data

def normalize_data(data):
    normalize_data = []
    for item in data:
        try:
            normalize_data.append(int(item))

        except ValueError:
            read_serial_data()

    normalize_data = str("".join(map(str, normalize_data)))
    return normalize_data

normalize_data_ = normalize_data(read_serial_data())
with open(WEIGHTFILE, 'w') as file:
    file.write(normalize_data_)