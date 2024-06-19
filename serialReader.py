import serial

with open('config_directory.txt', 'r') as file:
    WEIGHTFILE = file.read()
print('Aquiiiii!!!!!! _____------',WEIGHTFILE)

def read_serial_data():
    data = ''
    with open('config_port.txt', 'r') as file:
        port = file.read()

    with open('config_baundrate.txt', 'r') as file:
        baundrate = int(file.read())

    serialPort = serial.Serial(port, baundrate)
    serialPort.flushInput()

    byte = serialPort.read(11)
    if byte:
        data += byte.decode('utf-8')
        
    print(data)

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

    return normalize_data [0]

# apenas para teste
#fdata = '    0058560018/06/202415:043F    0058560018/06/202415:043F    0058560018/06/202415:043F    0058560018/06/202415:043F    0058560018/06/202415:043F    '
#print(normalize_data(fdata))

normalized_data = str(normalize_data(read_serial_data()))

with open(WEIGHTFILE, 'w') as file:
    file.write(normalized_data)

# normalize_data = str("".join(map(str, normalize_data))) transforma arrai em inteiro e converte em STR
