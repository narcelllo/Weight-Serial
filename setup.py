import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "includes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for
# a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="",
    version="0.1",
    description="",
    options={"build_exe": build_exe_options},
    executables=[Executable("config_logger\configLogger.py", base=base)]
    #executables=[Executable("serial_reader\serialReader.py", base=base)]
    #executables=[Executable("logger\logger.py", base=base)]
)