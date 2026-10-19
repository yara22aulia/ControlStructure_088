import tkinter as tk
import tkinter.messagebox as msg
top = tkinter.Tk() 
CheckVar1=tk.StringVar()
C=tk.Checkbutton(top,text="Gender, check kalau laki-laki",
                variable=CheckVar1,
                onvalue="Mr. ",offvalue="Ms. ",height=5)
C.pack()
L1=tk.label(top,text="Nama: ")
L1.pack()
E1=tk.Entry(top,bd=5)
E1.pack()
def helloCallBack():
    msg.showinfo("Belajar GUI","Assalamu'alaikum! "
                CheckVar1.get()+E1.get())
v1=tk.Button(top,text="Klik Saya!", commad=helloCallBack)
v1.pack()
top.mainloop()




