import re
from tkinter import Tk, ttk, Label, Button, filedialog
import serial, serial.tools.list_ports as SerialPortsLister

def listSerialPorts():
    ports = SerialPortsLister.comports()
    return [port.device for port in ports]

def saveConfiguration():
    CONFIGURATIONCOM = ".\config_port.txt"
    CONFIGURATIONCOMBAUNDRATE = ".\config_baundrate.txt"
    
    com = ttkSerialComboBox.get()
    rate = ttkLabelSerialBaundComboBox.get()

    with open(CONFIGURATIONCOM,  "w") as file: 
        file.write(com)

    with open(CONFIGURATIONCOMBAUNDRATE,  "w") as file: 
        file.write(rate)
    
    
    canvas.destroy() 

    canvasCallBack = Tk()
    canvasCallBack.title("Serial configuration")
    canvasCallBack.geometry("250x150")

    ttkLabelSerialComboBox = Label(canvasCallBack, text = f"{com} Successful configuration.")
    ttkOkButton = Button(canvasCallBack, text = "    Ok    ", command = canvasCallBack.destroy)
    ttkLabelCentralize = Label(canvasCallBack, text = "              ")
    ttkLabelSerialComboBox.grid(column = 1, row = 1)
    ttkLabelCentralize.grid(column = 0, row = 0)
    ttkOkButton.grid(column = 1, row = 2)

    canvasCallBack.mainloop()

serialPorts = listSerialPorts()
serialRate = ["300", "1200", "2400", "4800", "9600"]

canvas = Tk()
canvas.title("Serial configuration")
canvas.geometry("300x200")

ttkLabelSerialComboBox = Label(canvas, text = "COM")
ttkLabelSerialBaundComboBox = Label(canvas, text = "Velocidade")

ttkLabelCentralize = Label(canvas, text = "              ")
ttkLabelSerialComboBox.grid(column = 1, row = 3)
ttkLabelSerialBaundComboBox.grid(column = 1, row = 4)
ttkLabelCentralize.grid(column = 0, row = 0)

# Values for testing
#serialPorts = ["COM1", "COM2", "COM3", "COM4", "COM5", "COM6"]

ttkSerialComboBox = ttk.Combobox(canvas, values = serialPorts)
ttkSerialComboBox.set("Disconnected")
ttkLabelSerialBaundComboBox = ttk.Combobox(canvas, values = serialRate)
ttkCancelButton = Button(canvas, text = " Cancel ", command = canvas.destroy) 

ttkSerialComboBox.grid(column = 2, row = 3)
ttkLabelSerialBaundComboBox.grid(column = 2, row = 4)
ttkCancelButton.grid(column = 2, row = 5, padx = 5, pady = 5)

if serialPorts and serialRate:
    ttkSerialComboBox.set("--")
    ttkLabelSerialBaundComboBox.set("--")
    ttkSaveButton = Button(canvas, text = "   Save   ", command = saveConfiguration)  
    ttkSaveButton.grid(column = 2, row = 6, padx = 5, pady = 5)

canvas.mainloop()
