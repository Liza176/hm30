from tkinter import *
from tkinter import ttk
import random


tk = Tk()
tk.geometry('500x500')
tk.title('Chose a number game')



num = ''
random_num = random.randint(1,100)
print(random_num)
count = 5
flag = True
     
def bt1():
    global num
    global flag
    if flag == True:
        num += '1'

def bt2():
    global num
    global flag
    if flag == True:
        num += '2'

def bt3():
    global num
    global flag
    if flag == True:
        num += '3'

def bt4():
    global num
    global flag
    if flag == True:
        num += '4'

def bt5():
    global num
    global flag
    if flag == True:
        num += '5'

def bt6():
    global num
    global flag
    if flag == True:
        num += '6'

def bt7():
    global num
    global flag
    if flag == True:
        num += '7'
    
def bt8():
    global num
    global flag
    if flag == True:
        num += '8'

def bt9():
    global num
    global flag
    if flag == True:
        num += '9'

def bt0():
    global num
    global flag
    if flag == True:
        num += '0'

def b_or_m():
    global random_num
    global num
    global count

    global flag
    if flag == True:
        if int(num) < random_num:
            btn_b_or_m['text']='число больше'
            num = ''
            btn_num['text'] = 'Неверно'
            pop()

        elif int(num) > random_num:
            btn_b_or_m['text']='число меньше'
            num = ''
            btn_num['text'] = 'Неверно'
            pop()
        else:
            btn_b_or_m['text']=''
            btn_num['text'] = (f'Вы выиграли за {5-count} попыток')


        
def send():
    global flag
    if flag == True:
        b_or_m()

def pop():
    global flag
    global count

    if flag == True:
        count -= 1
        btn_pop['text'] = count
    # print(count)    
    if int(count) == 0:
        print(2)
        btn_num['text'] = 'Вы проиграли '
        flag = False

        




btn_1 = ttk.Button(text='1', command=bt1)
btn_1.place(x=30,y=450)
btn_2 = ttk.Button(text='2', command=bt2)
btn_2.place(x=120,y=450)
btn_3 = ttk.Button(text='3', command=bt3)
btn_3.place(x=210,y=450)
btn_4 = ttk.Button(text='4', command=bt4)
btn_4.place(x=300,y=450)
btn_5 = ttk.Button(text='5', command=bt5)
btn_5.place(x=390,y=450)
btn_6 = ttk.Button(text='6', command=bt6)
btn_6.place(x=30,y=400)
btn_7 = ttk.Button(text='7', command=bt7)
btn_7.place(x=120,y=400)
btn_8 = ttk.Button(text='8', command=bt8)
btn_8.place(x=210,y=400)
btn_9 = ttk.Button(text='9', command=bt9)
btn_9.place(x=300,y=400)
btn_0 = ttk.Button(text='0', command=bt0)
btn_0.place(x=390,y=400)

btn_send = ttk.Button(text='Send', command=send)
btn_send.place(x=390,y=350)

btn_num = ttk.Button(text='')
btn_num.place(x=210,y=50)


btn_b_or_m = ttk.Button(text='')
btn_b_or_m.place(x=30,y=100)

btn_pop = ttk.Button(text='5')
btn_pop.place(x=390,y=100)



tk.mainloop()