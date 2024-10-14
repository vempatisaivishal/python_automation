#to install we use pyautogui
#we have three things position,size,onscreen
#x-axis and y-axis position
import pyautogui
# pos=pyautogui.position()
# print(pos)
# size=pyautogui.size()#screen size
# print(size)
# #onscreen
# print(pyautogui.onScreen(1290,361))#this cordinate present on screen or not
#level 2
# pyautogui.moveTo(100,200)
# pyautogui.PAUSE=10
# pyautogui.moveTo(50,1)
# pyautogui.PAUSE=10
#above moves cursor here and there
#we ue FAILSAFE=False to avoid false when cursor moves to corner    and PAUSE is for that many milli seconds
#level 3
# while True:
#     x,y=pyautogui.position()
#     print(f"{x}:{y}")
#     pyautogui.sleep(2)
#level 4
# pyautogui.move(10,0)
#this is moving by 10 pixels right from current position
#so move and moveto has difference
#level 5
# pyautogui.FAILSAFE=False
# pyautogui.moveTo(100,100,2,pyautogui.easeInQuad)#start slow end fast
# pyautogui.moveTo(200,200,3,pyautogui.easeOutQuad)#start fast end slow
# pyautogui.moveTo(300,300,4,pyautogui.easeInOutQuad)#start and end fast middle slow
# pyautogui.moveTo(400,400,5,pyautogui.easeInBounce)#bound at end
# pyautogui.moveTo(500,500,6,pyautogui.easeInElastic)#rubber band at end

#level 6
# pyautogui.drag(20,20)#it is direction based
# pyautogui.dragTo(100,100)#it is to that position it drags
#level 7 clicks
# import time
# time.sleep(2)
# pyautogui.moveTo(600,600)
# x,y=pyautogui.position()
# time.sleep(5)
# pyautogui.click(x,y)#left click default
# time.sleep(5)
# pyautogui.doubleClick(x,y)
# #third parameter is button="right" or "left" or "middle"

#level 8
# pyautogui.sleep(2)
# pyautogui.mouseDown()#it holds the click continuosly->
# pyautogui.mouseUp()#click and release->this also takes arguments of x and y axis
#level 9 scroll
# pyautogui.sleep(4)
# pyautogui.scroll(-1000)#-1000 is 1000 negative clicks to move down
# pyautogui.sleep(4)
# pyautogui.scroll(1000)#up

#level 10
#keyboard functions
# pyautogui.sleep(5)
# pyautogui.write("hi hello")
# pyautogui.sleep(2)
# pyautogui.press('enter')
# pyautogui.sleep(5)
# pyautogui.write("Hello I am typing slowly",interval=0.1)#each second 10 letters
# pyautogui.press('enter')

#level 11
# pyautogui.sleep(5)
# pyautogui.keyDown('shift')#this keeps on holding shift
# pyautogui.write("hi hello",interval=0.1)
# pyautogui.sleep(4)
# pyautogui.press('enter')
#pyautogui.press('left',presses=5) #this clicks left key 5 times
#level 12
#hotkeys
# pyautogui.sleep(4)
# pyautogui.hotkey('ctrl','a')

#level 13
#alerts
# pyautogui.alert(text='Alert',title="alert box",button='ok')
# pyautogui.confirm(text='Alert',title="alert box",buttons=['ok','cancel'])
# pyautogui.prompt(text='Input',title="input box",default='username')
# pyautogui.password(text='Password',title="password box",default='masked password')#this in mask form

#level 13 small task
# con=pyautogui.confirm(text="Would you like to Login?",title="username",buttons=["Yes","No"])
# if con=='Yes':
#     pyautogui.prompt(text="Enter username",title="username",default='username')
#     pyautogui.password(text='Enter password',title="password",default='password')
#     print("Login successful")
# else:
#     print("Login cancelled")
#level 14
pyautogui.screenshot("microsoft.png",region=(0,0,1000,1000))
a=pyautogui.position()
print(a)
l=pyautogui.locateAllOnScreen("microsoft1.png")
print(l)
