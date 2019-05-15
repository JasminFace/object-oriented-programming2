class Vampire:
    
    coven = []

    def __init__(self, name, age, in_coffin = True, drank_blood_today = False):
        self.name = name
        self.age = age
        self.coffin = in_coffin
        self.drank = drank_blood_today
    
    @classmethod
    def create(cls, name, age, in_coffin = True, drank_blood_today = False):
        new_vampire = Vampire(name, age, in_coffin, drank_blood_today)
        cls.coven.append(new_vampire)
        return new_vampire