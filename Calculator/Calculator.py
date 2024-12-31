# importing the required libraries  
import tkinter  
from tkinter import *  
from tkinter import messagebox  
  
# setting the initial values of some variables  
var = ""  
A = 0  
operator = ""  
  
# defining the function for Button 1  
def button_1_is_Clicked():  
    global var  
    var = var + "1"  
    the_data.set(var)  
  
# defining the function for Button 2  
def button_2_is_Clicked():  
    global var  
    var = var + "2"  
    the_data.set(var)  
  
# defining the function for Button 3  
def button_3_is_Clicked():  
    global var  
    var = var + "3"  
    the_data.set(var)  
  
# defining the function for Button 4  
def button_4_is_Clicked():  
    global var  
    var = var + "4"  
    the_data.set(var)  
  
# defining the function for Button 5  
def button_5_is_Clicked():  
    global var  
    var = var + "5"  
    the_data.set(var)  
  
# defining the function for Button 6  
def button_6_is_Clicked():  
    global var  
    var = var + "6"  
    the_data.set(var)  
  
# defining the function for Button 7  
def button_7_is_Clicked():  
    global var  
    var = var + "7"  
    the_data.set(var)  
  
# defining the function for Button 8  
def button_8_is_Clicked():  
    global var  
    var = var + "8"  
    the_data.set(var)  
  
# defining the function for Button 9  
def button_9_is_Clicked():  
    global var  
    var = var + "9"  
    the_data.set(var)  
  
# defining the function for Button 0  
def button_0_is_Clicked():  
    global var  
    var = var + "0"  
    the_data.set(var)  
  
# defining the function for Button +  
def button_Add_is_Clicked():  
    global A  
    global var  
    global operator  
    A = float(var)  
    operator = "+"  
    var = var + "+"  
    the_data.set(var)  
  
# defining the function for Button -  
def button_Sub_is_Clicked():  
    global A  
    global var  
    global operator  
    A = float(var)  
    operator = "-"  
    var = var + "-"  
    the_data.set(var)  
  
# defining the function for Button *  
def button_Mul_is_Clicked():  
    global A  
    global var  
    global operator  
    A = float(var)  
    operator = "*"  
    var = var + "*"  
    the_data.set(var)  
  
# defining the function for Button /  
def button_Div_is_Clicked():  
    global A  
    global var  
    global operator  
    A = float(var)  
    operator = "/"  
    var = var + "/"  
    the_data.set(var)  
  
# defining the function for Button =  
def button_Equal_is_Clicked():  
    global A  
    global var  
    global operator  
    A = float(var)  
    operator = "="  
    var = var + "="  
    the_data.set(var)  
  
# defining the function for Button C  
def button_C_is_Clicked():  
    global A  
    global var  
    global operator  
    var = ""  
    A = 0  
    operator = ""  
    the_data.set(var)  
  
# defining the function to display result  
def res():  
    global A  
    global operator  
    global var  
    var2 = var  
    if operator == "+":  
        a = float((var2.split("+")[1]))  
        x = A + a  
        the_data.set(x)  
        var = str(x)  
    elif operator == "-":  
        a = float((var2.split("-")[1]))  
        x = A - a  
        the_data.set(x)  
        var = str(x)  
    elif operator == "*":  
        a = float((var2.split("*")[1]))  
        x = A * a  
        the_data.set(x)  
        var = str(x)  
    elif operator == "/":  
        a = float((var2.split("/")[1]))  
        if a == 0:  
            messagebox.showerror("Division by 0 Not Allowed.")  
            A == ""  
            var = ""  
            the_data.set(var)  
        else:  
            x = float(A/a)  
            the_data.set(x)  
            var = str(x)  
  
# creating an object of the Tk() class  
guiWindow = tkinter.Tk()  
# setting the size of the window  
guiWindow.geometry("320x500+400+400")  
# disabling the resize option for better UI  
guiWindow.resizable(0, 0)  
# setting the title of the Calculator window  
guiWindow.title("GUI Calculator")  
  
# creating the label for the window  
the_data = StringVar()  
guiLabel = Label(  
    guiWindow,  
    text = "Label",  
    anchor = SE,  
    font = ("Cambria Math", 20),  
    textvariable = the_data,  
    background = "#ffffff",  
    fg = "#000000"  
)  
# using the pack() method  
guiLabel.pack(expand = True, fill = "both")  
  
