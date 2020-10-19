"""
File: mouse_tracker.py
Name:
------------------------
This file shows how to use campy
mouse event to draw GOval
"""

from campy.graphics.gobjects import GRect
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmousemoved

# This constant controls the size of the GRect

SIZE = 100
window = GWindow()
rect = GRect(SIZE, SIZE)

def main():
	rect.filled = True
	rect.fill_color = 'salmon'
	rect.color = 'blue'
	window.add(rect)
	onmousemoved(position_track)

def position_track(mouse):
	rect.x = mouse.x - SIZE/2
	rect.y = mouse.y - SIZE/2



if __name__ == '__main__':
	main()
