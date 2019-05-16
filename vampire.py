class Vampire:
    
    coven = []

    def __init__(self, name, age, in_coffin = True, drank_blood_today = False):
        self.name = name
        self.age = age
        self.coffin = in_coffin
        self.drank = drank_blood_today
    
    def __str__(self):
        return f"Name: {self.name} In coffin? {self.coffin} Drank blood? {self.drank}"

    def drink_blood(self):
        self.drank = True
        return self.drank

    @classmethod
    def create(cls, name, age, in_coffin = True, drank_blood_today = False):
        new_vampire = Vampire(name, age, in_coffin, drank_blood_today)
        cls.coven.append(new_vampire)
        return new_vampire

    @classmethod
    def sunrise(cls):
        for vampire in Vampire.coven:
            if vampire.coffin == False or vampire.drank == False:
                cls.coven.remove(vampire)

    @classmethod
    def sunset(cls):
        for vampire in Vampire.coven:
            vampire.drank = False
            vampire.coffin = False
    
    @classmethod
    def go_home(cls):
        for vampire in Vampire.coven:
            vampire.coffin = True




count = Vampire.create("Count Dracula", 999)
mavis = Vampire.create("Mavis", 125)
johnny = Vampire.create("Johnny", 21)

print([str(vamp) for vamp in Vampire.coven])
Vampire.sunset()
print("-------------------------------------------------------------------------")
print([str(vamp) for vamp in Vampire.coven])
Vampire.go_home()
print("-------------------------------------------------------------------------")
print([str(vamp) for vamp in Vampire.coven])
Vampire.sunrise()
print("-------------------------------------------------------------------------")
print([str(vamp) for vamp in Vampire.coven])