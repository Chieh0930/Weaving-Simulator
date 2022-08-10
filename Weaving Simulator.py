#v0.0 

import tkinter as tk
import tkinter.ttk as ttk
import turtle
from tkinter.colorchooser import askcolor

def SelectWeaveMethod(event):
    global WeaveMethod
    WeaveMethod = weavemethod.current()
    button_overline.grid(row=2,column=1,padx=5,pady=5)

def draw():
   
    canvas = tk.Canvas(window, width=300, height=400)
    canvas.grid(row=1,column=6,rowspan=10)

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

def color_choose_overline():
    global Overline_Color_Code
    Overline_Color_Code = tk.colorchooser.askcolor(title ='選擇上線顏色', color ='blue')
    button_overline.configure(bg=Overline_Color_Code[1],fg=Overline_Color_Code[1]) 
    button_belowline.grid(row=3,column=1,padx=5,pady=5)
    return Overline_Color_Code

def color_choose_belowline():
    global Belowline_Color_Code
    Belowline_Color_Code = tk.colorchooser.askcolor(title ='選擇下線顏色', color ='blue')
    button_belowline.configure(bg=Belowline_Color_Code[1],fg=Belowline_Color_Code[1])
    button_start.grid(row=4,column=0,columnspan=3,padx=10,pady=1)
    return Belowline_Color_Code



if __name__ == '__main__':

    window = tk.Tk()
    window.title('Weaving Simulator v0.0')
    window.geometry('800x800')
    window.configure(background='white')
    window.iconbitmap('Logo.ico')

    label = tk.PhotoImage(file='永續復興USR計畫_LOGO完整.png')#未來要改放設計的label
    tk.Label(window, image=label).grid(row=0,column=0,columnspan=10)

    weavemethod_label = tk.Label(window, text='織法',font=('微軟正黑體',12))
    weavemethod_label.grid(row=1,column=0,padx=5,pady=5)
    weavemethod = ttk.Combobox(window, values=[
                                        '平織',
                                        '挑織',
                                        '斜紋織'],font=('微軟正黑體',12),state="readonly")
    weavemethod.grid(row=1,column=1)
    #weavemethod.current(0)
    WeaveMethod = weavemethod.current()
    weavemethod.bind("<<ComboboxSelected>>", SelectWeaveMethod)

    overline_label = tk.Label(window, text='上線',font=('微軟正黑體',12))
    overline_label.grid(row=2,column=0,padx=5,pady=5)
    button_overline = tk.Button(window, text='選擇上線顏色', command=lambda :color_choose_overline())

    belowline_label = tk.Label(window, text='下線',font=('微軟正黑體',12))
    belowline_label.grid(row=3,column=0,padx=5,pady=5)
    button_belowline = tk.Button(window, text='選擇下線顏色', command=lambda :color_choose_belowline())
    

    button_start = tk.Button(window, text='Start', font=('Arial',14), command=lambda :draw(),width=15,height=2)

    button_exit = tk.Button(window, text='Exit', font=('Arial',12), command=window.destroy)
    button_exit.grid(row=5,column=0,padx=10,pady=10)



    window.mainloop()
    
