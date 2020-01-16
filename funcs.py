import pyautogui,time,win32gui,win32con,os,win32api

def turn_off(xp,yp):
    pyautogui.click(xp, yp, clicks=1, button='left')
    yys = win32gui.GetForegroundWindow()
    win32gui.PostMessage(yys, win32con.WM_CLOSE, 0, 0)
    time.sleep(0.3)
    pyautogui.click(935,607)

def turn_off_all():
    os.system('%s%s' % ("taskkill /F /IM ", 'onmyoji.exe'))

def pos_adopt(num_client):
    ### adopt the position of clients before working
    desktop = win32gui.GetDesktopWindow()
    (des_right, des_bottom) = win32gui.GetWindowRect(desktop)[2:]

    if num_client == 2:
        yys = [1,1]
        yys[0] = win32gui.FindWindow(None, "阴阳师-网易游戏")
        (cap_left, cap_top, cap_right, cap_bottom) = win32gui.GetWindowRect(yys[0])
        win32gui.SetWindowPos(yys[0], win32con.HWND_TOP, des_right - (cap_right - cap_left), 0, 0, 0, win32con.SWP_NOSIZE)

        hWndList = []
        win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), hWndList)
        yys[1] = yys[0]
        for hwnd in hWndList:
            if win32gui.GetWindowText(hwnd) == "阴阳师-网易游戏" and hwnd != yys[0]: # solve the same title problem
                yys[1] = hwnd
                break
        win32gui.ShowWindow(yys[1], win32con.SW_RESTORE)
        win32gui.SetWindowPos(yys[1], win32con.HWND_TOP, 0, des_bottom - (cap_bottom - cap_top) - 40, 0, 0,
                              win32con.SWP_NOSIZE)
        return (des_right - (cap_right - cap_left),0, 0, des_bottom - (cap_bottom - cap_top) - 40)
    elif num_client == 1:
        yys1 = win32gui.FindWindow(None, "阴阳师-网易游戏")
        (cap_left, cap_top, cap_right, cap_bottom) = win32gui.GetWindowRect(yys1)
        win32gui.SetWindowPos(yys1, win32con.HWND_TOP, des_right - (cap_right - cap_left), 0, 0, 0, win32con.SWP_NOSIZE)
        return (des_right - (cap_right - cap_left),0)
    else:
        raise IOError("no support this input")



def click(hwnd, xr, yr):
    lParam = win32api.MAKELONG(xr, yr)
    win32gui.SendMessage(hwnd, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
    win32gui.SendMessage(hwnd, win32con.WM_RBUTTONDOWN, win32con.MK_LBUTTON, lParam)
    win32gui.SendMessage(hwnd, win32con.WM_RBUTTONUP, win32con.MK_LBUTTON, lParam)


def buff_switch(xp, yp):
    # only apply to team menu
    time.sleep(3.5)
    pyautogui.click(xp + 734, yp + 78)  # buff position, to be improved
    time.sleep(0.3)
    pyautogui.click(xp + 734 + 4, yp + 78 + 145)
    time.sleep(0.3)

def buff_switch_back(hwnd):
    time.sleep(3.5)
    click(hwnd,734,50) # memory (701,26) - (750,75) display (709,56) - (758,105)
    time.sleep(0.4)
    click(hwnd,734 + 4,50 + 145)
    time.sleep(0.4)