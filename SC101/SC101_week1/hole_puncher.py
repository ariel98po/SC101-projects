"""
File: hole_puncher.py
Name:
------------------------
This file shows how to use campy
mouse event to punch holes (GOval)
on GWindow
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# This constant controls the size of the hole
SIZE = 30
window = GWindow()


def main():
	onmouseclicked(hole_puncher)

def hole_puncher(event):
	hole = GOval(SIZE,SIZE, x=event.x-SIZE/2, y=event.y-SIZE/2)
	hole.filled = True
	window.add(hole)



if __name__ == '__main__':
	main()
