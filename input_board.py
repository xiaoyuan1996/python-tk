# coding:utf-8
from tkinter import *
import interface3 as itf3
import Globalvar as glo
import threading
import Software_API as API

def input_board(val):
    #初始化
    input_board=Toplevel()
    input_board.title("永诚科技喷水控制系统")  # 设置窗口标题
    input_board.geometry("640x400")  # 窗口大小显示
    input_board.resizable(width=False, height=False)  # 设置窗口是否可以变化长/宽，False不可变，True可变，默认为True

    Label(input_board, text="输入键值：", font=("Arial", 12), width=15, height=2).place(x=0, y=0)
    dis_value = Text(input_board)
    dis_value.place(x=110, y=10, width=200, height=20)
    dis_value.insert(END, '')

    def ok():
        glo.set("value_board",str(dis_value.get("0.0", "end")).replace('\n', ''))
        val.set(glo.get("value_board"))
        input_board.destroy()
    Button(input_board, text="OK", command=ok, width=20, height=4, bg="gray", fg="black").place(x=350, y=0,width=100,height=60)  # 确定按键

    def cancel():
        input_board.destroy()
    Button(input_board, text="Cancel", command=cancel, width=20, height=4, bg="gray", fg="black").place(x=470, y=0,width=160,height=60)  # 确定按键


    def q():
        dis_value.insert(END, 'q')
    Button(input_board, text="q", command=q, width=20, height=4, bg="gray", fg="black").place(x=20, y=160,width=60,height=60)  # 确定按键
    def w():
        dis_value.insert(END, 'w')
    Button(input_board, text="w", command=w, width=20, height=4, bg="gray", fg="black").place(x=80, y=160,width=60,height=60)  # 确定按键
    def e():
        dis_value.insert(END, 'e')
    Button(input_board, text="e", command=e, width=20, height=4, bg="gray", fg="black").place(x=140, y=160,width=60,height=60)  # 确定按键
    def r():
        dis_value.insert(END, 'r')
    Button(input_board, text="r", command=r, width=20, height=4, bg="gray", fg="black").place(x=200, y=160,width=60,height=60)  # 确定按键
    def t():
        dis_value.insert(END, 't')
    Button(input_board, text="t", command=t, width=20, height=4, bg="gray", fg="black").place(x=260, y=160,width=60,height=60)  # 确定按键
    def y():
        dis_value.insert(END, 'y')
    Button(input_board, text="y", command=y, width=20, height=4, bg="gray", fg="black").place(x=320, y=160,width=60,height=60)  # 确定按键
    def u():
        dis_value.insert(END, 'u')
    Button(input_board, text="u", command=u, width=20, height=4, bg="gray", fg="black").place(x=380, y=160,width=60,height=60)  # 确定按键
    def i():
        dis_value.insert(END, 'i')
    Button(input_board, text="i", command=i, width=20, height=4, bg="gray", fg="black").place(x=440, y=160,width=60,height=60)  # 确定按键
    def o():
        dis_value.insert(END, 'o')
    Button(input_board, text="o", command=o, width=20, height=4, bg="gray", fg="black").place(x=500, y=160,width=60,height=60)  # 确定按键
    def p():
        dis_value.insert(END, 'p')
    Button(input_board, text="p", command=p, width=20, height=4, bg="gray", fg="black").place(x=560, y=160,width=60,height=60)  # 确定按键
    def a():
        dis_value.insert(END, 'a')
    Button(input_board, text="a", command=a, width=20, height=4, bg="gray", fg="black").place(x=40, y=220,width=60,height=60)  # 确定按键
    def s():
        dis_value.insert(END, 's')
    Button(input_board, text="s", command=s, width=20, height=4, bg="gray", fg="black").place(x=100, y=220,width=60,height=60)  # 确定按键
    def d():
        dis_value.insert(END, 'd')
    Button(input_board, text="d", command=d, width=20, height=4, bg="gray", fg="black").place(x=160, y=220,width=60,height=60)  # 确定按键
    def f():
        dis_value.insert(END, 'f')
    Button(input_board, text="f", command=f, width=20, height=4, bg="gray", fg="black").place(x=220, y=220,width=60,height=60)  # 确定按键
    def g():
        dis_value.insert(END, 'g')
    Button(input_board, text="g", command=g, width=20, height=4, bg="gray", fg="black").place(x=280, y=220,width=60,height=60)  # 确定按键
    def h():
        dis_value.insert(END, 'h')
    Button(input_board, text="h", command=h, width=20, height=4, bg="gray", fg="black").place(x=340, y=220,width=60,height=60)  # 确定按键
    def j():
        dis_value.insert(END, 'j')
    Button(input_board, text="j", command=j, width=20, height=4, bg="gray", fg="black").place(x=400, y=220,width=60,height=60)  # 确定按键
    def k():
        dis_value.insert(END, 'k')
    Button(input_board, text="k", command=k, width=20, height=4, bg="gray", fg="black").place(x=460, y=220,width=60,height=60)  # 确定按键
    def l():
        dis_value.insert(END, 'l')
    Button(input_board, text="l", command=l, width=20, height=4, bg="gray", fg="black").place(x=520, y=220,width=60,height=60)  # 确定按键
    def z():
        dis_value.insert(END, 'z')
    Button(input_board, text="z", command=z, width=20, height=4, bg="gray", fg="black").place(x=60, y=280,width=60,height=60)  # 确定按键
    def x():
        dis_value.insert(END, 'x')
    Button(input_board, text="x", command=x, width=20, height=4, bg="gray", fg="black").place(x=120, y=280,width=60,height=60)  # 确定按键
    def c():
        dis_value.insert(END, 'c')
    Button(input_board, text="c", command=c, width=20, height=4, bg="gray", fg="black").place(x=180, y=280,width=60,height=60)  # 确定按键
    def v():
        dis_value.insert(END, 'v')
    Button(input_board, text="v", command=v, width=20, height=4, bg="gray", fg="black").place(x=240, y=280,width=60,height=60)  # 确定按键
    def b():
        dis_value.insert(END, 'b')
    Button(input_board, text="b", command=b, width=20, height=4, bg="gray", fg="black").place(x=300, y=280,width=60,height=60)  # 确定按键
    def n():
        dis_value.insert(END, 'n')
    Button(input_board, text="n", command=n, width=20, height=4, bg="gray", fg="black").place(x=360, y=280,width=60,height=60)  # 确定按键
    def m():
        dis_value.insert(END, 'm')
    Button(input_board, text="m", command=m, width=20, height=4, bg="gray", fg="black").place(x=420, y=280,width=60,height=60)  # 确定按键
    def d1():
        dis_value.insert(END, '1')
    Button(input_board, text="1", command=d1, width=20, height=4, bg="gray", fg="black").place(x=20, y=100,width=60,height=60)  # 确定按键
    def d2():
        dis_value.insert(END, '2')
    Button(input_board, text="2", command=d2, width=20, height=4, bg="gray", fg="black").place(x=80, y=100,width=60,height=60)  # 确定按键
    def d3():
        dis_value.insert(END, '3')
    Button(input_board, text="3", command=d3, width=20, height=4, bg="gray", fg="black").place(x=140, y=100,width=60,height=60)  # 确定按键
    def d4():
        dis_value.insert(END, '4')
    Button(input_board, text="4", command=d4, width=20, height=4, bg="gray", fg="black").place(x=200, y=100,width=60,height=60)  # 确定按键
    def d5():
        dis_value.insert(END, '5')
    Button(input_board, text="5", command=d5, width=20, height=4, bg="gray", fg="black").place(x=260, y=100,width=60,height=60)  # 确定按键
    def d6():
        dis_value.insert(END, '6')
    Button(input_board, text="6", command=d6, width=20, height=4, bg="gray", fg="black").place(x=320, y=100,width=60,height=60)  # 确定按键
    def d7():
        dis_value.insert(END, '7')
    Button(input_board, text="7", command=d7, width=20, height=4, bg="gray", fg="black").place(x=380, y=100,width=60,height=60)  # 确定按键
    def d8():
        dis_value.insert(END, '8')
    Button(input_board, text="8", command=d8, width=20, height=4, bg="gray", fg="black").place(x=440, y=100,width=60,height=60)  # 确定按键
    def d9():
        dis_value.insert(END, '9')
    Button(input_board, text="9", command=d9, width=20, height=4, bg="gray", fg="black").place(x=500, y=100,width=60,height=60)  # 确定按键
    def d0():
        dis_value.insert(END, '0')
    Button(input_board, text="0", command=d0, width=20, height=4, bg="gray", fg="black").place(x=560, y=100,width=60,height=60)  # 确定按键

    def Del():
        str_later=str(dis_value.get("0.0", "end")).replace('\n', '')
        str_num = len(str_later)
        str_new = str_later[0:str_num-1]
        dis_value.delete(1.0, END)
        dis_value.insert(END, str_new)
    Button(input_board, text="Del", command=Del, width=20, height=4, bg="gray", fg="black").place(x=480, y=280,width=100,height=60)  # 确定按键


    #面板2开启循环
    input_board.mainloop()

