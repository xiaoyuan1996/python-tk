#coding:utf-8

def open_A_open_B():   #valve_state0 = "阀1开启，阀2开启"
    pass

def close_A_open_B():   #valve_state1 = "阀1关闭，阀2开启"
    pass

def open_A_close_B():   #valve_state2 = "阀1开启，阀2关闭"
    pass

def close_A_close_B():   #valve_state3 = "阀1关闭，阀2关闭"
    pass

def send(value):
    for i in range(3):
        if (value == 1):
            break
        else:
            pass