# from robot import Robot
# from campy.graphics.gwindow import GWindow
#
# def main():
#     window = GWindow(500, 500)
#     r1 = Robot(180, 70)
#     r1_ball = r1.give_me_a_ball(100)
#     window.add(r1_ball, 100, 200)
#     r1.self_intro()
#     r1.bmi()
#     Robot.say_hi()
#
#
#
#
#     r2 = Robot(170, 55, color='salmon')
#     r2_ball = r2.give_me_a_ball(200)
#     window.add(r2_ball, 300, 300)
#     r2.self_intro()
#     r2.bmi()
#     Robot.say_hi()
#
#
# if __name__ =='__main__':
#     main()

from robot import SuperRobot
from campy.graphics.gwindow import GWindow


def main():
    print(f'__name__== {__name__}')
    window = GWindow(600, 400)

    r1 = SuperRobot(200, 100, super_c='salmon', counter=5)
    r1_ball = r1.give_me_a_ball(100)
    window.add(r1_ball, 200, 200)
    r1.self_intro()
    r1.bmi()
    SuperRobot.say_tater()
    r1.self_count()


if __name__ =='__main__':
     main()
