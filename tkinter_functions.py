from PIL import Image
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import webbrowser
import threading
from tkinter import ttk

logo_img='./img/logo.ico'

def get_filepathload_multiple():
    import tkinter as tk
    from tkinter import filedialog
    root = Tk()
    root.iconbitmap(logo_img)
    root.withdraw()
    filez=root.filename = filedialog.askopenfilenames(initialdir="/", title="Select files",
                                               filetypes=(("excel files", "*.xlsx"), ("all files", "*.*")),defaultextension=".xlsx")
    lst = list(filez)
    root.destroy()
    #return list with path of files to load!
    return lst

def get_filepathload_single():
    import tkinter as tk
    from tkinter import filedialog
    root = Tk()
    root.iconbitmap(logo_img)
    root.withdraw()
    filez=root.filename = filedialog.askopenfilename(initialdir="/", title="Select files",
                                               filetypes=(("excel files", "*.xlsx"), ("all files", "*.*")),defaultextension=".xlsx")
    lst = str(filez)
    root.destroy()
    #return string
    return lst

def get_filepathload_single_text():
    import tkinter as tk
    from tkinter import filedialog
    root = Tk()
    root.iconbitmap(logo_img)
    root.withdraw()
    filez=root.filename = filedialog.askopenfilename(initialdir="/", title="Select files",
                                               filetypes=(("excel files", "*.csv"), ("excel files", "*.txt"),  ("all files", "*.*")),defaultextension=".txt")
    lst = str(filez)
    root.destroy()
    #return string
    return lst