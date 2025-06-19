image Build1 = "images/locations/Xi_int_1.png"
image Build2 = "images/locations/Xi_int_4.png"
image battle = "images/battle screen/Attack.png"

define audio.Xi_dungeon = "audio/Music/Ambient/OCXi_ambient.mp3"
define sX= 530
define sY= 630
default mX=0
default dist=0
default standWalk=0
default rX= -1000
default rng = 0
default alert=0
default warning=4
default max_alert=5


screen checkMouse():
    if standWalk==0:
        key "mousedown_1" action Jump("battleCheck")

label OldCityXiStart:
    $ menu_choice = "n"
    play music Xi_dungeon loop volume 0.2 fadein 1.0
    scene OldCityXiStart:
        xpos rX
    show screen checkMouse
    show screen Alert

    jump standRight

label OldCityXi1:
    $ menu_choice = "n"
    call HideEnt from _call_HideEnt_2
    play music Xi_dungeon loop volume 0.2 fadein 1.0
    scene OldCityXi1:
        xpos rX
    show screen checkMouse
    show screen Alert

    jump standRight

label standRight:
    $ standWalk=0
    hide SanRun
    show semi Idle:
        xpos sX
        ypos sY
        xzoom 1.0

    call Intcheck from _call_Intcheck
    hide semi Idle
    show Sanidle:
        xpos sX
        ypos sY
        xzoom 1.0
    $ renpy.pause(hard=True)

label standLeft:
    $ standWalk=0
    hide SanRun
    show semi Idle:
        xpos sX
        ypos sY
        xzoom -1.0

    call Intcheck from _call_Intcheck_1
    hide semi Idle
    show Sanidle:
        xpos sX
        ypos sY
        xzoom -1.0

    $ renpy.pause(hard=True)

label walkRight:
    $ standWalk=1

    scene expression [Location.name]:
        xpos rX
        linear dist/225.0 xpos rX-dist

    show SanRun:
        xpos sX
        ypos sY
        xzoom 1.0


    $ renpy.pause(delay=dist/225.0, hard=True)
    $ rX -= dist
    jump standRight

label walkLeft:
    $ standWalk=1

    scene expression [Location.name]:
        xpos rX
        linear dist/225.0 xpos rX+dist

    show SanRun:
        xpos sX
        ypos sY
        xzoom -1.0


    $ renpy.pause(delay=dist/225.0, hard=True)
    $ rX += dist
    jump standLeft

label checkDist:
    $ mX=renpy.get_mouse_pos()[0]

    if mX>600:
        $ dist = mX-615
        if rX-dist<-5500:
            $ dist= 5500 + rX
        jump walkRight

    else:
        $ dist = 610-mX
        if rX+dist>-100:
            $ dist= -(100 + rX)
        jump walkLeft

label battleCheck:
    $ alert += 1

    if alert == max_alert:

        show battle at truecenter
        with vpunch

        $ renpy.pause(0.5)

        jump complicated_battle

    else:
        $ pass_time(5)
        call HideEnt from _call_HideEnt_3

        jump checkDist

screen Alert:
    vbox:
        align (.01, .95)
        bar value StaticValue(alert, warning):
            xmaximum 200
            ymaximum 5

label Intcheck:

    if Location == Local1:

        if rX <= -1761:
            show screen Ent1

        if rX <= -2100:
            hide screen Ent1

        if rX <= -3008:
            show screen Ent2

        if rX <= -3700:
            hide screen Ent2

        if rX <= -4150:
            show screen Ent3

        if rX <= -4500:
            hide screen Ent3
    if Location == Local2:
        if rX <= -4420:
            show battle at truecenter
            with vpunch
            jump TutBoss
    return

screen Ent1:
    vbox:
        xpos 600
        ypos 600
        textbutton ("Enter") text_style "buttonz" action Jump("Enter1")

screen Ent2:
    vbox:
        xpos 600
        ypos 600
        textbutton ("Enter") text_style "buttonz" action Jump("Enter2")

screen Ent3:
    vbox:
        xpos 600
        ypos 600
        textbutton ("Enter") text_style "buttonz" action Jump("Enter3")

label HideEnt:
    hide screen Ent1
    hide screen Ent2
    hide screen Ent3

    return

label Enter1:
    hide screen Ent1
    hide screen Alert
    scene Build1 with fade

    $ alert = 0

    hide screen checkMouse
    show SanBatDef at left
    with moveinleft

    menu:
        "Search Room":
            "You found nothing..."

            scene black with fade

            jump local_check

        "Return":
            scene black with fade
            jump local_check

label Enter2:
    $ Location = Local2

    call local_check from _call_local_check

label Enter3:
    hide screen Ent3
    hide screen Alert
    scene Build2 with fade

    $ alert = 0

    hide screen checkMouse
    show SanBatDef at left
    with moveinleft

    menu:
        "Search Room":
            "You found a Shield Restore!"
            $ Protag.shield = Protag.max_shield
            $ selected_character.shield = selected_character.max_shield

            scene black with fade

            jump local_check

        "Return":
            scene black with fade
            jump local_check
