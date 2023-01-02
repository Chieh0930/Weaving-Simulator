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

def SelectWeaveAmount(event):
    global WeaveAmount
    WeaveAmount = weaveamount.current()
    #button_overline.place(x=125,y=0)
    #button_1.place(x=80,y=10)

def color_choose_overline(i):
    global Overline_Color_Code
    Overline_Color_Code = tk.colorchooser.askcolor(title ='選擇上線顏色', color ='blue')
    #button_overline.configure(bg=Overline_Color_Code[1],fg=Overline_Color_Code[1]) 
    #button_belowline.place(x=125,y=35)
    my_button[i].configure(bg=Overline_Color_Code[1],fg=Overline_Color_Code[1]) 
    #button_2.place(x=105,y=35)
    return Overline_Color_Code

def color_choose_overline1():
    global Overline_Color_Code
    Overline_Color_Code = tk.colorchooser.askcolor(title ='選擇上線顏色', color ='blue')
    #button_overline.configure(bg=Overline_Color_Code[1],fg=Overline_Color_Code[1]) 
    #button_belowline.place(x=125,y=35)
    button_1.configure(bg=Overline_Color_Code[1],fg=Overline_Color_Code[1]) 
    #button_2.place(x=105,y=35)
    return Overline_Color_Code

def color_choose_overline3():
    global Overline_Color_Code
    Overline_Color_Code = tk.colorchooser.askcolor(title ='選擇上線顏色', color ='blue')
    #button_overline.configure(bg=Overline_Color_Code[1],fg=Overline_Color_Code[1]) 
    #button_belowline.place(x=125,y=35)
    button_3.configure(bg=Overline_Color_Code[1],fg=Overline_Color_Code[1]) 
    #button_4.place(x=155,y=35)
    return Overline_Color_Code

def color_choose_belowline2():
    global Belowline_Color_Code
    Belowline_Color_Code = tk.colorchooser.askcolor(title ='選擇下線顏色', color ='blue')
    #button_belowline.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1])
    button_2.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1])
    #button_3.place(x=130,y=10)
    return Belowline_Color_Code

def color_choose_belowline4():
    global Belowline_Color_Code
    Belowline_Color_Code = tk.colorchooser.askcolor(title ='選擇下線顏色', color ='blue')
    #button_belowline.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1])
    button_4.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1])
    button_start.place(x=20,y=0)
    return Belowline_Color_Code

def draw():
   
    canvas = tk.Canvas(frame7, width=300, height=400)
    canvas.grid(row=0, column=0)
    screen = turtle.TurtleScreen(canvas)
    raw = turtle.RawTurtle(screen)


if __name__ == '__main__':
    
    window = tk.Tk()
    window.title('Weaving Simulator v0.0')
    window.geometry('1150x900')
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
    frame4.place(x=0,y=445) 

    frame5 = tk.Frame(window,bg='white',width=300, height=900)
    frame5.place(x=300,y=300) 

    frame6 = tk.Frame(window,bg='white',width=300, height=900)
    frame6.place(x=370,y=380)

    frame7 = tk.Frame(window,bg='white',width=300, height=900)
    frame7.place(x=700,y=450) 

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

    overline_label = tk.Label(frame5, text='上線',font=('微軟正黑體',12))
    overline_label.place(x=20,y=10)
    button_1 = tk.Button(frame5, text='1', height=1, width=2, command=lambda :color_choose_overline1())
    button_3 = tk.Button(frame5, text='3', height=1, width=2, command=lambda :color_choose_overline3())

    overline_label = tk.Label(frame5, text='下線',font=('微軟正黑體',12))
    overline_label.place(x=20,y=40)
    button_2 = tk.Button(frame5, text='顏色2', height=1, width=2, command=lambda :color_choose_belowline2())
    button_4 = tk.Button(frame5, text='顏色4', height=1, width=2, command=lambda :color_choose_belowline4())
    
    overline_label = tk.Label(frame5, text='上線',font=('微軟正黑體',12))
    overline_label.place(x=20,y=80)
    overline_label = tk.Label(frame5, text='下線',font=('微軟正黑體',12))
    overline_label.place(x=20,y=110)

    my_button = [[None]*2]*30

    '''for i in range (2):
         for j in range(30):
             my_button[i] = tk.Button(frame6, text='顏色', height=1, width=2, command=lambda :color_choose_overline(j))
             #my_button[i][j].place(x=80,y=10)
             my_button[i].grid(row = i, column = j)
             #my_button[i][j] = tk.colorchooser.askcolor(title ='選擇下線顏色', color ='blue')'''

    items = []
    buttontest = [[None]*2]*30

    for item in ('A','B','C','D'):
        tk.Button(frame6, text=item, height=1, width=2, command=lambda: items.append(item)).pack()
        #tk.Button(frame6, text=item, height=1, width=2, command=lambda: items.append(item)).pack()
    frame6.bind('<KeyPress-A>', lambda : color_choose_belowline2())

    
    button_1.place(x=80,y=10)
    button_2.place(x=105,y=35)
    button_3.place(x=130,y=10)
    button_4.place(x=155,y=35)


    '''overline_label = tk.Label(frame3, text='上線',font=('微軟正黑體',12))
    overline_label.place(x=20,y=0)
    button_overline = tk.Button(frame3, text='選擇上線顏色', command=lambda :color_choose_overline())

    belowline_label = tk.Label(frame3, text='下線',font=('微軟正黑體',12))
    belowline_label.place(x=20,y=35)
    button_belowline = tk.Button(frame3, text='選擇下線顏色', command=lambda :color_choose_belowline())'''

    button_start = tk.Button(frame4, text='Start', font=('Arial',14), command=lambda :draw(),width=15,height=2)
    button_exit = tk.Button(frame4, text='Exit', font=('Arial',12), command=window.destroy)
    

    window.mainloop()
