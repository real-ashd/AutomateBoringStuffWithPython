#Controlling Keyboard with Python
import pyautogui


#Divide your screen in two parts
#Place a blank text file on the left and your python ide on right
print(pyautogui.position())	#This returns the position of the mouse pointer's current position
#Find the best position to make the text file active and feed the co-ordinates to click() function below

pyautogui.click(595,455)
pyautogui.typewrite("\nHello World!",interval=0.1)
pyautogui.typewrite(['\n','a','c','left','b','right'],interval=0.1)
keys = pyautogui.KEYBOARD_KEYS
print(keys)

#Keyboard Shortcut keys using hotkey
pyautogui.hotkey('ctrl','o')

pyautogui.press('winleft')	#This presses a single key