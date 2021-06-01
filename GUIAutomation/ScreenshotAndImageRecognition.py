#Screenshot and Image Recognition

#To match the object has to be pixel perfect

#Install Pillow module using 'pip install pillow'
import pyautogui

#This captures a screenshot in an image object
# print(pyautogui.screenshot())
#<PIL.Image.Image image mode=RGB size=1366x768 at 0x20E8118B370>

#Saves the screenshot
# pyautogui.screenshot(r'F:\Python Project\GUIAutomation\screenshot.png')

#Image recognition
#Take a snip of a calculator button, i have taken snip of 4 key

#This prints the position of the image passed as (left,top,width,height)
# print(pyautogui.locateOnScreen(r'F:\Python Project\GUIAutomation\key_4.png'))

#This prints at the center of the image
#print(pyautogui.locateCenterOnScreen(r'F:\Python Project\GUIAutomation\key_4.png'))
centerX,centerY = pyautogui.locateCenterOnScreen(r'F:\Python Project\GUIAutomation\4.png')

#Move the mouse pointer to the center of the image
pyautogui.moveTo(centerX,centerY,duration=1)
pyautogui.click()