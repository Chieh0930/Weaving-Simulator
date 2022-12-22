#v0.0 
# -*- coding: utf-8 -*-

from distutils.cmd import Command
from pickle import FRAME
from struct import pack
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.colorchooser import askcolor
import turtle

def SelectWeaveMethod(event):
    global WeaveMethod
    WeaveMethod = weavemethod.current()

    if WeaveMethod==0:
        print('織法:',WeaveMethod)
    elif WeaveMethod==1:
        print('織法:',WeaveMethod)
    elif WeaveMethod==2:
        print('織法:',WeaveMethod)

        overline_label.place(x=20,y=0)
        button_overline.place(x=125,y=0)

        belowline_label.place(x=20,y=35)
        button_belowline.place(x=125,y=35)

def SelectWeaveAmount(event):
    global WeaveAmount
    WeaveAmount = weaveamount.current()
    if WeaveMethod==0 and WeaveAmount==0:
        print('組數:',WeaveAmount)

        overline_label_1.place(x=20,y=10)
        overline_label_2.place(x=20,y=80)

        belowline_label_1.place(x=20,y=40)
        belowline_label_2.place(x=20,y=110)

        buttonover_1.place(x=80,y=10)
        buttonover_2.place(x=130,y=10)
        buttonover_3.place(x=180,y=10)
        buttonover_4.place(x=230,y=10)
        buttonover_5.place(x=280,y=10)
        buttonover_6.place(x=330,y=10)
        buttonover_7.place(x=380,y=10)
        buttonover_8.place(x=430,y=10)
        buttonover_9.place(x=480,y=10)
        buttonover_10.place(x=530,y=10)
        buttonover_11.place(x=580,y=10)
        buttonover_12.place(x=630,y=10)
        buttonover_13.place(x=680,y=10)
        buttonover_14.place(x=730,y=10)
        buttonover_15.place(x=780,y=10)
        buttonover_16.place(x=80,y=80)
        buttonover_17.place(x=130,y=80)
        buttonover_18.place(x=180,y=80)
        buttonover_19.place(x=230,y=80)
        buttonover_20.place(x=280,y=80)
        buttonover_21.place(x=330,y=80)
        buttonover_22.place(x=380,y=80)
        buttonover_23.place(x=430,y=80)
        buttonover_24.place(x=480,y=80)
        buttonover_25.place(x=530,y=80)
        buttonover_26.place(x=580,y=80)
        buttonover_27.place(x=630,y=80)
        buttonover_28.place(x=680,y=80)
        buttonover_29.place(x=730,y=80)
        buttonover_30.place(x=780,y=80)

        buttonbelow_1.place(x=105,y=35)
        buttonbelow_2.place(x=155,y=35)
        buttonbelow_3.place(x=205,y=35)
        buttonbelow_4.place(x=255,y=35)
        buttonbelow_5.place(x=305,y=35)
        buttonbelow_6.place(x=355,y=35)
        buttonbelow_7.place(x=405,y=35)
        buttonbelow_8.place(x=455,y=35)
        buttonbelow_9.place(x=505,y=35)
        buttonbelow_10.place(x=555,y=35)
        buttonbelow_11.place(x=605,y=35)
        buttonbelow_12.place(x=655,y=35)
        buttonbelow_13.place(x=705,y=35)
        buttonbelow_14.place(x=755,y=35)
        buttonbelow_15.place(x=805,y=35)
        buttonbelow_16.place(x=105,y=105)
        buttonbelow_17.place(x=155,y=105)
        buttonbelow_18.place(x=205,y=105)
        buttonbelow_19.place(x=255,y=105)
        buttonbelow_20.place(x=305,y=105)
        buttonbelow_21.place(x=355,y=105)
        buttonbelow_22.place(x=405,y=105)
        buttonbelow_23.place(x=455,y=105)
        buttonbelow_24.place(x=505,y=105)
        buttonbelow_25.place(x=555,y=105)
        buttonbelow_26.place(x=605,y=105)
        buttonbelow_27.place(x=655,y=105)
        buttonbelow_28.place(x=705,y=105)
        buttonbelow_29.place(x=755,y=105)
        buttonbelow_30.place(x=805,y=105)
      
    elif WeaveMethod==0 and WeaveAmount==1:
        print('組數:',WeaveAmount)
       
        overline_label_1.place(x=20,y=10)
        overline_label_2.place(x=20,y=80)
        overline_label_3.place(x=20,y=150)

        belowline_label_1.place(x=20,y=40)
        belowline_label_2.place(x=20,y=110)
        belowline_label_3.place(x=20,y=180)

    elif WeaveMethod==0 and WeaveAmount==2:
        print('組數:',WeaveAmount)
        overline_label_1.place(x=20,y=10)
        overline_label_2.place(x=20,y=80)
        overline_label_3.place(x=20,y=150)
        overline_label_4.place(x=20,y=220)

        belowline_label_1.place(x=20,y=40)
        belowline_label_2.place(x=20,y=110)
        belowline_label_3.place(x=20,y=180)
        belowline_label_4.place(x=20,y=250)


