import pyautogui, time, keyboard

def moveToCornerClick(x,y):
    """x,y pixels from top-left"""
    pyautogui.moveTo(x, y)
    pyautogui.click()
    time.sleep(300)

def writeToTxtFile():
    keyboard.press_and_release("windows")
    time.sleep(1)
    keyboard.write('notepad') 
    time.sleep(1)
    keyboard.press_and_release('enter')
    time.sleep(1)
    keyboard.write('hello') 
    return False

keep_going = True
count = 0

while keep_going:
    moveToCornerClick(50,900) #y=150 click a little lower on left to avoid hitting other windows toolbar
    count+=1
    print(f"iteration: {count}")
    # keep_going = writeToTxtFile()

print("done")