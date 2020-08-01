import pyautogui
import time
import webbrowser
import pyperclip
##pyautogui.press("winleft")
##pyautogui.write("chrome")
##pyautogui.press("enter")
##time.sleep(2) 
##pyautogui.write("Thailand")
##pyautogui.press("enter")

##chrome = (0, 281)
##pyautogui.moveTo(chrome, duration=1)
##pyautogui.click()

url = 'https://www.google.com'
webbrowser.open(url)

time.sleep(2)
pyautogui.write("Thailand")
pyautogui.press("enter")

def Search(word):
    time.sleep(2)
    for tab in range(7):
        pyautogui.press("tab")

    pyautogui.press("backspace")
    pyautogui.write(word)
    pyautogui.press("enter")
    time.sleep(2)
    #pyautogui.screenshot(word + '.png')

def SearchTH(word):
    time.sleep(2)
    pyperclip.copy(word)
    for tab in range(7):
        pyautogui.press('tab')

    pyautogui.hotkey('ctrlleft', 'v')
    pyautogui.press("enter")
    time.sleep(2)
    
##Search('Singapore')
##Search('USA')
##Search('China')
SearchTH("ภาษาไทย")
