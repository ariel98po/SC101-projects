"""
File: my_drawing.py
Name: 
----------------------
This file uses campy module to
draw on a GWindow object
"""

from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.graphics.gwindow import GWindow



def main():
    window = GWindow(width=800, height=500, title='Tater paws')
    paw1 = GOval(20, 20, x=200, y= 50)
    window.add(paw1)
    paw2 = GOval(20, 20, x=230, y=50)
    window.add(paw2)
    paw3 = GOval(20, 20, x=260, y=50)
    window.add(paw3)
    dogf = GRect(80, 40, x=200, y=100)
    window.add(dogf)
    face = GOval(150, 150, x=165, y=40)
    window.add(face)
    paw1.filled = True
    paw1.fill_color = 'indigo'
    paw2.filled = True
    paw2.fill_color = 'khaki'
    paw3.filled = True
    paw3.fill_color = 'beige'
    dogf.filled = True
    dogf.fill_color = 'olive'
    label = GLabel('Hello world!')
    label.font = '-10'
    window.add(label, 200, 100)



if __name__ == '__main__':
    main()
