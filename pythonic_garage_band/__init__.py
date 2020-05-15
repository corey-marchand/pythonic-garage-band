__version__ = '0.1.0'

class Musician:
    def __init__(self, members):
        self.members = members
    def __str__(self):
        return 'Musician(position= {self.members}'
    def __repr__(self):
       return {'member' : self.members} 

class Band(Musician):
    def __init__(self, name):
        self.name = name
    def play_solo(self):
        input(f'Can you play a solo, {self.name}? ')
    def __str__(self):
        return 'my name is {self.name}'
    def _repr_(self):
        return {'name' : Band(self.name)}
    def to_list(self):
        print(Musician(self._repr_))
  

guitarist = Band(name = 'Dillon')
print(guitarist)