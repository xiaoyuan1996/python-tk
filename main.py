# coding:utf-8
from tkinter import *
import interface2 as itf2
import Globalvar as glo
from PIL import Image, ImageTk
import input_board as ib
import datetime
import threading



###################################全局变量定义及初始化########################################################
glo.set_user_passwd(["a","a","b","b"])                # 用户名及密码初始化
glo.set_flag_user(2)                                    # 当前用户标志位 2 为无用户 0 为 admin 1 为 user

valve_state0 = "阀1开启，阀2开启"
valve_state1 = "阀1关闭，阀2开启"
valve_state2 = "阀1开启，阀2关闭"
valve_state3 = "阀1关闭，阀2关闭"
list_state = [valve_state0,valve_state1,valve_state2,valve_state3]
glo.set("list_state_chosen",list_state)

# 在界面二中一直更新此处内容
variable_valve_state_start = valve_state2               # 初始化时启动动作
variable_valve_state_end = valve_state1                 # 初始化时停止动作
variable_valve_state_shutdown = valve_state3            # 初始化时急停动作
glo.set("list_state_now" ,[variable_valve_state_start,variable_valve_state_end,variable_valve_state_shutdown])
# 设置时间保存
hours = 0 ; mins = 5 ; secs = 0
glo.set("list_time",[hours,mins,secs])

####################################第一界面###################################################################
#初始化界面
main_window = Tk()                                      # 初始化Tk
main_window.title( "永诚科技喷水控制系统")              # 设置窗口标题
main_window.geometry("1024x768")                       # 窗口大小显示
main_window.resizable(width=False, height=False)        # 设置窗口是否可以变化长/宽，False不可变，True可变，默认为True

# 设置输入用户名和密码
users_val = StringVar()
users=Entry(main_window,width=50,fg="black",textvariable=users_val)
users.place(x=375, y=110,width=100,height=20)
passwds_val = StringVar()
passwds=Entry(main_window,width=50,fg="black",textvariable=passwds_val)
passwds.place(x=575, y=110,width=100,height=20)

#############################################TEST#######################################################
def ADMIN():
    global users_val
    ib.input_board(users_val)
Button(main_window, text="用户名：", command=ADMIN, width=7, height=2, bg="gray", fg="black").place(x=310, y=110,width=60,height=20) #确定按键
def PASSWD():
    global passwds_val
    ib.input_board(passwds_val)
Button(main_window, text="密码：", command=PASSWD, width=7, height=2, bg="gray", fg="black").place(x=510, y=110,width=60,height=20) #确定按键


# 设置提示输入的按键   验证函数
def verify():
    user = users.get()
    passwd = passwds.get()

    f = open('./save.txt', 'r')
    data_get = f.readline().replace('[', '').replace(']', '').replace('\'', '').replace(',', '').split()
    f.close()

    if (user == data_get [0]):
        if (passwd == data_get [1] ):
            prompt_message.delete(1.0, END)
            prompt_message.insert(END, "输入正确！" + '\n')
            glo.set_flag_user(0)
            itf2.interface2()
        else:
            prompt_message.delete(1.0, END)
            prompt_message.insert(END, "登陆失败：密码输入错误！" + '\n')
            glo.set_flag_user(2)
    elif (user ==data_get [2]):
        if (passwd == data_get [3] ):
            prompt_message.delete(1.0, END)
            prompt_message.insert(END, "输入正确！" + '\n')
            glo.set_flag_user(1)
            itf2.interface2()
        else:
            prompt_message.delete(1.0, END)
            prompt_message.insert(END, "登陆失败：密码输入错误！" + '\n')
            glo.set_flag_user(2)
    else:
        prompt_message.delete(1.0, END)
        prompt_message.insert(END, "登陆失败：输入账号错误！" + '\n')
        glo.set_flag_user(2)

Button(main_window, text="确定", command=verify, width=20, height=4, bg="gray", fg="black").place(x=400, y=200,width=80,height=30) #确定按键

def reset():
    global users
    global passwds
    users = Entry(main_window, width=50, fg="black")
    users.place(x=375, y=110, width=100, height=20)
    passwds = Entry(main_window, width=50, fg="black")
    passwds.place(x=575, y=110, width=100, height=20)
    prompt_message.insert(END, '\n')
    prompt_message.see(END)
    prompt_message.update()
Button(main_window, text="重置", command=reset, width=20, height=4, bg="gray", fg="black").place(x=570, y=200,width=80,height=30) #确定按键

# 账户密码错误及正确提示
prompt_message = Text()
prompt_message.place(x=330, y=150,width=350,height=30)

#图片设置
load = Image.open('.\logo.jpg') # 我图片放桌面上
render= ImageTk.PhotoImage(load)
img = Label(main_window,image=render)
img.image = render
img.place(x=600,y=450)

mainloop()          #开始循环