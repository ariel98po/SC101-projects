"""
File: mouse_draw.py
Name:
------------------------
This file shows how to use campy
mouse event to draw GOval
"""

from campy.graphics.gobjects import GOval, GRect
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmousedragged

# This constant controls the size of the pen stroke
SIZE = 30
window = GWindow()

def main():
	onmousedragged(dragg)

def dragg(event):
	rect = GRect(SIZE, SIZE, x= event.x-SIZE/2,y=event.y-SIZE/2 )
	rect.filled = True
	if event.x < window.width/2:
		rect.color = 'tomato'
		rect.fill_color = 'tomato'
	else:
		rect.color = 'green'
		rect.fill_color = 'green'
	window.add(rect)



if __name__ == '__main__':
	main()
