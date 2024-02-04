#Design a basic calculator with basic arithmatic operations.#

#import libraries for GUI and Maths
import tkinter as tk
from math import sqrt

root = tk.Tk()

#size of the calculator
root.geometry("300x350")

#title of the calculator 
root.title("BASIC CALCULATOR")

calculation= ""

#function to add symbols and making complete string
def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0,calculation)
    
#function to evalvate and get the results
def eavalvate_calculation():
    global calculation
    try:
        result= str(eval(calculation))
        calculation= ""
        text_result.delete(1.0,"end")
        text_result.insert(1.0,result)
        
    except:
        clear_field()
        text_result.insert(1.0,"Error")

#function to clear fields      
def clear_field():
    global calculation
    calculation =""
    text_result.delete(1.0,"end")

#function to display result of sqrt √.
def root_result():
    result = sqrt(float(calculation))
    text_result.delete(1.0,"end")
    text_result.insert(1.0,result)

#function to delete last letter
def delete_last_letter():
    global calculation
    calculation = calculation[:-1]
    text_result.delete(1.0,"end")
    text_result.insert(1.0,calculation)
    

#added text box to display input and result
text_result = tk.Text(root,height = 1, width=16, font=("arial",24))
text_result.grid(columnspan=5)


#Buttons for row 2
B1 = tk.Button(root, text="C", command=clear_field ,width=4, font=("arial",20))
B1.grid(row=2, column=1)

B2 = tk.Button(root, text="x", command=delete_last_letter,width=4, font=("arial",20))
B2.grid(row=2, column=2)

B3= tk.Button(root, text="√" , command=lambda:root_result(),width=4, font=("arial",20))
B3.grid(row=2, column=3)

B4= tk.Button(root, text="%" , command=lambda:add_to_calculation("%"),width=4, font=("arial",20))
B4.grid(row=2, column=4)

#Buttons for row 3
B5 = tk.Button(root, text="1" , command=lambda:add_to_calculation(1), width=4, font=("arial",20))
B5.grid(row=3, column=1)

B6= tk.Button(root, text="2" , command=lambda:add_to_calculation(2),width=4, font=("arial",20))
B6.grid(row=3, column=2)

B7 = tk.Button(root, text="3" , command=lambda:add_to_calculation(3),width=4, font=("arial",20))
B7.grid(row=3, column=3)

B8= tk.Button(root, text="/" , command=lambda:add_to_calculation("/"),width=4, font=("arial",20))
B8.grid(row=3, column=4)

#Buttons for row 4
B9 = tk.Button(root, text="4" , command=lambda:add_to_calculation(4),width=4, font=("arial",20))
B9.grid(row=4, column=1)

B10 = tk.Button(root, text="5" , command=lambda:add_to_calculation(5),width=4, font=("arial",20))
B10.grid(row=4, column=2)

B11 = tk.Button(root, text="6" , command=lambda:add_to_calculation(6),width=4, font=("arial",20))
B11.grid(row=4, column=3)

B12= tk.Button(root, text="*" , command=lambda:add_to_calculation("*"),width=4, font=("arial",20))
B12.grid(row=4, column=4)


#Buttons for row 5
B13 = tk.Button(root, text="7" , command=lambda:add_to_calculation(7),width=4, font=("arial",20))
B13.grid(row=5, column=1)

B14 = tk.Button(root, text="8" , command=lambda:add_to_calculation(8),width=4, font=("arial",20))
B14.grid(row=5, column=2)

B15 = tk.Button(root, text="9" , command=lambda:add_to_calculation(9),width=4, font=("arial",20))
B15.grid(row=5, column=3)

B16= tk.Button(root, text="+" , command=lambda:add_to_calculation("+"),width=4, font=("arial",20))
B16.grid(row=5, column=4)

#Buttons for row 6
B17 = tk.Button(root, text="." ,  command=lambda:add_to_calculation("."),width=4, font=("arial",20))
B17.grid(row=6, column=1)

B18 = tk.Button(root, text="0" , command=lambda:add_to_calculation(0),width=4, font=("arial",20))
B18.grid(row=6, column=2)

B19 = tk.Button(root, text="=" , command=eavalvate_calculation,width=4, font=("arial",20))
B19.grid(row=6, column=3)

B20 = tk.Button(root, text="-" , command=lambda:add_to_calculation("-"),width=4, font=("arial",20))
B20.grid(row=6, column=4)

root.mainloop()
