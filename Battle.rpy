define audio.Battle = "audio/Music/battle/Xi_fight.mp3"
define audio.Tut_Boss = "audio/Music/battle/Tut_Boss.mp3"

# Random Number Generator
label dice_roll:
    $ d2 = renpy.random.randint(1, 2)
    $ d3 = renpy.random.randint(1, 3)
    $ d4 = renpy.random.randint(1, 4)
    $ d6 = renpy.random.randint(1, 6)
    $ d10 = renpy.random.randint(1, 10)
    $ d15 = renpy.random.randint(1, 15)
    $ d20 = renpy.random.randint(1, 20)
    return

## COMPLICATED BATTLE

label complicated_battle:
    $ menu_choice = "b"
    play music Battle loop volume 0.2
    hide screen checkMouse
    hide screen Alert
    call HideEnt from _call_HideEnt

    scene bg streets with Pixellate(1.0, 5)
    call enemy_check from _call_enemy_check

    $ enemyturn = True
    $ enemy = E1


    call battle from _call_battle

    $ party
    $ player_current = Protag





    while True:

        # Player 1 Turn
        if Protag.hp > 0:
            $ player_current = Protag
            call player_attack from _call_player_attack

        # Player 2 Turn
        if selected_character.hp > 0:
            $ player_current = selected_character
            call player2_attack from _call_player2_attack

        # Enemies Turn
            # Determines Enemy Turn
        while enemyturn == True:

            if E1.hp > 0:
                $ enemy = E1
                call enemy_scavenger from _call_enemy_scavenger

            if E2.hp > 0:
                $ enemy = E2
                call enemy_scavenger from _call_enemy_scavenger_1

            if E3.hp > 0:
                $ enemy = E3
                call enemy_scavenger from _call_enemy_scavenger_2

            $enemyturn = False


##########
label TutBoss:
    $ menu_choice = "b"
    play music Tut_Boss loop volume 0.2
    hide screen checkMouse
    hide screen Alert
    call HideEnt from _call_HideEnt_1

    scene bg streets with Pixellate(1.0, 5)

    $ enemyturn = True
    $ enemy = B1


    call tut_boss from _call_tut_boss

    call Cut5

    call battle from _call_battle_1

    $ party
    $ player_current = Protag


    while True:

        # Player 1 Turn
        if Protag.hp > 0:
            $ player_current = Protag
            call player_attack from _call_player_attack_1

        # Player 2 Turn
        if selected_character.hp > 0:
            $ player_current = selected_character
            call player2_attack from _call_player2_attack_1

        # Enemies Turn
            # Determines Enemy Turn
        while enemyturn == True:

            if B1.hp > 0:
                $ enemy = B1
                call tutboss_turn from _call_tutboss_turn

            if E4.hp >= 0:
                $ enemy = E4
                call enemy_demon from _call_enemy_demon

            if E4.hp <= 0 and B1.hp > 0:
                $ E4.hp = E4.max_hp

                show screen demon1
                with dissolve

                call Inter1 from _call_Inter1

            $enemyturn = False


##########


label player_attack:

    $ Protag.defense = 0
    $ Protag.element = "Tech"
    $ enemyturn = True

    call dice_roll from _call_dice_roll

    hide image [selected_character.name]
    with moveoutright

    show Sanavi Battle at right
    with moveinright

    menu:
        "Attack":
            if d10 >= 8:                                                # 30%
                $ Protag.attack = d4 + d6 + Protag.level

            elif d10 == 1:                                              # 10%
                $ Protag.attack = 0

            else:                                                       # 60%
                $ Protag.attack = d6 + Protag.level

            jump enemy_target
        "Skill":
            jump Skill

        "Defend":
            $ Protag.defense = 10

            return



    return

label player2_attack:

    $ selected_character.defense = 0

    call dice_roll from _call_dice_roll_1

    hide Sanavi Battle
    with moveoutright

    show image [selected_character.name] at right
    with moveinright

    menu:
        "Attack":
            if d10 >= 8:                                                # 30%
                $ selected_character.attack = d4 + d6 + selected_character.level

            elif d10 == 1:                                              # 10%
                $ selected_character.attack = 0

            else:                                                       # 60%
                $ selected_character.attack = d6 + selected_character.level

            jump enemy_target

        "Skill":
            jump Skill

        "Defend":
            $ selected_character.defense = 10

            return

    return

