class Superhero:
    people = 'people'

    def  __init__(self, name , nickname , superpower , health_points , catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.hp = health_points
        self.catchprase = catchphrase

    def names(self):
       return f'name : {self.name}'

    def hpx2(self):
       return self.hp * 2

    def __str__(self):
        print(f'его прозвище {self.nickname}\n'
              f' его здоровье {self.hp}\n'
              f'его суперспособность {self.superpower}\n')
    def __len__(self):
        return len(self.catchprase)





ironman = Superhero("tony" , 'ironman', 'Arrmors', 200 , 'im simple ironman')
print(ironman.names())
print(ironman.hpx2())
print(ironman.__str__())
print(ironman.__len__())