import time,sys,win32gui,funcs
from config_read import ConfigRead

config_my = ConfigRead("F:\python_sim\yys\config.ini")
TIME_ROOUND = config_my.get_time_round()
xr = config_my.get_horizontal_pos()
yr = config_my.get_vertical_pos()

TIME_WAIT_MAX = 7+TIME_ROOUND # as captain, the max time to wait (seconds)
color_first = 0  # color for reference
color_now = color_first # color now
time_first = time.time() # time for reference
time_start = time.time()

# (cl,ct,ml,mt) = funcs.pos_adopt(2)
clt1 = win32gui.FindWindow(None,"阴阳师-网易游戏")
win32gui.SetWindowText(clt1,"不要最小化&右下角不能被遮挡")

dc = win32gui.GetDC(win32gui.GetActiveWindow())
try:
    while 1:
        funcs.click(clt1,xr,yr)
        time.sleep(0.55)

        (cl, ct) = win32gui.GetWindowRect(clt1)[0:2]
        color_now = win32gui.GetPixel(dc,cl+xr, ct+yr) # getpixel needs screen uncoverd!!!!!!!
        if color_now != color_first: # color changed, update reference time and color
            color_first = color_now
            time_first = time.time()
        elif time.time() - time_first > TIME_WAIT_MAX: # color unchanged more than TIME_WAIT_MAX, no need to click
            break

    # loop stoped, turn off captain's buff and clients

    funcs.click(clt1,xr-4, yr-100) # make sure two in team
    time.sleep(0.3)

    funcs.buff_switch_back(clt1)
    # win32gui.SetWindowText(clt1, "阴阳师-网易游戏")
    funcs.turn_off_all()
except KeyboardInterrupt:
    win32gui.SetWindowText(clt1, "阴阳师-网易游戏")
    sys.exit(0)


