init python:
    class enemy:
        def __init__(self, name, max_hp = 10, hp = 10, element = "none", attack = 0, defense = 0):
            self.name = name
            self.max_hp = max_hp
            self.hp = hp
            self.element = element
            self.attack = attack
            self.defense = defense





default Comms = enemy("Communicator", 20, 20, "Tech")
default Model = enemy("Model", 15, 15, "Tech")
default Tender = enemy ("Tender", 25, 25, "Tech")
default Bear = enemy("Bear Demon", 25, 25, "Demon")
default Wolf = enemy("Wolf Demon", 25, 25, "Demon")
default TutBoss = enemy("Avarice Demon", 40, 40, "Demon")

default E1 = Comms
default E2 = Model
default E3 = Tender
default E4 = Wolf
default E5 = Bear
default B1 = TutBoss

image Communicator = "comms.png"
image Model = "model.png"
image Tender = "Tender.png"
image Wolf Demon = "boss-minion.png"
image Avarice Demon = "boss-tut.png"
