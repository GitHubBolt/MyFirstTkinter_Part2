
import sys
import GUITest_Support
from tkinter import messagebox
from support import InfiniteTimer, USB_Setup, matplotlib_animated as display, matplotlib_animated as display2, \
    matplotlib_animated as display3, matplotlib_animated as display4, matplotlib_animated as display5, \
    matplotlib_animated as display6, matplotlib_animated as display7, matplotlib_animated
from tkinter import filedialog

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


class Toplevel1:
    def __init__(self, top):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#d9d9d9'  # X11 color: 'gray85'
        font10 = "-family {Courier New} -size 10 -weight normal -slant " \
                 "roman -underline 0 -overstrike 0"
        font17 = "-family {@Arial Unicode MS} -size 12 -weight bold -slant" \
                 " roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant roman " \
                "-underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=
        [('selected', _compcolor), ('active', _ana2color)])

        top.geometry("800x480")
        top.title("Julio's Arduino Terminal 2.0")
        top.configure(background="#d9d9d9")

        self.menubar = tk.Menu(top, font=font9, bg=_bgcolor, fg=_fgcolor)
        top.configure(menu=self.menubar)

        self.sub_menu = tk.Menu(top, tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu,
                                 activebackground="#d9d9d9",
                                 activeforeground="#000000",
                                 background="#d9d9d9",
                                 compound="left",
                                 font=font9,
                                 foreground="#000000",
                                 label="File")
        self.sub_menu.add_command(
            activebackground="#d8d8d8",
            activeforeground="#000000",
            background="#d9d9d9",
            compound="left",
            font=font9,
            foreground="#000000",
            label="Open Template", command=self.open_template)
        self.sub_menu.add_command(
            activebackground="#d8d8d8",
            activeforeground="#000000",
            background="#d9d9d9",
            compound="left",
            font=font9,
            foreground="#000000",
            label="Save Template", command=self.save_template)
        self.sub_menu.add_command(
            activebackground="#d8d8d8",
            activeforeground="#000000",
            background="#d9d9d9",
            compound="left",
            font=font9,
            foreground="#000000",
            label="Close", command= self.exit)
        self.sub_menu1 = tk.Menu(top, tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu1,
                                 activebackground="#d9d9d9",
                                 activeforeground="#000000",
                                 background="#d9d9d9",
                                 compound="left",
                                 font=font9,
                                 foreground="#000000",
                                 label="Option")
        self.sub_menu1.add_command(
            activebackground="#d8d8d8",
            activeforeground="#000000",
            background="#d9d9d9",
            compound="left",
            font=font9,
            foreground="#000000",
            label="COM Setup", command=self.usb_op)

        self.USBFrame = tk.Frame(top)
        self.USBFrame.place(relx=0.025, rely=0.042, relheight=0.177, relwidth=0.194)
        self.USBFrame.configure(relief='groove')
        self.USBFrame.configure(borderwidth="2")
        self.USBFrame.configure(relief='groove')
        self.USBFrame.configure(background="#d9d9d9")
        self.USBFrame.configure(width=155)

        self.ConnectButton = tk.Button(self.USBFrame)
        self.ConnectButton.place(relx=0.065, rely=0.588, height=24, width=64)
        self.ConnectButton.configure(activebackground="#d9d9d9")
        self.ConnectButton.configure(activeforeground="#000000")
        self.ConnectButton.configure(background="#d9d9d9")
        self.ConnectButton.configure(disabledforeground="#a3a3a3")
        self.ConnectButton.configure(foreground="#000000")
        self.ConnectButton.configure(highlightbackground="#d9d9d9")
        self.ConnectButton.configure(highlightcolor="black")
        self.ConnectButton.configure(pady="0")
        self.ConnectButton.configure(text='''Connect''')
        self.ConnectButton.configure(command=GUITest_Support.openusb)

        self.Button2 = tk.Button(self.USBFrame)
        self.Button2.place(relx=0.516, rely=0.588, height=24, width=66)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(state='disabled')
        self.Button2.configure(text='''Enable AQ''')
        self.Button2.configure(command=self.AQenable)

        self.Label2 = tk.Label(self.USBFrame)
        self.Label2.place(relx=0.065, rely=0.176, height=21, width=71)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Connection:''')

        self.Label3 = tk.Label(self.USBFrame)
        self.Label3.place(relx=0.645, rely=0.118, height=34, width=34)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.img1 = tk.PhotoImage(file="./images/red_led.png")
        self.img2 = tk.PhotoImage(file="./images/green_led.png")
        self.Label3.configure(image=self.img1)
        self.Label3.configure(text='''Label''')

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.038, rely=0.021, height=21, width=60)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''USB/Serial''')

        self.DataFrame = tk.Frame(top)
        self.DataFrame.place(relx=0.254, rely=0.042, relheight=0.177, relwidth=0.378)
        self.DataFrame.configure(relief='groove')
        self.DataFrame.configure(borderwidth="2")
        self.DataFrame.configure(relief='groove')
        self.DataFrame.configure(background="#d9d9d9")
        self.DataFrame.configure(width=155)

        self.OpenFileButton = tk.Button(self.DataFrame)
        self.OpenFileButton.place(relx=0.030, rely=0.588, height=24, width=64)
        self.OpenFileButton.configure(activebackground="#d9d9d9")
        self.OpenFileButton.configure(activeforeground="#000000")
        self.OpenFileButton.configure(background="#d9d9d9")
        self.OpenFileButton.configure(disabledforeground="#a3a3a3")
        self.OpenFileButton.configure(foreground="#000000")
        self.OpenFileButton.configure(highlightbackground="#d9d9d9")
        self.OpenFileButton.configure(highlightcolor="black")
        self.OpenFileButton.configure(pady="0")
        self.OpenFileButton.configure(text='''Open File''')
        self.OpenFileButton.configure(command=self.open_file)

        self.NewFileButton = tk.Button(self.DataFrame)
        self.NewFileButton.place(relx=0.270, rely=0.588, height=24, width=64)
        self.NewFileButton.configure(activebackground="#d9d9d9")
        self.NewFileButton.configure(activeforeground="#000000")
        self.NewFileButton.configure(background="#d9d9d9")
        self.NewFileButton.configure(disabledforeground="#a3a3a3")
        self.NewFileButton.configure(foreground="#000000")
        self.NewFileButton.configure(highlightbackground="#d9d9d9")
        self.NewFileButton.configure(highlightcolor="black")
        self.NewFileButton.configure(pady="0")
        self.NewFileButton.configure(text='''New File''')
        self.NewFileButton.configure(command=self.new_file)

        self.RecButton = tk.Button(self.DataFrame)
        self.RecButton.place(relx=0.750, rely=0.588, height=24, width=64)
        self.RecButton.configure(activebackground="#d9d9d9")
        self.RecButton.configure(activeforeground="#000000")
        self.RecButton.configure(background="#d9d9d9")
        self.RecButton.configure(disabledforeground="#a3a3a3")
        self.RecButton.configure(foreground="#000000")
        self.RecButton.configure(highlightbackground="#d9d9d9")
        self.RecButton.configure(highlightcolor="black")
        self.RecButton.configure(pady="0")
        self.img3 = tk.PhotoImage(file="./images/rec.png")
        self.RecButton.configure(text='''Start ''', image=self.img3, compound="right")
        self.RecButton.configure(command=self.start_record)
        self.RecButton.configure(state='disable')

        self.FileLabel = tk.Label(self.DataFrame)
        self.FileLabel.place(relx=0.020, rely=0.176, height=21, width=71)
        self.FileLabel.configure(background="#d9d9d9")
        self.FileLabel.configure(disabledforeground="#a3a3a3")
        self.FileLabel.configure(foreground="#000000")
        self.FileLabel.configure(text='''File Name :''')

        self.FileName = tk.Label(self.DataFrame)
        self.FileName.place(relx=0.250, rely=0.176, height=21, width=200)
        self.FileName.configure(background="#d9d9d9")
        self.FileName.configure(disabledforeground="#a3a3a3")
        self.FileName.configure(foreground="#000000")
        self.FileName.configure(justify='left')
        self.FileName.configure(anchor='e')
        self.FileName.configure(text=GUITest_Support.record_path)


        self.DataLabel = tk.Label(top)
        self.DataLabel.place(relx=0.264, rely=0.021, height=21, width=70)
        self.DataLabel.configure(background="#d9d9d9")
        self.DataLabel.configure(disabledforeground="#a3a3a3")
        self.DataLabel.configure(foreground="#000000")
        self.DataLabel.configure(text='''Data Control''')

        self.ChnFrame = tk.Frame(top)
        self.ChnFrame.place(relx=0.038, rely=0.313, relheight=0.573, relwidth=0.056)
        self.ChnFrame.configure(relief='groove')
        self.ChnFrame.configure(borderwidth="2")
        self.ChnFrame.configure(relief='groove')
        self.ChnFrame.configure(background="#d9d9d9")
        self.ChnFrame.configure(width=45)

        self.ChnLabel1 = tk.Label(self.ChnFrame)
        self.ChnLabel1.place(relx=0.233, rely=0.073, height=21, width=18)
        self.ChnLabel1.configure(background="#d9d9d9")
        self.ChnLabel1.configure(disabledforeground="#a3a3a3")
        self.ChnLabel1.configure(foreground="#000000")
        self.ChnLabel1.configure(text='''Idx''')

        self.ChnLabel2 = tk.Label(self.ChnFrame)
        self.ChnLabel2.place(relx=0.333, rely=0.182, height=21, width=12)
        self.ChnLabel2.configure(background="#d9d9d9")
        self.ChnLabel2.configure(disabledforeground="#a3a3a3")
        self.ChnLabel2.configure(foreground="#000000")
        self.ChnLabel2.configure(text='''1''')

        self.ChnLabel3 = tk.Label(self.ChnFrame)
        self.ChnLabel3.place(relx=0.333, rely=0.291, height=21, width=12)
        self.ChnLabel3.configure(background="#d9d9d9")
        self.ChnLabel3.configure(disabledforeground="#a3a3a3")
        self.ChnLabel3.configure(foreground="#000000")
        self.ChnLabel3.configure(text='''2''')

        self.ChnLabel4 = tk.Label(self.ChnFrame)
        self.ChnLabel4.place(relx=0.333, rely=0.4, height=21, width=12)
        self.ChnLabel4.configure(background="#d9d9d9")
        self.ChnLabel4.configure(disabledforeground="#a3a3a3")
        self.ChnLabel4.configure(foreground="#000000")
        self.ChnLabel4.configure(text='''3''')

        self.ChnLabel5 = tk.Label(self.ChnFrame)
        self.ChnLabel5.place(relx=0.333, rely=0.509, height=21, width=12)
        self.ChnLabel5.configure(background="#d9d9d9")
        self.ChnLabel5.configure(disabledforeground="#a3a3a3")
        self.ChnLabel5.configure(foreground="#000000")
        self.ChnLabel5.configure(text='''4''')

        self.ChnLabel6 = tk.Label(self.ChnFrame)
        self.ChnLabel6.place(relx=0.333, rely=0.618, height=21, width=12)
        self.ChnLabel6.configure(background="#d9d9d9")
        self.ChnLabel6.configure(disabledforeground="#a3a3a3")
        self.ChnLabel6.configure(foreground="#000000")
        self.ChnLabel6.configure(text='''5''')

        self.ChnLabel7 = tk.Label(self.ChnFrame)
        self.ChnLabel7.place(relx=0.333, rely=0.727, height=21, width=12)
        self.ChnLabel7.configure(background="#d9d9d9")
        self.ChnLabel7.configure(disabledforeground="#a3a3a3")
        self.ChnLabel7.configure(foreground="#000000")
        self.ChnLabel7.configure(text='''6''')

        self.ChnLabel8 = tk.Label(self.ChnFrame)
        self.ChnLabel8.place(relx=0.333, rely=0.836, height=21, width=12)
        self.ChnLabel8.configure(background="#d9d9d9")
        self.ChnLabel8.configure(disabledforeground="#a3a3a3")
        self.ChnLabel8.configure(foreground="#000000")
        self.ChnLabel8.configure(text='''7''')

        self.ChnLabels = tk.Label(top)
        self.ChnLabels.place(relx=0.044, rely=0.292, height=21, width=28)
        self.ChnLabels.configure(background="#d9d9d9")
        self.ChnLabels.configure(disabledforeground="#a3a3a3")
        self.ChnLabels.configure(foreground="#000000")
        self.ChnLabels.configure(text='''Chn''')

        self.CurvFrame = tk.Frame(top)
        self.CurvFrame.place(relx=0.125, rely=0.313, relheight=0.573, relwidth=0.281)

        self.CurvFrame.configure(relief='groove')
        self.CurvFrame.configure(borderwidth="2")
        self.CurvFrame.configure(relief='groove')
        self.CurvFrame.configure(background="#d9d9d9")
        self.CurvFrame.configure(width=225)

        self.Entry1 = tk.Entry(self.CurvFrame)
        self.Entry1.place(relx=0.044, rely=0.073, height=20, relwidth=0.862)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font=font10)
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(width=194)
        self.Entry1.insert(0, 'Time')

        self.Entry2 = tk.Entry(self.CurvFrame)
        self.Entry2.place(relx=0.044, rely=0.182, height=20, relwidth=0.862)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font=font10)
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(width=194)
        self.Entry2.insert(0, 'Channel 1')

        self.Entry3 = tk.Entry(self.CurvFrame)
        self.Entry3.place(relx=0.044, rely=0.291, height=20, relwidth=0.862)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font=font10)
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(width=194)
        self.Entry3.insert(0, 'Channel 2')

        self.Entry4 = tk.Entry(self.CurvFrame)
        self.Entry4.place(relx=0.044, rely=0.4, height=20, relwidth=0.862)
        self.Entry4.configure(background="white")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font=font10)
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(insertbackground="black")
        self.Entry4.configure(width=194)
        self.Entry4.insert(0, 'Channel 3')

        self.Entry5 = tk.Entry(self.CurvFrame)
        self.Entry5.place(relx=0.044, rely=0.509, height=20, relwidth=0.862)
        self.Entry5.configure(background="white")
        self.Entry5.configure(disabledforeground="#a3a3a3")
        self.Entry5.configure(font=font10)
        self.Entry5.configure(foreground="#000000")
        self.Entry5.configure(insertbackground="black")
        self.Entry5.configure(width=194)
        self.Entry5.insert(0, 'Channel 4')

        self.Entry6 = tk.Entry(self.CurvFrame)
        self.Entry6.place(relx=0.044, rely=0.618, height=20, relwidth=0.862)
        self.Entry6.configure(background="white")
        self.Entry6.configure(disabledforeground="#a3a3a3")
        self.Entry6.configure(font=font10)
        self.Entry6.configure(foreground="#000000")
        self.Entry6.configure(insertbackground="black")
        self.Entry6.configure(width=194)
        self.Entry6.insert(0, 'Channel 5')

        self.Entry7 = tk.Entry(self.CurvFrame)
        self.Entry7.place(relx=0.044, rely=0.727, height=20, relwidth=0.862)
        self.Entry7.configure(background="white")
        self.Entry7.configure(disabledforeground="#a3a3a3")
        self.Entry7.configure(font=font10)
        self.Entry7.configure(foreground="#000000")
        self.Entry7.configure(insertbackground="black")
        self.Entry7.configure(width=194)
        self.Entry7.insert(0, 'Channel 6')

        self.Entry8 = tk.Entry(self.CurvFrame)
        self.Entry8.place(relx=0.044, rely=0.836, height=20, relwidth=0.862)
        self.Entry8.configure(background="white")
        self.Entry8.configure(disabledforeground="#a3a3a3")
        self.Entry8.configure(font=font10)
        self.Entry8.configure(foreground="#000000")
        self.Entry8.configure(insertbackground="black")
        self.Entry8.configure(width=194)
        self.Entry8.insert(0, 'Channel 7')

        self.CurveLabels = tk.Label(top)
        self.CurveLabels.place(relx=0.131, rely=0.292, height=21, width=100)
        self.CurveLabels.configure(background="#d9d9d9")
        self.CurveLabels.configure(disabledforeground="#a3a3a3")
        self.CurveLabels.configure(foreground="#000000")
        self.CurveLabels.configure(text='''Curve Description''')

        self.UnitFrame = tk.Frame(top)
        self.UnitFrame.place(relx=0.663, rely=0.313, relheight=0.573, relwidth=0.106)

        self.UnitFrame.configure(relief='groove')
        self.UnitFrame.configure(borderwidth="2")
        self.UnitFrame.configure(relief='groove')
        self.UnitFrame.configure(background="#d9d9d9")
        self.UnitFrame.configure(width=85)

        self.UnitTCombobox1 = ttk.Combobox(self.UnitFrame)
        self.UnitTCombobox1.place(relx=0.118, rely=0.073, relheight=0.076
                                  , relwidth=0.741)
        self.value_list = ['none', 'Min', 'Seg', 'mSeg', ]
        self.UnitTCombobox1.configure(values=self.value_list)
        self.UnitTCombobox1.configure(width=63)
        self.UnitTCombobox1.configure(takefocus="")
        self.UnitTCombobox1.set(self.value_list[2])

        self.UnitTCombobox2 = ttk.Combobox(self.UnitFrame)
        self.UnitTCombobox2.place(relx=0.118, rely=0.182, relheight=0.076
                                    , relwidth=0.741)
        self.value_list = ['none', 'Amp', 'Volt', 'mA', 'mV', 'DegC', 'DegF', 'Deg', 'mts', 'fts', 'mt/s', 'mt/m',
                           'ft/s', 'ft/m', 'grm', 'Kgm', ]
        self.UnitTCombobox2.configure(values=self.value_list)
        self.UnitTCombobox2.configure(takefocus="")
        self.UnitTCombobox2.set(self.value_list[0])

        self.UnitTCombobox3 = ttk.Combobox(self.UnitFrame)
        self.UnitTCombobox3.place(relx=0.118, rely=0.291, relheight=0.076
                                    , relwidth=0.741)
        self.value_list = ['none', 'Amp', 'Volt', 'mA', 'mV', 'DegC', 'DegF', 'Deg', 'mts', 'fts', 'mt/s', 'mt/m',
                           'ft/s', 'ft/m', 'grm', 'Kgm', ]
        self.UnitTCombobox3.configure(values=self.value_list)
        self.UnitTCombobox3.configure(takefocus="")
        self.UnitTCombobox3.set(self.value_list[0])

        self.UnitTCombobox4 = ttk.Combobox(self.UnitFrame)
        self.UnitTCombobox4.place(relx=0.118, rely=0.4, relheight=0.076
                                  , relwidth=0.741)
        self.value_list = ['none', 'Amp', 'Volt', 'mA', 'mV', 'DegC', 'DegF', 'Deg', 'mts', 'fts', 'mt/s', 'mt/m',
                           'ft/s', 'ft/m', 'grm', 'Kgm', ]
        self.UnitTCombobox4.configure(values=self.value_list)
        self.UnitTCombobox4.configure(takefocus="")
        self.UnitTCombobox4.set(self.value_list[0])

        self.UnitTCombobox5 = ttk.Combobox(self.UnitFrame)
        self.UnitTCombobox5.place(relx=0.118, rely=0.509, relheight=0.076
                                  , relwidth=0.741)
        self.value_list = ['none', 'Amp', 'Volt', 'mA', 'mV', 'DegC', 'DegF', 'Deg', 'mts', 'fts', 'mt/s', 'mt/m',
                           'ft/s', 'ft/m', 'grm', 'Kgm', ]
        self.UnitTCombobox5.configure(values=self.value_list)
        self.UnitTCombobox5.configure(takefocus="")
        self.UnitTCombobox5.set(self.value_list[0])

        self.UnitTCombobox6 = ttk.Combobox(self.UnitFrame)
        self.UnitTCombobox6.place(relx=0.118, rely=0.618, relheight=0.076
                                  , relwidth=0.741)
        self.value_list = ['none', 'Amp', 'Volt', 'mA', 'mV', 'DegC', 'DegF', 'Deg', 'mts', 'fts', 'mt/s', 'mt/m',
                           'ft/s', 'ft/m', 'grm', 'Kgm', ]
        self.UnitTCombobox6.configure(values=self.value_list)
        self.UnitTCombobox6.configure(takefocus="")
        self.UnitTCombobox6.set(self.value_list[0])

        self.UnitTCombobox7 = ttk.Combobox(self.UnitFrame)
        self.UnitTCombobox7.place(relx=0.118, rely=0.727, relheight=0.076
                                  , relwidth=0.741)
        self.value_list = ['none', 'Amp', 'Volt', 'mA', 'mV', 'DegC', 'DegF', 'Deg', 'mts', 'fts', 'mt/s', 'mt/m',
                           'ft/s', 'ft/m', 'grm', 'Kgm', ]
        self.UnitTCombobox7.configure(values=self.value_list)
        self.UnitTCombobox7.configure(takefocus="")
        self.UnitTCombobox7.set(self.value_list[0])

        self.UnitTCombobox8 = ttk.Combobox(self.UnitFrame)
        self.UnitTCombobox8.place(relx=0.118, rely=0.836, relheight=0.076
                                  , relwidth=0.741)
        self.value_list = ['none', 'Amp', 'Volt', 'mA', 'mV', 'DegC', 'DegF', 'Deg', 'mts', 'fts', 'mt/s', 'mt/m',
                           'ft/s', 'ft/m', 'grm', 'Kgm', ]
        self.UnitTCombobox8.configure(values=self.value_list)
        self.UnitTCombobox8.configure(takefocus="")
        self.UnitTCombobox8.set(self.value_list[0])

        self.GraphLabel = tk.Label(top)
        self.GraphLabel.place(relx=0.669, rely=0.292, height=21, width=33)
        self.GraphLabel.configure(background="#d9d9d9")
        self.GraphLabel.configure(disabledforeground="#a3a3a3")
        self.GraphLabel.configure(foreground="#000000")
        self.GraphLabel.configure(text='''Units''')

        self.ValueFrame = tk.Frame(top)
        self.ValueFrame.place(relx=0.438, rely=0.313, relheight=0.573
                              , relwidth=0.194)
        self.ValueFrame.configure(relief='groove')
        self.ValueFrame.configure(borderwidth="2")
        self.ValueFrame.configure(relief='groove')
        self.ValueFrame.configure(background="#d9d9d9")
        self.ValueFrame.configure(width=155)

        self.LabelChn1 = tk.Label(self.ValueFrame)
        self.LabelChn1.place(relx=0.065, rely=0.073, height=21, width=134)
        self.LabelChn1.configure(background="#d9d9d9")
        self.LabelChn1.configure(disabledforeground="#a3a3a3")
        self.LabelChn1.configure(font=font17)
        self.LabelChn1.configure(foreground="#000000")
        self.LabelChn1.configure(justify='right')
        self.LabelChn1.configure(text='''0''')
        self.LabelChn1.configure(width=134)

        self.LabelChn2 = tk.Label(self.ValueFrame)
        self.LabelChn2.place(relx=0.065, rely=0.182, height=21, width=134)
        self.LabelChn2.configure(activebackground="#f9f9f9")
        self.LabelChn2.configure(activeforeground="black")
        self.LabelChn2.configure(background="#d9d9d9")
        self.LabelChn2.configure(disabledforeground="#a3a3a3")
        self.LabelChn2.configure(font=font17)
        self.LabelChn2.configure(foreground="#000000")
        self.LabelChn2.configure(highlightbackground="#d9d9d9")
        self.LabelChn2.configure(highlightcolor="black")
        self.LabelChn2.configure(justify='right')
        self.LabelChn2.configure(text='''0''')

        self.LabelChn3 = tk.Label(self.ValueFrame)
        self.LabelChn3.place(relx=0.065, rely=0.291, height=21, width=134)
        self.LabelChn3.configure(activebackground="#f9f9f9")
        self.LabelChn3.configure(activeforeground="black")
        self.LabelChn3.configure(background="#d9d9d9")
        self.LabelChn3.configure(disabledforeground="#a3a3a3")
        self.LabelChn3.configure(font=font17)
        self.LabelChn3.configure(foreground="#000000")
        self.LabelChn3.configure(highlightbackground="#d9d9d9")
        self.LabelChn3.configure(highlightcolor="black")
        self.LabelChn3.configure(justify='right')
        self.LabelChn3.configure(text='''0''')

        self.LabelChn4 = tk.Label(self.ValueFrame)
        self.LabelChn4.place(relx=0.065, rely=0.4, height=21, width=134)
        self.LabelChn4.configure(activebackground="#f9f9f9")
        self.LabelChn4.configure(activeforeground="black")
        self.LabelChn4.configure(background="#d9d9d9")
        self.LabelChn4.configure(disabledforeground="#a3a3a3")
        self.LabelChn4.configure(font=font17)
        self.LabelChn4.configure(foreground="#000000")
        self.LabelChn4.configure(highlightbackground="#d9d9d9")
        self.LabelChn4.configure(highlightcolor="black")
        self.LabelChn4.configure(justify='right')
        self.LabelChn4.configure(text='''0''')

        self.LabelChn5 = tk.Label(self.ValueFrame)
        self.LabelChn5.place(relx=0.065, rely=0.509, height=21, width=134)
        self.LabelChn5.configure(activebackground="#f9f9f9")
        self.LabelChn5.configure(activeforeground="black")
        self.LabelChn5.configure(background="#d9d9d9")
        self.LabelChn5.configure(disabledforeground="#a3a3a3")
        self.LabelChn5.configure(font=font17)
        self.LabelChn5.configure(foreground="#000000")
        self.LabelChn5.configure(highlightbackground="#d9d9d9")
        self.LabelChn5.configure(highlightcolor="black")
        self.LabelChn5.configure(justify='right')
        self.LabelChn5.configure(text='''0''')

        self.LabelChn6 = tk.Label(self.ValueFrame)
        self.LabelChn6.place(relx=0.065, rely=0.618, height=21, width=134)
        self.LabelChn6.configure(activebackground="#f9f9f9")
        self.LabelChn6.configure(activeforeground="black")
        self.LabelChn6.configure(background="#d9d9d9")
        self.LabelChn6.configure(disabledforeground="#a3a3a3")
        self.LabelChn6.configure(font=font17)
        self.LabelChn6.configure(foreground="#000000")
        self.LabelChn6.configure(highlightbackground="#d9d9d9")
        self.LabelChn6.configure(highlightcolor="black")
        self.LabelChn6.configure(justify='right')
        self.LabelChn6.configure(text='''0''')

        self.LabelChn7 = tk.Label(self.ValueFrame)
        self.LabelChn7.place(relx=0.065, rely=0.727, height=21, width=134)
        self.LabelChn7.configure(activebackground="#f9f9f9")
        self.LabelChn7.configure(activeforeground="black")
        self.LabelChn7.configure(background="#d9d9d9")
        self.LabelChn7.configure(disabledforeground="#a3a3a3")
        self.LabelChn7.configure(font=font17)
        self.LabelChn7.configure(foreground="#000000")
        self.LabelChn7.configure(highlightbackground="#d9d9d9")
        self.LabelChn7.configure(highlightcolor="black")
        self.LabelChn7.configure(justify='right')
        self.LabelChn7.configure(text='''0''')

        self.LabelChn8 = tk.Label(self.ValueFrame)
        self.LabelChn8.place(relx=0.065, rely=0.836, height=21, width=134)
        self.LabelChn8.configure(activebackground="#f9f9f9")
        self.LabelChn8.configure(activeforeground="black")
        self.LabelChn8.configure(background="#d9d9d9")
        self.LabelChn8.configure(disabledforeground="#a3a3a3")
        self.LabelChn8.configure(font=font17)
        self.LabelChn8.configure(foreground="#000000")
        self.LabelChn8.configure(highlightbackground="#d9d9d9")
        self.LabelChn8.configure(highlightcolor="black")
        self.LabelChn8.configure(justify='right')
        self.LabelChn8.configure(text='''0''')

        self.Label15 = tk.Label(top)
        self.Label15.place(relx=0.444, rely=0.292, height=21, width=71)
        self.Label15.configure(background="#d9d9d9")
        self.Label15.configure(disabledforeground="#a3a3a3")
        self.Label15.configure(foreground="#000000")
        self.Label15.configure(text='''Input Values''')

        self.Frame6 = tk.Frame(top)
        self.Frame6.place(relx=0.8, rely=0.313, relheight=0.656, relwidth=0.181)
        self.Frame6.configure(relief='groove')
        self.Frame6.configure(borderwidth="2")
        self.Frame6.configure(relief='groove')
        self.Frame6.configure(background="#d9d9d9")
        self.Frame6.configure(width=145)

        # Un-comment to enable File Button
        # self.FileButton = tk.Button(self.Frame6)
        # self.FileButton.place(relx=0.138, rely=0.063, height=24, width=100)
        # self.FileButton.configure(activebackground="#d9d9d9")
        # self.FileButton.configure(activeforeground="#000000")
        # self.FileButton.configure(background="#d9d9d9")
        # self.FileButton.configure(disabledforeground="#a3a3a3")
        # self.FileButton.configure(foreground="#000000")
        # self.FileButton.configure(highlightbackground="#d9d9d9")
        # self.FileButton.configure(highlightcolor="black")
        # self.FileButton.configure(pady="0")
        # self.FileButton.configure(text='''Select File Name''')
        # self.FileButton.configure(state='normal')

        self.GraphButton1 = tk.Button(self.Frame6)
        self.GraphButton1.place(relx=0.080, rely=0.159, height=24, width=52)
        self.GraphButton1.configure(activebackground="#d9d9d9")
        self.GraphButton1.configure(activeforeground="#000000")
        self.GraphButton1.configure(background="#d9d9d9")
        self.GraphButton1.configure(disabledforeground="#a3a3a3")
        self.GraphButton1.configure(foreground="#000000")
        self.GraphButton1.configure(highlightbackground="#d9d9d9")
        self.GraphButton1.configure(highlightcolor="black")
        self.GraphButton1.configure(pady="0")
        self.GraphButton1.configure(text='''Graph 1''')
        self.GraphButton1.configure(command=self.plot_ch1)

        self.GraphButton2 = tk.Button(self.Frame6)
        self.GraphButton2.place(relx=0.080, rely=0.254, height=24, width=52)
        self.GraphButton2.configure(activebackground="#d9d9d9")
        self.GraphButton2.configure(activeforeground="#000000")
        self.GraphButton2.configure(background="#d9d9d9")
        self.GraphButton2.configure(disabledforeground="#a3a3a3")
        self.GraphButton2.configure(foreground="#000000")
        self.GraphButton2.configure(highlightbackground="#d9d9d9")
        self.GraphButton2.configure(highlightcolor="black")
        self.GraphButton2.configure(pady="0")
        self.GraphButton2.configure(text='''Graph 2''')
        self.GraphButton2.configure(command=self.plot_ch2)

        self.GraphButton3 = tk.Button(self.Frame6)
        self.GraphButton3.place(relx=0.080, rely=0.349, height=24, width=52)
        self.GraphButton3.configure(activebackground="#d9d9d9")
        self.GraphButton3.configure(activeforeground="#000000")
        self.GraphButton3.configure(background="#d9d9d9")
        self.GraphButton3.configure(disabledforeground="#a3a3a3")
        self.GraphButton3.configure(foreground="#000000")
        self.GraphButton3.configure(highlightbackground="#d9d9d9")
        self.GraphButton3.configure(highlightcolor="black")
        self.GraphButton3.configure(pady="0")
        self.GraphButton3.configure(text='''Graph 3''')
        self.GraphButton3.configure(command=self.plot_ch3)

        self.GraphButton4 = tk.Button(self.Frame6)
        self.GraphButton4.place(relx=0.080, rely=0.444, height=24, width=52)
        self.GraphButton4.configure(activebackground="#d9d9d9")
        self.GraphButton4.configure(activeforeground="#000000")
        self.GraphButton4.configure(background="#d9d9d9")
        self.GraphButton4.configure(disabledforeground="#a3a3a3")
        self.GraphButton4.configure(foreground="#000000")
        self.GraphButton4.configure(highlightbackground="#d9d9d9")
        self.GraphButton4.configure(highlightcolor="black")
        self.GraphButton4.configure(pady="0")
        self.GraphButton4.configure(text='''Graph 4''')
        self.GraphButton4.configure(command=self.plot_ch4)

        self.GraphButton5 = tk.Button(self.Frame6)
        self.GraphButton5.place(relx=0.080, rely=0.54, height=24, width=52)
        self.GraphButton5.configure(activebackground="#d9d9d9")
        self.GraphButton5.configure(activeforeground="#000000")
        self.GraphButton5.configure(background="#d9d9d9")
        self.GraphButton5.configure(disabledforeground="#a3a3a3")
        self.GraphButton5.configure(foreground="#000000")
        self.GraphButton5.configure(highlightbackground="#d9d9d9")
        self.GraphButton5.configure(highlightcolor="black")
        self.GraphButton5.configure(pady="0")
        self.GraphButton5.configure(text='''Graph 5''')
        self.GraphButton5.configure(command=self.plot_ch5)

        self.GraphButton6 = tk.Button(self.Frame6)
        self.GraphButton6.place(relx=0.080, rely=0.635, height=24, width=52)
        self.GraphButton6.configure(activebackground="#d9d9d9")
        self.GraphButton6.configure(activeforeground="#000000")
        self.GraphButton6.configure(background="#d9d9d9")
        self.GraphButton6.configure(disabledforeground="#a3a3a3")
        self.GraphButton6.configure(foreground="#000000")
        self.GraphButton6.configure(highlightbackground="#d9d9d9")
        self.GraphButton6.configure(highlightcolor="black")
        self.GraphButton6.configure(pady="0")
        self.GraphButton6.configure(text='''Graph 6''')
        self.GraphButton6.configure(command=self.plot_ch6)

        self.GraphButton7 = tk.Button(self.Frame6)
        self.GraphButton7.place(relx=0.080, rely=0.73, height=24, width=52)
        self.GraphButton7.configure(activebackground="#d9d9d9")
        self.GraphButton7.configure(activeforeground="#000000")
        self.GraphButton7.configure(background="#d9d9d9")
        self.GraphButton7.configure(disabledforeground="#a3a3a3")
        self.GraphButton7.configure(foreground="#000000")
        self.GraphButton7.configure(highlightbackground="#d9d9d9")
        self.GraphButton7.configure(highlightcolor="black")
        self.GraphButton7.configure(pady="0")
        self.GraphButton7.configure(text='''Graph 7''')
        self.GraphButton7.configure(command=self.plot_ch7)

        self.IntervalGraphButton = tk.Button(self.Frame6)
        self.IntervalGraphButton.place(relx=0.207, rely=0.857, height=24, width=87)
        self.IntervalGraphButton.configure(activebackground="#d9d9d9")
        self.IntervalGraphButton.configure(activeforeground="#000000")
        self.IntervalGraphButton.configure(background="#d9d9d9")
        self.IntervalGraphButton.configure(disabledforeground="#a3a3a3")
        self.IntervalGraphButton.configure(foreground="#000000")
        self.IntervalGraphButton.configure(highlightbackground="#d9d9d9")
        self.IntervalGraphButton.configure(highlightcolor="black")
        self.IntervalGraphButton.configure(pady="0")
        self.IntervalGraphButton.configure(text='''Graph Interval''')
        self.IntervalGraphButton.configure(width=87)

        # Uncomment to enable Check button:
        # self.Checkbutton1 = tk.Checkbutton(self.Frame6)
        # self.Checkbutton1.place(relx=0.552, rely=0.063, relheight=0.079
                                # , relwidth=0.372)
        # self.Checkbutton1.configure(activebackground="#d9d9d9")
        # self.Checkbutton1.configure(activeforeground="#000000")
        # self.Checkbutton1.configure(background="#d9d9d9")
        # self.Checkbutton1.configure(disabledforeground="#a3a3a3")
        # self.Checkbutton1.configure(foreground="#000000")
        # self.Checkbutton1.configure(highlightbackground="#d9d9d9")
        # self.Checkbutton1.configure(highlightcolor="black")
        # self.Checkbutton1.configure(justify='left')
        # self.Checkbutton1.configure(text='''G_En''')
        # self.che1 = tk.StringVar()
        # self.che1.set(False)
        # self.Checkbutton1.configure(variable=self.che1)

        self.Checkbutton2 = tk.Checkbutton(self.Frame6)
        self.Checkbutton2.place(relx=0.522, rely=0.159, relheight=0.079
                                , relwidth=0.382)
        self.Checkbutton2.configure(activebackground="#d9d9d9")
        self.Checkbutton2.configure(activeforeground="#000000")
        self.Checkbutton2.configure(background="#d9d9d9")
        self.Checkbutton2.configure(disabledforeground="#a3a3a3")
        self.Checkbutton2.configure(foreground="#000000")
        self.Checkbutton2.configure(highlightbackground="#d9d9d9")
        self.Checkbutton2.configure(highlightcolor="black")
        self.Checkbutton2.configure(justify='left')
        self.Checkbutton2.configure(text='''Rec_En''')
        self.che2 = tk.BooleanVar()
        self.che2.set(False)
        self.Checkbutton2.configure(variable=self.che2)

        self.Checkbutton3 = tk.Checkbutton(self.Frame6)
        self.Checkbutton3.place(relx=0.522, rely=0.254, relheight=0.079
                                , relwidth=0.382)
        self.Checkbutton3.configure(activebackground="#d9d9d9")
        self.Checkbutton3.configure(activeforeground="#000000")
        self.Checkbutton3.configure(background="#d9d9d9")
        self.Checkbutton3.configure(disabledforeground="#a3a3a3")
        self.Checkbutton3.configure(foreground="#000000")
        self.Checkbutton3.configure(highlightbackground="#d9d9d9")
        self.Checkbutton3.configure(highlightcolor="black")
        self.Checkbutton3.configure(justify='left')
        self.Checkbutton3.configure(text='''Rec_En''')
        self.che3 = tk.BooleanVar()
        self.che3.set(False)
        self.Checkbutton3.configure(variable=self.che3)

        self.Checkbutton4 = tk.Checkbutton(self.Frame6)
        self.Checkbutton4.place(relx=0.522, rely=0.349, relheight=0.079
                                , relwidth=0.382)
        self.Checkbutton4.configure(activebackground="#d9d9d9")
        self.Checkbutton4.configure(activeforeground="#000000")
        self.Checkbutton4.configure(background="#d9d9d9")
        self.Checkbutton4.configure(disabledforeground="#a3a3a3")
        self.Checkbutton4.configure(foreground="#000000")
        self.Checkbutton4.configure(highlightbackground="#d9d9d9")
        self.Checkbutton4.configure(highlightcolor="black")
        self.Checkbutton4.configure(justify='left')
        self.Checkbutton4.configure(text='''Rec_En''')
        self.che4 = tk.BooleanVar()
        self.che4.set(False)
        self.Checkbutton4.configure(variable=self.che4)

        self.Checkbutton5 = tk.Checkbutton(self.Frame6)
        self.Checkbutton5.place(relx=0.522, rely=0.444, relheight=0.079
                                , relwidth=0.382)
        self.Checkbutton5.configure(activebackground="#d9d9d9")
        self.Checkbutton5.configure(activeforeground="#000000")
        self.Checkbutton5.configure(background="#d9d9d9")
        self.Checkbutton5.configure(disabledforeground="#a3a3a3")
        self.Checkbutton5.configure(foreground="#000000")
        self.Checkbutton5.configure(highlightbackground="#d9d9d9")
        self.Checkbutton5.configure(highlightcolor="black")
        self.Checkbutton5.configure(justify='left')
        self.Checkbutton5.configure(text='''Rec_En''')
        self.che5 = tk.BooleanVar()
        self.che5.set(False)
        self.Checkbutton5.configure(variable=self.che5)

        self.Checkbutton6 = tk.Checkbutton(self.Frame6)
        self.Checkbutton6.place(relx=0.522, rely=0.54, relheight=0.079
                                , relwidth=0.382)
        self.Checkbutton6.configure(activebackground="#d9d9d9")
        self.Checkbutton6.configure(activeforeground="#000000")
        self.Checkbutton6.configure(background="#d9d9d9")
        self.Checkbutton6.configure(disabledforeground="#a3a3a3")
        self.Checkbutton6.configure(foreground="#000000")
        self.Checkbutton6.configure(highlightbackground="#d9d9d9")
        self.Checkbutton6.configure(highlightcolor="black")
        self.Checkbutton6.configure(justify='left')
        self.Checkbutton6.configure(text='''Rec_En''')
        self.che6 = tk.BooleanVar()
        self.che6.set(False)
        self.Checkbutton6.configure(variable=self.che6)

        self.Checkbutton7 = tk.Checkbutton(self.Frame6)
        self.Checkbutton7.place(relx=0.522, rely=0.635, relheight=0.079
                                , relwidth=0.382)
        self.Checkbutton7.configure(activebackground="#d9d9d9")
        self.Checkbutton7.configure(activeforeground="#000000")
        self.Checkbutton7.configure(background="#d9d9d9")
        self.Checkbutton7.configure(disabledforeground="#a3a3a3")
        self.Checkbutton7.configure(foreground="#000000")
        self.Checkbutton7.configure(highlightbackground="#d9d9d9")
        self.Checkbutton7.configure(highlightcolor="black")
        self.Checkbutton7.configure(justify='left')
        self.Checkbutton7.configure(text='''Rec_En''')
        self.che7 = tk.BooleanVar()
        self.che7.set(False)
        self.Checkbutton7.configure(variable=self.che7)
        self.Checkbutton7.configure(width=54)

        self.Checkbutton8 = tk.Checkbutton(self.Frame6)
        self.Checkbutton8.place(relx=0.522, rely=0.73, relheight=0.079
                                , relwidth=0.382)
        self.Checkbutton8.configure(activebackground="#d9d9d9")
        self.Checkbutton8.configure(activeforeground="#000000")
        self.Checkbutton8.configure(background="#d9d9d9")
        self.Checkbutton8.configure(disabledforeground="#a3a3a3")
        self.Checkbutton8.configure(foreground="#000000")
        self.Checkbutton8.configure(highlightbackground="#d9d9d9")
        self.Checkbutton8.configure(highlightcolor="black")
        self.Checkbutton8.configure(justify='left')
        self.Checkbutton8.configure(text='''Rec_En''')
        self.che8 = tk.BooleanVar()
        self.che8.set(False)
        self.Checkbutton8.configure(variable=self.che8)

        self.Label17 = tk.Label(top)
        self.Label17.place(relx=0.806, rely=0.292, height=21, width=83)
        self.Label17.configure(background="#d9d9d9")
        self.Label17.configure(disabledforeground="#a3a3a3")
        self.Label17.configure(foreground="#000000")
        self.Label17.configure(text='''Graph Options''')

    def usb_op(self):
        USB_Setup.create_Toplevel1(root)

    def connect(self):
        GUITest_Support.openusb()

    def disconnect(self):
       GUITest_Support.closeusb()

    def set_img_green(self):
        self.Label3.configure(image=self.img2)

    def set_img_red(self):
        self.Label3.configure(image=self.img1)

    def usb_connected(self):
        self.ConnectButton.configure(text='''Disconnect''')
        self.ConnectButton.configure(command=self.disconnect)
        self.Button2.configure(state='normal')

    def usb_disconnected(self):
        self.ConnectButton.configure(text='''Connect''')
        self.ConnectButton.configure(command=self.connect)
        self.Button2.configure(state='disable')

    def AQenable(self):
        self.Button2.configure(text='Stop AQ')
        self.Button2.configure(command=self.disable_usb)
        self.RecButton.configure(state='normal')
        GUITest_Support.act = True
        InfiniteTimer.t.start()

    def disable_usb(self):
        if GUITest_Support.record:
            self.stop_record()
        self.Button2.configure(text='Enable AQ')
        self.Button2.configure(command=self.AQenable)
        self.RecButton.configure(state='disable')
        GUITest_Support.act = False
        InfiniteTimer.t.cancel()

    def upd_ch1(self, ch1, ch2, ch3, ch4, ch5, ch6, ch7, ch8):
        self.LabelChn1.configure(text=ch1)
        self.LabelChn2.configure(text=ch2)
        self.LabelChn3.configure(text=ch3)
        self.LabelChn4.configure(text=ch4)
        self.LabelChn5.configure(text=ch5)
        self.LabelChn6.configure(text=ch6)
        self.LabelChn7.configure(text=ch7)
        self.LabelChn8.configure(text=ch8)

    def open_template(self):
        try:
            GUITest_Support.template_path = filedialog.askopenfilename(initialdir='./templates/',
                                                                       title='Open Template File',
                                                                       filetypes=(('Template files', '*.tpl'),
                                                                                  ('all files', '*.*'),
                                                                                  ('text files', '*.txt')))
            GUITest_Support.open_template()
        except:
            messagebox.showwarning('Warning', 'Failed to load template!')

    def save_template(self):
        try:
            GUITest_Support.template_path = filedialog.asksaveasfilename(initialdir='./templates/',
                                                                         title='Save Template File',
                                                                         defaultextension='*.tpl',
                                                                         filetypes=(('Template files', '*.tpl'),
                                                                                    ('all files', '*.*')))
            GUITest_Support.save_template()
            messagebox.showinfo('Template', 'Template saved successfully :D')
        except:
            messagebox.showwarning('Warning', 'Failed to save template!')

    def open_file(self):
        try:
            GUITest_Support.record_path = filedialog.askopenfilename(initialdir='./data/',
                                                                     title='Open Record File',
                                                                     defaultextension='*.csv',
                                                                     filetypes=(('CSV files', '*.csv'),
                                                                                ('all files', '*.*'),
                                                                                ('text files', '*.txt')))
            self.FileName.configure(text=GUITest_Support.record_path)
            GUITest_Support.open_file()
        except:
            messagebox.showwarning('Warning', 'Can\'t open file!')

    def new_file(self):
        try:
            GUITest_Support.record_path = filedialog.asksaveasfilename(initialdir='./data/',
                                                                       defaultextension='*.csv',
                                                                       title='New Record File',
                                                                       filetypes=(('Comma Separated', '*.csv'),
                                                                                ('text file', '*.txt'),
                                                                                ('all files', '*.*')))
            self.FileName.configure(text=GUITest_Support.record_path)
            GUITest_Support.new_file()
        except:
            messagebox.showwarning('Warning', 'Fail to Create New File!')

    def plot_ch1(self):
        self.GraphButton1.configure(state='disable')
        display.graph_plot_ch1()

    def plot_ch2(self):
        self.GraphButton2.configure(state='disable')
        display2.graph_plot_ch2()

    def plot_ch3(self):
        self.GraphButton3.configure(state='disable')
        display3.graph_plot_ch3()

    def plot_ch4(self):
        self.GraphButton4.configure(state='disable')
        display4.graph_plot_ch4()

    def plot_ch5(self):
        self.GraphButton5.configure(state='disable')
        display5.graph_plot_ch5()

    def plot_ch6(self):
        self.GraphButton6.configure(state='disable')
        display6.graph_plot_ch6()

    def plot_ch7(self):
        self.GraphButton7.configure(state='disable')
        display7.graph_plot_ch7()

    def start_record(self):
        if GUITest_Support.file_state:
            GUITest_Support.open_file()
        GUITest_Support.record = True
        self.RecButton.configure(text='Stop')
        self.RecButton.configure(command=self.stop_record)

    def stop_record(self):
        if GUITest_Support.file_state:
            GUITest_Support.record_file.close()
        GUITest_Support.record = False
        self.RecButton.configure(text='Start')
        self.RecButton.configure(command=self.start_record)

    def exit(self):
        self.disable_usb()
        root.destroy()


if __name__ == '__main__':
    root = tk.Tk()
    my_gui = Toplevel1(root)
    matplotlib_animated.init(root, my_gui)
    GUITest_Support.init(root, my_gui)
    root.mainloop()
