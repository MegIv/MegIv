class Player:
    nyawa = 100

    def __init__(self,nama,skill):
        self.nama = nama
        self.skill = skill


    def bunuh_diri(self):
        self.nyawa -= 10
        print(f'nama: {self.nama} skill: {self.skill}. sisa nyawa: {self.nyawa}.')

player1 = Player('ivan','bundir')

player1.bunuh_diri()