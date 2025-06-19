init python:
    class Partymem:
        def __init__(self, name, max_level = 60, level = 1, exp = 0, max_hp = 10, hp = 10, max_shield = 4, shield = 4, element = "none", skill = "none", attack = 0, defense = 0):
            self.name = name
            self.max_level = max_level
            self.level = level
            self.exp = exp
            self.max_hp = max_hp
            self.hp = hp
            self.max_shield = max_shield
            self.shield = shield
            self.element = element
            self.skill = skill
            self.attack = attack
            self.defense = defense

default Protag = Partymem("Sanavi", 60, 1, 0, 10, 10, 15, 15, "Tech")
default V1 = Partymem("Vastrial", 30, 2, 0, 15, 15, 20, 20, "Demon", "Fires of Greed")
default A1 = Partymem("Azrael", 30, 2, 0, 15, 15, 20, 20, "Angel", "Dark Rain")

default selected_character = V1

default party = Protag and selected_character

image Azrael = "Azrael_Sprite.png"

label level_check:
    if party.exp >= 500 and party.level < party.max_level:
        $ party.level += 1

        "You leveled up!"
    return

label companion_skill:

    if selected_character == V1:
        if d20 >= 15:
            $ V1.attack = 7 * V1.level
            $ enemyturn = False
            if E1.hp > 0:
                $ enemy = E1

            elif E2.hp > 0:
                $ enemy = E2

            elif E3.hp > 0:
                $ enemy = E3

        else:
            "It missed!"
            if E1.hp > 0:
                $ enemy = E1

            elif E2.hp > 0:
                $ enemy = E2

            elif E3.hp > 0:
                $ enemy = E3


        jump damage

    elif selected_character == A1:
        $ A1.attack = d15 * 2


        jump enemy_target

    return
