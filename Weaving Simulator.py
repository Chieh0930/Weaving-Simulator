#v0.0 
# -*- coding: utf-8 -*-

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
    button_overline.place(x=155, y=370)

def color_choose_overline():
    global Overline_Color_Code
    Overline_Color_Code = tk.colorchooser.askcolor(title ='選擇上線顏色', color ='blue')
    button_overline.configure(bg=Overline_Color_Code[1],fg=Overline_Color_Code[1]) 
    button_belowline.place(x=155, y=405)
    return Overline_Color_Code

def color_choose_belowline():
    global Belowline_Color_Code
    Belowline_Color_Code = tk.colorchooser.askcolor(title ='選擇下線顏色', color ='blue')
    button_belowline.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1])
    button_start.place(x=100, y=440)
    return Belowline_Color_Code

def draw():
   
    canvas = tk.Canvas(window, width=300, height=400)
    canvas.place(x=350, y=440)
    screen = turtle.TurtleScreen(canvas)
    raw = turtle.RawTurtle(screen)

    if WeaveMethod==0:#平織
        raw.hideturtle()
        raw.penup()
        raw.setposition(-150,-200)
        raw.pensize(10)
        raw.speed(0)
        for i in range(20):
    
            raw.pendown()
            raw.color(Overline_Color_Code[1])
            raw.forward(300)
            raw.penup()
            raw.setheading(90)
            raw.forward(10)
            raw.setheading(180)
            raw.color(Belowline_Color_Code[1])
            raw.pendown()
            raw.forward(300)
            raw.penup()
            raw.setheading(90)
            raw.forward(10)
            raw.setheading(0)
            raw.pendown()

        screen.mainloop()

if __name__ == '__main__':

    window = tk.Tk()
    window.title('Weaving Simulator v0.0')
    window.geometry('900x900')
    window.configure(background='white')
    window.iconbitmap('Logo.ico')                                            #圖片檔丟入資料夾

    label = tk.PhotoImage(file='永續復興USR計畫_LOGO完整.png')               #未來要改放設計的label
    tk.Label(window, image=label).place(x=0, y=0)                           

    weavemethod_label = tk.Label(window, text='織法',font=('微軟正黑體',12)) #中文出亂碼 https://ithelp.ithome.com.tw/articles/10232644
    weavemethod_label.place(x=30, y=300)
    weavemethod = ttk.Combobox(window, values=[
                                        '平織',
                                        '挑織',
                                        '斜紋織'],font=('微軟正黑體',12),state="readonly")
    weavemethod.place(x=100, y=300)
    WeaveMethod = weavemethod.current()
    weavemethod.bind("<<ComboboxSelected>>", SelectWeaveMethod)

    weaveamount_label = tk.Label(window, text='組數',font=('微軟正黑體',12))
    weaveamount_label.place(x=30, y=335)
    weaveamount = ttk.Combobox(window, values=[
                                             '30',
                                             '40',
                                             '50'],font=('微軟正黑體',12),state="readonly")
    weaveamount.place(x=100, y=335)
    WeaveAmount = weaveamount.current()
    weaveamount.bind("<<ComboboxSelected>>", SelectWeaveAmount)

    
    overline_label = tk.Label(window, text='上線',font=('微軟正黑體',12))
    overline_label.place(x=30, y=370)
    button_overline = tk.Button(window, text='選擇上線顏色', command=lambda :color_choose_overline())

    belowline_label = tk.Label(window, text='下線',font=('微軟正黑體',12))
    belowline_label.place(x=30, y=405)
    button_belowline = tk.Button(window, text='選擇下線顏色', command=lambda :color_choose_belowline())

    button_start = tk.Button(window, text='Start', font=('Arial',14), command=lambda :draw(),width=15,height=2)

    button_exit = tk.Button(window, text='Exit', font=('Arial',12), command=window.destroy)
    button_exit.place(x=30, y=510)

    window.mainloop()
