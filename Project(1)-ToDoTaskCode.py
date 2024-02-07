#!/usr/bin/env python
# coding: utf-8

# In[98]:


'''To create To-Do List application using by GUI
    and commmand line application in python'''

from tkinter import *
import re

root = Tk()

#width and height
root.geometry("400x650")

#Title for our program
root.title("To-Do-List")
root.resizable(False,False)

#task list
task_list=[]
currFieldvalue = ''
actionMode = 'ADD'

def modify(filepath, from_, to_):
    file = open(filepath,"r+")
    text = file.read()
    pattern = from_
    splitted_text = re.split(pattern,text)
    modified_text = to_.join(splitted_text)
    with open(filepath, 'w') as file:
        file.write(modified_text)

def on_key_press(event):
    global currFieldvalue
    global actionMode
    fieldValue = field.get()
    
    if fieldValue.strip() != "" and actionMode != "ADD": 
        if fieldValue.strip() != currFieldvalue.strip():
            btn_text.set("EDIT")
            button["state"] = "normal"
        else:
            btn_text.set("ADD")
            button["state"] = "disabled"
    else:
        btn_text.set("ADD")
        button["state"] = "normal"
        actionMode = 'ADD'


def singleClickTask(event):
    btn_text.set("ADD")
    entry_field_value.set('')
    
    
#a funtion to get user enter input
def addTask():
    global currFieldvalue
    global task_list
    action_btn = btn_text.get()
    if action_btn == "ADD":
        task = field.get()

        if task.strip() in task_list:
            res = messagebox.askquestion(title="Warning!", message=task + " is already in list. Do you want to continue?")
            if res == "no":
                entry_field_value.set('')
                return

        if task:
            field.delete(0,END)
            with open("tasklist.txt",'a') as taskfile:
                taskfile.write(f"\n{task}")
                task_list.append(task)
                listbox.insert(END,task)

    if action_btn == "EDIT":
        task = field.get()
    
        if task:
            field.delete(0,END)
            modify("tasklist.txt", currFieldvalue.strip(), task.strip())
            task_list=[]
            listbox.delete(0,'end')
            openTaskFile()
            btn_text.set("ADD")

def updateTask(event):
    global actionMode
    global currFieldvalue
    selected_list_item = event.widget.get(event.widget.curselection()[0])
    entry_field_value.set(selected_list_item.strip())
    currFieldvalue = selected_list_item
    actionMode = "EDIT"
    button["state"] = "disabled"
    

#a funtion to delete task
def deleteTask():
    global actionMode
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt",'w') as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")
        listbox.delete(ANCHOR)
        entry_field_value.set('')
        btn_text.set("ADD")
        button["state"] = "normal"
        actionMode = 'ADD'
    
def openTaskFile():
    
    try:
        global task_list
        with open("tasklist.txt","r") as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            if task !='\n':
                task_list.append(task.strip())
                listbox.insert(END,task.strip())

    except:
        file=open('tasklist.txt','w')
        file.close()

    
# Heading for our list

heading = Label(root,text="TO-DO LIST\n[ALL TASK] ", font="arial 20 bold", fg ="white",bg = "Green")
heading.pack(padx=100,pady=16)

#frame and entry space
frame = Frame(root,width=400,height=50,bg="white")
frame.place(x=0,y=180)

entry_field_value= StringVar()
field = Entry(frame,width=18,font="arial 20",bd=0, textvariable=entry_field_value)
field.place(x=10,y=7)

#Button for adding  task .
btn_text = StringVar()
button = Button(frame, textvariable=btn_text,font="arial 20 bold", width=6, bg="#5a95ff", fg="#fff",bd=0 ,command=addTask)
btn_text.set("ADD")
button.place(x=300,y=0)


#listbox.
f1=Frame(root,bd=3,width=700,height=200,bg="green")
f1.pack(pady=(160,0))

listbox = Listbox(f1,font=("arial",12),width=40,height=16,bg="green",cursor ="hand2",selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH,padx=2)
scrollbar=Scrollbar(f1)
scrollbar.pack(side=RIGHT,fill=BOTH)


openTaskFile()


#delete option
Delete = Button(root,text="Delete",font="arial 18 bold",width=5, bg="#5a95ff",fg="#fff",bd=0 , command=deleteTask).pack()

listbox.bind('<<ListboxSelect>>', singleClickTask)
listbox.bind('<Double-1>', updateTask)
field.bind('<KeyRelease>', on_key_press)

root.mainloop()


# In[ ]:




