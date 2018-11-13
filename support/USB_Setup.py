#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.18
#  in conjunction with Tcl version 8.6
#    Nov 01, 2018 07:04:31 PM EDT  platform: Windows NT

import sys
from tkinter import messagebox

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

from support import USB_Setup_support
import GUITest_Support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    USB_Setup_support.set_Tk_var()
    top = Toplevel1 (root)
    USB_Setup_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    USB_Setup_support.set_Tk_var()
    top = Toplevel1 (w)
    USB_Setup_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("221x196+431+147")
        top.title("USB COM Port")
        top.configure(background="#d9d9d9")

        self.MainFrame = tk.Frame(top)
        self.MainFrame.place(relx=0.045, rely=0.102, relheight=0.842
                , relwidth=0.882)
        self.MainFrame.configure(relief='groove')
        self.MainFrame.configure(borderwidth="2")
        self.MainFrame.configure(relief='groove')
        self.MainFrame.configure(background="#d9d9d9")
        self.MainFrame.configure(width=195)

        self.ApplyButton = tk.Button(self.MainFrame)
        self.ApplyButton.place(relx=0.359, rely=0.727, height=24, width=57)
        self.ApplyButton.configure(activebackground="#d9d9d9")
        self.ApplyButton.configure(activeforeground="#000000")
        self.ApplyButton.configure(background="#d9d9d9")
        self.ApplyButton.configure(disabledforeground="#a3a3a3")
        self.ApplyButton.configure(foreground="#000000")
        self.ApplyButton.configure(highlightbackground="#d9d9d9")
        self.ApplyButton.configure(highlightcolor="black")
        self.ApplyButton.configure(pady="0")
        self.ApplyButton.configure(text='''Save''')
        self.ApplyButton.configure(width=57)
        self.ApplyButton.configure(command= self.save_var)

        self.Label1 = tk.Label(self.MainFrame)
        self.Label1.place(relx=0.103, rely=0.242, height=21, width=28)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Port''')

        self.Label2 = tk.Label(self.MainFrame)
        self.Label2.place(relx=0.103, rely=0.424, height=21, width=53)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Baudrate''')

        self.Portbox1 = ttk.Combobox(self.MainFrame)
        self.Portbox1.place(relx=0.462, rely=0.242, relheight=0.127
                , relwidth=0.426)
        self.value_list = ['COM1','COM2','COM3','COM4','COM5','COM6','COM7','COM8','COM9','COM10','COM11','COM12','COM13','COM14','COM15','COM16','COM17','COM18','COM19','COM20',]
        self.Portbox1.configure(values=self.value_list)
        self.Portbox1.configure(textvariable=USB_Setup_support.portbox)
        self.Portbox1.configure(width=83)
        self.Portbox1.configure(takefocus="")
        self.Portbox1.set(GUITest_Support.comport)

        self.Baudbox2 = ttk.Combobox(self.MainFrame)
        self.Baudbox2.place(relx=0.462, rely=0.424, relheight=0.127
                , relwidth=0.426)
        self.value_list = [300,1200,2400,4800,9600,19200,38400,57600,74880,115200,230400,]
        self.Baudbox2.configure(values=self.value_list)
        self.Baudbox2.configure(textvariable=USB_Setup_support.baudbox)
        self.Baudbox2.configure(width=83)
        self.Baudbox2.configure(takefocus="")
        self.Baudbox2.set(GUITest_Support.baudrate)

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.09, rely=0.051, height=21, width=48)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Settings''')

    def save_var(self):
        try:
            GUITest_Support.set_baudrate(self.Baudbox2.get())
            GUITest_Support.set_COM(self.Portbox1.get())
            USB_Setup_support.destroy_window()
            messagebox.showinfo('COM Setup', 'Setting Applied')
        except:
            messagebox.showerror('Error', 'Wrong Input Parameter')




if __name__ == '__main__':
    vp_start_gui()





