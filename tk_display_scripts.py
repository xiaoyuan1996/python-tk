# coding:utf-8
from Tkinter import *

def interface2(variable_valve_state_start,variable_valve_state_shutdown,variable_valve_state_end):
    #初始化
    interface2=Toplevel()
    interface2.title("永诚科技喷水控制系统")  # 设置窗口标题
    interface2.geometry("1024x768")  # 窗口大小显示
    interface2.resizable(width=False, height=False)  # 设置窗口是否可以变化长/宽，False不可变，True可变，默认为True

    #剩余时间模块设计
    Label(interface2, text="剩余时间：", font=("Arial", 12), width=10, height=2).place(x=300, y=100)
    time_remain = Text(interface2)
    time_remain.place(x=310, y=150, width=200, height=20)

    #自动控制时间模块设计
    Label(interface2, text="自动控制时间：", font=("Arial", 12), width=15, height=2).place(x=200, y=200)
    time_stable = Text(interface2)
    time_stable.place(x=210, y=250, width=200, height=20)

    #启动动作模块设计
    Label(interface2, text="启动动作：", font=("Arial", 12), width=15, height=2).place(x=580, y=200)
    state_start = Text(interface2)
    state_start.place(x=610, y=250, width=200, height=20)
    state_start.insert(END, variable_valve_state_start + '\n')
    def state_start():
        pass
    Button(interface2, text="启动", command=state_start, width=20, height=4, bg="gray", fg="black").place(x=350, y=450,width=80,height=30)  # 确定按键


    #急停动作模块设计
    Label(interface2, text="急停动作：", font=("Arial", 12), width=15, height=2).place(x=180, y=350)
    state_shutdown = Text(interface2)
    state_shutdown.place(x=210, y=400, width=200, height=20)
    state_shutdown.insert(END, variable_valve_state_shutdown + '\n')
    def state_shutdown():
        pass
    Button(interface2, text="急停", command=state_shutdown, width=20, height=4, bg="gray", fg="black").place(x=550, y=450,width=80,height=30)  # 确定按键


    #停止动作模块设计
    Label(interface2, text="停止动作：", font=("Arial", 12), width=15, height=2).place(x=580, y=350)
    state_end = Text(interface2)
    state_end.place(x=610, y=400, width=200, height=20)
    state_end.insert(END, variable_valve_state_end + '\n')
    def state_end():
        pass
    Button(interface2, text="停止", command=state_end, width=20, height=4, bg="gray", fg="black").place(x=450, y=450,width=80,height=30)  # 确定按键

    #配置和退出按钮
    def state_configure():
        pass
    Button(interface2, text="配置", command=state_configure, width=20, height=4, bg="gray", fg="black").place(x=400, y=500,width=80,height=30)  # 确定按键

    def state_exit():
        interface2.destroy()
    Button(interface2, text="退出", command=state_exit, width=20, height=4, bg="gray", fg="black").place(x=500, y=500,width=80,height=30)  # 确定按键

    #面板2开启循环
    interface2.mainloop()