"""
File: whack_a_mole.py
Name: 
---------------------------
This program plays a game called
"whack a mole" in which players 
clicking the popping moles 
on screen to gain scores 
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLabel
from campy.graphics.gimage import GImage
from campy.gui.events.mouse import onmouseclicked
from campy.gui.events.timer import pause
import random

# Constants control the diameter of the window
WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 700

# Constant controls the pause time of the animation
DELAY = 550


# Global variables
# TODO:
window = GWindow(width = WINDOW_WIDTH, height = WINDOW_HEIGHT)
score = 0
score_label = GLabel('Score:'+str(score))
score_label.font = '-80'
def main():
    onmouseclicked(remove_mole)
    window.add(score_label, x=0, y= score_label.height+10)
    while True:
        mole = GImage('mole.jpeg')
        random_x = random.randint(0, window.width-mole.width)
        random_y = random.randint(0, window.height-mole.height)
        window.add(mole,random_x, random_y)
        pause(DELAY)


def remove_mole(mouse):
    global score
    maybe_mole = window.get_object_at(mouse.x, mouse.y)
    if maybe_mole is not None and maybe_mole is not score_label:
        window.remove(maybe_mole)
        score += 1
        print(score)
        score_label.text = 'Scores: '+ str(score)

if __name__ == '__main__':
    main()