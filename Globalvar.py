#coding:utf-8
class GlobalVar:
    list_state_chosen = None
    list_state_now = None
    list_time = None
    flag_user = None
    user_passwd = None
    time_remain = None
    value_board = None

# value_board
def set_value_board(value):
    GlobalVar.value_board = value
def get_value_board():
    return GlobalVar.value_board

# list_state_now
def set_list_state_now(value):
    GlobalVar.list_state_now = value
def get_list_state_now():
    return GlobalVar.list_state_now

# list_time
def set_list_time(value):
    GlobalVar.list_time = value
def get_list_time():
    return GlobalVar.list_time

# flag_user
def set_flag_user(value):
    GlobalVar.flag_user = value
def get_flag_user():
    return GlobalVar.flag_user

# user_passwd
def set_user_passwd(value):
    GlobalVar.user_passwd = value
def get_user_passwd():
    return GlobalVar.user_passwd

# list_state_chosen
def set_list_state_chosen(value):
    GlobalVar.list_state_chosen = value
def get_list_state_chosen():
    return GlobalVar.list_state_chosen

# time_remain
def set_time_remain(value):
    GlobalVar.time_remain = value
def get_time_remain():
    return GlobalVar.time_remain


def set(name,value):
    if (name == "list_state_now"):
        set_list_state_now(value)
    elif (name == "flag_user"):
        set_flag_user(value)
    elif (name == "user_passwd"):
        set_user_passwd(value)
    elif (name == "time_remain"):
        set_time_remain(value)
    elif (name == "list_state_chosen"):
        set_list_state_chosen(value)
    elif (name == "value_board"):
        set_value_board(value)
    else:
        set_list_time(value)

def get(name):
    if (name == "list_state_now"):
        return get_list_state_now()
    elif (name == "flag_user"):
        return get_flag_user()
    elif (name == "user_passwd"):
        return get_user_passwd()
    elif (name == "time_remain"):
        return get_time_remain()
    elif (name == "list_state_chosen"):
        return get_list_state_chosen()
    elif (name == "value_board"):
        return get_value_board()
    else:
        return get_list_time()