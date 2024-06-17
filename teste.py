import serial
import csv
 
ser = serial.Serial('COM3', 9600)
arquivo = open('dados.csv', 'w')
escritor = csv.writer(arquivo)


while ser.inWaiting() > 0:
    linha = ser.readline()
    print("LINHA!!!", linha)
    escritor.writerow(linha)
    print("escreveu!!!!!")
 
ser.close()
arquivo.close()