label enemy_scavenger:

    call dice_roll from _call_dice_roll_2

    hide Sanavi Battle
    with moveoutright

    hide image [selected_character.name]
    with moveoutright


    # Selects Player
    if Protag.hp > 0 and selected_character.hp > 0:
        if d20 > 10:
            $ player_current = Protag
        else:
            $ player_current = selected_character
    elif Protag.hp > 0:
        $ player_current = Protag
    else:
        $ player_current = selected_character

    # Attacks
    if player_current == Protag:
        if d10 == 10:
            show screen battSan
            with vpunch
            $ enemy.attack = d10
        elif d10 >= 1:
            show screen battSan
            with vpunch
            $ enemy.attack = d6
        else:
            $ enemy.attack = 0
    else:
        if d10 == 10:
            show screen battpartner
            with vpunch
            $ enemy.attack = d10
        elif d10 >= 1:
            show screen battpartner
            with vpunch
            $ enemy.attack = d6
        else:
            $ enemy.attack = 0


    # Show hit Player
    if enemy.attack == 0:
        "...but misses!"
    elif player_current.defense == 0 and player_current.shield >= 1:
        $ player_current.shield -= enemy.attack
        "[player_current.name]'s Shield takes [enemy.attack] damage!"
    elif player_current.defense == 0 and player_current.shield == 0:
        $ player_current.hp -= enemy.attack
        "[player_current.name] takes [enemy.attack] damage!"


    if player_current.hp <= 0:

        jump partydeathcheck

    return

label enemy_demon:

    call dice_roll from _call_dice_roll_3

    hide Sanavi Battle
    with moveoutright

    hide image [selected_character.name]
    with moveoutright


    # Selects Player
    if Protag.hp > 0 and selected_character.hp > 0:
        if d20 > 10:
            $ player_current = Protag
        else:
            $ player_current = selected_character
    elif Protag.hp > 0:
        $ player_current = Protag
    else:
        $ player_current = selected_character

    # Attacks
    if player_current == Protag:
        if d10 == 10:
            show screen battSan
            with vpunch
            $ enemy.attack = d15
        elif d10 >= 1:
            show screen battSan
            with vpunch
            $ enemy.attack = d10
        else:
            $ enemy.attack = 0
    else:
        if d10 == 10:
            show screen battpartner
            with vpunch
            $ enemy.attack = d15
        elif d10 >= 1:
            show screen battpartner
            with vpunch
            $ enemy.attack = d10
        else:
            $ enemy.attack = 0

    # Show hit Player
    if enemy.attack == 0:
        "...but misses!"
    elif player_current.defense == 0 and player_current.shield >= 1:
        $ player_current.shield -= enemy.attack
        "[player_current.name]'s Shield takes [enemy.attack] damage!"
    elif player_current.defense == 0 and player_current.shield == 0:
        $ player_current.hp -= enemy.attack
        "[player_current.name] takes [enemy.attack] damage!"


    if player_current.hp <= 0:

        jump partydeathcheck

    return

label tutboss_turn:

    call dice_roll from _call_dice_roll_4

    hide Sanavi Battle
    with moveoutright

    hide image [selected_character.name]
    with moveoutright


    # Selects Player
    if Protag.hp > 0 and selected_character.hp > 0:
        if d20 > 10:
            $ player_current = Protag
        else:
            $ player_current = selected_character
    elif Protag.hp > 0:
        $ player_current = Protag
    else:
        $ player_current = selected_character

    # Attacks
    if player_current == Protag:
        if d10 == 10:
            show screen battSan
            with vpunch
            $ enemy.attack = d20
        elif d10 >= 1:
            show screen battSan
            with vpunch
            $ enemy.attack = d15
        else:
            show screen battSan
            with vpunch
            $ enemy.attack = d10
    else:
        if d10 == 10:
            show screen battpartner
            with vpunch
            $ enemy.attack = d20
        elif d10 >= 1:
            show screen battpartner
            with vpunch
            $ enemy.attack = d15
        else:
            show screen battpartner
            with vpunch
            $ enemy.attack = d10

    # Show hit Player
    if enemy.attack == 0:
        "...but misses!"
    elif player_current.defense == 0 and player_current.shield >= 1:
        $ player_current.shield -= enemy.attack
        "[player_current.name]'s Shield takes [enemy.attack] damage!"
    elif player_current.defense == 0 and player_current.shield == 0:
        $ player_current.hp -= enemy.attack
        "[player_current.name] takes [enemy.attack] damage!"
    else:
        "...but misses!"

    if player_current.hp == 0:

        jump deathcheck

    return

