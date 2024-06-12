import serial

'''
WEIGHTFILE = "C:\DEV\weight\dados.txt"

serialPort = serial.Serial('com3', 9600)
serialPort.flushInput()

data = ''

byte = serialPort.read(11)
if byte:
    data += byte.decode('utf-8',errors='ignore')         

serialPort.flushInput()          
serialPort.close()
print(data)
'''
data = "0006460007/06/202415:4932    0006460007/06/202415:4932    0006460007/06/202415:4932    0006460007/06/202415:4932"

data_array = data.split()

data_array = [char for item in data_array for char in item]
#print(data_array)

type_data_array = []

for item in data_array:
    try:
        type_data_array.append(int(item))
    except ValueError:
        type_data_array.append(item)

type_data_array = [type(item) for item in type_data_array]

#print(type_data_array)
limit = 0
while limit <= 7:
    for item in type_data_array:
        if item == int:
            print(item)
            limit += 1
            print(limit)
        else:
            print("fim")



'''
with open(WEIGHTFILE, 'w') as file:
    file.write(data)
'''