def color_choose_overline():
        global Overline_Color_Code
        Overline_Color_Code = tk.colorchooser.askcolor(title ='選擇上線顏色', color ='blue')
        button_overline.configure(bg=Overline_Color_Code[1],fg=Overline_Color_Code[1]) 
        return Overline_Color_Code

def color_choose_belowline():
        global Belowline_Color_Code
        Belowline_Color_Code = tk.colorchooser.askcolor(title ='選擇下線顏色', color ='blue')
        button_belowline.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1])
        button_start.place(x=20,y=20)
        return Belowline_Color_Code

def color_choose_overline1():
    global Overline_Color_Code1
    Overline_Color_Code1 = tk.colorchooser.askcolor(title ='選擇上線顏色', color ='blue')
    buttonover_1.configure(bg=Overline_Color_Code1[1],fg=Overline_Color_Code1[1]) 
    buttonbelow_1.configure(bg=Overline_Color_Code1[1],fg=Overline_Color_Code1[1]) 
    return Overline_Color_Code1
def color_choose_overline2():
    global Overline_Color_Code2
    Overline_Color_Code2 = tk.colorchooser.askcolor(title ='選擇上線顏色', color ='blue')
    buttonover_2.configure(bg=Overline_Color_Code2[1],fg=Overline_Color_Code2[1]) 
    buttonbelow_2.configure(bg=Overline_Color_Code2[1],fg=Overline_Color_Code2[1])
    return Overline_Color_Code2
def color_choose_overline3():
    global Overline_Color_Code3
    Overline_Color_Code3 = tk.colorchooser.askcolor(title ='選擇上線顏色', color ='blue')
    buttonover_3.configure(bg=Overline_Color_Code3[1],fg=Overline_Color_Code3[1])
    buttonbelow_3.configure(bg=Overline_Color_Code3[1],fg=Overline_Color_Code3[1]) 
    return Overline_Color_Code3
def color_choose_overline4():
    global Overline_Color_Code4
    Overline_Color_Code4 = tk.colorchooser.askcolor(title ='選擇上線顏色', color ='blue')
    buttonover_4.configure(bg=Overline_Color_Code4[1],fg=Overline_Color_Code4[1]) 
    buttonbelow_4.configure(bg=Overline_Color_Code4[1],fg=Overline_Color_Code4[1]) 
    return Overline_Color_Code4
def color_choose_overline5():
    global Overline_Color_Code5
    Overline_Color_Code5 = tk.colorchooser.askcolor(title ='選擇上線顏色', color ='blue')
    buttonover_5.configure(bg=Overline_Color_Code5[1],fg=Overline_Color_Code5[1]) 
    buttonbelow_5.configure(bg=Overline_Color_Code5[1],fg=Overline_Color_Code5[1]) 
    return Overline_Color_Code5
def color_choose_overline6():
    global Overline_Color_Code6
    Overline_Color_Code6 = tk.colorchooser.askcolor(title ='選擇上線顏色', color ='blue')
    buttonover_6.configure(bg=Overline_Color_Code6[1],fg=Overline_Color_Code6[1]) 
    buttonbelow_6.configure(bg=Overline_Color_Code6[1],fg=Overline_Color_Code6[1]) 
    return Overline_Color_Code6
def color_choose_overline7():
    global Overline_Color_Code7
    Overline_Color_Code7 = tk.colorchooser.askcolor(title ='選擇上線顏色', color ='blue')
    buttonover_7.configure(bg=Overline_Color_Code7[1],fg=Overline_Color_Code7[1]) 
    buttonbelow_7.configure(bg=Overline_Color_Code7[1],fg=Overline_Color_Code7[1]) 
    return Overline_Color_Code7
def color_choose_overline8():
    global Overline_Color_Code8
    Overline_Color_Code8 = tk.colorchooser.askcolor(title ='選擇上線顏色', color ='blue')
    buttonover_8.configure(bg=Overline_Color_Code8[1],fg=Overline_Color_Code8[1]) 
    buttonbelow_8.configure(bg=Overline_Color_Code8[1],fg=Overline_Color_Code8[1]) 
    return Overline_Color_Code8
def color_choose_overline9():
    global Overline_Color_Code9
    Overline_Color_Code9 = tk.colorchooser.askcolor(title ='選擇上線顏色', color ='blue')
    buttonover_9.configure(bg=Overline_Color_Code9[1],fg=Overline_Color_Code9[1]) 
    buttonbelow_9.configure(bg=Overline_Color_Code9[1],fg=Overline_Color_Code9[1]) 
    return Overline_Color_Code9
def color_choose_overline10():
    global Overline_Color_Code10
    Overline_Color_Code10 = tk.colorchooser.askcolor(title ='選擇上線顏色', color ='blue')
    buttonover_10.configure(bg=Overline_Color_Code10[1],fg=Overline_Color_Code10[1]) 
    buttonbelow_10.configure(bg=Overline_Color_Code10[1],fg=Overline_Color_Code10[1]) 
    return Overline_Color_Code10
