class Animal:

    # a class attribute of the valid species in our universe
    valid_species = {
        'cat',
        'dog',
        'duck',
        'elf',
        'goblin',
        'horse',
        'human',
        'mermaid',
        'nightingale',
        'pig',
        'swan',
        'wolf'
    }

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f'{self.name} ({self._species})'
    
    # getter
    def species(self):
        #print("Getting species")
        return self._species
    
    # setter
    def set_species(self, into):
        #print("Setting species to", into)
        assert into in Animal.valid_species, Exception(f'invalid species: {into}')
        self._species = into
        
    species = property(species, set_species)