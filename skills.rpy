init python:
    class WeaponSkill:
        def __init__(self, name, skill = 0):
            self.name = name
            self.skill = skill


    class BaseSkill:
        def __init__(self, name, skill = 0):
            self.name = name
            self.skill = skill


default Ws1 = WeaponSkill("Divine", 1)
default Ws2 = WeaponSkill("Radiant", 2)
default Ab1 = BaseSkill("Exorcism", 1)
default Ab2 = BaseSkill("Soulrend", 2)

default Weapon = Ws1
default Ability = Ab1

label weapon_skill:
    if Weapon.skill == 1:
        $ Protag.attack = 10
        $ Protag.element = "Angel"
        "Element changed to Angel"

    elif Weapon.skill == 2:
        if d10 >=5:
            $ Protag.attack = 15
            $ Protag.element = "Angel"
        else:
            $ Protag.attack = 5

    jump enemy_target


label ability_skill:
    if Ability.skill == 1:
        if d10 >=5:
            $ Protag.attack = 15
        else:
            $ Protag.attack = 5


    elif Ability.skill == 2:
        if d10 >=2:
            $ Protag.attack = 12
        else:
            $ Protag.attack = 5

    jump enemy_target
