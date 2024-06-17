import serial
import csv

#WEIGHTFILE = "C:\DEV\weight\dados.txt"

def read_serial_data(port='COM3', baundrate=9600):
    data = ''
    normalize_data = []

    serialPort = serial.Serial(port, baundrate)
    serialPort.flushInput()

    byte = serialPort.read(11)
    if byte:
        data += byte.decode('utf-8',errors='ignore')

    for item in data:
        try:
            normalize_data.append(int(item))

        except ValueError:
            print('Ler novamente')             

    serialPort.flushInput()          
    serialPort.close()
    normalize_data = int("".join(map(str, normalize_data)))
    return normalize_data

read_serial_data()
print(read_serial_data(),"\n")

'''
with open(WEIGHTFILE, 'w') as file:
    file.write(data)
'''