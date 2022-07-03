import sys
from version import update, getNewUpdate, getVersionControl
from pynput import keyboard
import time
import pyautogui

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.001

def execMapFast():
    time.sleep(0.02)
    pyautogui.press("space")
    time.sleep(0.02)
    pyautogui.press("space")
    time.sleep(0.02)
    pyautogui.press("space")
    time.sleep(0.02)
    pyautogui.press("m")
    time.sleep(0.02)
    pyautogui.moveTo(1213,820)
    time.sleep(0.01)
    pyautogui.click()
    time.sleep(0.01)
    pyautogui.click()
    time.sleep(0.01)
    pyautogui.click()
    time.sleep(0.01)
    pyautogui.click()
    time.sleep(0.01)
    pyautogui.click()
    pyautogui.moveTo(988,676)
    time.sleep(0.01)
    pyautogui.click()
    time.sleep(0.01)
    pyautogui.click()
    time.sleep(0.01)
    pyautogui.click()
    time.sleep(0.01)
    pyautogui.click()
    time.sleep(0.01)
    pyautogui.press("esc")
    time.sleep(0.2)
    pyautogui.press("esc")
    time.sleep(0.2)
    pyautogui.press("esc")
    time.sleep(0.2)

def on_press(key):
    if key == keyboard.Key.esc:
        True
        #return False  # stop listener
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys
    # if k in ['1', '2', 'left', 'right']:  # keys of interest
    if k in ['f12']:
        # self.keys.append(k)  # store it in global-like variable
        print('Pulsado: ' + k)
        execMapFast()
        # return False  # stop listener; remove this if want more keys

def main():
    print (f"Pulsa f12 para saltar. v{getVersionControl}")
    listener = keyboard.Listener(on_press=on_press)
    listener.start()  # start to listen on a separate thread
    listener.join()

def elevate():
    import ctypes,sys
    def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    if is_admin(): #code of admin
        main()
    else:
        # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

if __name__ == '__main__':
    if not (len(sys.argv) >=2 and sys.argv[1] == "DEV"):
        if not update():
            getNewUpdate()
    elevate()