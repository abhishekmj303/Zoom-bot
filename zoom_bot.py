from pyautogui import *
from time import sleep
from subprocess import Popen
import getpass

def join(id):
    zoom = 'C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe'
    Popen([zoom])
    print('Opening Zoom .....')
    
    while (locateOnScreen('Zoom_Button.png',grayscale=True) is None):
        print('Waiting...')
        # sleep(1)
    join_btn = locateCenterOnScreen('Zoom_Button.png',grayscale=True)
    print('Clicking Join Button')
    moveTo(join_btn)
    click()

    while (locateOnScreen('Zoom_ID.png',grayscale=True) is None):
        print('Waiting...')
        # sleep(1)
    print('Typing the meeting ID')
    write(id)
    press('enter')

    sleep(0.2)
    getWindowsWithTitle('Zoom')[0].close()
    print('Joining Zoom Meeting with this id', id)

def pswd(pswd):
    while (locateOnScreen('Zoom_Passwd.png',grayscale=True) is None):
        print('Waiting...')
    print('Entering Password and Joining the Meeting')
    write(pswd)
    press('enter')

def leave():
    for x in range(len(getWindowsWithTitle('Zoom'))):
        if x==1:
            pass
        else:
            getWindowsWithTitle('Zoom')[x].close()
            print('Closing Window ...')
    
    print('Closed all Zoom Windows')
    # sleep(2)

    while (locateOnScreen('Zoom_Leave.png',grayscale=True) is None):
        print('Waiting...')
        # sleep(1)
    leave_btn = locateCenterOnScreen('Zoom_Leave.png',grayscale=True)
    print('Clicking Leave Meeting Button')
    moveTo(leave_btn)
    click()

    print('Left Meeting')
