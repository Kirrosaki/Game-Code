init python:
    class dungeon:
        def __init__(self, name, IsActive):
            self.name = name
            self.IsActive = IsActive



default tut1 = dungeon ("OldCityXiStart", True)
default tut2 = dungeon ("OldCityXi1", True)
default tut3 = dungeon ("Cut2", True)


default Local1 = tut1
default Local2 = tut2
default Local3 = tut3


label local_check:
    if Location == Local1:

        jump OldCityXiStart

    if Location == Local2:

        jump OldCityXi1

    if Location == Local3:

        jump Cut6

image OldCityXiStart = "images/locations/City1.jpg"
image OldCityXi1 = "images/locations/City2.jpg"