def color_choose_overline11():
    global Overline_Color_Code11
    Overline_Color_Code11 = tk.colorchooser.askcolor(title ='選擇上線顏色', color ='blue')
    buttonover_11.configure(bg=Overline_Color_Code11[1],fg=Overline_Color_Code11[1]) 
    buttonbelow_11.configure(bg=Overline_Color_Code11[1],fg=Overline_Color_Code11[1]) 
    return Overline_Color_Code11
def color_choose_overline12():
    global Overline_Color_Code12
    Overline_Color_Code12 = tk.colorchooser.askcolor(title ='選擇上線顏色', color ='blue')
    buttonover_12.configure(bg=Overline_Color_Code12[1],fg=Overline_Color_Code12[1]) 
    buttonbelow_12.configure(bg=Overline_Color_Code12[1],fg=Overline_Color_Code12[1]) 
    return Overline_Color_Code12
def color_choose_overline13():
    global Overline_Color_Code13
    Overline_Color_Code13 = tk.colorchooser.askcolor(title ='選擇上線顏色', color ='blue')
    buttonover_13.configure(bg=Overline_Color_Code13[1],fg=Overline_Color_Code13[1]) 
    buttonbelow_13.configure(bg=Overline_Color_Code13[1],fg=Overline_Color_Code13[1]) 
    return Overline_Color_Code13
def color_choose_overline14():
    global Overline_Color_Code14
    Overline_Color_Code14 = tk.colorchooser.askcolor(title ='選擇上線顏色', color ='blue')
    buttonover_14.configure(bg=Overline_Color_Code14[1],fg=Overline_Color_Code14[1]) 
    buttonbelow_14.configure(bg=Overline_Color_Code14[1],fg=Overline_Color_Code14[1]) 
    return Overline_Color_Code14
def color_choose_overline15():
    global Overline_Color_Code15
    Overline_Color_Code15 = tk.colorchooser.askcolor(title ='選擇上線顏色', color ='blue')
    buttonover_15.configure(bg=Overline_Color_Code15[1],fg=Overline_Color_Code15[1]) 
    buttonbelow_15.configure(bg=Overline_Color_Code15[1],fg=Overline_Color_Code15[1]) 
    return Overline_Color_Code15
def color_choose_overline16():
    global Overline_Color_Code16
    Overline_Color_Code16 = tk.colorchooser.askcolor(title ='選擇上線顏色', color ='blue')
    buttonover_16.configure(bg=Overline_Color_Code16[1],fg=Overline_Color_Code16[1]) 
    buttonbelow_16.configure(bg=Overline_Color_Code16[1],fg=Overline_Color_Code16[1]) 
    return Overline_Color_Code16
def color_choose_overline17():
    global Overline_Color_Code17
    Overline_Color_Code17 = tk.colorchooser.askcolor(title ='選擇上線顏色', color ='blue')
    buttonover_17.configure(bg=Overline_Color_Code17[1],fg=Overline_Color_Code17[1]) 
    buttonbelow_17.configure(bg=Overline_Color_Code17[1],fg=Overline_Color_Code17[1]) 
    return Overline_Color_Code17
def color_choose_overline18():
    global Overline_Color_Code18
    Overline_Color_Code18 = tk.colorchooser.askcolor(title ='選擇上線顏色', color ='blue')
    buttonover_18.configure(bg=Overline_Color_Code18[1],fg=Overline_Color_Code18[1]) 
    buttonbelow_18.configure(bg=Overline_Color_Code18[1],fg=Overline_Color_Code18[1]) 
    return Overline_Color_Code18
def color_choose_overline19():
    global Overline_Color_Code19
    Overline_Color_Code19 = tk.colorchooser.askcolor(title ='選擇上線顏色', color ='blue')
    buttonover_19.configure(bg=Overline_Color_Code19[1],fg=Overline_Color_Code19[1]) 
    buttonbelow_19.configure(bg=Overline_Color_Code19[1],fg=Overline_Color_Code19[1]) 
    return Overline_Color_Code19
def color_choose_overline20():
    global Overline_Color_Code20
    Overline_Color_Code20 = tk.colorchooser.askcolor(title ='選擇上線顏色', color ='blue')
    buttonover_20.configure(bg=Overline_Color_Code20[1],fg=Overline_Color_Code20[1]) 
    buttonbelow_20.configure(bg=Overline_Color_Code20[1],fg=Overline_Color_Code20[1]) 
    return Overline_Color_Code20
def color_choose_overline21():
    global Overline_Color_Code21
    Overline_Color_Code21 = tk.colorchooser.askcolor(title ='選擇上線顏色', color ='blue')
    buttonover_21.configure(bg=Overline_Color_Code21[1],fg=Overline_Color_Code21[1]) 
    buttonbelow_21.configure(bg=Overline_Color_Code21[1],fg=Overline_Color_Code21[1]) 
    return Overline_Color_Code21