label enemy_check:
    $ rng = renpy.random.randint(1, 30)

    if rng <= 5:

        $ E1.hp = E1.max_hp
        $ E2.hp = 0
        $ E3.hp = 0
        $ E4.hp = 0
        $ B1.hp = 0

        show screen enemy1
        with None

    elif rng >= 20:

        $ E1.hp = E1.max_hp
        $ E2.hp = E2.max_hp
        $ E3.hp = 0
        $ E4.hp = 0
        $ B1.hp = 0

        show screen enemy1
        with None

        show screen enemy2
        with None

    elif rng == 30:

        $ E1.hp = 0
        $ E2.hp = 0
        $ E3.hp = E3.max_hp
        $ E4.hp = 0
        $ B1.hp = 0

        show screen enemy4
        with None


    else:

        $ E1.hp = E1.max_hp
        $ E2.hp = 0
        $ E3.hp = E3.max_hp
        $ E4.hp = 0
        $ B1.hp = 0

        show screen enemy1
        with None

        show screen enemy3
        with None


    return

label tut_boss:
    $ E1.hp = 0
    $ E2.hp = 0
    $ E3.hp = 0
    $ E4.hp = E4.max_hp
    $ B1.hp = B1.max_hp

    show screen Boss1
    with None
    show screen demon1
    with None

    return

label Skill:
    menu:
        "[Weapon.name]" if player_current == Protag:
            jump weapon_skill

        "[Ability.name]" if player_current == Protag:
            jump ability_skill

        "[selected_character.skill]" if player_current == selected_character:
            jump companion_skill

    return

label enemy_target:
    menu attack_choice:
        "[E2.name]" if E2.hp > 0:
            $ enemy = E2

        "[E3.name]" if E3.hp > 0:
            $ enemy = E3

        "[E1.name]" if E1.hp > 0:
            $ enemy = E1

        "[E4.name]" if E4.hp > 0:
            $ enemy = E4

        "[B1.name]" if B1.hp > 0:
            $ enemy = B1

    jump damage

label damage:
    # Weakness + Resist
    if enemy.element == "Tech" and player_current.element ==  "Tech":
        $ player_current.attack *= player_current.level
    elif enemy.element == "Demon" and player_current.element ==  "Angel":
        $ player_current.attack *= player_current.level
    elif enemy.element == "Tech" and player_current.element ==  "Demon":
        $ player_current.attack += player_current.level
    elif enemy.element == "Tech" and player_current.element ==  "Angel":
        $ player_current.attack += player_current.level
    elif enemy.element == "Angel" and player_current.element ==  "Demon":
        $ player_current.attack *= player_current.level
    else:
        $ player_current.attack *= 1

    # Transfer Damage
    if enemy == E1:
        $ E1.hp -= player_current.attack
    elif enemy == E2:
        $ E2.hp -= player_current.attack
    elif enemy == E3:
        $ E3.hp -= player_current.attack
    elif enemy == E4:
        $ E4.hp -= player_current.attack
    elif enemy == B1:
        $ B1.hp -= player_current.attack



    # Communicate Damage
    if player_current.attack >= 1:
        $ player_current.exp = d20
        "[player_current.name] dealt [player_current.attack] damage to the [enemy.name]!"

    elif player_current.attack == 0:
        "[player_current.name] Missed!"


    if enemy.hp <= 0:

        jump enemdeathcheck

    return

label partydeathcheck:
    if Protag.hp <= 0:
        hide screen battSan
        with dissolve

    if selected_character.hp <= 0:
        hide screen battpartner
        with dissolve
    # Evaluates Death
    if Protag.hp <=0 and selected_character.hp <= 0:

        call hidebattle from _call_hidebattle

        scene black with Pixellate(1.0, 5)

        "You lost..."

        jump Cut7

    return

label enemdeathcheck:

    # Evaluate for Death
    if E1.hp <= 0:
        hide screen enemy1
        with dissolve

    if E2.hp <= 0:
        hide screen enemy2
        with dissolve

    if E3.hp <= 0:
        hide screen enemy3
        with dissolve

        hide screen enemy4
        with dissolve

    if E4.hp <= 0:
        hide screen demon1
        with dissolve

    if B1.hp <= 0:
        hide screen Boss1
        with dissolve

    #win

    if E1.hp <= 0 and E2.hp <= 0 and E3.hp <= 0 and E4.hp <= 0 and B1.hp <= 0:

        "You win the combat encounter!"

        call level_check from _call_level_check

        call hidebattle from _call_hidebattle_1
        scene black with Pixellate(1.0, 5)

        stop music fadeout 1.0

        $ alert = 0
        $ pass_time(15)
        jump local_check

    return

label hidebattle:
    hide screen battSan
    hide screen battpartner

    return


label battle:
    show screen battSan
    with moveintop

    show screen battpartner
    with moveintop

    return

screen battSan:

    add im.Scale("Sanavi_Stats.png", 552, 239):
        xpos 20
        ypos 10

    vbox:
        xpos 255
        ypos 60
        xmaximum 100
        text "Sanavi"

    vbox:
        bar value StaticValue(Protag.shield, Protag.max_shield):
            xpos 280
            ypos 110
            xmaximum 200
            ymaximum 5
            left_bar Frame("bar_sp.png", 10, 0)
            right_bar Frame("bar_empty.png", 10, 0)


    vbox:
        bar value StaticValue(Protag.hp, Protag.max_hp):
            xpos 290
            ypos 150
            xmaximum 200
            ymaximum 5
            left_bar Frame("bar_hp.png", 10, 0)
            right_bar Frame("bar_empty.png", 10, 0)


screen battpartner:
    add im.Scale("Vastrial_Stats.png", 552, 239):
        xpos 700
        ypos 10

    vbox:
        xpos 900
        ypos 60
        xmaximum 100
        text "Vastrial"

    vbox:
        bar value StaticValue(selected_character.shield, selected_character.max_shield):
            xpos 925
            ypos 110
            xmaximum 200
            ymaximum 5
            left_bar Frame("bar_dem.png", 10, 0)
            right_bar Frame("bar_empty.png", 10, 0)


    vbox:
        bar value StaticValue(selected_character.hp, selected_character.max_hp):
            xpos 945
            ypos 150
            xmaximum 200
            ymaximum 5
            left_bar Frame("bar_hp.png", 10, 0)
            right_bar Frame("bar_empty.png", 10, 0)


screen enemy1:
    add [E1.name]:
        xpos 705
        ypos 220

    vbox:
        bar value StaticValue(E1.hp, E1.max_hp):
            xpos 850
            ypos 860
            xmaximum 200
            ymaximum 5
            left_bar Frame("bar_hp.png", 10, 0)
            right_bar Frame("bar_empty.png", 10, 0)

screen enemy2:
    add[E2.name]:
        xpos 240
        ypos 300

    vbox:
        bar value StaticValue(E2.hp, E2.max_hp):
            xpos 380
            ypos 960
            xmaximum 200
            ymaximum 5
            left_bar Frame("bar_hp.png", 10, 0)
            right_bar Frame("bar_empty.png", 10, 0)

screen enemy3:
    add[E3.name]:
        xpos 240
        ypos 300

    vbox:
        bar value StaticValue(E3.hp, E3.max_hp):
            xpos 380
            ypos 960
            xmaximum 200
            ymaximum 5
            left_bar Frame("bar_hp.png", 10, 0)
            right_bar Frame("bar_empty.png", 10, 0)

screen enemy4:
    add [E3.name]:
        xpos 705
        ypos 220

    vbox:
        bar value StaticValue(E3.hp, E3.max_hp):
            xpos 850
            ypos 860
            xmaximum 200
            ymaximum 5
            left_bar Frame("bar_hp.png", 10, 0)
            right_bar Frame("bar_empty.png", 10, 0)

screen demon1:
    add[E4.name]:
        xpos 240
        ypos 300

    vbox:
        bar value StaticValue(E4.hp, E4.max_hp):
            xpos 380
            ypos 960
            xmaximum 200
            ymaximum 5
            left_bar Frame("bar_hp.png", 10, 0)
            right_bar Frame("bar_empty.png", 10, 0)

screen Boss1:
    add [B1.name]:
        xpos 705
        ypos 220

    vbox:
        bar value StaticValue(B1.hp, B1.max_hp):
            xpos 850
            ypos 860
            xmaximum 200
            ymaximum 5
            left_bar Frame("bar_hp.png", 10, 0)
            right_bar Frame("bar_empty.png", 10, 0)
