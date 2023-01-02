#v0.0 
# -*- coding: utf-8 -*-

from pickle import FRAME
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.colorchooser import askcolor
import turtle

def SelectWeaveMethod(event):
    global WeaveMethod
    WeaveMethod = weavemethod.current()

def SelectWeaveAmount(event):
    global WeaveAmount
    WeaveAmount = weaveamount.current()
    button_overline.place(x=125,y=0)

def color_choose_overline():
    global Overline_Color_Code
    Overline_Color_Code = tk.colorchooser.askcolor(title ='��ܤW�u�C��', color ='blue')
    button_overline.configure(bg=Overline_Color_Code[1],fg=Overline_Color_Code[1]) 
    button_belowline.place(x=125,y=35)
    return Overline_Color_Code

def color_choose_belowline():
    global Belowline_Color_Code
    Belowline_Color_Code = tk.colorchooser.askcolor(title ='��ܤU�u�C��', color ='blue')
    button_belowline.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1])
    button_start.place(x=20,y=0)
    return Belowline_Color_Code

def draw():
   
    canvas = tk.Canvas(frame6, width=300, height=400)
    canvas.grid(row=0, column=0)
    screen = turtle.TurtleScreen(canvas)
    raw = turtle.RawTurtle(screen)



if __name__ == '__main__':

    window = tk.Tk()
    window.title('Weaving Simulator v0.0')
    window.geometry('1050x900')
    window.configure(background='white')
    window.iconbitmap('Logo.ico')                                                 #�Ϥ��ɥ�J��Ƨ�

    frame1 = tk.Frame(window,bg='white',width=1050, height=295)
    frame1.place(x=0,y=0)  
    label = tk.PhotoImage(file='����_��USR�p�e_LOGO����.png')                    #���ӭn���]�p��label
    tk.Label(frame1, image=label).place(x=0,y=0)             

    frame2 = tk.Frame(window,bg='white',width=285, height=80)
    frame2.place(x=0,y=295) 
    frame3 = tk.Frame(window,bg='white',width=285, height=70)
    frame3.place(x=0,y=375) 
    frame4 = tk.Frame(window,bg='white',width=285, height=700)
    frame4.place(x=0,y=445) 
    frame6 = tk.Frame(window,bg='white',width=300, height=900)
    frame6.place(x=700,y=305) 

    weavemethod_label = tk.Label(frame2, text='´�k',font=('�L�n������',12))      #����X�ýX https://ithelp.ithome.com.tw/articles/10232644
    weavemethod_label.place(x=20,y=10)
    weavemethod = ttk.Combobox(frame2, values=[
                                        '��´',
                                        '�D´',
                                        '�ׯ�´'],font=('�L�n������',12),state="readonly")
    weavemethod.place(x=80,y=10)
    WeaveMethod = weavemethod.current()
    weavemethod.bind("<<ComboboxSelected>>", SelectWeaveMethod)

    weaveamount_label = tk.Label(frame2, text='�ռ�',font=('�L�n������',12))
    weaveamount_label.place(x=20,y=45)
    weaveamount = ttk.Combobox(frame2, values=[
                                             '30',
                                             '40',
                                             '50'],font=('�L�n������',12),state="readonly")
    weaveamount.place(x=80,y=45)
    WeaveAmount = weaveamount.current()
    weaveamount.bind("<<ComboboxSelected>>", SelectWeaveAmount)

    overline_label = tk.Label(frame3, text='�W�u',font=('�L�n������',12))
    overline_label.place(x=20,y=0)
    button_overline = tk.Button(frame3, text='��ܤW�u�C��', command=lambda :color_choose_overline())

    belowline_label = tk.Label(frame3, text='�U�u',font=('�L�n������',12))
    belowline_label.place(x=20,y=35)
    button_belowline = tk.Button(frame3, text='��ܤU�u�C��', command=lambda :color_choose_belowline())

    button_start = tk.Button(frame4, text='Start', font=('Arial',14), command=lambda :draw(),width=15,height=2)
    button_exit = tk.Button(frame4, text='Exit', font=('Arial',12), command=window.destroy)

    window.mainloop()