def color_choose_overline22():
    global Overline_Color_Code22
    Overline_Color_Code22 = tk.colorchooser.askcolor(title ='選擇上線顏色', color ='blue')
    buttonover_22.configure(bg=Overline_Color_Code22[1],fg=Overline_Color_Code22[1]) 
    buttonbelow_22.configure(bg=Overline_Color_Code22[1],fg=Overline_Color_Code22[1]) 
    return Overline_Color_Code22
def color_choose_overline23():
    global Overline_Color_Code23
    Overline_Color_Code23 = tk.colorchooser.askcolor(title ='選擇上線顏色', color ='blue')
    buttonover_23.configure(bg=Overline_Color_Code23[1],fg=Overline_Color_Code23[1]) 
    buttonbelow_23.configure(bg=Overline_Color_Code23[1],fg=Overline_Color_Code23[1]) 
    return Overline_Color_Code23
def color_choose_overline24():
    global Overline_Color_Code24
    Overline_Color_Code24 = tk.colorchooser.askcolor(title ='選擇上線顏色', color ='blue')
    buttonover_24.configure(bg=Overline_Color_Code24[1],fg=Overline_Color_Code24[1]) 
    buttonbelow_24.configure(bg=Overline_Color_Code24[1],fg=Overline_Color_Code24[1]) 
    return Overline_Color_Code24
def color_choose_overline25():
    global Overline_Color_Code25
    Overline_Color_Code25 = tk.colorchooser.askcolor(title ='選擇上線顏色', color ='blue')
    buttonover_25.configure(bg=Overline_Color_Code25[1],fg=Overline_Color_Code25[1]) 
    buttonbelow_25.configure(bg=Overline_Color_Code25[1],fg=Overline_Color_Code25[1]) 
    return Overline_Color_Code25
def color_choose_overline26():
    global Overline_Color_Code26
    Overline_Color_Code26 = tk.colorchooser.askcolor(title ='選擇上線顏色', color ='blue')
    buttonover_26.configure(bg=Overline_Color_Code26[1],fg=Overline_Color_Code26[1]) 
    buttonbelow_26.configure(bg=Overline_Color_Code26[1],fg=Overline_Color_Code26[1]) 
    return Overline_Color_Code26
def color_choose_overline27():
    global Overline_Color_Code27
    Overline_Color_Code27 = tk.colorchooser.askcolor(title ='選擇上線顏色', color ='blue')
    buttonover_27.configure(bg=Overline_Color_Code27[1],fg=Overline_Color_Code27[1]) 
    buttonbelow_27.configure(bg=Overline_Color_Code27[1],fg=Overline_Color_Code27[1]) 
    return Overline_Color_Code27
def color_choose_overline28():
    global Overline_Color_Code28
    Overline_Color_Code28 = tk.colorchooser.askcolor(title ='選擇上線顏色', color ='blue')
    buttonover_28.configure(bg=Overline_Color_Code28[1],fg=Overline_Color_Code28[1]) 
    buttonbelow_28.configure(bg=Overline_Color_Code28[1],fg=Overline_Color_Code28[1]) 
    return Overline_Color_Code28
def color_choose_overline29():
    global Overline_Color_Code29
    Overline_Color_Code29 = tk.colorchooser.askcolor(title ='選擇上線顏色', color ='blue')
    buttonover_29.configure(bg=Overline_Color_Code29[1],fg=Overline_Color_Code29[1]) 
    buttonbelow_29.configure(bg=Overline_Color_Code29[1],fg=Overline_Color_Code29[1]) 
    return Overline_Color_Code29
def color_choose_overline30():
    global Overline_Color_Code30
    Overline_Color_Code30 = tk.colorchooser.askcolor(title ='選擇上線顏色', color ='blue')
    buttonover_30.configure(bg=Overline_Color_Code30[1],fg=Overline_Color_Code30[1]) 
    buttonbelow_30.configure(bg=Overline_Color_Code30[1],fg=Overline_Color_Code30[1]) 
    button_start.place(x=20,y=20)
    return Overline_Color_Code30


def color_choose_belowline1():
    global Belowline_Color_Code
    Belowline_Color_Code = tk.colorchooser.askcolor(title ='選擇下線顏色', color ='blue')
    buttonover_1.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1])
    buttonbelow_1.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1]) 
    return Belowline_Color_Code
def color_choose_belowline2():
    global Belowline_Color_Code
    Belowline_Color_Code = tk.colorchooser.askcolor(title ='選擇下線顏色', color ='blue')
    buttonover_2.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1])
    buttonbelow_2.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1]) 
    return Belowline_Color_Code
def color_choose_belowline3():
    global Belowline_Color_Code
    Belowline_Color_Code = tk.colorchooser.askcolor(title ='選擇下線顏色', color ='blue')
    buttonover_3.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1])
    buttonbelow_3.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1]) 
    return Belowline_Color_Code
def color_choose_belowline4():
    global Belowline_Color_Code
    Belowline_Color_Code = tk.colorchooser.askcolor(title ='選擇下線顏色', color ='blue')
    buttonover_4.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1])
    buttonbelow_4.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1]) 
    return Belowline_Color_Code
