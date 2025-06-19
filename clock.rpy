init -1 python:
    time_in_minutes = 1300
    total_hours = time_in_minutes/60
    day = total_hours/24
    hours = total_hours%24
    minutes = time_in_minutes%60
    month = day/28

    def pass_time(minutes=1):
        store.time_in_minutes += minutes




image base = "Clock_temp.png"
default Day = "Sunday"
default Month = "April 3086"

screen clock():
    add "Clock_temp.png" align (1.0, 0.0)
    $ minutes = time_in_minutes % 60
    $ hours = (time_in_minutes / 60) % 24
    text ("%d:%02d" % (hours, minutes)) align (.95, .05)

screen day():
    $ day = (time_in_minutes / 60 / 24) % 28
    $ month = (time_in_minutes / 60/ 24 / 28) % 12

    text ("[Day], [Month]"):
        align (.95, .01)
        color "#FFFFFF"
        outlines [(2, "#820F8A", 0,0)]

label daycheck:

    if day <= 0:
        $ Day = "Sunday"

    if day <= 1:
        $ Day = "Monday"

    return
