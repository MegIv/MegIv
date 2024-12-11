class Superhero:
    def __init__(self,nama,power):
        self.__nama = nama
        self.__power = power

    def get_nama(self):
        return self.__nama

    def get_power(self):
        return self.__power

    def attack(self):
        return f'{self.__nama} menyerang dengan kekuatan {self.__power} !'

    def defense(self):
        return f'{self.__nama} bertahan dengan pertahanan super !'

class AerialHeroes(Superhero):
    def __init__(self,nama,power,speed,flyHight):
        super().__init__(nama, power)
        self.speed = speed
        self.flyHight = flyHight

class GroundHeroes(Superhero):
    def __init__(self,nama,power,speed):
        super().__init__(nama,power)
        self.speed = speed