def color_choose_belowline5():
    global Belowline_Color_Code
    Belowline_Color_Code = tk.colorchooser.askcolor(title ='選擇下線顏色', color ='blue')
    buttonover_5.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1])
    buttonbelow_5.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1]) 
    return Belowline_Color_Code
def color_choose_belowline6():
    global Belowline_Color_Code
    Belowline_Color_Code = tk.colorchooser.askcolor(title ='選擇下線顏色', color ='blue')
    buttonover_6.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1])
    buttonbelow_6.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1]) 
    return Belowline_Color_Code
def color_choose_belowline7():
    global Belowline_Color_Code
    Belowline_Color_Code = tk.colorchooser.askcolor(title ='選擇下線顏色', color ='blue')
    buttonover_7.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1])
    buttonbelow_7.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1]) 
    return Belowline_Color_Code
def color_choose_belowline8():
    global Belowline_Color_Code
    Belowline_Color_Code = tk.colorchooser.askcolor(title ='選擇下線顏色', color ='blue')
    buttonover_8.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1])
    buttonbelow_8.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1]) 
    return Belowline_Color_Code
def color_choose_belowline9():
    global Belowline_Color_Code
    Belowline_Color_Code = tk.colorchooser.askcolor(title ='選擇下線顏色', color ='blue')
    buttonover_9.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1])
    buttonbelow_9.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1]) 
    return Belowline_Color_Code
def color_choose_belowline10():
    global Belowline_Color_Code
    Belowline_Color_Code = tk.colorchooser.askcolor(title ='選擇下線顏色', color ='blue')
    buttonover_10.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1])
    buttonbelow_10.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1]) 
    return Belowline_Color_Code
def color_choose_belowline11():
    global Belowline_Color_Code
    Belowline_Color_Code = tk.colorchooser.askcolor(title ='選擇下線顏色', color ='blue')
    buttonover_11.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1])
    buttonbelow_11.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1]) 
    return Belowline_Color_Code
def color_choose_belowline12():
    global Belowline_Color_Code
    Belowline_Color_Code = tk.colorchooser.askcolor(title ='選擇下線顏色', color ='blue')
    buttonover_12.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1])
    buttonbelow_12.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1]) 
    return Belowline_Color_Code
def color_choose_belowline13():
    global Belowline_Color_Code
    Belowline_Color_Code = tk.colorchooser.askcolor(title ='選擇下線顏色', color ='blue')
    buttonover_13.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1])
    buttonbelow_13.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1]) 
    return Belowline_Color_Code
def color_choose_belowline14():
    global Belowline_Color_Code
    Belowline_Color_Code = tk.colorchooser.askcolor(title ='選擇下線顏色', color ='blue')
    buttonover_14.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1])
    buttonbelow_14.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1]) 
    return Belowline_Color_Code
def color_choose_belowline15():
    global Belowline_Color_Code
    Belowline_Color_Code = tk.colorchooser.askcolor(title ='選擇下線顏色', color ='blue')
    buttonover_15.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1])
    buttonbelow_15.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1]) 
    return Belowline_Color_Code
def color_choose_belowline16():
    global Belowline_Color_Code
    Belowline_Color_Code = tk.colorchooser.askcolor(title ='選擇下線顏色', color ='blue')
    buttonover_16.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1])
    buttonbelow_16.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1]) 
    return Belowline_Color_Code
def color_choose_belowline17():
    global Belowline_Color_Code
    Belowline_Color_Code = tk.colorchooser.askcolor(title ='選擇下線顏色', color ='blue')
    buttonover_17.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1])
    buttonbelow_17.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1]) 
    return Belowline_Color_Code
def color_choose_belowline18():
    global Belowline_Color_Code
    Belowline_Color_Code = tk.colorchooser.askcolor(title ='選擇下線顏色', color ='blue')
    buttonover_18.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1])
    buttonbelow_18.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1]) 
    return Belowline_Color_Code
def color_choose_belowline19():
    global Belowline_Color_Code
    Belowline_Color_Code = tk.colorchooser.askcolor(title ='選擇下線顏色', color ='blue')
    buttonover_19.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1])
    buttonbelow_19.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1]) 
    return Belowline_Color_Code
def color_choose_belowline20():
    global Belowline_Color_Code
    Belowline_Color_Code = tk.colorchooser.askcolor(title ='選擇下線顏色', color ='blue')
    buttonover_20.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1])
    buttonbelow_20.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1]) 
    return Belowline_Color_Code
def color_choose_belowline21():
    global Belowline_Color_Code
    Belowline_Color_Code = tk.colorchooser.askcolor(title ='選擇上下線顏色', color ='blue')
    buttonover_21.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1])
    buttonbelow_21.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1]) 
    return Belowline_Color_Code
def color_choose_belowline22():
    global Belowline_Color_Code
    Belowline_Color_Code = tk.colorchooser.askcolor(title ='選擇下線顏色', color ='blue')
    buttonover_22.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1])
    buttonbelow_22.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1]) 
    return Belowline_Color_Code
