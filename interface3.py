# coding:utf-8
import tkinter.ttk as ttk
from tkinter import *
import Globalvar as glo
import interface2 as itf2
import Software_API as API
import importlib,sys

import input_board as ib


import numpy as np


def interface3(interface2,time_remain):
    #初始化
    importlib.reload(sys)
    #sys.setdefaultencoding('utf8')

    interface3=Toplevel()
    interface3.title("永诚科技喷水控制系统")             # 设置窗口标题
    interface3.geometry("1024x768")                     # 窗口大小显示
    interface3.resizable(width=False, height=False)      # 设置窗口是否可以变化长/宽，False不可变，True可变，默认为True

    #自动控制时间模块
    Label(interface3, text="自动控制时间：", font=("Arial", 12), width=12, height=2).place(x=700, y=100)
    Label(interface3, text="时：", font=("Arial", 12), width=4, height=2).place(x=700, y=150)
    Label(interface3, text="分：", font=("Arial", 12), width=4, height=2).place(x=760, y=150)
    Label(interface3, text="秒：", font=("Arial", 12), width=4, height=2).place(x=820, y=150)

    list_time = glo.get("list_time")

    hours_val = StringVar()
    hours = Entry(interface3, width=50, fg="black",textvariable=hours_val)     # 输入小时
    hours.place(x=730, y=160, width=30, height=20)
    hours_val.set(list_time[0])

    def hour_sub():
        if(int(hours_val.get())==0):
            hours_val.set(59)
        else:
            hours_val.set(int(hours_val.get())-1)
    Button(interface3, text="-", command=hour_sub, width=20, height=4, bg="gray", fg="black").place(x=730, y=190, width=30,height=20)


    mins_val = StringVar()
    mins = Entry(interface3, width=50, fg="black",textvariable=mins_val)      # 输入分钟
    mins.place(x=790, y=160, width=30, height=20)
    mins_val.set(list_time[1])

    secs_val = StringVar()
    secs = Entry(interface3, width=50, fg="black",textvariable=secs_val)      # 输入秒
    secs.place(x=850, y=160, width=30, height=20)
    secs_val.set(list_time[2])



    # 启动动作
    Label(interface3, text="启动动作：", font=("Arial", 12), width=8, height=2).place(x=200, y=300)
    state_start_num = StringVar()                                              # 启动列表
    state_start = ttk.Combobox(interface3,width=16,textvariable=state_start_num)
    state_start['values'] = (glo.get("list_state_chosen"))
    state_start["state"] = "readonly"
    state_start.place(x=200,y=350)

    for i in range(4):
        if( glo.get("list_state_now")[0] == glo.get("list_state_chosen")[i] ):
            state_start.current(i)
        else:
            pass

    # 停止动作
    Label(interface3, text="停止动作：", font=("Arial", 12), width=8, height=2).place(x=500, y=300)
    state_end_num = StringVar()                                                 # 停止列表
    state_end = ttk.Combobox(interface3,width=16,textvariable=state_end_num)
    state_end['values'] = (glo.get("list_state_chosen"))
    state_end["state"] = "readonly"
    state_end.place(x=500,y=350)

    for i in range(4):
        if( str(glo.get("list_state_chosen")[i])== str(glo.get("list_state_now")[1])):
            state_end.current(i)
        else:
            pass    

    # 急停动作
    Label(interface3, text="急停动作：", font=("Arial", 12), width=8, height=2).place(x=800, y=300)
    state_shutdown_num = StringVar()                                            # 急停列表
    state_shutdown = ttk.Combobox(interface3,width=16,textvariable=state_shutdown_num)
    state_shutdown['values'] = (glo.get("list_state_chosen"))
    state_shutdown["state"] = "readonly"
    state_shutdown.place(x=800,y=350)

    for i in range(4):
        if( str(glo.get("list_state_chosen")[i])== str(glo.get("list_state_now")[2])):
            state_shutdown.current(i)
        else:
            pass

    # 如果是管理员 则显示账户密码修改
    if(glo.get("flag_user")==0):

        f = open('./save.txt', 'r')
        data_get = f.readline().replace('[', '').replace(']', '').replace('\'', '').replace(',', '').split()
        f.close()

        admin_val = StringVar()
        global admin_val
        admin = Entry(interface3, width=50, fg="black",textvariable=admin_val)     # 输入小时
        admin.place(x=210, y=140, width=100, height=20)
        admin_val.set(data_get[0])
        def ADMIN():
            global admin_val
            ib.input_board(admin_val)
        Button(interface3, text="管理员：", command=ADMIN, width=7, height=2, bg="gray", fg="black").place(x=200, y=100, width=60, height=20)  # 确定按键

        passwd0_val = StringVar()
        global passwd0_val
        passwd0 = Entry(interface3, width=50, fg="black",textvariable=passwd0_val)     # 输入小时
        passwd0.place(x=370, y=140, width=100, height=20)
        passwd0_val.set(data_get[1])
        def PASSWD0():
            global passwd0_val
            ib.input_board(passwd0_val)
        Button(interface3, text="密码：", command=PASSWD0, width=7, height=2, bg="gray", fg="black").place(x=350, y=100,width=60, height=20)  # 确定按键

        user_val = StringVar()
        global user_val
        user = Entry(interface3, width=50, fg="black",textvariable=user_val)     # 输入小时
        user.place(x=210, y=210, width=100, height=20)
        user_val.set(data_get[2])
        def USER():
            global user_val
            ib.input_board(user_val)
        Button(interface3, text="用户：", command=USER, width=7, height=2, bg="gray", fg="black").place(x=200, y=170, width=60, height=20)  # 确定按键

        passwd1_val = StringVar()
        global passwd1_val
        passwd1 = Entry(interface3, width=50, fg="black",textvariable=passwd1_val)     # 输入小时
        passwd1.place(x=370, y=210, width=100, height=20)
        passwd1_val.set(data_get[3])
        def PASSWD1():
            global passwd1_val
            ib.input_board(passwd1_val)
        Button(interface3, text="密码：", command=PASSWD1, width=7, height=2, bg="gray", fg="black").place(x=350, y=170,width=60, height=20)  # 确定按键
    else:
        pass


    # 按键设置模块
    def save():                                                               # 保存按键
        glo.set("list_state_now" ,[state_start.get(),state_end.get(),state_shutdown.get()])
        glo.set("list_time",[hours.get(),mins.get(),secs.get()])
        glo.set("time_remain", int(glo.get("list_time")[0]) * 3600 + int(glo.get("list_time")[1]) * 60 + int(glo.get("list_time")[2]))
        glo.set("user_passwd",[admin.get(),passwd0.get(),user.get(),passwd1.get()])
        if (glo.get("flag_user") == 0):
            f = open('./save.txt','w')
            f.write(str(glo.get("user_passwd")))
            f.close()

        else:
            pass

        state_end_temp = Text(interface2)
        state_end_temp.place(x=610, y=400, width=120, height=18)
        state_end_temp.insert(END, glo.get("list_state_now")[1] + '\r')

        state_start_temp = Text(interface2)
        state_start_temp.place(x=610, y=250, width=120, height=18)
        state_start_temp.insert(END, glo.get("list_state_now")[0] + '\r')

        state_shutdown_temp = Text(interface2)
        state_shutdown_temp.place(x=210, y=400, width=120, height=18)
        state_shutdown_temp.insert(END, glo.get("list_state_now")[2] + '\r')

        time_stable = Text(interface2)
        time_stable.place(x=210, y=250, width=200, height=20)
        list_time_temp = glo.get("list_time")
        time_stable.insert(END, str(list_time_temp[0])+'：'+str(list_time_temp[1])+'：'+str(list_time_temp[2]) + '\r')

        remain_time = glo.get("time_remain")
        time_remain.delete(1.0, END)
        time_remain.insert(END, str(itf2.itv2time(remain_time)))
        time_remain.update()

        interface3.destroy()

    Button(interface3, text="保存", command=save, width=20, height=4, bg="gray", fg="black").place(x=300, y=450,width=80,height=30)

    def cancel():                                                             # 取消按键
        interface3.destroy()
    Button(interface3, text="取消", command=cancel, width=20, height=4, bg="gray", fg="black").place(x=450, y=450,width=80,height=30)

    def reset():# 重置按键
        if (glo.get("flag_user") == 0):
            admin_val.set(glo.get("user_passwd")[0])
            passwd0_val.set(glo.get("user_passwd")[1])
            user_val.set(glo.get("user_passwd")[2])
            passwd1_val.set(glo.get("user_passwd")[3])
        else:
            pass
        hours_val.set(list_time[0])
        mins_val.set(list_time[1])
        secs_val.set(list_time[2])
        for i in range(4):
            if (str(glo.get("list_state_chosen")[i]) == glo.get("list_state_now")[0]):
                state_start.current(i)
            else:
                pass

        for i in range(4):
            if (str(glo.get("list_state_chosen")[i]) == glo.get("list_state_now")[1]):
                state_end.current(i)
            else:
                pass

        for i in range(4):
            if (str(glo.get("list_state_chosen")[i]) == glo.get("list_state_now")[2]):
                state_shutdown.current(i)
            else:
                pass

    Button(interface3, text="重置", command=reset, width=20, height=4, bg="gray", fg="black").place(x=600, y=450,width=80,height=30)

    def exit():                                                               # 退出按键
        API.excute_state(3)
        interface2.destroy()
        interface3.destroy()
    Button(interface3, text="退出", command=exit, width=20, height=4, bg="gray", fg="black").place(x=750, y=450,width=80,height=30)

    #面板3开启循环
    interface3.mainloop()