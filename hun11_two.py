import pyautogui,time,sys,win32gui,funcs

TIME_WAIT_MAX = 20 # as captain, the max time to wait (seconds)
TIME_ROOUND = 23 # time of one round, 23 of hun11, 17 of hun10
# TIME_TOTAL = (7+TIME_ROOUND) * 29 # pve total time (seconds), 30 rounds, 1 round no need to play

color_first = 0  # color for reference
color_now = color_first # color now
time_first = time.time() # time for reference
# time_start = time.time()

(cl,ct,ml,mt) = funcs.pos_adopt(2)
x1 = cl+1092 # the position1 clicked, to be improved!!!
y1 = ct+608
x2 = ml+1097 # the position2 clicked
y2 = mt+578
try:
    while 1:
        pyautogui.click(x1, y1, clicks=1, button='left')
        time.sleep(0.1)
        pyautogui.click(x2, y2, clicks=1, button='left')
        time.sleep(0.5)

        # if time.time() - time_start > TIME_TOTAL:
        #     break

        dc = win32gui.GetDC(win32gui.GetActiveWindow())
        color_now = win32gui.GetPixel(dc,x1,y1)
        if color_now != color_first: # color changed, update reference time and color
            color_first = color_now
            time_first = time.time()
        elif time.time() - time_first > TIME_WAIT_MAX: # color unchanged more than TIME_WAIT_MAX, no need to click
            break
        if pyautogui.position()[0] != x1 and pyautogui.position()[0] != x2:
            sys.exit(0)
    # loop stoped, turn off captain's buff and clients
    # time.sleep(7+TIME_ROOUND+18) # in case time up, wait for reward acquired automatically
    pyautogui.click(x1 - 4, y1 - 100)
    time.sleep(0.3)
    pyautogui.click(x2 - 4, y2 - 100)  # make sure two in team
    time.sleep(0.3)  # make sure two in team

    pyautogui.click(x1 - 4, y1 - 100)
    funcs.buff_switch(cl, ct)
    pyautogui.click(x2 - 4, y2 - 100)
    funcs.buff_switch(ml, mt)
    funcs.turn_off_all()
except KeyboardInterrupt:
    sys.exit(0)