def color_choose_belowline23():
    global Belowline_Color_Code
    Belowline_Color_Code = tk.colorchooser.askcolor(title ='選擇下線顏色', color ='blue')
    buttonover_23.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1])
    buttonbelow_23.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1]) 
    return Belowline_Color_Code
def color_choose_belowline24():
    global Belowline_Color_Code
    Belowline_Color_Code = tk.colorchooser.askcolor(title ='選擇下線顏色', color ='blue')
    buttonover_24.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1])
    buttonbelow_24.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1]) 
    return Belowline_Color_Code
def color_choose_belowline25():
    global Belowline_Color_Code
    Belowline_Color_Code = tk.colorchooser.askcolor(title ='選擇下線顏色', color ='blue')
    buttonover_25.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1])
    buttonbelow_25.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1]) 
    return Belowline_Color_Code
def color_choose_belowline26():
    global Belowline_Color_Code
    Belowline_Color_Code = tk.colorchooser.askcolor(title ='選擇下線顏色', color ='blue')
    buttonover_26.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1])
    buttonbelow_26.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1]) 
    return Belowline_Color_Code
def color_choose_belowline27():
    global Belowline_Color_Code
    Belowline_Color_Code = tk.colorchooser.askcolor(title ='選擇下線顏色', color ='blue')
    buttonover_27.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1])
    buttonbelow_27.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1]) 
    return Belowline_Color_Code
def color_choose_belowline28():
    global Belowline_Color_Code
    Belowline_Color_Code = tk.colorchooser.askcolor(title ='選擇下線顏色', color ='blue')
    buttonover_28.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1])
    buttonbelow_28.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1]) 
    return Belowline_Color_Code
def color_choose_belowline29():
    global Belowline_Color_Code
    Belowline_Color_Code = tk.colorchooser.askcolor(title ='選擇下線顏色', color ='blue')
    buttonover_29.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1])
    buttonbelow_29.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1]) 
    return Belowline_Color_Code
def color_choose_belowline30():
    global Belowline_Color_Code
    Belowline_Color_Code = tk.colorchooser.askcolor(title ='選擇下線顏色', color ='blue')
    buttonover_30.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1])
    buttonbelow_30.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1]) 
    button_start.place(x=20,y=20)
    return Belowline_Color_Code



def draw():
   
    cv = tk.Canvas(frame7, width=300, height=400)
    cv.grid(row=0, column=0)
    screen = turtle.TurtleScreen(cv)
    raw = turtle.RawTurtle(screen)
   
    

