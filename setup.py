import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os", "serial", "sys"], "includes": ["tkinter", "serial.tools.list_ports"]}

# GUI applications require a different base on Windows (the default is for
# a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    #name="config_logger",
    #name="serial_reader",
    name="logger",
    version="0.1",
    description="",
    options={"build_exe": build_exe_options},
    #executables=[Executable("weight\config_logger\config_logger.py", base=base)]
    #executables=[Executable("weight\serial_reader\serial_reader.py", base=base)]
    executables=[Executable("weight\logger\logger.py", base=base)]
)