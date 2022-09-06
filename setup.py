# coding=utf8
#launch from cmd: python setup.py build
     
from cx_Freeze import setup, Executable

target = Executable(
    script="mac_converter.py",
    #base="Win32GUI",
    icon="logo.ico"
    )

setup(
    name="MAC CONVERTER",
    version="0.1",
    description="Put : points in MAC Address",
    author="Xosé Brais Noya García",
    executables=[target]
    )