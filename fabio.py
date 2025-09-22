import pyautogui as p
from time import sleep 

p.PAUSE = 0.2
p.hotkey('win', 'down')
for i in range(582):
    p.click(x=133, y=298)
    p.hotkey('ctrl','c')
    p.click(x=1033, y=281)
    p.click(x=757, y=587)
    p.press('tab')
    p.hotkey('ctrl','v')
    p.click(x=850, y=656)
    p.moveTo(x=960, y=598)
    p.scroll(-500)
    p.click(x=968, y=685)
    p.click(x=1112, y=298)
    p.hotkey('ctrl','c')
    p.click(x=353, y=300)
    p.hotkey('ctrl','v')
    p.click(x=27, y=301,button="right")
    p.click(x=106, y=500)