def draw2():
    canvas = tk.Canvas(frame8, width=330, height=390)
    canvas.grid(row=0, column=0)
    screen = turtle.TurtleScreen(canvas)
    raw = turtle.RawTurtle(screen)


    if WeaveMethod==0:#平織
        raw.hideturtle()
        raw.penup()
        raw.setposition(-150,-195)
        raw.pensize(10)
        raw.speed(0)

        
        raw.pendown()
        raw.color(Overline_Color_Code1[1])
        raw.setheading(90)
        raw.forward(400)
        raw.penup()
        raw.setheading(0)
        raw.forward(10)
        raw.pendown()
        raw.color(Overline_Color_Code2[1])
        raw.setheading(270)
        raw.forward(400)
        raw.penup()
        raw.setheading(0)
        raw.forward(10)
        raw.pendown()
        raw.color(Overline_Color_Code3[1])
        raw.setheading(90)
        raw.forward(400)
        raw.penup()
        raw.setheading(0)
        raw.forward(10)
        raw.pendown()
        raw.color(Overline_Color_Code4[1])
        raw.setheading(270)
        raw.forward(400)
        raw.penup()
        raw.setheading(0)
        raw.forward(10)
        raw.pendown()
        raw.color(Overline_Color_Code5[1])
        raw.setheading(90)
        raw.forward(400)
        raw.penup()
        raw.setheading(0)
        raw.forward(10)
        raw.pendown()
        raw.color(Overline_Color_Code6[1])
        raw.setheading(270)
        raw.forward(400)
        raw.penup()
        raw.setheading(0)
        raw.forward(10)
        raw.pendown()
        raw.color(Overline_Color_Code7[1])
        raw.setheading(90)
        raw.forward(400)
        raw.penup()
        raw.setheading(0)
        raw.forward(10)
        raw.pendown()
        raw.color(Overline_Color_Code8[1])
        raw.setheading(270)
        raw.forward(400)
        raw.penup()
        raw.setheading(0)
        raw.forward(10)
        raw.pendown()
        raw.color(Overline_Color_Code9[1])
        raw.setheading(90)
        raw.forward(400)
        raw.penup()
        raw.setheading(0)
        raw.forward(10)
        raw.pendown()
        raw.color(Overline_Color_Code10[1])
        raw.setheading(270)
        raw.forward(400)
        raw.penup()
        raw.setheading(0)
        raw.forward(10)
        raw.pendown()

        raw.color(Overline_Color_Code11[1])
        raw.setheading(90)
        raw.forward(400)
        raw.penup()
        raw.setheading(0)
        raw.forward(10)
        raw.pendown()
        raw.color(Overline_Color_Code12[1])
        raw.setheading(270)
        raw.forward(400)
        raw.penup()
        raw.setheading(0)
        raw.forward(10)
        raw.pendown()
        raw.color(Overline_Color_Code13[1])
        raw.setheading(90)
        raw.forward(400)
        raw.penup()
        raw.setheading(0)
        raw.forward(10)
        raw.pendown()
        raw.color(Overline_Color_Code14[1])
        raw.setheading(270)
        raw.forward(400)
        raw.penup()
        raw.setheading(0)
        raw.forward(10)
        raw.pendown()
        raw.color(Overline_Color_Code15[1])
        raw.setheading(90)
        raw.forward(400)
        raw.penup()
        raw.setheading(0)
        raw.forward(10)
        raw.pendown()
        raw.color(Overline_Color_Code16[1])
        raw.setheading(270)
        raw.forward(400)
        raw.penup()
        raw.setheading(0)
        raw.forward(10)
        raw.pendown()
        raw.color(Overline_Color_Code17[1])
        raw.setheading(90)
        raw.forward(400)
        raw.penup()
        raw.setheading(0)
        raw.forward(10)
        raw.pendown()
        raw.color(Overline_Color_Code18[1])
        raw.setheading(270)
        raw.forward(400)
        raw.penup()
        raw.setheading(0)
        raw.forward(10)
        raw.pendown()
        raw.color(Overline_Color_Code19[1])
        raw.setheading(90)
        raw.forward(400)
        raw.penup()
        raw.setheading(0)
        raw.forward(10)
        raw.pendown()
        raw.color(Overline_Color_Code20[1])
        raw.setheading(270)
        raw.forward(400)
        raw.penup()
        raw.setheading(0)
        raw.forward(10)
        raw.pendown()

        raw.color(Overline_Color_Code21[1])
        raw.setheading(90)
        raw.forward(400)
        raw.penup()
        raw.setheading(0)
        raw.forward(10)
        raw.pendown()
        raw.color(Overline_Color_Code22[1])
        raw.setheading(270)
        raw.forward(400)
        raw.penup()
        raw.setheading(0)
        raw.forward(10)
        raw.pendown()
        raw.color(Overline_Color_Code23[1])
        raw.setheading(90)
        raw.forward(400)
        raw.penup()
        raw.setheading(0)
        raw.forward(10)
        raw.pendown()
        raw.color(Overline_Color_Code24[1])
        raw.setheading(270)
        raw.forward(400)
        raw.penup()
        raw.setheading(0)
        raw.forward(10)
        raw.pendown()
        raw.color(Overline_Color_Code25[1])
        raw.setheading(90)
        raw.forward(400)
        raw.penup()
        raw.setheading(0)
        raw.forward(10)
        raw.pendown()
        raw.color(Overline_Color_Code26[1])
        raw.setheading(270)
        raw.forward(400)
        raw.penup()
        raw.setheading(0)
        raw.forward(10)
        raw.pendown()
        raw.color(Overline_Color_Code27[1])
        raw.setheading(90)
        raw.forward(400)
        raw.penup()
        raw.setheading(0)
        raw.forward(10)
        raw.pendown()
        raw.color(Overline_Color_Code28[1])
        raw.setheading(270)
        raw.forward(400)
        raw.penup()
        raw.setheading(0)
        raw.forward(10)
        raw.pendown()
        raw.color(Overline_Color_Code29[1])
        raw.setheading(90)
        raw.forward(400)
        raw.penup()
        raw.setheading(0)
        raw.forward(10)
        raw.pendown()
        raw.color(Overline_Color_Code30[1])
        raw.setheading(270)
        raw.forward(400)
        raw.penup()
        screen.mainloop()




