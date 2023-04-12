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

class Airhero(Superhero):
    air = ' air '
    def __init__(self, name , nickname , superpower , health_points , catchphrase , damage , fly = False ):
        super().__init__(name , nickname , superpower , health_points , catchphrase)
        self.damage = damage
        self.fly = fly

        def hpx2(self):
            return self.hp * self.hp

        def run(self):
            self.fly = True
            return f'fly in the {self.fly}_phrase'


class Earthhero(Superhero):
    earth = ' earth '
    def __init__(self, name , nickname , superpower , health_points , catchphrase , damage , fly = False ):
        super().__init__(name , nickname , superpower , health_points , catchphrase)
        self.damage = damage
        self.fly = fly

    def hpx2(self):
        return self.hp * self.hp

    def run(self):
        self.fly = True
        return f'fly in the {self.fly}_phrase'


class Villlain(Airhero):
    Airhero.people = 'monster'

    def gen_x(self):
        pass

    def crit(self, ofter):
        return ofter.damage **2



