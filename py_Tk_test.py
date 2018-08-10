# coding:utf-8
from Tkinter import *
import tk_display_scripts as dis
import datetime
import threading

###################################全局变量定义################################################################
admin0 = "admin" ; passwd0 = "su06"                   # 管理员用户名
admin1 = "user" ; passwd1 = "01"                      #  用户用户名
flag_users = 0                                          # 当前用户标志位 2 为无用户 0 为 admin 1 为 user

class AppUI():
    def __init__(self):
        ####################################初始化界面################################################################
        main_window = Tk()  # 初始化Tk
        main_window.title("永诚科技喷水控制系统")  # 设置窗口标题
        main_window.geometry("1024x768")  # 窗口大小显示
        main_window.resizable(width=False, height=False)  # 设置窗口是否可以变化长/宽，False不可变，True可变，默认为True