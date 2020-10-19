from campy.gui.events.timer import pause
from zonegraphics import ZoneGraphics

FRAME_RATE = 1000 / 120 # 120 frames per second.
NUM_LIVES = 3


def main():
    """
    This program plays a Python game 'zone'
    A ball will be bouncing around the GWindow
    Players must defend the zone indicated by black
    line at the middle of the GWindow by clicking on
    the bouncing ball
    """
    graphics = ZoneGraphics()
    lives = NUM_LIVES
    while True:
        if graphics.ball_in_zone():
            lives -= 1
            if lives > 0:
                graphics.reset_ball()
            else:
                break

        graphics.move_ball()
        graphics.handle_wall_collisions()
        pause(FRAME_RATE)

if __name__ == '__main__':
    main()
