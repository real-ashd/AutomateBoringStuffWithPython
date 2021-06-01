#GUI Automation
#Use the module pyautogui and install it using 'pip install pyautogui'
import pyautogui


#CheckOut file Making a Spiral Square file after this program
#In case the mouse is out of control drag it to top left corner


#Top left corner of screen is (0,0) going down increases the y-axis and going right increases x-axis

#pyautogui.size() returns the screen resolution
print(pyautogui.size())			#Size(width=1366, height=768)
width,height = pyautogui.size() #Multiple assignment trick

"""
The last point in the screen will have one pixel less as the pixels start from (0,0)

Size(width=1366, height=768)
Point(x=1365, y=767)
"""
print(pyautogui.position())		#This returns the current position of the mouse eg:Point(x=573, y=260), Point(x=658, y=403)

# #Controlling the mouse using move()
# pyautogui.moveTo(100,100)					#Moving to a specific point
# pyautogui.moveTo(100,100, duration=1.5)	#Moving to a specific point in some duration in seconds


# pyautogui.moveRel(200,0)					#Moving mouse relative to the current position(xOffset,yOffset)
# pyautogui.moveRel(100,0, duration=1.5)		#Moving mouse relative to the current position(xOffset,yOffset) in some duration
# #To go up use (x,-y) as arg 
# pyautogui.moveRel(0,-100, duration=1.5)

# #Clicking the mouse button
# pyautogui.click(width-1,height-7)		#Clicking on a specific pixel, here it is the desktop button in windows

# #Move the mouse position to something clickable

# pyautogui.click()			#Single clicks where the mouse currently is.

# #Move the mouse position to an icon on desktop to open it
# pyautogui.doubleClick()

# #Move the mouse position to blank screen on desktop
# pyautogui.rightClick()			
# pyautogui.middleClick()

