# coding:utf-8
from Tkinter import *
import tk_display_scripts as dis
import datetime
import threading

#全局变量设置
state_now_flag = 1   # 0 停止 1 打开
d1 = 0 # 上一次时间
d2 = 0 # 下一次时间

#初始化Tk
main_window = Tk()

#设置窗口标题
main_window.title( "**科技")

#窗口大小显示
main_window.geometry("1024x768")

# 设置窗口是否可以变化长/宽，False不可变，True可变，默认为True
main_window.resizable(width=False, height=False)

# 设置标签
Label(main_window, text="永诚科技喷水控制系统", bg="blue", font=("Arial",14), width=19, height=2).place(x=375, y=0)

#按键  当前函数按下按键在界面text上打印信息
def printhello():
    global state_now_flag
    if state_now_flag == 0:
        state_now_flag = 1
    else:
        state_now_flag = 0

    time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    global d1
    global d2
    if state_now_flag == 0:
        t.insert(END,time_now + "   喷水开始" + '\n')
        d1 = datetime.datetime.now()
    else:
        d2 = datetime.datetime.now()
        t.insert(END,time_now + "   喷水结束,此次喷水时间："+ str((d2 - d1).seconds)+"秒" + '\n')
    dis.ch_text(main_window,printhello,state_now_flag)
    t.see(END)
    t.update()
Button(main_window, text="当前状态：停止喷水", command=printhello, width=20, height=4, bg="red", fg="black").place(x=50, y=200)
t = Text()
t.place(x=0, y=300,width=380,height=100)

#####################################################################################################
##############################  第二线程  ############################################################
t2 = Text()
t2.place(x=700, y=30,width=140,height=18)
def fun_timer():
    global timer
    time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    t2.insert(END,time_now+'\r')
    t2.see(END)
    t2.update()
    timer = threading.Timer(0.2,fun_timer)
    timer.start()
timer = threading.Timer(0.2,fun_timer)
timer.start()




mainloop()