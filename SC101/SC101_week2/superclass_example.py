class Equus:
    def __init__(self, is_male):
        pass
    def run(self):
        print(f'I run at speed {self.speed}')
        print(f'I\'m {self.gender}')
class Horse(Equus):
    def __init__(self, is_male):
        print('Horse init')
        self.speed = 30
        self.gender = 'male' if is_male else 'female'
        self.is_horse = True
    def roar(self):
        print('Hee haw~')
class Donkey(Equus):
    def __init__(self, is_female):
        print('Donkey init')
        self.speed = 20
        self.gender = 'female' if is_female else 'male'
        self.is_donkey = True
    def roar(self):
        print('Hee haw hee hee haw~')