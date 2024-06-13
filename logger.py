import serial
import numpy

#WEIGHTFILE = "C:\DEV\weight\dados.txt"

def read_serial_data(port='COM3', baundrate=9600):
    data = ''

    serialPort = serial.Serial(port, baundrate)
    serialPort.flushInput()

    byte = serialPort.read(11)
    if byte:
        data += byte.decode('utf-8',errors='ignore')

             

    serialPort.flushInput()          
    serialPort.close()

    return data


#data = read_serial_data()
data = "   f  0050340"

data_array = data.split()

data_array = [char for item in data_array for char in item]

type_data_array = []

for item in data_array:
    try:
        type_data_array.append(int(item))
    except ValueError:
        #read_serial_data()
        print('Ler novamente')
        break

data_int = int("".join(map(str,type_data_array)))

print(data_int)

'''
loop = 0
teste = [].
while loop <= 7:
    for item in type_data_array:
        if isinstance(item,int):
            teste.append(item)
            loop =+ 1
        else:
            
            break

print(teste)
'''
'''
with open(WEIGHTFILE, 'w') as file:
    file.write(data)
'''