# creating the frames for the buttons  
# first frame  
frameOne = Frame(guiWindow, bg = "#000000")  
frameOne.pack(expand = True, fill = "both") # frame can expand if it gets some space  
  
# second frame  
frameTwo = Frame(guiWindow, bg = "#000000")  
frameTwo.pack(expand = True, fill = "both")  
  
# third frame  
frameThree = Frame(guiWindow, bg = "#000000")  
frameThree.pack(expand = True, fill = "both")  
  
# fourth frame  
frameFour = Frame(guiWindow, bg = "#000000")  
frameFour.pack(expand = True, fill = "both")  
  
# creating buttons for each frame  
# buttons for first frame  
# button 1  
buttonONE = Button(  
    frameOne,  
    text = "1",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_1_is_Clicked  
)  
# placing buttons side by side  
buttonONE.pack(side = LEFT, expand = True, fill = "both")  
  
# button 2  
buttonTWO = Button(  
    frameOne,  
    text = "2",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_2_is_Clicked  
)  
# placing buttons side by side  
buttonTWO.pack(side = LEFT, expand = True, fill = "both")  
  
# button 3  
buttonTHREE = Button(  
    frameOne,  
    text = "3",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_3_is_Clicked  
)  
# placing buttons side by side  
buttonTHREE.pack(side = LEFT, expand = True, fill = "both")  
  
# button C  
buttonC = Button(  
    frameOne,  
    text = "C",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_C_is_Clicked  
)  
# placing buttons side by side  
buttonC.pack(side = LEFT, expand = True, fill = "both")  
  
# buttons for second frame  
# button 4  
buttonFOUR = Button(  
    frameTwo,  
    text = "4",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_4_is_Clicked  
)  
# placing buttons side by side  
buttonFOUR.pack(side = LEFT, expand = True, fill = "both")  
  
# button 5  
buttonFIVE = Button(  
    frameTwo,  
    text = "5",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_5_is_Clicked  
)  
# placing buttons side by side  
buttonFIVE.pack(side = LEFT, expand = True, fill = "both")  
  
# button 6  
buttonSIX = Button(  
    frameTwo,  
    text = "6",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_6_is_Clicked  
)  
# placing buttons side by side  
buttonSIX.pack(side = LEFT, expand = True, fill = "both")  
  
# button +  
buttonADD = Button(  
    frameTwo,  
    text = "+",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_Add_is_Clicked  
)  
# placing buttons side by side  
buttonADD.pack(side = LEFT, expand = True, fill = "both")  
  
# buttons for third frame  
# button 7  
buttonSEVEN = Button(  
    frameThree,  
    text = "7",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_7_is_Clicked  
)  
# placing buttons side by side  
buttonSEVEN.pack(side = LEFT, expand = True, fill = "both")  
  
# button 8  
buttonEIGHT = Button(  
    frameThree,  
    text = "8",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_8_is_Clicked  
)  
# placing buttons side by side  
buttonEIGHT.pack(side = LEFT, expand = True, fill = "both")  
  
# button 9  
buttonNINE = Button(  
    frameThree,  
    text = "9",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_9_is_Clicked  
)  
# placing buttons side by side  
buttonNINE.pack(side = LEFT, expand = True, fill = "both")  
  
# button -  
buttonSUB = Button(  
    frameThree,  
    text = "-",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_Sub_is_Clicked  
)  
# placing buttons side by side  
buttonSUB.pack(side = LEFT, expand = True, fill = "both")  
  
# buttons for fourth frame  
# button 0  
buttonZERO = Button(  
    frameFour,  
    text = "0",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_0_is_Clicked  
)  
# placing buttons side by side  
buttonZERO.pack(side = LEFT, expand = True, fill = "both")  
  
# button *  
buttonMUL = Button(  
    frameFour,  
    text = "*",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_Mul_is_Clicked  
)  
# placing buttons side by side  
buttonMUL.pack(side = LEFT, expand = True, fill = "both")  
  
# button /  
buttonDIV = Button(  
    frameFour,  
    text = "/",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_Div_is_Clicked  
)  
# placing buttons side by side  
buttonDIV.pack(side = LEFT, expand = True, fill = "both")  
  
# button +  
buttonEQUAL = Button(  
    frameFour,  
    text = "=",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = res  
)  
# placing buttons side by side  
buttonEQUAL.pack(side = LEFT, expand = True, fill = "both")  
  
# running the GUI  
guiWindow.mainloop()  