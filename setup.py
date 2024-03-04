import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["tkinter", "PIL"], "excludes": []}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="TemporizadorMVP",
    version="1.0",
    description="Descripción de tu aplicación",
    options={"build_exe": build_exe_options},
    executables=[Executable("Ro.py", base=base)]
)
