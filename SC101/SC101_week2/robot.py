# from campy.graphics.gobjects import GOval
#
# class Robot:
#     #constructor
#
#     # print(f'__name__== {__name__})
#     def __init__(self, height, weight, color = 'green'):
#         self.h = height
#         self.w = weight
#         self.c = color
#
#     #Method
#     def give_me_a_ball(self, size):
#         ball = GOval(size, size)
#         ball.color = self.c
#         ball.filled = True
#         ball.fill_color = self.c
#         return ball
#
#     #Instance Method
#     def self_intro(self):
#         print(f'h = {self.h}/ w = {self.w}')
#
#     def bmi(self):
#         h_in_meter = self.h/100
#         n_bmi = self.w/(h_in_meter**2)
#         print(f'bmi = {n_bmi}')
#
#     #Static Method
#     @staticmethod
#     def say_hi():
#         print('Hi')
#
#
#
#
#
# class SuperRobot(Robot):
#
#     def __init__(self, h_s, w_s, c_s = 'green', counter =3):
#         super().__init__(h_s, w_s, color = c_s)
#         self.count = counter
#
#     def start_count(self):
#         for i in range(self.count):
#             print(f'{i+1}...', end='')
#
# def main():
#     r1 = Robot(180, 60)
#     r1.self_intro()
#     r1.say_hi()
#
#
#     r2 = SuperRobot(160, 45, c_s='limegreen', counter = 6)
#     r2.self_intro()
#     r2.say_hi()
#     r2.start_count()
#
#
#
#
# if __name__ =='__main__':
#     main()


from campy.graphics.gobjects import GOval

class Robot:

    def __init__(self, height, weight, color='green'):
        print(f'__name__== {__name__}')
        self.h = height
        self.w = weight
        self.c = color

    def give_me_a_ball(self, size):
        ball = GOval(size, size)
        ball.color = self.c
        ball.filled = True
        ball.fill_color = self.c
        return ball

    def self_intro(self):
        print(f'height={self.h}/weight={self.w}')

    def bmi(self):
        height_meter = self.h/100
        bmi_n = self.w/(height_meter**2)
        print(f'bmi = {bmi_n}')

    @staticmethod
    def say_tater():
        print(f'TATER NUMBER ONE')

class SuperRobot(Robot):
    def __init__(self, super_h, super_w, super_c = 'green', counter = 9):
        super().__init__(super_h, super_w, super_c)
        self.counter = counter

    def self_count(self):
        for i in range(self.counter):
            print(f'{i}...', end='')



def main():
    r1 = Robot(180,70)
    r1.self_intro()
    r1.say_tater()

    r2 = SuperRobot(300,150,super_c = 'lightcoral', counter=5)
    r2.self_intro()
    r2.say_tater()
    r2.self_count()

if __name__ == '__main__':
    main()