if __name__ == '__main__':
    
    window = tk.Tk()
    window.title('Weaving Simulator v0.0')
    window.geometry('1300x900')
    window.configure(background='white')
    window.iconbitmap('Logo.ico')                                                 #圖片檔丟入資料夾

    frame1 = tk.Frame(window,bg='white',width=1050, height=295)
    frame1.place(x=0,y=0)  
    label = tk.PhotoImage(file='永續復興USR計畫_LOGO完整.png')                    #未來要改放設計的label
    tk.Label(frame1, image=label).place(x=0,y=0)             

    frame2 = tk.Frame(window,bg='white',width=285, height=80)
    frame2.place(x=0,y=295) 
    frame3 = tk.Frame(window,bg='white',width=285, height=70)
    frame3.place(x=0,y=375) 
    frame4 = tk.Frame(window,bg='white',width=285, height=700)
    frame4.place(x=300,y=295)

    frame5 = tk.Frame(window,bg='white',width=850, height=900)
    frame5.place(x=0,y=445) 

    frame7 = tk.Frame(window,bg='white',width=300, height=900)
    frame7.place(x=850,y=450)
    frame8 = tk.Frame(window,bg='white',width=550, height=900)
    frame8.place(x=850,y=290) 

    weavemethod_label = tk.Label(frame2, text='織法',font=('微軟正黑體',12))      #中文出亂碼 https://ithelp.ithome.com.tw/articles/10232644
    weavemethod_label.place(x=20,y=10)
    weavemethod = ttk.Combobox(frame2, values=[
                                        '平織',
                                        '挑織',
                                        '斜紋織'],font=('微軟正黑體',12),state="readonly")
    weavemethod.place(x=80,y=10)
    WeaveMethod = weavemethod.current()
    weavemethod.bind("<<ComboboxSelected>>", SelectWeaveMethod)

    weaveamount_label = tk.Label(frame2, text='組數',font=('微軟正黑體',12))
    weaveamount_label.place(x=20,y=45)
    weaveamount = ttk.Combobox(frame2, values=[
                                             '30',
                                             '40',
                                             '50'],font=('微軟正黑體',12),state="readonly")
    weaveamount.place(x=80,y=45)
    WeaveAmount = weaveamount.current()
    weaveamount.bind("<<ComboboxSelected>>", SelectWeaveAmount)

    overline_label = tk.Label(frame3, text='上線',font=('微軟正黑體',12))
    button_overline = tk.Button(frame3, text='選擇上線顏色', command=lambda :color_choose_overline())
    belowline_label = tk.Label(frame3, text='下線',font=('微軟正黑體',12))
    button_belowline = tk.Button(frame3, text='選擇下線顏色', command=lambda :color_choose_belowline())

    overline_label_1 = tk.Label(frame5, text='上線',font=('微軟正黑體',12))
    overline_label_2 = tk.Label(frame5, text='上線',font=('微軟正黑體',12))
    overline_label_3 = tk.Label(frame5, text='上線',font=('微軟正黑體',12))
    overline_label_4 = tk.Label(frame5, text='上線',font=('微軟正黑體',12))

    belowline_label_1 = tk.Label(frame5, text='下線',font=('微軟正黑體',12))   
    belowline_label_2 = tk.Label(frame5, text='下線',font=('微軟正黑體',12))
    belowline_label_3 = tk.Label(frame5, text='下線',font=('微軟正黑體',12))
    belowline_label_4 = tk.Label(frame5, text='下線',font=('微軟正黑體',12))
        
    buttonover_1 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_overline1())
    buttonover_2 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_overline2())
    buttonover_3 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_overline3())
    buttonover_4 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_overline4())
    buttonover_5 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_overline5())
    buttonover_6 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_overline6())
    buttonover_7 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_overline7())
    buttonover_8 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_overline8())
    buttonover_9 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_overline9())
    buttonover_10 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_overline10())
    buttonover_11 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_overline11())
    buttonover_12 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_overline12())
    buttonover_13 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_overline13())
    buttonover_14 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_overline14())
    buttonover_15 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_overline15())
    buttonover_16 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_overline16())
    buttonover_17 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_overline17())
    buttonover_18 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_overline18())
    buttonover_19 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_overline19())
    buttonover_20 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_overline20())
    buttonover_21 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_overline21())
    buttonover_22 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_overline22())
    buttonover_23 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_overline23())
    buttonover_24 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_overline24())
    buttonover_25 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_overline25())
    buttonover_26 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_overline26())
    buttonover_27 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_overline27())
    buttonover_28 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_overline28())
    buttonover_29 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_overline29())
    buttonover_30 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_overline30())

    buttonbelow_1 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_belowline1())
    buttonbelow_2 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_belowline2())
    buttonbelow_3 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_belowline3())
    buttonbelow_4 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_belowline4())
    buttonbelow_5 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_belowline5())
    buttonbelow_6 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_belowline6())
    buttonbelow_7 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_belowline7())
    buttonbelow_8 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_belowline8())
    buttonbelow_9 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_belowline9())
    buttonbelow_10 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_belowline10())
    buttonbelow_11 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_belowline11())
    buttonbelow_12 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_belowline12())
    buttonbelow_13 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_belowline13())
    buttonbelow_14 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_belowline14())
    buttonbelow_15 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_belowline15())
    buttonbelow_16 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_belowline16())
    buttonbelow_17 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_belowline17())
    buttonbelow_18 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_belowline18())
    buttonbelow_19 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_belowline19())
    buttonbelow_20 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_belowline20())
    buttonbelow_21 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_belowline21())
    buttonbelow_22 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_belowline22())
    buttonbelow_23 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_belowline23())
    buttonbelow_24 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_belowline24())
    buttonbelow_25 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_belowline25())
    buttonbelow_26 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_belowline26())
    buttonbelow_27 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_belowline27())
    buttonbelow_28 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_belowline28())
    buttonbelow_29 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_belowline29())
    buttonbelow_30 = tk.Button(frame5, text='', height=1, width=2, bg ='lightgray', command=lambda :color_choose_belowline30())

    button_start = tk.Button(frame4, text='Start', font=('Arial',14), command=lambda :draw2(),width=15,height=2)
    button_exit = tk.Button(frame4, text='Exit', font=('Arial',12), command=window.destroy)
    

    window.mainloop()