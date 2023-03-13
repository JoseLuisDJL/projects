import sys
import os
from cx_Freeze import setup,Executable

file = ['icons_rc.py']

exe = Executable(script="main.py",base="Win32GUI")

setup(
    name="PSUTIL",
    version="1.0",
    description="Application that monitoring our OS",
    author="DebuggerJL",
    options={'build_exe':{'include_files':file}},
    executables = [exe]
)
