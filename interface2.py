# coding:utf-8
from tkinter import *
import interface3 as itf3
import Globalvar as glo
import threading
import Software_API as API

def interface2():
    #初始化
    interface2=Toplevel()
    interface2.title("永诚科技喷水控制系统")  # 设置窗口标题
    interface2.geometry("1024x768")  # 窗口大小显示
    interface2.resizable(width=False, height=False)  # 设置窗口是否可以变化长/宽，False不可变，True可变，默认为True

    #剩余时间模块设计
    Label(interface2, text="剩余时间：", font=("Arial", 12), width=10, height=2).place(x=300, y=100)
    time_remain = Text(interface2)
    time_remain.place(x=310, y=150, width=200, height=20)

    #####################################################################################################
    ##############################  第二线程  ############################################################

    glo.set("time_remain",int(glo.get("list_time")[0]) * 3600 + int(glo.get("list_time")[1]) * 60 + int(glo.get("list_time")[2]))
    remain_time = glo.get("time_remain")
    time_remain.delete(1.0, END)
    time_remain.insert(END, str(itv2time(remain_time)))
    time_remain.update()
    def fun_timer():
        global timer

        remain_time = glo.get("time_remain")
        time_remain.delete(1.0, END)
        time_remain.insert(END,str(itv2time(remain_time)))
        time_remain.update()

        if (remain_time !=0):
            glo.set("time_remain",remain_time - 1 )
            timer = threading.Timer(1, fun_timer)
            timer.start()
        else:
            API.end()
            timer.cancel()

    #####################################################################################################
    #自动控制时间模块设计
    Label(interface2, text="自动控制时间：", font=("Arial", 12), width=15, height=2).place(x=200, y=200)
    time_stable = Text(interface2)
    time_stable.place(x=210, y=250, width=200, height=20)
    list_time_temp = glo.get("list_time")
    time_stable.insert(END, str(list_time_temp[0]) + ':' + str(list_time_temp[1]) + ':' + str(list_time_temp[2])  + '\r')


    list_state_now=glo.get("list_state_now")

    #停止动作模块设计
    Label(interface2, text="停止动作：", font=("Arial", 12), width=15, height=2).place(x=580, y=350)
    state_end = Text(interface2)
    state_end.place(x=610, y=400, width=120, height=18)
    state_end.insert(END, list_state_now[1] + '\r')
    def state_end():
        global timer
        timer.cancel()
        API.end()
        glo.set("time_remain", int(glo.get("list_time")[0]) * 60 + int(glo.get("list_time")[1]) * 60 + int(glo.get("list_time")[2]))
        remain_time = glo.get("time_remain")
        time_remain.delete(1.0, END)
        time_remain.insert(END, str(itv2time(remain_time)))
        time_remain.update()

    Button(interface2, text="停止", command=state_end, width=20, height=4, bg="gray", fg="black").place(x=450, y=450,width=80,height=30)  # 确定按键


    #启动动作模块设计
    Label(interface2, text="启动动作：", font=("Arial", 12), width=15, height=2).place(x=580, y=200)
    state_start_temp = Text(interface2)
    state_start_temp.place(x=610, y=250, width=120, height=18)
    state_start_temp.insert(END, glo.get("list_state_now")[0] + '\r')

    timer = threading.Timer(0.3, fun_timer)
    global timer
    timer.start()
    timer.cancel()
    def state_start():
        global timer
        timer.cancel()
        glo.set("time_remain",int(glo.get("list_time")[0]) * 3600 + int(glo.get("list_time")[1]) * 60 + int(glo.get("list_time")[2]))
        timer = threading.Timer(0.3, fun_timer)
        API.start()
        timer.start()
    Button(interface2, text="启动", command=state_start, width=20, height=4, bg="gray", fg="black").place(x=350, y=450,width=80,height=30)  # 确定按键


    #急停动作模块设计
    Label(interface2, text="急停动作：", font=("Arial", 12), width=15, height=2).place(x=180, y=350)
    state_shutdown_temp = Text(interface2)
    state_shutdown_temp.place(x=210, y=400, width=120, height=18)
    state_shutdown_temp.insert(END, glo.get("list_state_now")[2] + '\r')
    def state_shutdown():
        API.shutdown()
    Button(interface2, text="急停", command=state_shutdown, width=20, height=4, bg="gray", fg="black").place(x=550, y=450,width=80,height=30)  # 确定按键



    #配置和退出按钮
    def state_configure():
        itf3.interface3(interface2,time_remain)
    Button(interface2, text="配置", command=state_configure, width=20, height=4, bg="gray", fg="black").place(x=400, y=500,width=80,height=30)  # 确定按键

    def state_exit():
        API.excute_state(3)
        interface2.destroy()
    Button(interface2, text="退出", command=state_exit, width=20, height=4, bg="gray", fg="black").place(x=500, y=500,width=80,height=30)  # 确定按键

    #面板2开启循环
    interface2.mainloop()

# 将秒数间隔转换为计时器"时:分:秒"字符串
def itv2time(iItv):

    if type(iItv) == type(1):
        h = int(iItv / 3600)
        sUp_h = iItv - 3600 * h
        m = int(sUp_h / 60)
        sUp_m = sUp_h - 60 * m
        s = int(sUp_m)

        return ":".join(map(str, (h, m, s)))
    else:
        return "[InModuleError]:itv2time(iItv) invalid argument type"