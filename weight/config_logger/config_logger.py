import os
import sys
from tkinter import Tk, ttk, Label, Button, filedialog
import serial.tools.list_ports as SerialPortsLister

current_directory = os.path.dirname(os.path.abspath(sys.executable if hasattr(sys, 'frozen') else __file__))

parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
config_port = os.path.join(parent_directory, "config_port.txt")
config_baudrate = os.path.join(parent_directory, "config_baudrate.txt")
config_directory = os.path.join(parent_directory, "config_directory.txt")

def listSerialPorts():
    ports = SerialPortsLister.comports()
    return [port.device for port in ports]

def selectDirectory():
    selectDirectory = filedialog.askdirectory()

    if selectDirectory:
        ttkLabelDiretorio.config(text=f"Diretório selecionado: {selectDirectory}", wraplength=canvasLimit - 120, justify="left")

        with open(config_directory, "w") as file: 
            file.write(selectDirectory)
    else:
        ttkLabelDiretorio.config(text="Nenhum diretório selecionado.")



def saveConfiguration():
    com = ttkSerialComboBox.get()
    rate = ttkSerialBaundComboBox.get()

    with open(config_port, "w") as file: 
        file.write(com)

    with open(config_baudrate, "w") as file: 
        file.write(rate)

    canvas.destroy()

    canvasCallBack = Tk()
    canvasCallBack.title("Serial configuration")
    canvasCallBack.geometry("250x150")

    ttkLabelSerialComboBox = Label(canvasCallBack, text=f"{com} Successful configuration.")
    ttkLabelSerialComboBox.grid(column=1, row=1)

    ttkOkButton = Button(canvasCallBack, text="    Ok    ", command=canvasCallBack.destroy)
    ttkOkButton.grid(column=1, row=2)

    ttkLabelCentralize = Label(canvasCallBack, text="              ")
    ttkLabelCentralize.grid(column=0, row=0)

    canvasCallBack.mainloop()

serialPorts = listSerialPorts()



# Valores de teste para as portas seriais
#serialPorts = ["COM1", "COM2", "COM3", "COM4", "COM5", "COM6"]

canvas = Tk()
canvas.title("Serial configuration")
canvas.geometry("300x200")
canvasLimit = 300

ttkLabelCentralize = Label(canvas, text="              ")
ttkLabelCentralize.grid(column=0, row=0)

ttkLabelSerialComboBox = Label(canvas, text="COM")
ttkLabelSerialComboBox.grid(column=1, row=3)

ttkSerialComboBox = ttk.Combobox(canvas, values=serialPorts)
ttkSerialComboBox.set("COM Desconectada")
ttkSerialComboBox.grid(column=2, row=3)

ttkCancelButton = Button(canvas, text=" Cancel ", command=canvas.destroy)
ttkCancelButton.grid(column=2, row=7, padx=5, pady=5)

if serialPorts:
    canvas.geometry("380x250")
    serialRate = ["300", "1200", "2400", "4800", "9600"]
    ttkSerialComboBox.set("--")

    ttkSerialBaundComboBox = ttk.Combobox(canvas, values=serialRate)
    ttkSerialBaundComboBox.set("--")
    ttkSerialBaundComboBox.grid(column=2, row=4)

    ttkLabelSerialBaundComboBox = Label(canvas, text="Velocidade")
    ttkLabelSerialBaundComboBox.grid(column=1, row=4)

    ttkLabelDiretorio = Label(canvas, text="Nenhum diretório selecionado.")
    ttkLabelDiretorio.grid(column=2, row=5)

    ttkButtonDiretorio = Button(canvas, text="Escolha o Diretório", command=selectDirectory)
    ttkButtonDiretorio.grid(column=2, row=6)

    ttkSaveButton = Button(canvas, text="   Save   ", command=saveConfiguration)
    ttkSaveButton.grid(column=2, row=8, padx=5, pady=5)

canvas.mainloop()
