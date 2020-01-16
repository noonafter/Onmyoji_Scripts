import time,sys,win32con,win32gui,win32api

TIME_WAIT_MAX = 20 # max time to wait (seconds)

cal = win32gui.FindWindow(None, "阴阳师-网易游戏")
lParam = win32api.MAKELONG(1038, 600)
try:
    while 1:
        win32gui.SendMessage(cal, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
        win32gui.SendMessage(cal, win32con.WM_RBUTTONDOWN, win32con.MK_LBUTTON, lParam)
        win32gui.SendMessage(cal, win32con.WM_RBUTTONUP, win32con.MK_LBUTTON, lParam)
        time.sleep(0.75)
except KeyboardInterrupt:
    sys.exit(0)