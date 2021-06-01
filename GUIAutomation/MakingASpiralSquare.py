import pyautogui

#Using dragRel() function
#Open a blank paint file select the brush and click to put drawing program in focus


pyautogui.click()
distance = 200          #Adjust accordingly
shrink = 10             #Space between the walls

def spiralSquare1(distance,shrink):
    while distance > 0:
        pyautogui.dragRel(distance, 0, duration=0.1)   # move right
        distance = distance - shrink
        pyautogui.dragRel(0, distance, duration=0.1)   # move down
        pyautogui.dragRel(-distance, 0, duration=0.1)  # move left
        distance = distance - shrink
        pyautogui.dragRel(0, -distance, duration=0.1)  # move up
def spiralSquare3(distance,shrink):
    while distance > 0:
        pyautogui.dragRel(-distance, 0, duration=0.1)  # move left
        distance = distance - shrink
        pyautogui.dragRel(0, -distance, duration=0.1)  # move up
        pyautogui.dragRel(distance, 0, duration=0.1)   # move right
        distance = distance - shrink
        pyautogui.dragRel(0, distance, duration=0.1)   # move down
def spiralSquare2(distance,shrink):
    while distance > 0:
        pyautogui.dragRel(distance, 0, duration=0.1)   # move right
        distance = distance - shrink
        pyautogui.dragRel(0, -distance, duration=0.1)  # move up
        pyautogui.dragRel(-distance, 0, duration=0.1)  # move left
        distance = distance - shrink
        pyautogui.dragRel(0, distance, duration=0.1)   # move down
def spiralSquare4(distance,shrink):
    while distance > 0:
        pyautogui.dragRel(-distance, 0, duration=0.1)  # move left
        distance = distance - shrink
        pyautogui.dragRel(0, distance, duration=0.1)   # move down
        pyautogui.dragRel(distance, 0, duration=0.1)   # move right
        distance = distance - shrink
        pyautogui.dragRel(0, -distance, duration=0.1)  # move up

"""Uncomment and run the program as per you likeness"""

spiralSquare1(distance,shrink)
# spiralSquare2(distance,shrink)
# spiralSquare3(distance,shrink)
# spiralSquare4(distance,shrink)