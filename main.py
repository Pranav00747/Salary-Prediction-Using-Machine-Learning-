from tkinter import *
import tkinter.font
from tkinter.ttk import Combobox
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from matplotlib.colors  import ListedColormap
import numpy as np

def create_main_ui():
    t = Tk()
    t.geometry("690x490+220+100")
    t.title("ML Annual Salary of Employees")
    t.resizable(False, False)
    t.overrideredirect(1)
    c = Canvas(t, width=690, height=490)
    c.create_rectangle(0, 0, 690, 490, fill="gray")
    c.create_line(0, 0, 0, 490, fill="#D15605", width=15)
    c.create_line(685, 0, 685, 490, fill="#D15605" , width=5)
    c.create_line(0, 485, 685, 485, fill="#D15605", width=5)
    c.create_rectangle(0, 0, 690, 40, fill="#D15605")
    c.place(x=0, y=0)
    lab1 = Label(c, text='ML Annual Salary of Employees', background='#D15605',
                 fg='white', font=tkinter.font.Font(family="MS Sans Serif", size=10))
    lab1.place(x=20, y=10)
    def lab1_e(e):
     lab1.config(fg='black', font=tkinter.font.Font(family="MS Sans Serif", size=12))
    def lab1_l(e):
     lab1.config(fg='white', font=tkinter.font.Font(family="MS Sans Serif", size=10))
    lab1.bind("<Enter>", lab1_e)
    lab1.bind("<Leave>", lab1_l)

    close = Label(c, text='x', background='#D15605', fg='white', font=tkinter.font.Font(family="MS Sans Serif", size=12))
    close.place(x=660, y=10 )

    def close_enter(event):
         close.config(fg='black', font=tkinter.font.Font(family="MS Sans Serif", size=14))
    def close_leave(event):
        close.config(fg='white', font=tkinter.font.Font(family="MS Sans Serif", size=12))
    def close_click(event):
        t.destroy()

    close.bind("<Enter>", close_enter)
    close.bind("<Leave>", close_leave)
    close.bind("<Button>", close_click)
    lab2 = Label(c, text='Employee 1 Name', background='gray', fg='white', font=tkinter.font.Font(family="MS Sans Serif", size=10))
    lab2.place(x=20, y=100 )
    lab3 = Label(c, text='Employee 2 Name', background='gray', fg='white',
                 font=tkinter.font.Font(family="MS Sans Serif", size=10))
    lab3.place(x=20, y=140)
    labb4 = Label(c, text='Employee 3 Name', background='gray', fg='white',
                 font=tkinter.font.Font(family="MS Sans Serif", size=10))
    labb4.place(x=20, y=180)

    labb5 = Label(c, text='Employee 4 Name', background='gray', fg='white',
                 font=tkinter.font.Font(family="MS Sans Serif", size=10))
    labb5.place(x=20, y=220)
    lab4 = Label(c, text='Basic Pay', background='gray', fg='white', font=tkinter.font.Font(family="MS Sans Serif", size=10))
    lab4.place(x=300, y=100)
    lab5 = Label(c, text='Basic Pay', background='gray', fg='white',
                 font=tkinter.font.Font(family="MS Sans Serif", size=10))
    lab5.place(x=300, y=140)
    labb6 = Label(c, text='Basic Pay', background='gray', fg='white',
                 font=tkinter.font.Font(family="MS Sans Serif", size=10))
    labb6.place(x=300, y=180)
    labb7 = Label(c, text='Basic Pay', background='gray', fg='white',
                 font=tkinter.font.Font(family="MS Sans Serif", size=10))
    labb7.place(x=300, y=220)
    lab6 = Label(c, text='Annual', background='gray', fg='white',
                 font=tkinter.font.Font(family="MS Sans Serif", size=10))
    lab6.place(x=510, y=100)
    lab7 = Label(c, text='Annual', background='gray', fg='white',
                 font=tkinter.font.Font(family="MS Sans Serif", size=10))
    lab7.place(x=510, y=140)
    labb8 = Label(c, text='Annual', background='gray', fg='white',
                 font=tkinter.font.Font(family="MS Sans Serif", size=10))
    labb8.place(x=510, y=180)

    labb9 = Label(c, text='Annual', background='gray', fg='white',
                 font=tkinter.font.Font(family="MS Sans Serif", size=10))
    labb9.place(x=510, y=220)

    lab7 = Label(c, text='Annual', background='gray', fg='white',
                 font=tkinter.font.Font(family="MS Sans Serif", size=10))
    lab7.place(x=510, y=140)
    labb8 = Label(c, text='Annual', background='gray', fg='white',
                  font=tkinter.font.Font(family="MS Sans Serif", size=10))
    labb8.place(x=510, y=180)

    labb9 = Label(c, text='Annual', background='gray', fg='white',
                  font=tkinter.font.Font(family="MS Sans Serif", size=10))
    labb9.place(x=510, y=220)

    labb10 = Label(c, text='Employee 5 Name', background='gray', fg='white',
                  font=tkinter.font.Font(family="MS Sans Serif", size=10))
    labb10.place(x=20, y=260)
    labb11 = Label(c, text='Employee 6 Name', background='gray', fg='white',
                  font=tkinter.font.Font(family="MS Sans Serif", size=10))
    labb11.place(x=20, y=300)
    labb12 = Label(c, text='Basic Pay', background='gray', fg='white',
                 font=tkinter.font.Font(family="MS Sans Serif", size=10))
    labb12.place(x=300, y=260)
    labb13 = Label(c, text='Basic Pay', background='gray', fg='white',
                 font=tkinter.font.Font(family="MS Sans Serif", size=10))
    labb13.place(x=300, y=300)
    labb14 = Label(c, text='Annual', background='gray', fg='white',
                  font=tkinter.font.Font(family="MS Sans Serif", size=10))
    labb14.place(x=510, y=260)
    labb15 = Label(c, text='Annual', background='gray', fg='white',
                  font=tkinter.font.Font(family="MS Sans Serif", size=10))
    labb15.place(x=510, y=300)

    edt1str = StringVar()
    edt2str = StringVar()
    edt3str = StringVar()
    edt4str = StringVar()
    edt5str = StringVar()
    edt6str = StringVar()
    edt7str = StringVar()
    edt8str = StringVar()
    edt9str = StringVar()
    edt10str = StringVar()
    edt11str = StringVar()
    edt12str = StringVar()
    edt13str = StringVar()
    edt14str = StringVar()
    edt15str = StringVar()
    edt16str = StringVar()
    edt17str = StringVar()
    edt18str = StringVar()
    edit1 = Entry(c, textvariable=edt1str, bd=2, background='white')
    edit1.place(x=150, y=100)
    edit2 = Entry(c, textvariable=edt2str, bd=2, background='white')
    edit2.place(x=380, y=100)
    edit3 = Entry(c, textvariable=edt3str, bd=2, background='white', width=16)
    edit3.place(x=570, y=100)
    edit4 = Entry(c, textvariable=edt4str, bd=2, background='white')
    edit4.place(x=150, y=140)
    edit5 = Entry(c, textvariable=edt5str, bd=2, background='white')
    edit5.place(x=380, y=140)
    edit6 = Entry(c, textvariable=edt6str, bd=2, background='white', width=16)
    edit6.place(x=570, y=140)
    edit7 = Entry(c, textvariable=edt7str, bd=2, background='white')
    edit7.place(x=150, y=180)
    edit8 = Entry(c, textvariable=edt8str, bd=2, background='white')
    edit8.place(x=380, y=180)
    edit9 = Entry(c, textvariable=edt9str, bd=2, background='white', width=16)
    edit9.place(x=570, y=180)
    edit10 = Entry(c, textvariable=edt10str, bd=2, background='white')
    edit10.place(x=150, y=220)
    edit11 = Entry(c, textvariable=edt11str, bd=2, background='white')
    edit11.place(x=380, y=220)
    edit12 = Entry(c, textvariable=edt12str, bd=2, background='white', width=16)
    edit12.place(x=570, y=220)
    edit13 = Entry(c, textvariable=edt13str, bd=2, background='white')
    edit13.place(x=150, y=260)
    edit14 = Entry(c, textvariable=edt14str, bd=2, background='white')
    edit14.place(x=380, y=260)
    edit15 = Entry(c, textvariable=edt15str, bd=2, background='white', width=16)
    edit15.place(x=570, y=260)
    edit16 = Entry(c, textvariable=edt16str, bd=2, background='white')
    edit16.place(x=150, y=300)
    edit17 = Entry(c, textvariable=edt17str, bd=2, background='white')
    edit17.place(x=380, y=300)
    edit18 = Entry(c, textvariable=edt18str, bd=2, background='white', width=16)
    edit18.place(x=570, y=300)
    label1 = Label(c, text="Accuracy:", background='gray', fg='white',
                 font=tkinter.font.Font(family="MS Sans Serif", size=10))
    label1.place(x=50, y=400)
    label2 = Label(c, text="", background='gray', fg='white',
                   font=tkinter.font.Font(family="MS Sans Serif", size=10), width=1)
    label2.place(x=120, y=400)

    label3 = Label(c, text="Confuse matrix:", background='gray', fg='white',
                   font=tkinter.font.Font(family="MS Sans Serif", size=10))
    label3.place(x=250, y=400)
    label4 = Label(c, text="", background='gray', fg='white',
                   font=tkinter.font.Font(family="MS Sans Serif", size=10), width=1)
    label4.place(x=350, y=400)
    label5 = Label(c, text="Select:", background='gray', fg='white',
                   font=tkinter.font.Font(family="MS Sans Serif", size=12))
    label6 = Label(c, text="Designed by Pranav Kulkarni", background='gray', fg='white',
                   font=tkinter.font.Font(family="MS Sans Serif", size=12), width=25)
    label6.place(x=400, y=360)

    def btn_clk():
       arr1 = []
       arr2 = []
       arr1.append(int(edt2str.get()))
       arr2.append(int(edt3str.get()))
       arr1.append(int(edt5str.get()))
       arr2.append(int(edt6str.get()))
       arr1.append(int(edt8str.get()))
       arr2.append(int(edt9str.get()))
       arr1.append(int(edt11str.get()))
       arr2.append(int(edt12str.get()))
       arr1.append(int(edt14str.get()))
       arr2.append(int(edt15str.get()))
       arr1.append(int(edt17str.get()))
       arr2.append(int(edt18str.get()))
       print(arr1)
       print(arr2)
       xtrain, xtest, ytrain, ytest = train_test_split(arr1, arr2, test_size=0.25,
                                                  random_state=0)
       sc = StandardScaler()
       #xtrain = sc.fit_transform(xtrain)
      # xtest = sc.transform(xtest)
       classify = LogisticRegression(random_state=0)
       #classify.fit(xtrain, ytrain)
       #y_pred = classify.predict(xtest)
       #c = confusion_matrix(ytest, y_pred)
       #print(c)
       #print(accuracy_score(ytest, y_pred))
       plt.title("Salary Prtediction Scatter")
       plt.xlabel("Basic Pay")
       plt.ylabel("Annual")
       plt.scatter(xtest, ytest, c='red')
       plt.scatter(xtrain, ytrain, c='blue')
       plt.legend()
       plt.show()
       plt.title("Salary Prtediction Plot")
       plt.xlabel("Basic Pay")
       plt.ylabel("Annual")
       plt.plot(xtest, ytest)
       plt.plot(xtrain, ytrain)
       plt.legend()
       plt.show()

    def clear_ck():
         edt1str.set('')
         edt2str.set('')
         edt3str.set('')
         edt4str.set('')
         edt5str.set('')
         edt6str.set('')
         edt7str.set('')
         edt8str.set('')
         edt9str.set('')
         edt10str.set('')
         edt11str.set('')
         edt12str.set('')
         edt13str.set('')
         edt14str.set('')
         edt15str.set('')
         edt16str.set('')
         edt17str.set('')
         edt18str.set('')


    
    btn1 = Button(c, text="Get Prediction", command = btn_clk, background='#D15605', fg='white',
                  font=tkinter.font.Font(family="MS Sans Serif", size=8), width=22, height=2)
    btn1.place(x=220, y=440)
    def btn1_e(e):
     btn1.config(fg='black',
                  font=tkinter.font.Font(family="MS Sans Serif", size=10))
    def btn1_l(e):
     btn1.config(fg='white',
                  font=tkinter.font.Font(family="MS Sans Serif", size=8))
    btn1.bind("<Enter>", btn1_e)
    btn1.bind("<Leave>", btn1_l)


    btn2 = Button(c, text="Clear", command=clear_ck, background='#D15605', fg='white',
                  font=tkinter.font.Font(family="MS Sans Serif", size=8), width=8, height=2)
    btn2.place(x=380, y=440)
    def btn2_e(e):
     btn2.config(fg='black',
                  font=tkinter.font.Font(family="MS Sans Serif", size=10))
    def btn2_l(e):
     btn2.config(fg='white',
                  font=tkinter.font.Font(family="MS Sans Serif", size=8))
    btn2.bind("<Enter>", btn2_e)
    btn2.bind("<Leave>", btn2_l)

    def moved_win(e):
     t.geometry("+"+str(int(e.x))+"+"+str(int(e.y)))

    c.bind("<B1-Motion>", moved_win)
    t.mainloop()

if __name__ == '__main__':
   create_main_ui()