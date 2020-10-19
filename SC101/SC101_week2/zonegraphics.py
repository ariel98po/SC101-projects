from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect
from campy.gui.events.mouse import onmouseclicked
import random

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
ZONE_WIDTH = 100
ZONE_HEIGHT = 100
BALL_RADIUS = 15
MAX_SPEED = 6
MIN_Y_SPEED = 2


class ZoneGraphics:

    def __init__(self, window_width=WINDOW_WIDTH, window_height=WINDOW_HEIGHT,
                 zone_width=ZONE_WIDTH, zone_height=ZONE_HEIGHT, ball_radius=BALL_RADIUS):
        # Create window
        self.window = GWindow(window_width, window_height, title='Zone Game')

        # Create zone
        self.zone = GRect(zone_width, zone_height, x=(window_width - zone_width) / 2,
                          y=(window_height - zone_height) / 2)
        self.zone.color = 'blue'
        self.window.add(self.zone)

        # Create ball and initialize velocity/position
        self.ball = GOval(2 * ball_radius, 2 * ball_radius)
        self.ball.filled = True
        self.ball.fill_color = 'salmon'

        self.dx = 0
        self.dy = 0

        self.reset_ball()

        # Initialize mouse listeners
        onmouseclicked(self.handle_click)

        # Set ball position at random inside the window

    def set_ball_position(self):
        self.ball.x = random.randint(0, self.window.width - self.ball.width)
        self.ball.y = random.randint(0, self.window.height - self.ball.height)

    def set_ball_velocity(self):
        self.dx = random.randint(0, MAX_SPEED)
        if random.random() > 0.5:
            self.dx = -self.dx
        self.dy = random.randint(MIN_Y_SPEED, MAX_SPEED)
        if random.random() > 0.5:
            self.dy = -self.dy

    def reset_ball(self):
        self.set_ball_position()
        while self.ball_in_zone():
            self.set_ball_position()
        self.set_ball_velocity()
        self.window.add(self.ball)

    def move_ball(self):
        self.ball.move(self.dx, self.dy)

    def handle_wall_collisions(self):
        if self.ball.x + self.ball.width >= self.window.width or self.ball.x <= 0:
            self.dx = -self.dx
        if self.ball.y + self.ball.height >= self.window.height or self.ball.y <= 0:
            self.dy = -self.dy

    def ball_in_zone(self):
        zone_left_side = self.zone.x
        zone_right_side = self.zone.x + self.zone.width
        ball_x_in_zone = zone_left_side <= self.ball.x <= zone_right_side - self.ball.width

        zone_top_side = self.zone.y
        zone_bottom_side = self.zone.y + self.zone.height
        ball_y_in_zone = zone_top_side <= self.ball.y <= zone_bottom_side - self.ball.height

        return ball_x_in_zone and ball_y_in_zone

    def handle_click(self, event):
        obj = self.window.get_object_at(event.x, event.y)
        if self.ball == obj:
            self.reset_ball()
