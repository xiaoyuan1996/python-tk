#coding:utf-8
import importlib,sys


import Globalvar as glo
import Hardware_API as API

def excute_state(state_num):
    if(state_num == 0):         #valve_state0 = "阀1开启，阀2开启"
        API.open_A_open_B()
    elif(state_num == 1):       #valve_state1 = "阀1关闭，阀2开启"
        API.close_A_open_B()
    elif(state_num == 2):       #valve_state2 = "阀1开启，阀2关闭"
        API.open_A_close_B()
    elif(state_num == 3):       #valve_state3 = "阀1关闭，阀2关闭"
        API.close_A_close_B()
    else:
        pass

def encoding_init():
    importlib.reload(sys)
    #sys.setdefaultencoding('utf8')

def start():
    encoding_init()
    for i in range(4):
        if(glo.get("list_state_now")[0]==glo.get("list_state_chosen")[i]):
            excute_state(i)
        else:
            pass

def end():
    encoding_init()
    for i in range(4):
        if(glo.get("list_state_now")[1]==glo.get("list_state_chosen")[i]):
            excute_state(i)
        else:
            pass

def shutdown():
    encoding_init()
    for i in range(4):
        if(glo.get("list_state_now")[2]==glo.get("list_state_chosen")[i]):
            excute_state(i)
        else:
            pass