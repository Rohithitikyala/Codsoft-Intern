from tkinter import*
import string
import random
import pyperclip
def generator():
    s_a=string.ascii_lowercase
    c_a=string.ascii_uppercase
    n=string.digits
    s_c=string.punctuation
    all=s_a+c_a+n+s_c
    p_l=int(lb.get())
    if choice.get()==1:
        pf.insert(0,random.sample(s_a,p_l))
    if choice.get()==2:
        pf.insert(0,random.sample(s_a,c_a,p_l))
    if choice.get()==3:
        pf.insert(0,random.sample(all,p_l))
pen=Tk()
choice=IntVar()
pen.config(bg="grey")
font=("times new roman",14,"bold")
pl=Label(pen,text=" Password Generator", font=("times new roman",20,"bold"),bg="grey", fg="white")
pl.grid(pady=10)
wrb=Radiobutton(pen,text="week",value=1,variable=choice,font=font)
wrb.grid(pady=5)
mrb=Radiobutton(pen,text="medium",value=2,variable=choice,font=font)
mrb.grid(pady=5)
srb=Radiobutton(pen,text="strong",value=3,variable=choice,font=font)
srb.grid(pady=5)
plength=Label(pen,text=" Password length", font=font)
plength.grid(pady=5)
lb=Spinbox(pen, from_= 8,to_=16,width=10,font=font)
lb.grid(pady=5)
gb=Button(pen,text="Generate",font=font,command=generator)
gb.grid(pady=5)
pf=Entry(pen,width=30,bd=2)
pf.grid()
c=Button(pen,text='copy',font=font)
c.grid(pady=5)
