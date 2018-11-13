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

import serial

comport = 'COM3'
baudrate = 9600
act = False
ch1 = None
ch2 = None
ch3 = None
ch4 = None
ch5 = None
ch6 = None
ch7 = None
ch8 = None
chk_ch2 = False
chk_ch3 = False
chk_ch4 = False
chk_ch5 = False
chk_ch6 = False
chk_ch7 = False
chk_ch8 = False

template_path = " "       # Used in the tk file dialog to browse for the file path
record_path = " "         # Used in the tk file dialog to browse for the file path

template_file = None      # store the file to safe the templates or call the templates
record_file = None        # store the file to be record in

template_file_select = False  # variable attached to verify if the template file was successfully open
record_file_select = False    # variable attached to verify if the file was selected and open

record = False          # variable attached to the record button
file_state = False      # State of the files if is Close of Open to record...

def set_baudrate(baud):
  global baudrate
  baudrate = baud


def set_COM(com):
  global comport
  comport = com


def get_baudrate():
  return comport


def get_COM():
  return baudrate


def openusb():
  global ser, root
  ser = serial.Serial()
  ser.baudrate = baudrate
  ser.port = comport
  ser.timeout = None
  try:
    ser.open()
  except:
    messagebox.showerror('USB Port', 'Could not open port ' + comport)

  if ser.is_open:
    print(ser.is_open)
    w.set_img_green()
    w.usb_connected()


def closeusb():
  ser.close()
  if not ser.is_open:
    print(ser.is_open)
    w.set_img_red()
    w.usb_disconnected()


def test2():
  #print('inloop')
  global ch1, ch2, ch3, ch4, ch5, ch6, ch7, ch8, act
  if act:
    try:
      if ser.in_waiting > 0:
        datain = ser.readline().strip()
        ser.flushInput()
        asciidata = datain.decode('ascii')
        asciidata = asciidata.split(';')

        ch1, ch2, ch3, ch4, ch5, ch6, ch7, ch8 = asciidata

        w.upd_ch1(ch1, ch2, ch3, ch4, ch5, ch6, ch7, ch8)           # update the main window labels
        if record:
          rec_begin()
    except:
      messagebox.showerror('USB Error', 'Fail to read data from port!')
      w.disable_usb()
                       # Goes to rutine to store data in record_file


def init(top, gui, *args, **kwargs):
  global w, top_level, root
  w = gui
  top_level = top
  root = top


def save_template():
  global template_file
  template_text = (w.Entry1.get() + ';' + w.UnitTCombobox1.get() + '\n' +
                   w.Entry2.get() + ';' + w.UnitTCombobox2.get() + ';' + str(w.che2.get()) + '\n' +
                   w.Entry3.get() + ';' + w.UnitTCombobox3.get() + ';' + str(w.che3.get()) + '\n' +
                   w.Entry4.get() + ';' + w.UnitTCombobox4.get() + ';' + str(w.che4.get()) + '\n' +
                   w.Entry5.get() + ';' + w.UnitTCombobox5.get() + ';' + str(w.che5.get()) + '\n' +
                   w.Entry6.get() + ';' + w.UnitTCombobox6.get() + ';' + str(w.che6.get()) + '\n' +
                   w.Entry7.get() + ';' + w.UnitTCombobox7.get() + ';' + str(w.che7.get()) + '\n' +
                   w.Entry8.get() + ';' + w.UnitTCombobox8.get() + ';' + str(w.che8.get()) + '\n')
  template_file = open(template_path, 'w')
  template_file.write(template_text)
  template_file.close()


def open_template():
  global template_file
  template_file = open(template_path, 'r')
  template_list = template_file.readlines()
  template_file.close()
  entry1, unit1 = template_list[0].split(';')
  entry2, unit2, box2 = template_list[1].split(';')
  entry3, unit3, box3 = template_list[2].split(';')
  entry4, unit4, box4 = template_list[3].split(';')
  entry5, unit5, box5 = template_list[4].split(';')
  entry6, unit6, box6 = template_list[5].split(';')
  entry7, unit7, box7 = template_list[6].split(';')
  entry8, unit8, box8 = template_list[7].split(';')
  w.Entry1.delete(0, 194)
  w.Entry2.delete(0, 194)
  w.Entry3.delete(0, 194)
  w.Entry4.delete(0, 194)
  w.Entry5.delete(0, 194)
  w.Entry6.delete(0, 194)
  w.Entry7.delete(0, 194)
  w.Entry8.delete(0, 194)
  w.Entry1.insert(0, entry1)
  w.Entry2.insert(0, entry2)
  w.Entry3.insert(0, entry3)
  w.Entry4.insert(0, entry4)
  w.Entry5.insert(0, entry5)
  w.Entry6.insert(0, entry6)
  w.Entry7.insert(0, entry7)
  w.Entry8.insert(0, entry8)
  w.UnitTCombobox1.set(unit1)
  w.UnitTCombobox2.set(unit2)
  w.UnitTCombobox3.set(unit3)
  w.UnitTCombobox4.set(unit4)
  w.UnitTCombobox5.set(unit5)
  w.UnitTCombobox6.set(unit6)
  w.UnitTCombobox7.set(unit7)
  w.UnitTCombobox8.set(unit8)
  box2 = box2.strip()
  box3 = box3.strip()
  box4 = box4.strip()
  box5 = box5.strip()
  box6 = box6.strip()
  box7 = box7.strip()
  box8 = box8.strip()
  if box2 == "True":
    w.che2.set(True)
  else:
    w.che2.set(False)

  if box3 == "True":
    w.che3.set(True)
  else:
    w.che3.set(False)

  if box4 == "True":
    w.che4.set(True)
  else:
    w.che4.set(False)

  if box5 == "True":
    w.che5.set(True)
  else:
    w.che5.set(False)

  if box6 == "True":
    w.che6.set(True)
  else:
    w.che6.set(False)

  if box7 == "True":
    w.che7.set(True)
  else:
    w.che7.set(False)

  if box8 == "True":
    w.che8.set(True)
  else:
    w.che8.set(False)


def open_file():
  global record_file, file_state
  record_file = open(record_path, 'a')
  record_selection_check()
  file_state = True

def new_file():
  global record_file, record_path
  record_file = open(record_path, 'w')
  header = file_header()
  headerNames = header[0] + '\n'
  headerUnits = header[1] + '\n'
  record_file.write(headerNames)
  record_file.write(headerUnits)
  record_file.close()


def file_header():
  global chk_ch2, chk_ch3, chk_ch4, chk_ch5, chk_ch6, chk_ch7, chk_ch8
  chk_ch2 = False
  chk_ch3 = False
  chk_ch4 = False
  chk_ch5 = False
  chk_ch6 = False
  chk_ch7 = False
  chk_ch8 = False
  headerString = ""
  headerUnits = ""
  headerString += w.Entry1.get() + ','
  headerUnits += w.UnitTCombobox1.get() + ','
  if w.che2.get():
    headerString += w.Entry2.get() + ','
    headerUnits += w.UnitTCombobox2.get() + ','
    chk_ch2 = True

  if w.che3.get():
    headerString += w.Entry3.get() + ','
    headerUnits += w.UnitTCombobox3.get() + ','
    chk_ch3 = True

  if w.che4.get():
    headerString += w.Entry4.get() + ','
    headerUnits += w.UnitTCombobox4.get() + ','
    chk_ch4 = True

  if w.che5.get():
    headerString += w.Entry5.get() + ','
    headerUnits += w.UnitTCombobox5.get() + ','
    chk_ch5 = True

  if w.che6.get():
    headerString += w.Entry6.get() + ','
    headerUnits += w.UnitTCombobox6.get() + ','
    chk_ch6 = True

  if w.che7.get():
    headerString += w.Entry7.get() + ','
    headerUnits += w.UnitTCombobox7.get() + ','
    chk_ch7 = True

  if w.che8.get():
    headerString += w.Entry8.get() + ','
    headerUnits += w.UnitTCombobox8.get() + ','
    chk_ch8 = True

  return headerString, headerUnits


def record_selection_check():
    global chk_ch2, chk_ch3, chk_ch4, chk_ch5, chk_ch6, chk_ch7, chk_ch8
    chk_ch2 = False
    chk_ch3 = False
    chk_ch4 = False
    chk_ch5 = False
    chk_ch6 = False
    chk_ch7 = False
    chk_ch8 = False
    if w.che2.get():
      chk_ch2 = True

    if w.che3.get():
      chk_ch3 = True

    if w.che4.get():
      chk_ch4 = True

    if w.che5.get():
      chk_ch5 = True

    if w.che6.get():
      chk_ch6 = True

    if w.che7.get():
      chk_ch7 = True

    if w.che8.get():
      chk_ch8 = True


def file_record_append():
  record_line = " "
  record_line = ch1 + ','
  if chk_ch2:
    record_line += ch2 + ','

  if chk_ch3:
    record_line += ch3 + ','

  if chk_ch4:
    record_line += ch4 + ','

  if chk_ch5:
    record_line += ch5 + ','

  if chk_ch6:
    record_line += ch6 + ','

  if chk_ch7:
    record_line += ch7 + ','

  if chk_ch8:
    record_line += ch8 + ','

  return record_line


def rec_begin():
  global file_state
  if not file_state:
      try:
        open_file()
      except:
        messagebox.showerror('Record', 'Can\'t Open File to record')
        file_state = False
        w.stop_record()

  if record and file_state:
    append_line = file_record_append()
    try:
      record_file.write(append_line + '\n')
    except:
      messagebox.showerror('File Error', 'Can\'t open File')
