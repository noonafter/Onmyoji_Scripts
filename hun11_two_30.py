import time,sys,win32gui,funcs
from config_read import ConfigRead

config_my = ConfigRead("F:\python_sim\yys\config.ini")
TIME_ROOUND = config_my.get_time_round()
TIME_TOTAL = (10+TIME_ROOUND) * config_my.get_num_round_two()
xr = config_my.get_horizontal_pos()
yr = config_my.get_vertical_pos()

TIME_WAIT_MAX = 7+TIME_ROOUND # as captain, the max time to wait (seconds)
color_first = 0  # color for reference
color_now = color_first # color now
time_first = time.time() # time for reference
time_start = time.time()

clt1 = win32gui.FindWindow(None,"阴阳师-网易游戏")
win32gui.SetWindowText(clt1,"app")
clt2 = win32gui.FindWindow(None,"阴阳师-网易游戏")
win32gui.SetWindowText(clt1,"阴阳师-网易游戏")

try:
    while 1:
        funcs.click(clt1,xr,yr)
        time.sleep(0.1)
        funcs.click(clt2, xr, yr)
        time.sleep(0.5)

        if time.time() - time_start > TIME_TOTAL:
            time.sleep(10 + TIME_ROOUND + 18)  # in case time up, wait for reward acquired automatically
            break

    # loop stoped, turn off captain's buff and clients
    funcs.click(clt1,xr-4, yr-100) # make sure two in team
    time.sleep(0.1)
    funcs.click(clt2,xr-4, yr-100)
    time.sleep(0.1)

    funcs.buff_switch_back(clt1)
    funcs.buff_switch_back(clt2)
    # win32gui.SetWindowText(clt1, "app")
    funcs.turn_off_all()
except KeyboardInterrupt:
    sys.exit(0)


